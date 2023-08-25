# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Schema

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Person(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Person()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsPerson(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Person
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Person
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Person
    def Age(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint16Flags, o + self._tab.Pos)
        return 0

    # Person
    def Weight(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # Person
    def Gender(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def PersonStart(builder):
    builder.StartObject(4)

def Start(builder):
    PersonStart(builder)

def PersonAddName(builder, name):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(name), 0)

def AddName(builder, name):
    PersonAddName(builder, name)

def PersonAddAge(builder, age):
    builder.PrependUint16Slot(1, age, 0)

def AddAge(builder, age):
    PersonAddAge(builder, age)

def PersonAddWeight(builder, weight):
    builder.PrependFloat32Slot(2, weight, 0.0)

def AddWeight(builder, weight):
    PersonAddWeight(builder, weight)

def PersonAddGender(builder, gender):
    builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(gender), 0)

def AddGender(builder, gender):
    PersonAddGender(builder, gender)

def PersonEnd(builder):
    return builder.EndObject()

def End(builder):
    return PersonEnd(builder)
