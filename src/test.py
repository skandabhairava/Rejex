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
            .except_expr(Static.literal("\\"))
        .compile()
    )

print(rejex_test)

rejex.test_regex(rejex_test, "\\") #False
rejex.test_regex(rejex_test, "a") #False