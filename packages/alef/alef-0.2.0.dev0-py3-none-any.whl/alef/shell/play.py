import time
from .wrap import SSH


def timed(f, *args, **kwds):
    t = time.time()
    o = f(*args, **kwds)
    print(f"**** time :: {time.time() - t:.7f}")
    return o


if __name__ == "__main__":
    c = SSH("localhost")

    timed(c.run, "echo hello")
    timed(c.run, "echo hello")
    timed(c.local, "echo hello")
    timed(c.local, "echo hello")
