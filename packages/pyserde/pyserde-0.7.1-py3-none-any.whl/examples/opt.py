from serde import serde
from serde.json import to_json, from_json
from typing import Optional

@serde
class Bar:
    c: Optional[int]

@serde
class Foo:
    a: Optional[int]
    b: Optional[Bar]


if __name__ == "__main__":
    f = Foo(10, Bar(100))
    s = to_json(f)
    print(s)
    f = from_json(Foo, s)
    print(f)

    s = to_json(10)
    print(s)
    v = from_json(Optional[int], s)
    print(v)
