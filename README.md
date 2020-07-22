# livecover-py

## Installation

```
pip install livecover
```

## Quickstart

### Tornado

```python

from livecover import get_coverage

class MyHandler(RequestHandler):

    def prepare(self):
        get_coverage(ratio=0.1, entrypoint=self.__class__.__name__)
```
