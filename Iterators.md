# Iterators

An **iterator** in Python is an object that allows you to traverse through all the elements in a collection, such as lists, tuples, or dictionaries, without needing to use indexing or a loop counter. Iterators are implemented using two main methods:


1.   __iter__(): Returns the iterator object itself.
2.   
__next__(): Returns the next element in the sequence. When there are no more elements, it raises a StopIteration exception to signal that the iteration is complete.

So let's first consider the basic python range function:


```python
range(10)
range(0, 10)
```




    range(0, 10)




```python
total = 0
for x in range(int(1e6)):
    total += x
```


```python
total
```




    499999500000



In order to avoid allocating a million integers, range actually uses an iterator.
We don't actually need a million integers at once, just each integer in turn up to a million.

Because we can get an iterator from it, we say that a range is an iterable.
So we can for-loop over it:


```python
for i in range(3):
    print(i)
```

    0
    1
    2
    

There are two important Python built-in functions for working with iterables. First is iter, which lets us create an iterator from any iterable object.


```python
a = iter(range(3))
```

Once we have an iterator object, we can pass it to the next function. This moves the iterator forward, and gives us its next element:


```python
next(a)
```




    0




```python
next(a)
```




    1




```python
next(a)
```




    2




```python
next(a)
```


    ---------------------------------------------------------------------------

    StopIteration                             Traceback (most recent call last)

    <ipython-input-11-15841f3f11d4> in <cell line: 1>()
    ----> 1 next(a)
    

    StopIteration: 


This tells Python that the iteration is over. For example, if we are in a for i in range(3) loop, this lets us know when we should exit the loop.

We can turn an iterable or iterator into a list with the list constructor function:


```python
list(range(5))
```




    [0, 1, 2, 3, 4]



## Step-by-Step Implementation:



1.  **Define the Iterator Class:** Implement the __iter__ and __next__ methods.
         
2. **Initialize the Iterator:**
Set the starting point and any required variables.
3. **Handle the Iteration Logic:**
Define how to return the next element and when to raise StopIteration.


```python
class EvenNumbers:
    def __init__(self, max_numbers):
        self.max_numbers = max_numbers
        self.current = 0
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_numbers:
            raise StopIteration
        else:
            even_number = self.current
            self.current += 2
            self.count += 1
            return even_number

# Using the EvenNumbers iterator
even_numbers_iterator = EvenNumbers(5)

for num in even_numbers_iterator:
    print(num)

```

    0
    2
    4
    6
    8
    

## Explanation of the above code -

###**Initialization:**



*   The __init__ method initializes the iterator.
*   It takes max_numbers as an argument to define how many even numbers to generate.
*  It also initializes self.current to 0 and self.count to 0.

###**Iterator Protocol:**

*   The __iter__ method returns self, indicating that the object itself is the iterator.
*  The __next__ method contains the logic to return the next even number.
*  If the count of generated numbers has reached max_numbers, it raises StopIteration. Otherwise, it calculates the next even number, updates the state, and returns the current even number.

###**Using the Iterator:**

*   An instance of EvenNumbers is created with max_numbers set to 5.
*   A for loop is used to iterate through the even numbers.
* The loop internally calls the __next__ method until StopIteration is raised.






## Using Built-in Iterators

Python has several built-in objects that implement the iterator protocol, such as lists, tuples, and dictionaries. You can easily convert these objects into iterators using the iter() function and get the next item using the next() function.

Example :


```python
# Using a list as an iterator
my_list = [1, 2, 3, 4]
my_iterator = iter(my_list)

print(next(my_iterator))  # Output: 1
print(next(my_iterator))  # Output: 2
print(next(my_iterator))  # Output: 3
print(next(my_iterator))  # Output: 4

# Raises StopIteration as there are no more items
print(next(my_iterator))

```

    1
    2
    3
    4
    


    ---------------------------------------------------------------------------

    StopIteration                             Traceback (most recent call last)

    <ipython-input-14-ede86052819e> in <cell line: 11>()
          9 
         10 # Raises StopIteration as there are no more items
    ---> 11 print(next(my_iterator))
    

    StopIteration: 


## Explanation of Built-in Iterators:


*   **Conversion:** The iter() function is used to convert a list (my_list) into an iterator (my_iterator).

*   **Iteration:** The next() function retrieves the next item from the iterator until the end of the list is reached. When there are no more items, it raises a StopIteration exception.


```python
# Convert notebook to HTML
!jupyter nbconvert --to html your_notebook.ipynb

# Convert notebook to Markdown
!jupyter nbconvert --to markdown your_notebook.ipynb

```

## Conclusion

Iterators provide a powerful and memory-efficient way to handle sequences of data in Python. By implementing the iterator protocol (__iter__ and __next__), custom objects can support iteration, allowing for more flexible and reusable code. Built-in collections like lists and dictionaries already support iteration, making it easy to traverse their elements without needing explicit counters or indexing.
