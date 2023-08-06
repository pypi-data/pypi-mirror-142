""" Report class """

class Report:
  """
  Report definition

  Available attributes
  --------------------
    name (str): Report name. The exported name will have an timestamp to prevent duplicity in our servers.
    pages (list(ReportPage)): List of pages to append into report
    format (ReportFormat): Format to export the report
  """
  def __init__(self, name, pages, format):
    self.__name = name
    self.__pages = pages
    self.__format = format

  @property
  def name(self):
    """ Report name. The exported name will have an timestamp to prevent duplicity in our servers. """
    return self.__name

  @property
  def pages(self):
    """ List of pages to append into report """
    return self.__pages

  @property
  def format(self):
    """ Format to export the report """
    return self.__format

  def __str__(self):
    """ Readable property """
    return f'Report(name={self.name}, pages={self.pages}, format={self.format})'

  def __repr__(self):
    """ Readable property """
    return f'Report(name={self.name}, pages={self.pages}, format={self.format})'
