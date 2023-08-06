# tuuid

**tuuid** is a Python library for generating unique identifers that are:

- Small (only 13 characters)
- URL safe
- Guaranteed to be unique (see below)
- Able to be decoded to a `datetime.datetime` or timestamp

Internally, a `threading.Lock` mutex is used to ensure unique values across the system.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install tuuid
```

## Usage

```python
import tuuid

tuuid.random()
# returns 'gJD9zjQwq4AkD'

tuuid.decode('gJD9zjQwq4AkD')
# returns 'datetime.datetime(2022, 3, 13, 3, 11, 11)'

```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/). You can freely use tuuids in open source projects and commercial products.
