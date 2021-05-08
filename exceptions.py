class WrongKey(Exception):
    def __init__(self, key_len, inp_len):
        super().__init__()
        self.key_len = key_len
        self.inp_len = inp_len


class WrongArgumentNum(Exception):
    def __init__(self, needed_num, provided_num):
        super().__init__()
        self.needed_num = needed_num
        self.provided_num = provided_num


class UnexpectedError(Exception):
    def __init__(self):
        pass
