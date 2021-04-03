import BareEncoder


class CaesarEncoder(BareEncoder.BareEncoder):  # only with english alphabet yet

    def __init__(self, *args):
        super().__init__(*args)
        self.key = self.find_key()

    def find_key(self):
        if len(self.params) != 0:
            return int(self.params[0])
        freq = {}
        with open(self.input_path) as inp:
            for line in inp:
                for char in line:
                    if char.isalpha():
                        char = char.lower()
                        if char in freq:
                            freq[char] += 1
                        else:
                            freq[char] = 1
        maximal = ('', -1)
        for letter in freq:
            if freq[letter] > maximal[1]:
                maximal = (letter, freq[letter])
        return (-ord('e') + ord(maximal[0]) + 26) % 26

    def encode(self, line):
        new_line = ''
        for symbol in line:
            if symbol.isalpha():
                new_line += chr(((ord(symbol) + self.key - 97) % 26) + 97)
            else:
                new_line += symbol
        return new_line

    def decode(self, line):
        new_line = ''
        for symbol in line:
            if symbol.isalpha():
                new_line += chr(((ord(symbol) - self.key - 97 + 26) % 26) + 97)
            else:
                new_line += symbol
        return new_line
