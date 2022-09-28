# py-amazing-marvin

A Python 3 package providing a _very_ limited and experimental API client for [Amazing Marvin](https://amazingmarvin.com/).

## Features

- Retrieve some information about your account (`AmazingMarvinAPI.me`)
- Get tasks and projects scheduled for today (`AmazingMarvinAPI.today_items`)

## Installation with pip

```
pip install git+https://github.com/ustuehler/py-amazing-marvin
```

## Usage

To use this package, you must have an [active subscription](https://app.amazingmarvin.com/signup) and [API token](https://app.amazingmarvin.com/pre?api) for Amazing Marvin.

Example:

```python
import os
from amazing_marvin import AmazingMarvinAPI

# Get your API token from somewhere
api_token = os.environ['AMAZING_MARVIN_API_TOKEN']

# Create an instance of the experimental API client
client = AmazingMarvinAPI(api_token)

# Retrieve some information about your account
client.me()

# Get tasks and projects scheduled for today
client.today_items()
```

## Contributing

See the [Contributing Guide](CONTRIBUTING.md) for instructions on how to set up
a local environment for development and testing.

## License

[MIT](LICENSE)
