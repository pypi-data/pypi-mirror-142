import setuptools

with open('README.md', 'r') as fh:
	long_description = fh.read()

setuptools.setup(
	name='py_ext_to_format',
	version='0.0.1',
	author='Elon Salfati',
	author_email='elon@salfati.io',
	description='A simple tool to convert file extensions to file formats',
	long_description=long_description,
	long_description_content_type='text/markdown',
	url='https://github.com/elonsalfati/py-ext-to-format',
	packages=setuptools.find_packages(),
	package_data={'py_ext_to_format': ['formats.json']},
)
