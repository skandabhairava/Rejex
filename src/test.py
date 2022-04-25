import rejex
from rejex import Rejex, Static, CommonRejex

rejex_string = (
    Rejex()
        .n_number_times(2, Rejex()
            .literal("l")
            .literal("k")
            .any_char_except_newline()
            .alternative([5, 4])
            .compile()
        )
        .compile()
)

rejex_test = (
    Rejex()
        .zero_or_one(Static.any_number())
        .any_number()
        .alternative(Static.literal("/"), Static.literal("-"))
        .zero_or_one(Static.any_number())
        .any_number()
        .alternative(Static.literal("/"), Static.literal("-"))
        .zero_or_one(
            Static.n_number_times(2, Static.any_number())
        )
        .n_number_times(2, Static.any_number())
    .compile()
)

print(rejex_test)

print(rejex.test_regex(rejex_test, "25/12/2019"))