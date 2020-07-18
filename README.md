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
        super().prepare()
        self.coverage = get_coverage(api_key=..., entrypoint=self.__class__.__name__)

    def before_finish(self, my_data):
        self.coverage.finish()
        self.finish(...)
```
