import rejex
from rejex import Rejex, Static

rejex_string = (
    Rejex()
        .n_number_times(2, Rejex()
            .literal("l")
            .any_char_except_newline()
            .alternative([5, 4])
            .compile())
        .compile()
)

print(rejex_string)

print(bool(rejex.match(rejex_string, "l_5l_4")))