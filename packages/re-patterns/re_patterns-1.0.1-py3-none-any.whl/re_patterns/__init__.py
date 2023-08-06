#!/usr/bin/env python


"""
Helper functions to construct raw regular expressions strings
"""


from __future__ import annotations
from datetime import date
from . import version
import re


__author__ = "Sven Siegmund"
__author_email__ = "sven.siegmund@gmail.com"
__maintainer__ = __author__
__maintainer_email__ = __author_email__
__release_date__ = date(year=2022, month=3, day=11)
__version__ = version.version
__repository__ = "https://github.com/Nagidal/re_patterns"


class Rstr(str):
    """
    Subclass of str which adds functions generating
    raw regex strings
    """
    # We put the whole re module here, because then you
    # only need to `from re_patterns import Rstr`
    # and you can access re as Rstr.re
    re = re
    def __add__(self, other) -> Rstr:
        return Rstr("".join((self, other), ))
    def named(self, name: str, optional: bool=False) -> Rstr:
        result = Rstr(r"".join((name.join((r"(?P<", r">")), self, r")")))
        if optional:
            return result.append(r"?")
        return result
    def followed_by(self, following: str) -> Rstr:
        return Rstr("".join((self, "".join((r"(?=", following, r")")))))
    def not_followed_by(self, following: str) -> Rstr:
        return Rstr("".join((self, following.join((r"(?!", r")")))))
    def preceded_by(self, preceding: str) -> Rstr:
        return Rstr("".join(("".join((r"(?<=", preceding, r")")), self)))
    def not_preceded_by(self, preceding: str) -> Rstr:
        return Rstr("".join((preceding.join((r"(?<!", r")")), self)))
    def no_capture(self) -> Rstr:
        return Rstr("".join((r"(?:", self, r")")))
    def group(self) -> Rstr:
        return Rstr("".join((r"[", self, r"]")))
    def unnamed(self, optional: bool=False) -> Rstr:
        result = Rstr("".join((r"(", self, r")")))
        if optional:
            return result.append(r"?")
        return result
    def comment(self) -> Rstr:
        return Rstr("".join((r"(?#", self, r")")))
    def append(self, appendix: str) -> Rstr:
        return Rstr("".join((self, appendix)))
    def prepend(self, prependix: str) -> Rstr:
        return Rstr("".join((prependix, self)))
    def join(self, *args, **kwargs) -> Rstr:
        return Rstr("".join((self, *args, ), **kwargs))
    def __or__(self, *args, **kwargs) -> Rstr:
        return Rstr("|".join((self, *args, ), **kwargs))
    def compile(self, *args, **kwargs) -> re.Pattern:
        return re.compile(self, *args, **kwargs)
    def match(self, *args, **kwargs) -> re.Match:
        return re.match(self, *args, **kwargs)
    def search(self, *args, **kwargs) -> re.Match:
        return re.search(self, *args, **kwargs)
    def finditer(self, *args, **kwargs) -> Iterable[re.Match]:
        return re.finditer(self, *args, **kwargs)
    def findall(self, *args, **kwargs) -> list[str]:
        return re.findall(self.compile(), *args, **kwargs)
    def print_out(self) -> str:
        return self.compile().pattern.replace("\\\\", "\\")
    as_group = group
    as_comment = comment
    capture_group = unnamed

