
# def fibonacci(number: int) -> int:
    # if(number <= 1):
        # return 1
    # else:
        # return fibonacci(number - 1) + fibonacci(number - 2)

# print(fibonacci(9))


from typing import Iterator

def fib(n: int) -> Iterator[int]:
    a,b = 0,1
    while a<n:
        yield a
        a, b = b, a + b

for item in fib(9):
    print(item)

def greet(name: str) -> str:
    return "Hi "+ name
