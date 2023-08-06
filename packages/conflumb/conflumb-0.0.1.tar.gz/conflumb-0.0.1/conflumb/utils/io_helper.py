
import os
from os.path import abspath, dirname

from .exception import GErrorFileNotFound


def full_path(path):
    return os.path.join(os.getcwd(), path)


def file_loader(path, read_lines=False):
    if not os.path.isabs(path):
        path = os.path.join(dirname(dirname(abspath(__file__))), path)
    if not os.path.exists(path):
        raise GErrorFileNotFound('File does not exist! [Path: {}]'.format(path))
    with open(path, encoding="utf-8") as f:
        return f.readlines() if read_lines else f.read()
