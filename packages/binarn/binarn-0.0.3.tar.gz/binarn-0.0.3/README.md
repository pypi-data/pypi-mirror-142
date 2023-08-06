# binarn

**binarn** is a small tool to find an arbitrary key in a deep dictionary. It returns the full path
to that key (if any) as well as its value.

It is intended as a debugging/exploration tool only.

## Install

    pip install binarn

## Usage

```python3
import binarn

binarn.find_one(my_deep_dict, key="my_key")
# => (("key1", "key2", "my_key"), "value")
```

## Origin of the name

"binarn" may look like a random name, but it has a true meaning. It stands for "binarn is not a
random name".
