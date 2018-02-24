import excel_import
import data_container as dc
 


class AccountType:

	def __init__(self, name, tax_status, is_deferred, is_exempt, changes_allowed, limited):
		self.name = name
		self.tax_status = tax_status
		self.is_deferred = is_deferred
		self.is_exempt = is_exempt
		self.changes_allowed = changes_allowed
		self.limited = limited


#Do I need to use data from the data container to start populating each instance? Do you know how to do this?

#Is this ultimately going to be incorporated into the main_functions.py folder?

 