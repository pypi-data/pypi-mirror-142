# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FBOutput

import tdw.flatbuffers

class CompositeObjects(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsCompositeObjects(cls, buf, offset):
        n = tdw.flatbuffers.encode.Get(tdw.flatbuffers.packer.uoffset, buf, offset)
        x = CompositeObjects()
        x.Init(buf, n + offset)
        return x

    # CompositeObjects
    def Init(self, buf, pos):
        self._tab = tdw.flatbuffers.table.Table(buf, pos)

    # CompositeObjects
    def Objects(self, j):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += tdw.flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from .CompositeObject import CompositeObject
            obj = CompositeObject()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # CompositeObjects
    def ObjectsLength(self):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def CompositeObjectsStart(builder): builder.StartObject(1)
def CompositeObjectsAddObjects(builder, objects): builder.PrependUOffsetTRelativeSlot(0, tdw.flatbuffers.number_types.UOffsetTFlags.py_type(objects), 0)
def CompositeObjectsStartObjectsVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def CompositeObjectsEnd(builder): return builder.EndObject()
