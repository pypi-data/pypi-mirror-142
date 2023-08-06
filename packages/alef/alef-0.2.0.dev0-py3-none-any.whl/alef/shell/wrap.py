from typing import Iterable, Mapping, Optional, Tuple, Union

import docker
import fabric
import invoke


class Local(invoke.Context):
    def __init__(self, config=None):
        super().__init__(config=config)


class SSH(fabric.Connection):
    def __init__(self, *args, **kwds):
        super().__init__(*args, **kwds)

    def rsync_put(self, to, fr, **kwds):
        return self._rsync(to, fr, "upload", **kwds)

    def rsync_get(self, to, fr, **kwds):
        return self._rsync(to, fr, "download", **kwds)

    def _rsync(self, to, fr, side, **kwds):
        return _rsync(
            self.local,
            side=side,
            user=self.user,
            host=self.host,
            port=self.port,
            source=fr,
            target=to,
            **kwds,
        )


class Container(invoke.Context):
    def __init__(self, config=None):
        super().__init__(config=config)


def _rsync(
    run,
    *,
    side: str,
    user: str,
    host: str,
    port: Union[str, int],
    source: str,
    target: str,
    key_filename: Union[str, Iterable[str]] = (),
    exclude: Union[str, Iterable[str]] = (),
    delete: bool = False,
    strict_host_keys: bool = True,
    rsync_opts: str = "",
    ssh_opts: str = "",
    run_kwargs: Optional[Mapping] = None,
):
    """
    Convenient wrapper around your friendly local ``rsync``.

    Specifically, it calls your local ``rsync`` program via a subprocess. It
    provides Python level keyword arguments for some common rsync options, and
    allows you to specify custom options via a string if required (see below.)

    For details on how ``rsync`` works, please see its manpage. ``rsync`` must
    be installed on both the invoking system and the target in order for this
    function to work correctly.

    .. note::
        For reference, the approximate ``rsync`` command-line call that is
        constructed by this function is the following::

            rsync [--delete] [--exclude exclude[0][, --exclude[1][, ...]]] \\
                -pthrvz [rsync_opts] <source> <host_string>:<target>

    :param str source:
        The local path to copy from. Actually a string passed verbatim to
        ``rsync``, and thus may be a single directory (``"my_directory"``) or
        multiple directories (``"dir1 dir2"``). See the ``rsync`` documentation
        for details.
    :param str target:
        The path to sync with on the remote end. Due to how ``rsync`` is
        implemented, the exact behavior depends on the value of ``source``:

        - If ``source`` ends with a trailing slash, the files will be dropped
          inside of ``target``. E.g. ``rsync(c, "foldername/",
          "/home/username/project")`` will drop the contents of ``foldername``
          inside of ``/home/username/project``.
        - If ``source`` does **not** end with a trailing slash, ``target`` is
          effectively the "parent" directory, and a new directory named after
          ``source`` will be created inside of it. So ``rsync(c, "foldername",
          "/home/username")`` would create a new directory
          ``/home/username/foldername`` (if needed) and place the files there.

    :param exclude:
        Optional, may be a single string or an iterable of strings, and is
        used to pass one or more ``--exclude`` options to ``rsync``.
    :param bool delete:
        A boolean controlling whether ``rsync``'s ``--delete`` option is used.
        If True, instructs ``rsync`` to remove remote files that no longer
        exist locally. Defaults to False.
    :param bool strict_host_keys:
        Boolean determining whether to enable/disable the SSH-level option
        ``StrictHostKeyChecking`` (useful for frequently-changing hosts such as
        virtual machines or cloud instances.) Defaults to True.
    :param str rsync_opts:
        An optional, arbitrary string which you may use to pass custom
        arguments or options to ``rsync``.
    :param str ssh_opts:
        Like ``rsync_opts`` but specifically for the SSH options string
        (rsync's ``--rsh`` flag.)
    """
    if isinstance(exclude, str):
        exclude = [exclude]
    else:
        assert isinstance(exclude, (list, tuple))
        exclude = list(exclude)
    exclude_opts = ' --exclude "{}"' * len(exclude)
    # Double-backslash-escape
    exclusions = tuple([str(s).replace('"', '\\\\"') for s in exclude])
    # Honor SSH key(s)
    if isinstance(key_filename, str):
        keys = [keys]
    else:
        assert isinstance(key_filename, (list, tuple))
        keys = list(key_filename)
    if len(keys) > 0:
        key_string = "-i " + " -i ".join(keys)
    else:
        key_string = ""
    # Get base cxn params
    assert isinstance(port, (str, int))
    port_string = "-p {}".format(port)
    # Remote shell (SSH) options
    rsh_string = ""
    rsh_parts = [key_string, port_string, ssh_opts]
    if any(rsh_parts):
        rsh_string = "--rsh='ssh {}'".format(" ".join(rsh_parts))
    # Set up options part of string
    options_map = {
        "delete": "--delete" if delete else "",
        "exclude": exclude_opts.format(*exclusions),
        "rsh": rsh_string,
        "extra": rsync_opts,
    }
    options = "{delete}{exclude} -auv {extra} {rsh}".format(**options_map)
    # TODO: richer host object exposing stuff like .address_is_ipv6 or whatever
    assert isinstance(user, str)
    assert isinstance(host, str)
    if host.count(":") > 1:
        u_h = "[{}@{}]".format(user, host)
    else:
        u_h = "{}@{}".format(user, host)
    # Create and run final command string
    assert isinstance(side, str)
    assert side in ("upload", "download", "local")
    if side == "upload":
        cmd = "rsync {} {} {}:{}".format(options, source, u_h, target)
    elif side == "download":
        cmd = "rsync {} {}:{} {}".format(options, u_h, source, target)
    elif side == "local":
        cmd = "rsync {} {} {}".format(options, source, target)
    else:
        raise RuntimeError("should not reach here")
    if run_kwargs is None:
        run_kwargs = {}
    return run(cmd, **run_kwargs)
