"""Rejex is a tool used to build regex expressions for python."""

from re import *
from .rejex_class import Rejex
from .rejex_static import Static

def test_regex(regex_pattern:str, string:str) -> bool:
    return bool(match(regex_pattern, string))

class CommonRejex:
    phone_number: str = r"(\+(\d)+)?(\()?\d\d\d(\))?( )?\d\d\d(-)?\d\d\d\d"
    short_date:str = r"\d?\d(/|-)\d?\d(/|-)(\d\d)?\d\d"
    basic_time:str = r"[0-9]?[0-9]:[0-9][0-9](:[0-9][0-9])?"