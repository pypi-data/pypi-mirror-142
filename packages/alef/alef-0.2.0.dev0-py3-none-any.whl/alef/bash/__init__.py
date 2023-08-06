import subprocess
import sys
from pathlib import Path
from typing import Optional, Union
from urllib.parse import urlparse

from .logging import getLogger

logging = getLogger(__name__)


class RunResult:
    def __init__(self, rc, serr, sout, cmd):
        self.rc = rc
        self.serr = serr
        self.sout = sout
        self.cmd = cmd

    def __str__(self):
        # return f"""RunResult({self.rc}, serr={self.serr}, sout={self.sout}, cmd={self.cmd})"""
        return f"""RunResult({self.rc}, serr={self.serr}, sout={self.sout})"""


class RunResultDetached:
    def __init__(self, process, cmd):
        self.pid = process.pid
        self.process = process
        self.cmd = cmd

    def __str__(self):
        return f"""RunResultDetached({self.process}, cmd={self.cmd})"""


def run(
    cmd,
    *,
    logname="bash",
    remote="",
    check=True,
    dry_run=False,
    detach=False,
    capture_output=False,
    interactive=False,
    cwd=None,
):
    if dry_run:
        logging.info(f"{logname}: run dry_run: {cmd}")
        return RunResult(0, "", "", cmd)
    logging.debug(f"{logname}: running: {cmd}")
    if remote == "":
        cmds = ["bash", "-s"]
    else:
        cmds = ["ssh", remote, "bash -s"]
    if detach:
        assert not capture_output
        assert not check
        assert not interactive
        cmds = ["nohup"] + cmds
        p = subprocess.Popen(
            cmds,
            stdin=subprocess.PIPE,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            cwd=cwd,
        )
        p.stdin.write(cmd.encode("utf8"))
        p.stdin.close()
        logging.info(f"{logname}: detach mode: pid: {p.pid}")
        return RunResultDetached(p, cmd)
    if interactive:
        # TODO: at least Ctrl-C cannot work easily without disabling python's handler first
        if remote == "":
            cmds = ["bash", "-c", cmd]
        else:
            # TODO: why this does not work: ["ssh", "-t", remote, "bash", "-c", cmd]
            cmds = ["ssh", "-t", remote, cmd]
        assert not check
        assert not detach
        # TODO: capture_output actually make sense, we may like tee-like behavior
        assert not capture_output
        p = subprocess.Popen(
            cmds,
            # stdin=sys.stdin,
            # stdout=subprocess.DEVNULL,
            # stderr=subprocess.DEVNULL,
            bufsize=0,
            cwd=cwd,
        )
        with p:
            pass
        return RunResultDetached(p, cmd)
    if capture_output:
        p = subprocess.run(
            cmds, input=cmd.encode("utf8"), check=False, capture_output=True, cwd=cwd,
        )
        rc = p.returncode
        serr = p.stderr.decode("utf8")
        sout = p.stdout.decode("utf8")
        if check and rc != 0:
            logging.error(f'{logname} "{cmd}" returns {rc}')
            logging.error(f'{logname} "{cmd}" stderr: {serr}')
            logging.error(f'{logname} "{cmd}" stdout: {sout}')
            raise RuntimeError(f'{logname} failing: "{cmd}"')
        logging.debug(f"{logname}: captured stdout:\n" + sout.strip())
        return RunResult(rc, serr, sout, cmd)
    if check:
        subprocess.run(cmds, input=cmd.encode("utf8"), check=True, cwd=cwd)
        return RunResult(0, "", "", cmd)
    p = subprocess.run(cmds, input=cmd.encode("utf8"), check=False, cwd=cwd)
    rc = p.returncode
    return RunResult(rc, "", "", cmd)


class SSHHost:
    def __init__(self, user, host, logname=None):
        self.user = user
        self.host = host
        self.__uh = f"{self.user}@{self.host}"
        self.__p_unit = Path(f"/home/{self.user}/.config/systemd/user")
        if logname is None:
            self.__logname = self.__uh
        else:
            self.__logname = logname

    def run(self, *args, **kwds):
        kwds.setdefault("logname", self.__logname)
        kwds["remote"] = self.__uh
        return run(*args, **kwds)

    def rsync_put(self, to, fr, options="-auv"):
        run(f"rsync {options} {fr} {self.__uh}:{to}")

    def rsync_get(self, to, fr, options="-auv"):
        run(f"rsync {options} {self.__uh}:{fr} {to}")

    def rsync_put_dir_content(self, to, fr, mode=0o755, options="-auv"):
        to = str(to).rstrip("/") + "/"
        fr = str(fr).rstrip("/") + "/"
        self.mkdir(to, parents=True, exist_ok=True, mode=mode)
        self.rsync_put(to, fr, options=options)

    def touch(self, path):
        self.run(f"touch {path}")

    def mkdir(self, path, parents=False, mode=0o755, exist_ok=False):
        p = str(path)
        assert p.startswith("/")
        mode = oct(mode)[2:]
        assert len(mode) == 3
        assert all(int(d) <= 7 for d in mode)
        s_p = "-p" if parents else ""
        if exist_ok:
            s_ok = f"[[ -d '{path}' ]] && exit 0"
        else:
            s_ok = f"[[ -d '{path}' ]] && echo 'already exists:' '{path}' && exit -1"
        s_p = "-p" if parents else ""
        self.run(
            f"""
set -eu
{s_ok}
mkdir {s_p} -m {mode} {path}
"""
        )

    def is_file(self, path):
        return self._zero_true_one_false(f"[[ -f {path} ]]")

    def is_dir(self, path):
        return self._zero_true_one_false(f"[[ -d {path} ]]")

    def exists(self, path):
        return self._zero_true_one_false(f"[[ -e {path} ]]")

    def _zero_true_one_false(self, cmd):
        rslt = self.run(cmd, check=False)
        if rslt.rc == 0:
            return True
        if rslt.rc == 1:
            return False
        raise RuntimeError(rslt)

    def ps(self, pattern):
        return self.run(
            f"ps -e -o pid,pgid,fuid,ruid,euid,cmd|grep {pattern}",
            check=False,
            capture_output=True,
        )

    def unit_install(self, p):
        self.mkdir(self.__p_unit, parents=True, exist_ok=True)
        self.run(f"cp -a {p} {self.__p_unit}/.")

    def unit_start(self, name):
        self.run(f"systemctl --user start {name}")


def download_unpack(
    d: Union[Path, str],
    url: str,
    name: Optional[str] = None,
    suffix: Optional[str] = None,
):
    d = Path(d)
    fn = Path(urlparse(url).path)
    if name is None:
        name = fn.stem
    if suffix is None:
        suffix = "".join(_ for _ in fn.suffixes if _[1] not in "0123456789").strip(".")
        # suffix = "".join(fn.suffixes).strip(".")
    assert suffix in ("tar.gz", "tar.bz2")
    ofn = d / (name + "." + suffix)
    if not ofn.exists():
        run(f"curl -LJ -o {ofn} {url}")
    odn = d / name
    odn.mkdir(exist_ok=True)
    cmd = f"tar -x --strip-components=1 -f {ofn} -C {odn}"
    run(cmd)
    return name
