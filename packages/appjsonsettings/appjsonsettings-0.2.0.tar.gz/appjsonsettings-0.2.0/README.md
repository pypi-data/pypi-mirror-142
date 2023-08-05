# appjsonsettings
[![PayPal Donate][paypal_img]][paypal_link]
[![PyPI version][pypi_img]][pypi_link]
[![Downloads][downloads_img]][downloads_link]
[![Documentation Status][docs_img]][docs_link]

  [paypal_img]: https://github.com/jacklinquan/images/blob/master/paypal_donate_badge.svg
  [paypal_link]: https://www.paypal.me/jacklinquan
  [pypi_img]: https://badge.fury.io/py/appjsonsettings.svg
  [pypi_link]: https://badge.fury.io/py/appjsonsettings
  [downloads_img]: https://pepy.tech/badge/appjsonsettings
  [downloads_link]: https://pepy.tech/project/appjsonsettings
  [docs_img]: https://readthedocs.org/projects/appjsonsettings/badge/?version=latest
  [docs_link]: https://appjsonsettings.readthedocs.io/en/latest/?badge=latest

A Python module for easy application settings in JSON format.

## Installation
`pip install appjsonsettings`

## Usage
``` python
>>> import appjsonsettings
>>> settings_file_path = "settings.json"
>>> default_settings = {'a': 0, 'b': 'hello', 'c': []}
>>> # In case the file does not exist, it creates a new one with default_settings.
>>> settings = appjsonsettings.load(settings_file_path, default_settings)
>>> settings
{'a': 0, 'b': 'hello', 'c': []}
>>> settings['a'] += 1
>>> settings['b'] += ' world!'
>>> settings['c'].append(1.23)
>>> appjsonsettings.save(settings_file_path, settings)
>>> settings = appjsonsettings.load(settings_file_path, default_settings)
>>> settings
{'a': 1, 'b': 'hello world!', 'c': [1.23]}
```
