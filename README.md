# csv2json-fixture
This script can be used to convert CSV data to [Django fixtures](https://docs.djangoproject.com/en/stable/howto/initial-data/) JSON format.

## Requirements
* Python 3.x

## Usage
```
python csv2json.py file.csv app.Model
python manage.py loaddata file.json
```

## License
This is a Korean port of [maur1th's code](https://github.com/maur1th/csv2json-fixture) which is a Python 3 port of [Brian Gershon's code](https://djangosnippets.org/snippets/1680/) licensed under the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0)
