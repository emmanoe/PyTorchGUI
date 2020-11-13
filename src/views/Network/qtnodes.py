"""Manual tests."""

from PySide import QtGui

from .knob import InputKnob, OutputKnob
from .header import Header
from .node import Node
from .widget import NodeGraphWidget

#Todo: factor this duplicated codes
class Conv1d(Node):

    def __init__(self, *args, **kwargs):
        super(Conv1d, self).__init__(*args, **kwargs)
        self.addHeader(Header(node=self, text="Conv1d"))
        self.addKnob(InputKnob(name="Input"))
        self.addKnob(OutputKnob(name="Output"))
        #self.header.fillColor = QtGui.QColor(36, 128, 18)

class Conv2d(Node):

    def __init__(self, *args, **kwargs):
        super(Conv2d, self).__init__(*args, **kwargs)
        self.addHeader(Header(node=self, text="Conv2d"))
        self.addKnob(InputKnob(name="Input"))
        self.addKnob(OutputKnob(name="Output"))
        # self.header.fillColor = QtGui.QColor(36, 128, 18)

class Conv3d(Node):

    def __init__(self, *args, **kwargs):
        super(Conv3d, self).__init__(*args, **kwargs)
        self.addHeader(Header(node=self, text="Conv3d"))
        self.addKnob(InputKnob(name="Input"))
        self.addKnob(OutputKnob(name="Output"))
        # self.header.fillColor = QtGui.QColor(36, 128, 18)

class ConvTranspose1d(Node):

    def __init__(self, *args, **kwargs):
        super(ConvTranspose1d, self).__init__(*args, **kwargs)
        self.addHeader(Header(node=self, text="Conv_transpose1d"))
        self.addKnob(InputKnob(name="Input"))
        self.addKnob(OutputKnob(name="Output"))
        # self.header.fillColor = QtGui.QColor(36, 128, 18)

class ConvTranspose2d(Node):

    def __init__(self, *args, **kwargs):
        super(ConvTranspose2d, self).__init__(*args, **kwargs)
        self.addHeader(Header(node=self, text="Conv_transpose2d"))
        self.addKnob(InputKnob(name="Input"))
        self.addKnob(OutputKnob(name="Output"))
        # self.header.fillColor = QtGui.QColor(36, 128, 18)

class ConvTranspose3d(Node):

    def __init__(self, *args, **kwargs):
        super(ConvTranspose3d, self).__init__(*args, **kwargs)
        self.addHeader(Header(node=self, text="Conv_transpose3d"))
        self.addKnob(InputKnob(name="Input"))
        self.addKnob(OutputKnob(name="Output"))
        # self.header.fillColor = QtGui.QColor(36, 128, 18)

class Unfold(Node):

    def __init__(self, *args, **kwargs):
        super(Unfold, self).__init__(*args, **kwargs)
        self.addHeader(Header(node=self, text="unfold"))
        self.addKnob(InputKnob(name="Input"))
        self.addKnob(OutputKnob(name="Output"))
        # self.header.fillColor = QtGui.QColor(36, 128, 18)

class Fold(Node):

    def __init__(self, *args, **kwargs):
        super(Fold, self).__init__(*args, **kwargs)
        self.addHeader(Header(node=self, text="fold"))
        self.addKnob(InputKnob(name="Input"))
        self.addKnob(OutputKnob(name="Output"))
        # self.header.fillColor = QtGui.QColor(36, 128, 18)


class MaxPool1d(Node):

    def __init__(self, *args, **kwargs):
        super(MaxPool1d, self).__init__(*args, **kwargs)
        self.addHeader(Header(node=self, text="MaxPool1d"))
        self.addKnob(InputKnob(name="Input"))
        self.addKnob(OutputKnob(name="Output"))
        # self.header.fillColor = QtGui.QColor(36, 128, 18)

class MaxPool2d(Node):

    def __init__(self, *args, **kwargs):
        super(MaxPool2d, self).__init__(*args, **kwargs)
        self.addHeader(Header(node=self, text="MaxPool2d"))
        self.addKnob(InputKnob(name="Input"))
        self.addKnob(OutputKnob(name="Output"))
        # self.header.fillColor = QtGui.QColor(36, 128, 18)

