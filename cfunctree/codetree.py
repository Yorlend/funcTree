

class CodeTree:
    def __init__(self, funcs: list[str], calls: list[typle[str]]):
        self.funcs = funcs
        self.calls = calls


    def get_func_list(self) -> list[str]:
        """
        Returns list of strings - function names
        """

        return self.funcs[:]


    def get_dep_list(self, func: str) -> list[str]:
        """
        Returns list of function names that are called by func
        """

        deps = []
        for func_a, func_b in self.calls:
            if func == func_a:
                deps.append(func_b)
        return deps
