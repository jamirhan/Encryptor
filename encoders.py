import BareEncoder
import CaesarEncoder
import VigenerEncoder
import VernamEncoder


encoders = {
    'Bare': BareEncoder.BareEncoder,
    'Caesar': CaesarEncoder.CaesarEncoder,
    'Vigener': VigenerEncoder.VigenerEncoder,
    'Vernam': VernamEncoder.VernamEncoder,
}

required_encode_params = {
    'Bare': 0,
    'Caesar': 1,
    'Vigener': 1,
    'Vernam': 1,
}

required_decode_params = {
    'Bare': 0,
    'Caesar': 0,  # if no arguments provided, decoding will go through frequency analysis
    'Vigener': 1,
    'Vernam': 1,
}