class MaxPool3d(Node):

    def __init__(self, *args, **kwargs):
        super(MaxPool3d, self).__init__(*args, **kwargs)
        self.addHeader(Header(node=self, text="MaxPool3d"))
        self.addKnob(InputKnob(name="Input"))
        self.addKnob(OutputKnob(name="Output"))
        # self.header.fillColor = QtGui.QColor(36, 128, 18)

class MaxUnpool1d(Node):

    def __init__(self, *args, **kwargs):
        super(MaxUnpool1d, self).__init__(*args, **kwargs)
        self.addHeader(Header(node=self, text="MaxUnpool1d"))
        self.addKnob(InputKnob(name="Input"))
        self.addKnob(OutputKnob(name="Output"))
        # self.header.fillColor = QtGui.QColor(36, 128, 18)

class MaxUnpool2d(Node):

    def __init__(self, *args, **kwargs):
        super(MaxUnpool2d, self).__init__(*args, **kwargs)
        self.addHeader(Header(node=self, text="MaxUnpool2d"))
        self.addKnob(InputKnob(name="Input"))
        self.addKnob(OutputKnob(name="Output"))
        # self.header.fillColor = QtGui.QColor(36, 128, 18)

class MaxUnpool3d(Node):

    def __init__(self, *args, **kwargs):
        super(MaxUnpool3d, self).__init__(*args, **kwargs)
        self.addHeader(Header(node=self, text="MaxUnpool3d"))
        self.addKnob(InputKnob(name="Input"))
        self.addKnob(OutputKnob(name="Output"))
        # self.header.fillColor = QtGui.QColor(36, 128, 18)

class AvgPool1d(Node):

    def __init__(self, *args, **kwargs):
        super(AvgPool1d, self).__init__(*args, **kwargs)
        self.addHeader(Header(node=self, text="AvgPool1d"))
        self.addKnob(InputKnob(name="Input"))
        self.addKnob(OutputKnob(name="Output"))
        # self.header.fillColor = QtGui.QColor(36, 128, 18)

class AvgPool2d(Node):

    def __init__(self, *args, **kwargs):
        super(AvgPool2d, self).__init__(*args, **kwargs)
        self.addHeader(Header(node=self, text="AvgPool2d"))
        self.addKnob(InputKnob(name="Input"))
        self.addKnob(OutputKnob(name="Output"))
        # self.header.fillColor = QtGui.QColor(36, 128, 18)

class AvgPool3d(Node):

    def __init__(self, *args, **kwargs):
        super(AvgPool3d, self).__init__(*args, **kwargs)
        self.addHeader(Header(node=self, text="AvgPool3d"))
        self.addKnob(InputKnob(name="Input"))
        self.addKnob(OutputKnob(name="Output"))
        # self.header.fillColor = QtGui.QColor(36, 128, 18)

class FractionalMaxPool2d(Node):

    def __init__(self, *args, **kwargs):
        super(FractionalMaxPool2d, self).__init__(*args, **kwargs)
        self.addHeader(Header(node=self, text="FractionalMaxPool2d"))
        self.addKnob(InputKnob(name="Input"))
        self.addKnob(OutputKnob(name="Output"))
        # self.header.fillColor = QtGui.QColor(36, 128, 18)

class LPPool1d(Node):

    def __init__(self, *args, **kwargs):
        super(LPPool1d, self).__init__(*args, **kwargs)
        self.addHeader(Header(node=self, text="LPPool1d"))
        self.addKnob(InputKnob(name="Input"))
        self.addKnob(OutputKnob(name="Output"))
        # self.header.fillColor = QtGui.QColor(36, 128, 18)

class LPPool2d(Node):

    def __init__(self, *args, **kwargs):
        super(LPPool2d, self).__init__(*args, **kwargs)
        self.addHeader(Header(node=self, text="LPPool2d"))
        self.addKnob(InputKnob(name="Input"))
        self.addKnob(OutputKnob(name="Output"))
        # self.header.fillColor = QtGui.QColor(36, 128, 18)

