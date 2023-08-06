# Python Extension to File Format

This small package returns the file format of a given file extension or `Unknown` if file extension is unknown.

## Installation
```sh
pip install py-ext-to-format
```

## Usage
```python
from py_ext_to_format import ExtToFormat

converter = ExtToFormat()
converter.get_format('.js') # returns JavaScript
```

## Contribution
We'd love contributions to the known file extensions/formats.

Any file extension and its file format is available under `py_ext_to_format/formats.json`.

```json
{
	".js": "JavaScript"
}
```
