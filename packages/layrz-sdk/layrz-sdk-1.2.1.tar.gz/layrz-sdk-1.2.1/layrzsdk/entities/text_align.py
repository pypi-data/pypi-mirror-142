""" Text alignment """
from enum import Enum

class TextAlignment:
  """ Text alignment enum definition """
  CENTER = 'center'
  LEFT = 'left'
  RIGHT = 'right'
  JUSTIFY = 'justify'

  @property
  def __readable(self):
    """ Readable """
    return f'TextAlignment.{self.value}'

  def __str__(self):
    """ Readable property """
    return self.__readable

  def __repr__(self):
    """ Readable property """
    return self.__readable
