import typing

import dataclasses

from marshmallow_annotations.ext.dataclasses import DataClassSchema


@dataclasses.dataclass
class SomeDataClass:
    a: int
    b: typing.Optional[int]
    c: typing.Optional[int] = 5


def test_instance_conversion(registry_):
    class SomeDataClassSchema(DataClassSchema):
        class Meta:
            registry = registry_
            target = SomeDataClass

    s = SomeDataClassSchema(DataClassSchema)
    result = s.load({'a': 1, 'b': 2, 'c': 3})

    expected = SomeDataClass(a=1, b=2, c=3)
    assert not result.errors
    assert result.data == expected


def test_missing_values(registry_):
    class SomeDataClassSchema(DataClassSchema):
        class Meta:
            registry = registry_
            target = SomeDataClass

    s = SomeDataClassSchema(DataClassSchema)
    result = s.load({'a': 1})

    expected = SomeDataClass(a=1, b=None, c=5)
    assert not result.errors
    assert result.data == expected


def test_dump(registry_):
    class SomeDataClassSchema(DataClassSchema):
        class Meta:
            registry = registry_
            target = SomeDataClass

    s = SomeDataClassSchema(DataClassSchema)
    result = s.dump(SomeDataClass(a=1, b=None, c=5))

    expected = {'a': 1, 'b': None, 'c': 5}
    assert not result.errors
    assert result.data == expected
