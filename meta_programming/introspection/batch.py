from itertools import chain

#  chain łaczy kolekcje i robi flata
class Batch:

    def __init__(self, iterables=()):
        self._iterables = list(iterables)

    def append(slef, iterable):
        self._iterables.append(iterable)

    def __iter__(self):
        return chain(*self._iterables)

# i = 7
# type(i)
# repr(i)
# type(i)(42)
# type(type(i))
# i.__class__
# i.__class__.__class__
# i.__class__.__class__.__class__
# issubclass(type, object)
# type.__mro__
# isinstance(i, int)
# isinstance(int, type)
# a = 42
# dir(a)
# getattr(a, 'denominator')
# getattr(a, 'numerator')
# getattr(a, 'conjugate')
# callable(getattr(a, 'conjugate'))
# globals()
# from pprint import pprint as pp
#
# pp(globals())
# globals()["yolo"] = 42
# yolo
# locals()
#
#
# def report_scope(arg):
#     import sys
#     x = 42
#     pp(locals(), width=10)
#
#
# report_scope(666)
# import inspect
# import batch
#
# inspect.ismodule(batch)
# inspect.getmembers(batch)
# inspect.getmembers(batch, inspect.isfunction)
# init_sig = inspect.signature(batch.Batch.__init__)
# init_sig
# init_sig.parameters
# init_sig.parameters['iterables'].default
#
#
# def num_vowels(text: str) -> int:
#     return sum(1 if c.lower() == 'aeiou' else 0 for c in text)
#
#
# def num_vowels(text: str) -> int:
#     return sum(1 if c.lower() in 'aeiou' else 0 for c in text)
#
#
# i = 7
# type(i)
# repr(i)
# type(i)(42)
# type(type(i))
# i.__class__
# i.__class__.__class__
# i.__class__.__class__.__class__
# issubclass(type, object)
# type.__mro__
# isinstance(i, int)
# isinstance(int, type)
# a = 42
# dir(a)
# getattr(a, 'denominator')
# getattr(a, 'numerator')
# getattr(a, 'conjugate')
# callable(getattr(a, 'conjugate'))
# globals()
# from pprint import pprint as pp
#
# pp(globals())
# globals()["yolo"] = 42
# yolo
# locals()
#
#
# def report_scope(arg):
#     import sys
#     x = 42
#     pp(locals(), width=10)
#
#
# report_scope(666)
# import inspect
# import batch
#
# inspect.ismodule(batch)
# inspect.getmembers(batch)
# inspect.getmembers(batch, inspect.isfunction)
# init_sig = inspect.signature(batch.Batch.__init__)
# init_sig
# init_sig.parameters
# init_sig.parameters['iterables'].default
#
#
# def num_vowels(text: str) -> int:
#     return sum(1 if c.lower() == 'aeiou' else 0 for c in text)
#
#
# def num_vowels(text: str) -> int:
#     return sum(1 if c.lower() in 'aeiou' else 0 for c in text)
#
#
# sig = inspect.signature(num_vowels)
# sig.parameter['text']
# sig.parameters['text']
# sig.parameters['text'].annotation
# sig.return_annotation
# num_vowels.__annotations__