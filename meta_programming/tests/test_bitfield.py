import re
from weakref import WeakKeyDictionary

import pytest


class BitFieldBase:
    def __init__(self, **kwargs):
        self._validate_arg_names(kwargs)


        for field_name in type(self)._field_widths.keys():
            setattr(self, field_name, kwargs.get(field_name, 0))

    def __setattr__(self, name, value):
        self._validate_arg_values({f'{name}': value})
        super().__setattr__(name, value)

    def _validate_arg_names(self, kwargs):
        mismatched_args = set(kwargs) - set(type(self)._field_widths)

        if len(mismatched_args) != 0:
            mismatched_args_txt = ', '.join(repr(arg_name) for arg_name in kwargs if arg_name in mismatched_args)

            raise TypeError(
                f"{type(self).__name__}.__init__() got unexpected"
                f" keyword argument{'' if len(mismatched_args) == 1 else 's'}: {mismatched_args_txt}"
            )

    def __int__(self):
        #TODO rethink
        accumulator = 0
        shift = 0

        for name, width in type(self)._field_widths.items():
            value = getattr(self, name)
            accumulator |= value << shift
            shift += width
        return accumulator

    def to_bytes(self):
        v = int(self)
        num_bytes = sum(type(self)._field_widths.values()) + 7 // 8
        return v.to_bytes(
            length=num_bytes,
            byteorder="little",
            signed=False,
        )


class BitFieldDescriptor:

    def __init__(self, name,  width):
        self._instande_data = WeakKeyDictionary()
        self._width = width
        self._name = name

    def __get__(self, instance, owner):


    def __set__(self, instance, value):
        min_value = 0
        max_value = 2 ** self._width - 1
        if not (min_value <= value <= max_value):
            raise ValueError(
                f"{type(instance).__name__} field {self._name!r} "
                f"got value {value} which is out of "
                f"range {min_value}-{max_value} for a {self._width} bit field"
            )

        self._instande_data[instance] = value


class BitFieldMeta(type):
    def __new__(mcs, name, bases, namespace, **kwargs):
        try:
            namespace["_field_widths"] = namespace["__annotations__"]
        except KeyError as e:
            raise TypeError(f'{name} with metaclass "{mcs.__name__}" has no fields.') from e

        for field_name, width in namespace["_field_widths"].items():
            if field_name.startswith("_"):
                raise TypeError(
                    f"{name} field {field_name!r} begins with an underscore"
                )

            if not isinstance(width, int):
                raise TypeError(
                    f"{name} field {field_name!r} has annotation {width!r} that is not an integer"
                )

            if width < 1:
                raise TypeError(
                    f"{name} field {field_name!r} has non-positive field width {width!r}"
                )

        for field_name, width in namespace["_field_widths"].items():
            namespace[field_name] = BitFieldDescriptor(field_name, width)

        bases = (BitFieldBase,) + bases
        return super().__new__(mcs, name, bases, namespace)


def test_define_bitfield():
    class DateBitField(metaclass=BitFieldMeta):
        day: 5


def test_instantiate_default_bitfield():
    class DateBitField(metaclass=BitFieldMeta):
        day: 5

    _ = DateBitField(day=23)


def test_bitfield_without_fields_raises_type_error():
    with pytest.raises(TypeError, match='EmptyBitField with metaclass "BitFieldMeta" has no fields.'):
        class EmptyBitField(metaclass=BitFieldMeta):
            pass


def test_mismatched_constructor_argument_names_raises_type_error():
    class DateBitField(metaclass=BitFieldMeta):
        day: 5
        month: 4
        year: 14

    with pytest.raises(TypeError, match=re.escape("DateBitField.__init__() got unexpected"
                                                  " keyword arguments: 'mnth', 'yr'")):
        DateBitField(day=13, mnth=5, yr=1999)


def test_non_integer_annotation_value_raises_type_error():
    with pytest.raises(TypeError, match=re.escape("DateBitField field 'day'"
                                                  " has annotation 'Wednesday' that is not an integer")):
        class DateBitField(metaclass=BitFieldMeta):
            day: "Wednesday"


def test_negative_field_width_raises_type_error():
    with pytest.raises(TypeError, match=re.escape("DateBitField field 'day'"
                                                  " has non-positive field width -1")):
        class DateBitField(metaclass=BitFieldMeta):
            day: -1


def test_field_name_with_leading_underscore_raises_type_error():
    with pytest.raises(TypeError, match=re.escape("DateBitField field '_day'"
                                                  " begins with an underscore")):
        class DateBitField(metaclass=BitFieldMeta):
            _day: 5


def test_initialization_out_of_upper_field_range_raises_value_error():
    class DateBitField(metaclass=BitFieldMeta):
        day: 5

    with pytest.raises(ValueError, match=re.escape("DateBitField field 'day' got value 32 "
                                                   "which is out of range 0-31 for a 5 bit field")):
        DateBitField(day=32)


def dest_fields_are_default_initialized_to_zero():
    class DateBitField(metaclass=BitFieldMeta):
        day: 5

    d = DateBitField()
    assert d.day == 0


def test_initialized_field_values_can_be_retrived():
    class DateBitField(metaclass=BitFieldMeta):
        day: 5

    d = DateBitField(day=15)
    assert d.day == 15


def test_conversion_to_integer():
    class DateBitField(metaclass=BitFieldMeta):
        day: 5
        month: 4
        year: 14

    d = DateBitField(day=25, month=3, year=2010)
    i = int(d)

    assert (i ==
            0b00011111011010_0011_11001
            # < -------2010> <-3> <-25>
            # bin(2010)
            )

def test_conversion_to_bytes(): # TODO unfinnished
    class DateBitField(metaclass=BitFieldMeta):
        day: 5
        month: 4
        year: 14

    d = DateBitField(day=25, month=3, year=2010)
    b = d.to_bytes()

    assert (b ==
            (0b00011111011010_0011_11001).to_bytes(3, "little", signed=False)
            # < -------2010> <-3> <-25>
            # bin(2010)
            )

def tes_assigning_to_field_sets_value():
    class DateBitField(metaclass=BitFieldMeta):
        day: 5

    d = DateBitField()
    d.day = 26
    assert d.day == 26

def test_assigning_out_of_upper_range_to_field_raises_value_error():
    class DateBitField(metaclass=BitFieldMeta):
        day: 5

    d = DateBitField()
    with pytest.raises(ValueError, match=re.escape("DateBitField field 'day' got value 32 "
                                                   "which is out of range 0-31 for a 5 bit field")):
        d.day = 32

# TODO validate field values are integers
# TODO named constructor to construct from in or bytes objects
# TODO support a metaclass keyword argument reverse=True to reverse field order
# TODO provides endianes control when converting bitfields to integers
# TODO prevent field deeletion by overriding __delete__ on the descriptor
class DateBitField(metaclass=BitFieldMeta):
    day: 5