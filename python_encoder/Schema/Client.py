# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Schema

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Client(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Client()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsClient(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Client
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Client
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Client
    def ClientDataType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # Client
    def ClientData(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            from flatbuffers.table import Table
            obj = Table(bytearray(), 0)
            self._tab.Union(obj, o)
            return obj
        return None

def ClientStart(builder):
    builder.StartObject(3)

def Start(builder):
    ClientStart(builder)

def ClientAddName(builder, name):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(name), 0)

def AddName(builder, name):
    ClientAddName(builder, name)

def ClientAddClientDataType(builder, clientDataType):
    builder.PrependUint8Slot(1, clientDataType, 0)

def AddClientDataType(builder, clientDataType):
    ClientAddClientDataType(builder, clientDataType)

def ClientAddClientData(builder, clientData):
    builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(clientData), 0)

def AddClientData(builder, clientData):
    ClientAddClientData(builder, clientData)

def ClientEnd(builder):
    return builder.EndObject()

def End(builder):
    return ClientEnd(builder)
