# Generators


Generator functions allow you to declare a function that behaves like an iterator, i.e. it can be used in a for loop.

###The simplification of code is a result of generator function and generator expression support provided by Python.

To illustrate this, we will compare different implementations that implement a function, "firstn", that represents the first n non-negative integers, where n is a really big number, and assume that each integer takes up a lot of space, say 10 megabytes each.

First, let us consider the simple example of building a list and returning it.


```python
def first_n(n):
    '''Generate numbers from 0 to n-1'''
    num = 0
    while num < n:
        yield num
        num += 1

sum_of_first_n = sum(first_n(1000000))
print(sum_of_first_n)

```

    499999500000
    

The code is quite simple and straightforward, but it builds the full list in memory. This is clearly not acceptable in our case, because we cannot afford to keep all n "10 megabyte" integers in memory.

The following implements generator as an iterable object.


```python
class first_n(object):

    def __init__(self, n):
        self.n = n
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.num < self.n:
            cur, self.num = self.num, self.num + 1
            return cur
        else:
            raise StopIteration()

    def next(self):
        return self.__next__()

# Calculate the sum of the first n numbers using the iterator
sum_of_first_n = sum(first_n(1000000))
print(sum_of_first_n)

```

    499999500000
    

This will perform as we expect, but we have the following issues:



*   there is a lot of boilerplate
*   the logic has to be expressed in a somewhat convoluted way

Furthermore, this is a pattern that we will use over and over for many similar constructs. Imagine writing all that just to get an iterator.

Python provides generator functions as a convenient shortcut to building iterators. Lets us rewrite the above iterator as a generator function:


```python
def firstn(n):
    """Generate numbers from 0 to n-1."""
    num = 0
    while num < n:
        yield num
        num += 1

sum_of_first_n = sum(firstn(1000000))
print(sum_of_first_n)

```

    499999500000
    

## How Generators Work

A generator in Python is created using a function with at least one yield statement. When the function is called, it returns an iterator object but does not start execution immediately. Each subsequent call to the iterator's __next__() method resumes the function execution from the point where it left off (just after the last yield statement). The function can run and yield multiple times, thus producing a sequence of results over time.

## Key Points




*  **Memory Efficiency:** Generators allow you to generate large sequences of values without using up memory for all of the values at once.

*   **Lazy Evaluation:** Values are produced only as needed, rather than all at once.
* **Maintain State:** Generators maintain their state between calls, which can be useful for complex iteration scenarios.




```python
def simple_generator(n):
    """A generator that yields numbers from 0 to n-1."""
    for i in range(n):
        yield i

# Using the generator
gen = simple_generator(5)
for value in gen:
    print(value)

```

    0
    1
    2
    3
    4
    

## Generator Expression

Python also provides a generator expression, which is similar to a list comprehension but with parentheses instead of square brackets. Here’s an example:


```python
gen_exp = (x * x for x in range(5))

for value in gen_exp:
    print(value)

```

    0
    1
    4
    9
    16
    

## Another Example :


```python
def fibonacci():
    """An infinite generator for Fibonacci numbers."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Using the generator
fib_gen = fibonacci()
for _ in range(10):  # Print the first 10 Fibonacci numbers
    print(next(fib_gen))

```

    0
    1
    1
    2
    3
    5
    8
    13
    21
    34
    

## Explanation for the above code :

*   **Function Definition:** def fibonacci() defines the generator function.
*   **Initial State**: a, b = 0, 1 initializes the first two Fibonacci numbers.
* **Infinite Loop:** while True: creates an infinite loop.
* **Yielding Values**: yield a yields the current value of a.
* **State Update**: a, b = b, a + b updates the values of a and b to the next two Fibonacci numbers.
* **Using the Generator:** fib_gen = fibonacci() creates an instance of the generator, and next(fib_gen) is called to get the next Fibonacci number.

## Benefits of Generators



*   **Efficiency:** Generators are more memory-efficient than lists, especially for large datasets.
*   **Lazy Evaluation:** Values are computed only when needed, avoiding unnecessary computations.
* **Maintainability**: Generators can simplify code that deals with iterators and sequences.


