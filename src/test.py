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

print(rejex_test)

print(rejex.test_regex(rejex_test, "a456 456-7890"))