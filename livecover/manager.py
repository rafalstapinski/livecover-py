import abc
import json
import random
import socket
from typing import Optional

import coverage
from coverage.report import get_analysis_to_report
from coverage.html import HtmlDataGeneration

INDENTATION_DEPTH = 4


class BaseCoverage:
    @abc.abstractmethod
    def __init__(self):
        raise NotImplementedError

    @abc.abstractmethod
    def finish(self):
        raise NotImplementedError


class OpCoverage(BaseCoverage):

    reference: Optional[str]

    def __init__(self, reference: Optional[str] = None):
        self.cov = coverage.Coverage(omit=["*site-packages*"], data_file=None)
        self.cov.start()
        self.reference = reference

    def finish(self):
        try:
            self._finish()
        except Exception:
            pass

    def _finish(self):
        self.cov.stop()

        morfs = self.cov._data.measured_files()

        datagen = HtmlDataGeneration(self.cov)

        if not isinstance(morfs, (list, tuple, set)):
            morfs = [morfs]

        called_functions = set()

        for file_reporter, analysis in get_analysis_to_report(self.cov, morfs):
            file_data = datagen.data_for_file(file_reporter, analysis)
            definitions = []
            namespace = []

            for lineno, ldata in enumerate(file_data.lines, 1):
                token_types = [t[0] for t in ldata.tokens]
                token_names = [t[1] for t in ldata.tokens]

                if len(token_types) == 0:
                    continue

                depth = 0

                # get depths
                if token_types[0] == "ws":
                    _, indentation = token_types.pop(0), token_names.pop(0)

                    # dont update depths if remainder is empty line
                    if len(token_types) == 0:
                        continue

                    depth = int(len(indentation) / INDENTATION_DEPTH)

                if token_types[0] == "key" and token_names[0] == "async":
                    token_types = token_types[2:]
                    token_names = token_names[2:]

                # if definition
                if token_types[0] == "key" and token_names[0] in ("def", "class"):

                    definition_name = token_names[2]

                    if depth > (len(namespace) + 1):
                        namespace.append(definition_name)

                    elif depth == (len(namespace) + 1):
                        if len(namespace) == 0:
                            namespace.append(definition_name)
                        else:
                            namespace[-1] = definition_name

                    else:
                        namespace = namespace[:depth]
                        namespace.append(definition_name)

                    module_path = "{}.{}".format(
                        file_reporter.relative_filename()
                        .replace("/", ".")
                        .replace(".py", ""),
                        ".".join(namespace),
                    )

                    definitions.append((lineno, module_path))

            executed_lines = sorted(analysis.executed)
            definitions = list(sorted(definitions, key=lambda d: d[0], reverse=True))
            for executed_line in executed_lines:
                called_function = next(
                    d[1] for d in definitions if d[0] < executed_line
                )
                called_functions.add(called_function)

        self._send(called_functions)

    def _send(self, called_functions: set):
        report = {"called": list(called_functions), "reference": self.reference}

        message = bytes(json.dumps(report), "utf-8")
        open_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        open_socket.sendto(message, ("127.0.0.1", 8125))
        open_socket.close()


class NoopCoverage(BaseCoverage):
    def __init__(self):
        ...

    def finish(self):
        ...


def get_coverage(ratio: float = 1) -> BaseCoverage:
    return OpCoverage() if random.random() < ratio else NoopCoverage()