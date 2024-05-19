# Functional Programming Paradigm

Functional programming is a programming paradigm in which we try to bind everything in pure mathematical functions style. It is a declarative type of programming style. Its main focus is on “what to solve” in contrast to an imperative style where the main focus is “how to solve”. It uses expressions instead of statements. An expression is evaluated to produce a value whereas a statement is executed to assign variables.

## Functional Programming is based on Lambda Calculus:

Lambda calculus is a framework developed by Alonzo Church to study computations with functions. It can be called as the smallest programming language in the world. It gives the definition of what is computable. Anything that can be computed by lambda calculus is computable. It is equivalent to Turing machine in its ability to compute.

Concepts of functional programming:
*   Pure functions
*   Recursion
* Referential transparency
* Functions are First-Class and can be Higher-Order
* Variables are Immutable

## Pure Functions

A pure function is a function where the output value is determined only by its input values, without observable side effects.

Characteristics:



*   Given the same input, it will always return the same output.
*   No side effects (e.g., modifying a global variable or a data structure, I/O operations).





```python
# Pure function: no side effects and returns the same result for the same inputs.
def add(x, y):
    return x + y

print(add(3, 5))  # Output: 8
print(add(3, 5))  # Output: 8 (always the same for the same inputs)

```

    8
    8
    

## Recursion

Recursion is a technique where a function calls itself in order to solve a problem. Functional programming relies heavily on recursion instead of traditional looping constructs.


```python
# Function to calculate factorial using recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120

```

    120
    

## Referential Transparency

A function is referentially transparent if it can be replaced with its value without changing the program's behavior. This is closely related to the concept of pure functions.


```python
# Pure function and referentially transparent
def square(x):
    return x * x

# Replace function call with its result
result = square(4)  # 16
print(result)  # Output: 16

# Replace the function call with its value directly
result = 16
print(result)  # Output: 16

```

    16
    16
    

## Functions are First-Class and can be Higher-Order

In functional programming, functions are first-class citizens. This means they can be passed as arguments to other functions, returned as values from other functions, and assigned to variables. Higher-order functions are functions that take other functions as arguments or return them as results.


```python
# Function as first-class citizen
def greet(name):
    return f"Hello, {name}!"

def call_function(func, value):
    return func(value)

print(call_function(greet, "Alice"))  # Output: "Hello, Alice!"

# Higher-order function
def apply_twice(func, value):
    return func(func(value))

def increment(x):
    return x + 1

print(apply_twice(increment, 3))  # Output: 5 (incremented twice)

```

    Hello, Alice!
    5
    

## Variables are Immutable

In functional programming, variables once created cannot be modified. Instead of changing the state, new states are created as needed.


```python
# Immutable data example with tuples
x = (1, 2, 3)
y = x + (4, 5, 6)

print(x)  # Output: (1, 2, 3) (original tuple is unchanged)
print(y)  # Output: (1, 2, 3, 4, 5, 6) (new tuple created)

# Immutable variables example
x = 10
y = x + 5

print(x)  # Output: 10 (original value is unchanged)
print(y)  # Output: 15 (new value)

```

    (1, 2, 3)
    (1, 2, 3, 4, 5, 6)
    10
    15
    

## Summary



*   **Pure Functions:** Functions that always produce the same output for the same input without side effects.
*   **Recursion:** Solving problems by defining functions that call themselves.
* **Referential Transparency:** Expressions can be replaced by their values without affecting the program.
* **First-Class and Higher-Order Functions**: Functions are treated as values and can be passed as arguments or returned by other functions.
* **Immutable Variables:** Variables and data are not altered; instead, new values and states are created.

By adhering to these principles, functional programming ensures more predictable and maintainable code, making it easier to reason about and test.
