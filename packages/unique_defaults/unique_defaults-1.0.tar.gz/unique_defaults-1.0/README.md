# unique_defaults

Guarantee new objects are used for each function call.

This allows writing signatures with mutable defaults *without* sharing the
underlying object between function calls.

```python
from unique_defaults import unique_lists

def classic(a=[]):
    a.append("again")
    return " ".join(a)

classic() == "again"
classic() == "again again"

@unique_lists
def unique(a=[]):
    a.append("again")
    return " ".join(a)

unique() == "again"
unique() == "again"
```

Using the mutable object directly in the function signature leads to shorter and
more accurate annotations, as well as simplifying the function's logic.

```python
from typing import List, Optional
from unique_defaults import unique_lists

def classic(a: Optional[List] = None):
    if a is None:
        a = []
    a.append("again")
    return " ".join(a)

classic() == "again"
classic() == "again"

@unique_lists
def unique(a: List = []):
    a.append("again")
    return " ".join(a)

unique() == "again"
unique() == "again"
```

Individual arguments can be targeted, instead of a general type.

```python
from unique_defaults import unique_defaults

@unique_defaults('line_list')
def log_list(line_list=[], _running_log=[]):
    line_list[:0] = ["NOTICE:"]
    line = " ".join(line_list)
    _running_log.append(line)
    return _running_log

log_list(["first"]) == ["NOTICE: first"]
log_list(["second"]) == ["NOTICE: first", "NOTICE: second"]
```

Any types can be made unique

```python
from unique_defaults import unique_defaults

class Count:
    def __init__(self):
        self.count = 0
    def add(self, n):
        self.count += n

def classic(a=Count()):
    a.add(1)
    return a

classic().count == 1
classic().count == 2

@unique_defaults(Count)
def unique(a=Count()):
    a.add(1)
    return a

unique().count == 1
unique().count == 1
```
