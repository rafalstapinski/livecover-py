import abc
import sys
import json
import os
import random
import socket
from typing import Optional
import inspect


class OpCoverage:

    entrypoint: Optional[str]

    def _get_namespace(self, frame, relpath):
        source, lineno = inspect.findsource(frame)

        while source[lineno].startswith("@"):
            lineno += 1

        if relpath in self.cache:
            if lineno in self.cache[relpath]:
                return self.cache[relpath][lineno]

        prev_leading_spaces = len(source[lineno]) - len(source[lineno].lstrip())

        namespace = [source[lineno]]

        if self.debug:
            print("ns", namespace)

        while lineno > 0:
            lineno -= 1
            if "def " in source[lineno] or "class " in source[lineno]:
                leading_spaces = len(source[lineno]) - len(source[lineno].lstrip())
                if leading_spaces < prev_leading_spaces:
                    namespace.insert(0, source[lineno])
                    prev_leading_spaces = leading_spaces

                if leading_spaces == 0:
                    break

        _namespace = relpath.replace("/", ".").replace(".py", "")
        for ns in namespace:
            ns = ns.lstrip().split(" ")[1].split("(")[0].split(":")[0]
            _namespace += ".{}".format(ns)

        if relpath in self.cache:
            self.cache[relpath][lineno] = _namespace
        else:
            self.cache[relpath] = {}
            self.cache[relpath][lineno] = _namespace

        if self.debug:
            print("ns", _namespace)

        return _namespace

    def _report(self, frame, event, arg):
        if event == "call":
            try:
                if (
                    "site-packages" in frame.f_code.co_filename
                    or "/lib/" in frame.f_code.co_filename
                ):
                    return
                relpath = os.path.relpath(frame.f_code.co_filename, self.cwd)
                if relpath.startswith(".."):
                    return
                ns = self._get_namespace(frame, relpath)
                self._send(ns)
            except Exception as e:
                if self.debug:
                    print("e", e)

    def _send(self, ns):
        self.sock.sendto(
            bytes(json.dumps({"called": ns, "entrypoint": self.entrypoint}), "utf-8"),
            ("d.livecover.io", 80),
        )

    def __init__(self, entrypoint: Optional[str] = None, debug=False):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.entrypoint = entrypoint
        self.cwd = os.getcwd()
        self.cache = {}
        self.debug = debug
        sys.settrace(self._report)


class NoopCoverage:
    pass


def get_coverage(ratio: float = 1, entrypoint: str = None, debug=False):
    return (
        OpCoverage(entrypoint=entrypoint, debug=debug)
        if random.random() < ratio
        else NoopCoverage()
    )
