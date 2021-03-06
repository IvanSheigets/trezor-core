# Automatically generated by pb2py
import protobuf as p
from .HDNodeType import HDNodeType


class HDNodePathType(p.MessageType):
    FIELDS = {
        1: ('node', HDNodeType, 0),  # required
        2: ('address_n', p.UVarintType, p.FLAG_REPEATED),
    }

    def __init__(
        self,
        node: HDNodeType = None,
        address_n: list = None,
        **kwargs,
    ):
        self.node = node
        self.address_n = [] if address_n is None else address_n
        p.MessageType.__init__(self, **kwargs)
