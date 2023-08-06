import fire

from .logging import getLogger, initLogging

logging = getLogger("alef")


def _main():
    print("hello")


def main():
    fire.Fire(_main)
