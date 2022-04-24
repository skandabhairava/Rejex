from .rejex_static import Static

class Rejex:
    def __init__(self, start_flag:bool=False, end_flag:bool=False) -> None:
        self.string:str = ""

        self._start_flag:bool = start_flag
        self._end_flag:bool = end_flag

        if start_flag:
            self.string += "^"

    @property
    def start_flag(self) -> bool:
        return self._start_flag

    @property
    def end_flag(self) -> bool:
        return self._end_flag

    def compile(self) -> str:
        if self._end_flag:
            self.string += "$"

        return self.string

    def literal(self, literal:str) -> 'Rejex':
        """ Literal is a string that will be matched exactly.

        Args:
            literal (str): Literal string to be matched.

        Returns:
            Rejex: Rejex object.
        """

        self.string += Static.literal(literal)

        return self

    def any_char_except_newline(self) -> 'Rejex':
        """ Any character except newline.

        Returns:
            Rejex: Rejex object.
        """
        self.string += Static.any_char_except_newline()

        return self

    def alternative(self, alts:list) -> 'Rejex':
        """ If a string matches any one in the alts list then it will match.

        Args:
            alts (list): The list of alt strings/chars.

        Returns:
            Rejex: Rejex object.
        """
        self.string += Static.alternative(alts)

        return self

    def n_number_times(self, n:int, expr:str) -> 'Rejex':
        """ Match 'expr' expression set exactly 'n' number of times.

        Args:
            n (int): The number of times the previous set will be matched/searched for.
            expr (str): The expression set to be matched exactly 'n' number of times.

        Returns:
            Rejex: Rejex object.
        """
        self.string += Static.n_number_times(n, expr)

        return self

    def zero_or_more(self, expr:str) -> 'Rejex':
        """ The 'expr' to be matched zero or more times.

        Args:
            expr (str): The 'exp' to be matched zero or more times.

        Returns:
            Rejex: Rejex object.
        """
        self.string += Static.zero_or_more(expr)

        return self

    def one_or_more(self, expr:str) -> 'Rejex':
        """ The 'expr' to be matched one or more times.

        Args:
            expr (str): The 'exp' to be matched one or more times.

        Returns:
            Rejex: Rejex object.
        """
        self.string += Static.one_or_more(expr)

        return self

    def zero_or_one(self, expr:str) -> 'Rejex':
        """ The 'expr' to be matched zero or one time.

        Args:
            expr (str): The 'exp' to be matched zero or one time.

        Returns:
            Rejex: Rejex object.
        """
        self.string += Static.zero_or_one(expr)

        return self