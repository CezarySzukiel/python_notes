import csv
import json
from collections import defaultdict
from io import StringIO
from pathlib import Path
from pprint import pprint

# plug-in architecture, nie modyfikujemy bazowego kodu, można go rozszerzać
class RegisterMeta(type):
    def __new__(mcs, name, bases, namespace, **kwargs):
        cls = super().__new__(mcs, name, bases, namespace)
        cls.register(**kwargs)
        return cls


# class TableDecoder(metaclass=RegisterMeta):
class TableDecoder(metaclass=RegisterMeta):
    _register = {}

    # @classmethod
    # def register(cls, extension=None):
    #     if extension is None:
    #         return
    #     cls._register[cls.__name__] = cls

    @classmethod
    def __init_subclass__(cls, *, extension, **kwargs):
        super().__init_subclass__(**kwargs)
        cls._register[extension] = cls


    @classmethod
    def create(cls, name):
        decoder_class = cls._register[name]
        return decoder_class()

    @classmethod
    def decoders(cls):
        return list(cls._register.keys())

    @staticmethod
    def decode(text):
        raise NotImplementedError


class JsonTableEncoder(TableDecoder, extension='json'):
    @staticmethod
    def decode(text):
        objs = json.loads(text)
        table = defaultdict(list)
        for obj in objs:
            for key, value in obj.items():
                table[key].append(value)
        return dict(table)


class CsvTableEncoder(TableDecoder, extension='csv'):
    @staticmethod
    def decode(text):
        with StringIO(text) as csv_stream:
            reader = csv.DictReader(csv_stream)
            table = defaultdict(list)
            for row in reader:
                for key, value in row.items():
                    table[key].append(value)
        return dict(table)


# JsonTableEncoder.register()


def load_table(filepath):
    filepath = Path(filepath)
    text = filepath.read_text()
    extension = filepath.suffix.removeprefix('.')
    decoder = TableDecoder.create('CsvTableEncoder')
    table = decoder.decode(text)
    return table


def main():
    # table = load_table("table.json")
    print(TableDecoder.decoders())
    table = load_table("table.csv")
    pprint(table)


if __name__ == "__main__":
    main()

    # czym się różni dekoder od enkodera?