class AdaptiveMaxPool1d(Node):

    def __init__(self, *args, **kwargs):
        super(AdaptiveMaxPool1d, self).__init__(*args, **kwargs)
        self.addHeader(Header(node=self, text="AdaptiveMaxPool1d"))
        self.addKnob(InputKnob(name="Input"))
        self.addKnob(OutputKnob(name="Output"))
        # self.header.fillColor = QtGui.QColor(36, 128, 18)

class AdaptiveMaxPool2d(Node):

    def __init__(self, *args, **kwargs):
        super(AdaptiveMaxPool2d, self).__init__(*args, **kwargs)
        self.addHeader(Header(node=self, text="AdaptiveMaxPool2d"))
        self.addKnob(InputKnob(name="Input"))
        self.addKnob(OutputKnob(name="Output"))
        # self.header.fillColor = QtGui.QColor(36, 128, 18)
    
class AdaptiveMaxPool3d(Node):

    def __init__(self, *args, **kwargs):
        super(AdaptiveMaxPool3d, self).__init__(*args, **kwargs)
        self.addHeader(Header(node=self, text="AdaptiveMaxPool3d"))
        self.addKnob(InputKnob(name="Input"))
        self.addKnob(OutputKnob(name="Output"))
        # self.header.fillColor = QtGui.QColor(36, 128, 18)

class AdaptiveAvgPool1d(Node):

    def __init__(self, *args, **kwargs):
        super(AdaptiveAvgPool1d, self).__init__(*args, **kwargs)
        self.addHeader(Header(node=self, text="AdaptiveAvgPool1d"))
        self.addKnob(InputKnob(name="Input"))
        self.addKnob(OutputKnob(name="Output"))
        # self.header.fillColor = QtGui.QColor(36, 128, 18)

class AdaptiveAvgPool2d(Node):

    def __init__(self, *args, **kwargs):
        super(AdaptiveAvgPool2d, self).__init__(*args, **kwargs)
        self.addHeader(Header(node=self, text="AdaptiveAvgPool2d"))
        self.addKnob(InputKnob(name="Input"))
        self.addKnob(OutputKnob(name="Output"))
        # self.header.fillColor = QtGui.QColor(36, 128, 18)

class AdaptiveAvgPool3d(Node):

    def __init__(self, *args, **kwargs):
        super(AdaptiveAvgPool3d, self).__init__(*args, **kwargs)
        self.addHeader(Header(node=self, text="AdaptiveAvgPool3d"))
        self.addKnob(InputKnob(name="Input"))
        self.addKnob(OutputKnob(name="Output"))
        # self.header.fillColor = QtGui.QColor(36, 128, 18)

class ReflectionPad1d(Node):

    def __init__(self, *args, **kwargs):
        super(ReflectionPad1d, self).__init__(*args, **kwargs)
        self.addHeader(Header(node=self, text="ReflectionPad1d"))
        self.addKnob(InputKnob(name="Input"))
        self.addKnob(OutputKnob(name="Output"))
        # self.header.fillColor = QtGui.QColor(36, 128, 18)

class ReflectionPad2d(Node):

    def __init__(self, *args, **kwargs):
        super(ReflectionPad2d, self).__init__(*args, **kwargs)
        self.addHeader(Header(node=self, text="ReflectionPad2d"))
        self.addKnob(InputKnob(name="Input"))
        self.addKnob(OutputKnob(name="Output"))
        # self.header.fillColor = QtGui.QColor(36, 128, 18)

class ReplicationPad1d(Node):

    def __init__(self, *args, **kwargs):
        super(ReplicationPad1d, self).__init__(*args, **kwargs)
        self.addHeader(Header(node=self, text="ReplicationPad1d"))
        self.addKnob(InputKnob(name="Input"))
        self.addKnob(OutputKnob(name="Output"))
        # self.header.fillColor = QtGui.QColor(36, 128, 18)

class ReplicationPad2d(Node):

    def __init__(self, *args, **kwargs):
        super(ReplicationPad2d, self).__init__(*args, **kwargs)
        self.addHeader(Header(node=self, text="ReplicationPad2d"))
        self.addKnob(InputKnob(name="Input"))
        self.addKnob(OutputKnob(name="Output"))
        # self.header.fillColor = QtGui.QColor(36, 128, 18)

