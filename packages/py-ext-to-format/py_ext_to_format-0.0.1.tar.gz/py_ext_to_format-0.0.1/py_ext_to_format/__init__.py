import json
import importlib.resources


class ExtToFormat:
	'''
	Converts file extensions to file formats
	'''

	def __init__(self):
		'''
		Load the file formats
		'''
		with importlib.resources.open_text('py_ext_to_format', 'formats.json') as file:
			self.file_formats = json.load(file)

	def get_format(self, ext: str) -> str:
		'''
		Get the file format for a given extension
		'''
		return self.file_formats.get(ext.lower(), 'Unknown')
