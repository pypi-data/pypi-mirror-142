# python-gotify

This python module allows to manage and send messages to your [gotify server](https://github.com/gotify/server) without handling requests manually.

## Installation

python-gotify can be installed from [PyPi](https://pypi.org/project/gotify/) using pip:

```
pip install gotify
```

## Usage

To send messages:

```python
from gotify import Gotify

gotify = Gotify(
    base_url="https://gotify.example.com",
    app_token="AsWIJhvlHb.xgKe",
)

gotify = Gotify(
    "Hello you wonderful people!",
    title="Hello World",
    priority=0,
)
```

**Note:** To send messages you need to create a new application and set `app_token` accordingly.

You can also manage things like applications:

```python
from gotify import Gotify

gotify = Gotify(
    base_url="https://gotify.example.com",
    client_token="CoLwHBCAr8z2MMA",
)

app = gotify.create_application("foobar", description="test application")

print("Created new application:", app)
```

would result in

```plain
Created new application: {'id': 42, 'token': 'ArHD_yGYf63-A13', 'name': 'foobar', 'description': 'test application', 'internal': False, 'image': 'static/defaultapp.png'}
```

**Note:** For most things you need to create a new client and set `client_token` accordingly.

This module tries to implement every endpoint of the gotify API as an instance method of the `Gotify` class.

More details about the capabilities of gotify's API can be found in its [API documentation](https://gotify.net/api-docs).

**Note:** since I don't use any gotify plugins, plugin-related functions are completely untested.