class ReplicationPad3d(Node):

    def __init__(self, *args, **kwargs):
        super(ReplicationPad3d, self).__init__(*args, **kwargs)
        self.addHeader(Header(node=self, text="ReplicationPad3d"))
        self.addKnob(InputKnob(name="Input"))
        self.addKnob(OutputKnob(name="Output"))
        # self.header.fillColor = QtGui.QColor(36, 128, 18)

class ZeroPad2d(Node):

    def __init__(self, *args, **kwargs):
        super(ZeroPad2d, self).__init__(*args, **kwargs)
        self.addHeader(Header(node=self, text="ZeroPad2d"))
        self.addKnob(InputKnob(name="Input"))
        self.addKnob(OutputKnob(name="Output"))
        # self.header.fillColor = QtGui.QColor(36, 128, 18)

class ConstantPad1d(Node):

    def __init__(self, *args, **kwargs):
        super(ConstantPad1d, self).__init__(*args, **kwargs)
        self.addHeader(Header(node=self, text="ConstantPad1d"))
        self.addKnob(InputKnob(name="Input"))
        self.addKnob(OutputKnob(name="Output"))
        # self.header.fillColor = QtGui.QColor(36, 128, 18)

class ConstantPad2d(Node):

    def __init__(self, *args, **kwargs):
        super(ConstantPad2d, self).__init__(*args, **kwargs)
        self.addHeader(Header(node=self, text="ConstantPad2d"))
        self.addKnob(InputKnob(name="Input"))
        self.addKnob(OutputKnob(name="Output"))
        # self.header.fillColor = QtGui.QColor(36, 128, 18)

class ConstantPad3d(Node):

    def __init__(self, *args, **kwargs):
        super(ConstantPad3d, self).__init__(*args, **kwargs)
        self.addHeader(Header(node=self, text="ConstantPad3d"))
        self.addKnob(InputKnob(name="Input"))
        self.addKnob(OutputKnob(name="Output"))
        # self.header.fillColor = QtGui.QColor(36, 128, 18)

class Linear(Node):

    def __init__(self, *args, **kwargs):
        super(Linear, self).__init__(*args, **kwargs)
        self.addHeader(Header(node=self, text="Linear"))
        self.addKnob(InputKnob(name="Input"))
        self.addKnob(OutputKnob(name="Output"))
        # self.header.fillColor = QtGui.QColor(36, 128, 18)



class BigNode(Node):

    def __init__(self, *args, **kwargs):
        super(BigNode, self).__init__(*args, **kwargs)
        self.addHeader(Header(node=self, text="BigNode"))
        self.addKnob(InputKnob(name="i1"))
        self.addKnob(OutputKnob(name="o1"))
        self.addKnob(InputKnob(name="i2"))
        self.addKnob(OutputKnob(name="o2"))
        self.addKnob(InputKnob(name="i3"))
        self.addKnob(OutputKnob(name="o3"))
        self.addKnob(InputKnob(name="i4"))
        self.addKnob(OutputKnob(name="o4"))
        self.addKnob(InputKnob(name="i5"))
        self.addKnob(OutputKnob(name="o5"))
        self.addKnob(InputKnob(name="i6"))
        self.addKnob(OutputKnob(name="o6"))
        self.addKnob(InputKnob(name="i7"))
        self.addKnob(OutputKnob(name="o7"))
        self.addKnob(InputKnob(name="i8"))
        self.addKnob(OutputKnob(name="o8"))
        self.addKnob(InputKnob(name="i9"))
        self.addKnob(OutputKnob(name="o9"))


class Directory(Node):

    def __init__(self, *args, **kwargs):
        super(Directory, self).__init__(*args, **kwargs)
        self.addHeader(Header(node=self, text="Directory"))
        self.addKnob(InputKnob(name="parent"))
        self.addKnob(OutputKnob(name="children"))


class File(Node):

    def __init__(self, *args, **kwargs):
        super(File, self).__init__(*args, **kwargs)
        self.addHeader(Header(node=self, text="File"))
        self.addKnob(InputKnob(name="parent"))


class MaxObject(Node):

    def __init__(self):
        super(MaxObject, self).__init__()
        self.addHeader(Header(node=self, text=self.__class__.__name__))
        self.addKnob(InputKnob(name="children"))
        self.addKnob(OutputKnob(name="parent"))

