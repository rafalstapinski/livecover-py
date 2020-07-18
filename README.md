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
        self.coverage = get_coverage(ratio=0.1, entrypoint=self.__class__.__name__)

    def before_finish(self, my_data):
        self.coverage.finish()
        self.finish(...)
```
