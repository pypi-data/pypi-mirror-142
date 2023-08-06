""" Report header """
from ..text_align import TextAlignment

class ReportHeader:
  """
  Report header definition

  Available attributes
  --------------------
    label (str): Display name
    size (tuple(float, float)): Size (width, height) of the cell, in points (pt)
    color (str): Cell color
    text_color (str): Text color
    align (TextAlignment): Text Alignment
  """
  def __init__(self, label, size, color, text_color, align=TextAlignment.CENTER):
    self.__label = label
    self.__size = size
    self.__color = color
    self.__text_color = text_color
    self.__align = align

  @property
  def label(self):
    """ Display name """
    return self.__label

  @property
  def size(self):
    """ Size (width, height) of the cell, in points (pt) """
    return self.__size

  @property
  def color(self):
    """ Cell color """
    return self.__color

  @property
  def text_color(self):
    """ Text color """
    return self.__text_color

  @property
  def align(self):
    """ Text Alignment """
    return self.__align

  def __str__(self):
    """ Readable property """
    return f'ReportHeader(label={self.label}, size={self.size}, color={self.color}, text_color={self.text_color}, align={self.align})'

  def __repr__(self):
    """ Readable property """
    return f'ReportHeader(label={self.label}, size={self.size}, color={self.color}, text_color={self.text_color}, align={self.align})'
