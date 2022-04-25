"""Rejex is a tool used to build regex expressions for python."""

from re import *
from re import RegexFlag
from .rejex_class import Rejex
from .rejex_static import Static

def test_regex(regex_pattern:str, string:str, flag:int=0) -> bool:
    return bool(match(regex_pattern, string, flag))

class CommonRejex:
    phone_number: str = r"(\+(\d)+)?( )?(\()?(\d){3}(\))?( )?(\d){3}(-)?(\d){4}"
    """ 
    (
        Rejex()
            .zero_or_one(
                Rejex()
                    .literal("+")
                    .one_or_more(
                        Static.any_number()
                    )
                    .compile()
            )
            .zero_or_one(Static.literal(" "))
            .zero_or_one(Static.literal("("))
            .n_number_times(3, Static.any_number())
            .zero_or_one(Static.literal(")"))
            .zero_or_one(Static.literal(" "))
            .n_number_times(3, Static.any_number())
            .zero_or_one(Static.literal("-"))
            .n_number_times(4, Static.any_number())
        .compile()
    ) 
    
    +1 (555) 555-1234
    +911234567890
    (123) 123-4567
    456 456-7890
    ...
    """

    short_date:str = r"\d?\d(/|-)\d?\d(/|-)(\d\d)?\d\d"
    basic_time:str = r"[0-9]?[0-9]:[0-9][0-9](:[0-9][0-9])?"