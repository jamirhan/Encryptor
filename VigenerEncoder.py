import BareEncoder


class VigenerEncoder(BareEncoder.BareEncoder):

    def __init__(self, *args):
        super().__init__(*args)
        self.params[0] = self.get_param().lower()

    def get_param(self):
        ans = ''
        with open(self.params[0]) as key:
            for line in key:
                ans += line
        return ans

    @staticmethod
    def multiply(word, new_size):
        result = ''
        for i in range(new_size // len(word)):
            result += word
        result += word[:new_size % len(word)]
        return result

    def encode(self, line):
        new_line = ''
        keyword = self.multiply(self.params[0], len([x for x in line if x in [chr(y) for y in range(97, 97 + 26)]]))
        index = 0
        shift = 0
        while index + shift < len(line):
            if line[index + shift].isalpha():
                new_line += chr((ord(line[index + shift]) - 97 + ord(keyword[index]) - 97) % 26 + 97)
                index += 1
            else:
                new_line += line[index + shift]
                shift += 1
        new_line += '\n'
        return new_line

    def decode(self, line):
        new_line = ''
        keyword = self.multiply(self.params[0], len([x for x in line if x in [chr(y) for y in range(97, 97 + 26)]]))
        index = 0
        shift = 0
        while index + shift < len(line):
            if line[index + shift].isalpha():
                new_line += chr((ord(line[index + shift]) - 97 + 26 - ord(keyword[index]) + 97) % 26 + 97)
                index += 1
            else:
                new_line += line[index + shift]
                shift += 1
        new_line += '\n'
        return new_line
