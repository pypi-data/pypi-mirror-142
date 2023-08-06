import sys
import textwrap

import coloring


class Printer:
    def __init__(self, level=1, indent=0):
        self._indent = indent

    def print(
        self,
        *text,
        end: str = "\n",
        sep: str = " ",
        file=sys.stdout,
        flush: bool = False,
        indent=0,
    ):
        text = sep.join([str(e) for e in text])
        indent = " " * self._indent

        text = textwrap.indent(text, indent)

        file.write(text)
        file.write(end)
        if flush:
            file.flush()

    def info(self, *args, **kwargs):
        self.print(
            coloring.colorize(
                coloring.consts.TXT_INFO,
                c=coloring.consts.COLOR_INFO,
                s=coloring.consts.STYLE_INFO,
            ),
            *args,
            **kwargs,
        )

    def success(self, *args, **kwargs):
        self.print(
            coloring.colorize(
                coloring.consts.TXT_SUCCESS,
                c=coloring.consts.COLOR_SUCCESS,
                s=coloring.consts.STYLE_SUCCESS,
            ),
            *args,
            **kwargs,
        )

    def verbose(self, *args, **kwargs):
        pass

    def debug(self, *args, **kwargs):
        pass

    def indent(self):
        self._indent += 1

    def dedent(self):
        self._indent -= 1

    def f(self):
        pass

    pass


printer = Printer()
