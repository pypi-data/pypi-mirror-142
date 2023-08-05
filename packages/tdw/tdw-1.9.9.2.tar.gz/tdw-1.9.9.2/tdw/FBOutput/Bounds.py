# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FBOutput

import tdw.flatbuffers

class Bounds(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsBounds(cls, buf, offset):
        n = tdw.flatbuffers.encode.Get(tdw.flatbuffers.packer.uoffset, buf, offset)
        x = Bounds()
        x.Init(buf, n + offset)
        return x

    # Bounds
    def Init(self, buf, pos):
        self._tab = tdw.flatbuffers.table.Table(buf, pos)

    # Bounds
    def Objects(self, j):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += tdw.flatbuffers.number_types.UOffsetTFlags.py_type(j) * 88
            from .BoundsData import BoundsData
            obj = BoundsData()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Bounds
    def ObjectsLength(self):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def BoundsStart(builder): builder.StartObject(1)
def BoundsAddObjects(builder, objects): builder.PrependUOffsetTRelativeSlot(0, tdw.flatbuffers.number_types.UOffsetTFlags.py_type(objects), 0)
def BoundsStartObjectsVector(builder, numElems): return builder.StartVector(88, numElems, 4)
def BoundsEnd(builder): return builder.EndObject()
