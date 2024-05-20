# Decorators




Decorators in Python are a powerful and versatile feature that allow you to modify or extend the behavior of functions or methods. They provide a way to wrap another function in order to extend its behavior without permanently modifying it.

## Basic Concept of Decorators

A decorator is a function that takes another function as an argument, extends its behavior, and returns a new function with the extended behavior.

Here's a basic example of a decorator:


```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_hello():
    print("Hello!")

say_hello = my_decorator(say_hello)
say_hello()

```

    Something is happening before the function is called.
    Hello!
    Something is happening after the function is called.
    

In the above example:

*   my_decorator is a decorator function.
*   wrapper is an inner function that adds some behavior before and after calling the original function (func).
* say_hello is the original function that we want to decorate.
* say_hello = my_decorator(say_hello) applies the decorator to say_hello.

## Using the @ Syntax

Python provides a more convenient way to apply decorators using the @ syntax:


```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

```

    Something is happening before the function is called.
    Hello!
    Something is happening after the function is called.
    

The above functionally is equivalent to the previous example but uses the @ syntax to apply the decorator.

## Decorators with Arguments

If your original function takes arguments, the wrapper function must accept these arguments and pass them along to the original function:


```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")

```

    Something is happening before the function is called.
    Hello, Alice!
    Something is happening after the function is called.
    

## Returning Values from Decorated Functions

If the original function returns a value, the wrapper function should also return that value:


```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper

@my_decorator
def add(a, b):
    return a + b

result = add(3, 4)
print(f"Result: {result}")

```

    Something is happening before the function is called.
    Something is happening after the function is called.
    Result: 7
    

## Chaining Decorators

You can apply multiple decorators to a single function. They are applied in the order from the closest to the function signature outwards:


```python
def decorator1(func):
    def wrapper(*args, **kwargs):
        print("Decorator 1 before")
        result = func(*args, **kwargs)
        print("Decorator 1 after")
        return result
    return wrapper

def decorator2(func):
    def wrapper(*args, **kwargs):
        print("Decorator 2 before")
        result = func(*args, **kwargs)
        print("Decorator 2 after")
        return result
    return wrapper

@decorator1
@decorator2
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

```

    Decorator 1 before
    Decorator 2 before
    Hello, Alice!
    Decorator 2 after
    Decorator 1 after
    

## Using functools.wraps

When you use decorators, the original function’s metadata (like its name, docstring, etc.) is lost. To preserve this metadata, you should use functools.wraps:


```python
import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    """Greet someone by their name."""
    print(f"Hello, {name}!")

print(say_hello.__name__)  # Outputs: say_hello
print(say_hello.__doc__)   # Outputs: Greet someone by their name.

```

    say_hello
    Greet someone by their name.
    

## Decorators with Parameters

Sometimes you might want to pass parameters to your decorators. To do this, you need to define a function that returns a decorator:


```python
import functools

def repeat(times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(times=3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

```

    Hello, Alice!
    Hello, Alice!
    Hello, Alice!
    

In the above example, repeat is a function that takes an argument times and returns a decorator decorator_repeat.

Thus, Decorators are a powerful tool in Python for extending and modifying the behavior of functions and methods. They can be simple or complex, and they can handle function arguments, return values, and even metadata. Using the @ syntax makes decorators easy to apply and read. Additionally, by using functools.wraps, you can preserve the original function’s metadata. Decorators with parameters allow for even more flexible and reusable code.
