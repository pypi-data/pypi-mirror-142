from typing import Generic, TypeVar, get_args, get_origin
from dataclasses import fields

from serde import from_dict, serde, to_dict

T = TypeVar('T')

U = TypeVar('U')


@serde
class Bar:
    n: int


@serde
class Foo(Generic[T, U]):
    a: T
    b: U


def main():
    f = Foo[Bar, int](Bar(10), 10)
    d = to_dict(f)
    ff = fields(Foo)[0]
    df = fields(Foo)[1]
    print(type(ff.type), ff.type.__name__, type(df.type), df.type.__name__)
    print(d)
    print(get_args(Foo[Bar, int]))
    print(get_args(Foo))
    print(get_origin(Foo))
    print(Foo.__class__)
    print(Foo.__bases__)
    generic = Foo.__bases__[0]
    print(get_args(generic))
    generics = Foo.__orig_bases__[0]
    print(generics)
    print(get_args(generics))
    args = get_args(generics)
    print(args[0].__name__)
    print(args[1].__name__)
    print(type(generics))
    print(get_origin(Foo[Bar, int]))
    print(get_origin(Foo))
    print("__serde__", hasattr(Foo, "__serde__"))
    print(get_origin(Foo[int, str]))
    print("__serde__", hasattr(get_origin(Foo[int, str]), "__serde__"))
    f = Foo[int, str](10, "a")
    print("__serde__", hasattr(f, "__serde__"))
    # print(generics[0], generics[1])

if __name__ == "__main__":
    main()

