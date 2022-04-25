import rejex
from rejex import Rejex, Static, CommonRejex

rejex_string = (
    Rejex()
        .n_number_times(2, Rejex()
            .literal("l")
            .literal("k")
            .any_char_except_newline()
            .alternative([5, 4])
            .compile())
        .compile()
)

#print(rejex_string)

print(rejex.test_regex(CommonRejex.short_date, "25/4-2022"))