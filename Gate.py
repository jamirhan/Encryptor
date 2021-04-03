import encoders
import exceptions


class AutomatedList(list):
    def get_last_pop(self):
        last_obj = self[-1]
        self.pop(-1)
        return last_obj


class Command:
    def get_input_path(self):
        return self.input_path

    def get_output_path(self):
        return self.output_path

    def get_encoder(self):
        return self.encoder

    def get_parameters(self):
        return self.parameters

    def get_mode(self):
        return self.mode

    def __init__(self, string):
        ar = string.split()
        self.input_path = ar[0]
        self.output_path = ar[1]
        self.encoder = ar[2]
        self.mode = ar[3]
        if len(ar) > 3:
            self.parameters = ar[4:]
        else:
            self.parameters = list()


class Gate:

    def __init__(self):
        self.commands = AutomatedList()

    def __handle_command__(self):
        new_command = Command(input())
        if new_command.get_mode() == 'encode':
            if encoders.required_encode_params[new_command.get_encoder()] > len(new_command.get_parameters()):
                raise exceptions.WrongArgumentNum(encoders.required_encode_params[new_command.get_encoder()],
                                                  len(new_command.get_parameters()))
        elif new_command.get_mode() == 'decode':
            if encoders.required_decode_params[new_command.get_encoder()] > len(new_command.get_parameters()):
                raise exceptions.WrongArgumentNum(encoders.required_decode_params[new_command.get_encoder()],
                                                  len(new_command.get_parameters()))
        self.commands.append(new_command)

    def get_last_command(self):
        if len(self.commands) == 0:
            self.__handle_command__()
        return self.commands.get_last_pop()
