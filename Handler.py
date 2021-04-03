import Gate
import encoders
import exceptions


class Handler:
    def __init__(self):
        self.gate_obj = Gate.Gate()
        self.start()

    @staticmethod
    def is_running():
        return True

    @staticmethod
    def get_encoder_object(command):
        if command.get_encoder() in encoders.encoders:
            return encoders.encoders[command.get_encoder()](command.get_input_path(), command.get_output_path(),
                                                            command.get_parameters())
        return None

    @staticmethod
    def operate_code(encoder_obj, mode):
        if mode == 'encode':
            encoder_obj.write_encode()
        elif mode == 'decode':
            encoder_obj.write_decode()

    @staticmethod
    def leave():
        print("\nexiting...")
        exit(0)

    def start(self):
        while self.is_running():
            try:
                current_command = self.gate_obj.get_last_command()
                encoder_obj = self.get_encoder_object(current_command)
                if encoder_obj is not None:
                    self.operate_code(encoder_obj, current_command.get_mode())
            except KeyboardInterrupt:
                self.leave()
            except TypeError:
                print('Wrong argument type provided')
                continue
            except exceptions.WrongKey as exc:
                print(f'provided key is of inappropriate length. input message len: {exc.inp_len},'
                      f' key len: {exc.key_len}')
                continue
            except exceptions.WrongArgumentNum as exc:
                print(f'wrong argument number. Was provided: {exc.provided_num} though needed: {exc.needed_num}')
                continue
            except Exception:
                print('Error occurred, consider checking command signature')
                continue
