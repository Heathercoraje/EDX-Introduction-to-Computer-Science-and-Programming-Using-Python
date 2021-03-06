# Structure types
## Tuples and lists
---
### Tuples
Tuples, lists, mutability, cloning

Now we can apply functions on number and string, we'd like to to able to look at bigger collection of data. Tuple is an order sequence of elements yet here it does not mean that elements in the sequence are ordered meaning smallest to largest. It means that the sequence itself has an order so that I can get to different parts of sequence by using simple indexing. Just like a string, tuples are immutable. We can't change inner piece of tuples.

```
t = ()
te = (0, 'one', '1')
t + te # I can also concatenate tuples
te[1] = 4 # this throws an error because tuples are immutable
t[1:2] # prints ('one',) and this extra comma indicates that it is a tuple

```
+ Tuples are very convenient when swapping values.

```
(x,y) = (y,x)

```
+ Tuples are used to return more than one value from a function

```
def  quotient_and_remainder(x,y):
    q = x//y
    r = x%y
    return (q,r)
(quot, rem) = quotient_and_remainder(4,5) # binding vales of q and r to quot and rem

```
+ Tuples are iterable

```
def get_data(aTuple):
  nums = () # emply Tuple
  words = ()
  for t in aTuple:
    nums = nums + (t[0],) # gathering int in each tuple in aTuple(collection of tuples),
    # if t[0] instead of (t[0],), it throws an error because it can only concatenate tuple() to tuple()
    if t[1] not in words: # while iterating tuples, if t[1], which is a char, is unique then add it to words tuple
        words = words + (t[1],)
  min_nums = min(nums)
  max_nums = max(nums)
  unique_words = len(words)

  return (min_nums, max_nums, unique_words)

```

### Lists
Lists are mutable and iterable, therefore it can be convenient but also brings challenges.

```
# Iterating over a list
total = 0
 for i in L: # list
  total += 1
print(total)

```

### List operations
As strings come with standard operations in python, so do lists and tuples. One can append items at the end of a list or expend a list. You can concatenate, remove, extend or apply many other methods to objects(list, tuples, functions, etc). It is important to remember that every method has different effect on **mutation**. For example, ```x.sort()```mutates the list itself while ```sorted(x)``` returns a new list

```
x = [1, 2, 3, 4]
x.append(5)
x # returns [1, 2, 3, 4, 5] # it is mutated

```
