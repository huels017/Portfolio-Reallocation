import unittest
import pandas as pd
from reallocate.data_container import DataContainer

class TestDataContainer(unittest.TestCase):

	def setUp(self):
		self.rows = ['R1', 'R2', 'R3']
		self.data = {'col1': [1, 2.4, 5.4], 'col2': [3, 0, 1.2], 'col3': [6.1, 9.2, 7.4]}
		
		dataframe = pd.DataFrame(data=self.data, index=self.rows)
		self.data_container = DataContainer(dataframe)

	def test_can_get_value(self):
		returned_value = self.data_container.getValue('R1', 'col1')
		ROW_INDEX = 0
		self.assertEqual(self.data['col1'][ROW_INDEX], returned_value)

	def test_can_set_value(self):
		NEW_VALUE = 8765
		self.data_container.setValue('R2', 'col3', NEW_VALUE)
		self.assertEqual(NEW_VALUE, self.data_container.getValue('R2', 'col3'))

	def test_can_get_columns(self):
		keys = ['col2', 'col3']
		filtered_data = dict((k, self.data[k]) for k in keys if k in self.data)
		expected_dataframe = pd.DataFrame(data=filtered_data, index=self.rows)

		dataframes_are_equal = self.data_container.getColumns(['col2', 'col3']).equals(expected_dataframe)
		self.assertTrue(dataframes_are_equal)

	def test_can_get_header_names(self):
		# Convert to sets because we don't care about the order of the returned names;
		# also makes comparing easy since lists with elements in different orders may
		# be seen as "unequal"
		self.assertEqual(set(self.data.keys()), set(self.data_container.getHeaderNames()))

	def test_can_get_row_names(self):
		self.assertEqual(set(self.rows), set(self.data_container.getRowNames()))

	def test_can_get_number_of_rows(self):
		self.assertEqual(len(self.rows), self.data_container.numberOfRows())

	def test_can_get_number_of_columns(self):
		self.assertEqual(len(self.data.keys()), self.data_container.numberOfColumns())
