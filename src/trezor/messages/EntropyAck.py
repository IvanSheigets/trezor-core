# Automatically generated by pb2py
import protobuf as p


class EntropyAck(p.MessageType):
    FIELDS = {
        1: ('entropy', p.BytesType, 0),
    }
    MESSAGE_WIRE_TYPE = 36

    def __init__(
        self,
        entropy: bytes = None,
        **kwargs,
    ):
        self.entropy = entropy
        p.MessageType.__init__(self, **kwargs)
