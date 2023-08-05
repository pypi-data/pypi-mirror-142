# type-converter

type-converter is provides type conversion of lists, dictionaries, sets and tuples. With this function, you can simply convert the type you want 🤟.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install type-converter.

```bash
pip install py-type-converter
```

## Usage

```python
import py_type_converter as converter

# returns 'list'
my_set = {1, 2, "three"}
converter.set_to_list(my_set)
# output: [1, 2, "three"]

# returns 'set'
my_tuple = ("one", "two", "three", "three")
converter.tuple_to_set(my_tuple)
# output: {"one", "two", "three"}

# returns 'list'
my_dict = {"a":1, "b":2, "c":3}
converter.dict_values_to_list(my_dict)
# output: [1, 2, 3]

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)