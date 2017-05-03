# interpolation string
# name = "vito"
# print(f"Hello {name}")

# Preserving keyword argument order
# def argument_dictionary(**kwargs):
    # return list(kwargs.keys())

# print(argument_dictionary(a=12,b=41,c=65, dd="vito"))

# simpler customization of class creation
# class Foo:
    # def __init_subclass__(cls, whom, **kwargs):
        # super().__init_subclass__(**kwargs)
        # cls.hello = lambda: print(f"Hello {whom}")

# class Hello(Foo, whom="vito"):
    # pass

# Hello.hello()

#local time disambiguation
# import datetime
# dt = datetime.datetime(2016,11,6,1,30)
# pdt = dt.astimezone().strftime('%Y-%m-%d %T %Z%z')
# pst = dt.replace(fold=1).astimezone().strftime('%Y-%m-%d %T %Z%z')

# print(pdt)
# print(pst)

#underscore in numeric literals
# print(1_000_000)

#Asynchronous generators & comprehesions
import asyncio
from typing import Iterator

async def ticker(delay: int, to: int) -> Iterator[int] :
    for i in range(to):
        yield i
        await asyncio.sleep(delay)

ticker(5,50)

async def async_comprehesions() -> Iterator[int]:
    comp_with_async = [i async for i in range(50) if i % 2]
    comp_with_await = [await number for number in range(10)]

