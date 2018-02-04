import pandas as pd
import data_container as dc

def importExcel(fileName, header):
	"""Import an Excel file.

	Args:
		fileName (string): Path to the Excel file (example: "./excel/accounts.xlsx")
		header (int): Row which contains the header labels

	Returns: 
		dict: A dictionary of dataframes each representing an Excel worksheet

	"""
	# Use the first column as the row-labels of the DataFrame
	EXCEL_INDEX_COL = 0
	excelFile = pd.ExcelFile(fileName)

	# Setting sheet_name=None requests all sheets
	dataframes = excelFile.parse(sheet_name=None, header=header, index_col=EXCEL_INDEX_COL)
	return dataframes
