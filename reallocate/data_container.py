import pandas as pd

class DataContainer(object):
	""" Represents data from an Excel worksheet.
	"""

	def __init__(self, dataframe):
		""" Initialize an instance of this class.
		
		Args:
			dataframe (dataframe): A pandas dataframe representing the data.
		"""
		self.data = dataframe.copy(deep=True)

	def __getitem__(self, indices):
		row, column = indices
		return self.getValue(row, column)

	def getValue(self, row, column):
		"""Get the value at the intersection of (row, column).

		Args:
			row (string): The row.
			column (string): The column.

		Returns:
			The data at point (row, column).
		"""
		return self.data.at[row, column]

	def setValue(self, row, column, value):
		"""Set the value at the intersection of (row, column).

		Args:
			row (string): The row.
			column (string): The column.
			value: The new value that should be set.
		"""
		self.data.at[row, column] = value

	def getColumns(self, columns):
		"""Get the values from the specified columns; the columns are returned
		in the specified order.

		Args:
			columns (list): A list of columns to select. The columns are
			returned in the same order as in the provided list.

		Example:
			getColumns(['Cash/MMKT', 'Sm/Mid Growth'])
		
		Returns: 
			A pandas dataframe with the specified columns.
		"""
		return self.data[columns]

	def getHeaderNames(self):
		"""Get the names of each column.

		Returns:
			A list of all column names.
		"""
		return list(self.data)

	def getRowNames(self):
		"""Get the names of each row.

		Returns:
			A list of all row names.
		"""
		return list(self.data.index)

	def numberOfRows(self):
		"""Get the number of rows.

		Returns:
			The number of rows.
		"""
		numberOfRows, numberOfColumns = self.data.shape
		return numberOfRows

	def numberOfColumns(self):
		"""Get the number of columns.

		Returns:
			The number of columns.
		"""
		numberOfRows, numberOfColumns = self.data.shape
		return numberOfColumns
