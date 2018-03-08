class VarUtil:

    def __init__(self):
        pass

    @staticmethod
    def exist(var_name_str):
        try:
            type(eval(var_name_str))
        except NameError:
            return 0
        else:
            return 1

    @staticmethod
    def has_length(var_name):
        return not (var_name is None or var_name.strip() == '')

