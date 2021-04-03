import BareEncoder
import linecache
import exceptions


class VernamEncoder(BareEncoder.BareEncoder):
    def __init__(self, *args):
        super().__init__(*args)
        self.key_line = 0
        self.key_ind = 0
        key_symbols = self.get_key_symbols_num()
        inp_symbols = self.get_input_symbols_num()
        if key_symbols != inp_symbols:
            raise exceptions.WrongKey(key_symbols, inp_symbols)

    def get_key_symbols_num(self):
        ans = 0
        with open(self.params[0]) as key:
            for line in key:
                ans += len(line)
                if line[-1] == '\n':
                    ans -= 1
        return ans

    def get_input_symbols_num(self):
        ans = 0
        with open(self.input_path) as inp:
            for line in inp:
                ans += len(line)
        return ans

    def encode_wrapper(self, line):
        result = self.encode(line)
        return result

    def decode_wrapper(self, line):
        result = self.decode(line)
        return result

    def encode(self, line):
        new_line = ''
        index = 0
        while index < len(line):
            cur_line = linecache.getline(self.params[0], self.key_line + 1)
            key_char = cur_line[self.key_ind]
            while key_char == '\n':
                self.key_line += 1
                self.key_ind = 0
                cur_line = linecache.getline(self.params[0], self.key_line + 1)
                key_char = cur_line[self.key_ind]
            new_line += str(((ord(line[index]) - 97) ^ (ord(key_char) - 97)) + 97) + ' '
            self.key_ind += 1
            index += 1
        new_line += '\n'
        return new_line

    def decode(self, line):
        new_line = ''
        index = 0
        line = [int(x) for x in line.split()]
        while index < len(line):
            cur_line = linecache.getline(self.params[0], self.key_line + 1)
            key_char = cur_line[self.key_ind]
            while key_char == '\n':
                self.key_line += 1
                self.key_ind = 0
                cur_line = linecache.getline(self.params[0], self.key_line + 1)
                key_char = cur_line[self.key_ind]
            new_line += chr((((line[index]) - 97) ^ (ord(key_char) - 97)) + 97)
            self.key_ind += 1
            index += 1
        return new_line
