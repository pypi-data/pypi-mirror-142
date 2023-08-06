""" Report row """
from ..text_align import TextAlignment

class ReportRow:
  """
  Report row definition

  Available attributes
  --------------------
    label (str): Display name
    height (float): Height of the cell, in points (pt)
    color (str): Cell color
    text_color (str): Text color
    align (TextAlignment): Text Alignment
    compact (bool): Compact mode
  """
  def __init__(self, label, height, color, text_color, compact=False, align=TextAlignment.LEFT):
    self.__label = label
    self.__height = height
    self.__color = color
    self.__text_color = text_color
    self.__align = align
    self.__compact = compact

  @property
  def label(self):
    """ Display name """
    return self.__label

  @property
  def height(self):
    """ Height of the cell, in points (pt) """
    return self.__height

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

  @property
  def compact(self):
    """ Compact mode """
    return self.__compact

  def __str__(self):
    """ Readable property """
    return f'ReportRow(label={self.label}, height={self.height}, color={self.color}, text_color={self.text_color}, align={self.align}, compact={self.compact})'

  def __repr__(self):
    """ Readable property """
    return f'ReportRow(label={self.label}, height={self.height}, color={self.color}, text_color={self.text_color}, align={self.align}, compact={self.compact})'