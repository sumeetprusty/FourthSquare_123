# Context Manager

In any programming language, the usage of resources like file operations or database connections is very common. But these resources are limited in supply. Therefore, the main problem lies in making sure to release these resources after usage. If they are not released then it will lead to resource leakage and may cause the system to either slow down or crash. It would be very helpful if users have a mechanism for the automatic setup and teardown of resources. In Python, it can be achieved by the usage of context managers which facilitate the proper handling of resources.

##  Basic Usage with with Statement

The with statement simplifies exception handling by encapsulating common preparation and cleanup tasks. For example, when working with files:


```python
with open('example.txt', 'w') as file:
    file.write('Hello, world!')

```

In the above example:
*   The **open** function returns a file object that acts as a context manager.
*   The **with** statement ensures that the file is properly closed after its suite finishes, even if an exception is raised.




##  Implementing a Context Manager with a Class

You can create your own context managers using classes by implementing the __enter__ and __exit__ methods.


```python
class MyContextManager:
    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")
        if exc_type:
            print(f"An exception occurred: {exc_type}")
        return True  # Suppress exceptions if True

with MyContextManager() as manager:
    print("Within the context")
    # Raise an exception to see how it's handled
    raise ValueError("An error occurred")

```

    Entering the context
    Within the context
    Exiting the context
    An exception occurred: <class 'ValueError'>
    

## Implementing a Context Manager with contextlib Library

The contextlib module provides a simpler way to create context managers using the @contextmanager decorator.


```python
from contextlib import contextmanager

@contextmanager
def my_context_manager():
    print("Entering the context")
    try:
        yield
    except Exception as e:
        print(f"Exception occurred: {e}")
        raise
    finally:
        print("Exiting the context")

try:
    with my_context_manager():
        print("Within the context")
        # Raise an exception to see how it's handled
        raise ValueError("An error occurred")
except ValueError as e:
    print(f"Caught an exception: {e}")

```

    Entering the context
    Within the context
    Exception occurred: An error occurred
    Exiting the context
    Caught an exception: An error occurred
    

## Practical Example: Database Connection


```python
class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        print(f"Connecting to database {self.db_name}")
        # Simulate opening a database connection
        self.connection = f"Connection to {self.db_name}"
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Closing database {self.db_name}")
        # Simulate closing a database connection
        self.connection = None

with DatabaseConnection('my_database') as conn:
    print(f"Using {conn}")
    # Perform database operations here

```

    Connecting to database my_database
    Using Connection to my_database
    Closing database my_database
    

## Handling Exceptions

If you need to handle exceptions that occur within the context, you can do so in the __exit__ method or within the try block when using contextlib.


```python
@contextmanager
def managed_resource():
    print("Acquiring resource")
    try:
        yield
    except Exception as e:
        print(f"Exception: {e}")
    finally:
        print("Releasing resource")

with managed_resource():
    print("Using resource")
    raise RuntimeError("Something went wrong")

```

    Acquiring resource
    Using resource
    Exception: Something went wrong
    Releasing resource
    

Thus, context managers in Python provide a robust way to ensure that resources are properly managed. Whether using the with statement with built-in context managers, creating your own with classes, or using the contextlib module, context managers help make your code cleaner and more reliable.
