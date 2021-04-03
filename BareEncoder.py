class BareEncoder:
    def __init__(self, input_path, output_path, params):
        self.input_path = input_path
        self.output_path = output_path
        self.params = params

    def encode_wrapper(self, line):
        result = self.encode(line.lower())
        return self.prettify(result, line)

    def decode_wrapper(self, line):
        result = self.decode(line.lower())
        return self.prettify(result, line)

    def write_encode(self):
        with open(self.input_path, 'r') as input_file:
            with open(self.output_path, 'w') as output_file:
                for line in input_file:
                    output_file.write(self.encode_wrapper(line))
        print('done.')

    def write_decode(self):
        with open(self.input_path, 'r') as input_file:
            with open(self.output_path, 'w') as output_file:
                for line in input_file:
                    output_file.write(self.decode_wrapper(line))
        print('done.')

    @staticmethod
    def prettify(new_line, line):
        prettified = ''
        for ind in range(len(line)):
            char = line[ind]
            if char.isalpha() and char.isupper():
                prettified += new_line[ind].upper()
            else:
                prettified += new_line[ind]
        return prettified

    def encode(self, line):
        return line

    def decode(self, line):
        return line
