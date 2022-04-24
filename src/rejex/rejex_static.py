class Static:

    @staticmethod
    def literal(literal:str) -> str:
        """ Literal is a string that will be matched exactly.

        Args:
            literal (str): Literal string to be matched.

        Returns:
            str: Rejex string.
        """
        if not isinstance(literal, str):
            try:
                literal = str(literal)
            except Exception:
                raise ValueError(f"Literal '{literal}' must be a string or should be convertable to string.")

        to_be_escaped = "^$.|()*+?{}[]\\"
        new_literal = ""
        for i in literal:
            if i not in to_be_escaped:
                new_literal += i
            else:
                new_literal += "\\" + i

        return new_literal

    @staticmethod
    def any_char_except_newline() -> str:
        """ Any character except newline.

        Returns:
            str: Rejex string.
        """
        return "."

    @staticmethod
    def alternative(alts:list) -> str:
        """ If a string matches any one in the alts list then it will match.

        Args:
            alts (list): The list of alt strings/chars.

        Returns:
            str: Rejex string.
        """
        assert isinstance(alts, list), "alts must be a list."
        try:
            new_alts = []
            for i in alts:
                if isinstance(i, str):
                    new_alts.append(i)
                else:
                    new_alts.append(str(i))
        except Exception:
            raise ValueError(f"All values in alts '{alts}' must be a string or should be convertable to string.")

        if all(len(i)==1 for i in new_alts):
            #if all of them are single chars, use [abc] notation
            return f"([{''.join(new_alts)}])"
        else:
            #if any of them are more than one char, use a|b|c notation
            return f"({'|'.join(new_alts)})"

    @staticmethod
    def n_number_times(n:int, expr:str) -> str:
        """ Match 'expr' expression set exactly 'n' number of times.

        Args:
            n (int): The number of times the previous set will be matched/searched for.
            expr (str): The expression set to be matched exactly 'n' number of times.

        Returns:
            str: Rejex string.
        """
        assert isinstance(n, int), "n must be an integer."
        
        if not isinstance(expr, str):
            try:
                expr = str(expr)
            except ValueError:
                raise ValueError(f"Expression '{expr}' must be a string or should be convertable to string.")

        return f"({expr}){{{n}}}"

    @staticmethod
    def zero_or_more(expr:str) -> str:
        """ The 'expr' to be matched zero or more times.

        Args:
            expr (str): The 'exp' to be matched zero or more times.

        Returns:
            str: Rejex string.
        """
        if not isinstance(expr, str):
            try:
                expr = str(expr)
            except ValueError:
                raise ValueError(f"Expression '{expr}' must be a string or should be convertable to string.")

        return f"({expr})*"

    @staticmethod
    def one_or_more(expr:str) -> str:
        """ The 'expr' to be matched one or more times.

        Args:
            expr (str): The 'exp' to be matched one or more times.

        Returns:
            str: Rejex string.
        """
        if not isinstance(expr, str):
            try:
                expr = str(expr)
            except ValueError:
                raise ValueError(f"Expression '{expr}' must be a string or should be convertable to string.")

        return f"({expr})+"

    @staticmethod
    def zero_or_one(expr:str) -> str:
        """ The 'expr' to be matched zero or one time.

        Args:
            expr (str): The 'exp' to be matched zero or one time.

        Returns:
            str: Rejex string.
        """
        if not isinstance(expr, str):
            try:
                expr = str(expr)
            except ValueError:
                raise ValueError(f"Expression '{expr}' must be a string or should be convertable to string.")

        return f"({expr})?"