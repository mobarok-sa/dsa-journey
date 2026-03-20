~~~
array = [5, 3, 8, 2]
less = []

for i in array[1:]:
    if i <= pivot:
        less.append(i)
~~~

lst comprehension

~~~
array = [5, 3, 8, 2]
less = [i for i in array[1:] if i <= pivot]
~~~



less = [i for i in array[1:] if i <= pivot]

the first i means the value that will be added to the new list.

Structure of a list comprehension

General form:

[expression for item in iterable if condition]