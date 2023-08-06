""" Report col """
from ..text_align import TextAlignment

class ReportCol:
  """
  Report col definition

  Available attributes
  --------------------
    content (str): Display content
    color (str): Cell color
    text_color (str): Text color
    align (TextAlignment): Text Alignment
  """
  def __init__(self, content, color='#ffffff', text_color='#000000', align=TextAlignment.LEFT):
    self.__content = content
    self.__color = color
    self.__text_color = text_color
    self.__align = align

  @property
  def content(self):
    """ Display content """
    return self.__content

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
    return f'ReportCol(content={self.content}, color={self.color}, text_color={self.text_color}, align={self.align})'

  def __repr__(self):
    """ Readable property """
    return f'ReportCol(content={self.content}, color={self.color}, text_color={self.text_color}, align={self.align})'
