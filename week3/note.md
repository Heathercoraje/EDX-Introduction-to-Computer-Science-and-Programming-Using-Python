# Week 3: Structured types
## Tuples and lists
---
### Tuples
Tuples, lists, mutability, cloning

Now we can apply functions on number and string, we'd like to to able to look at bigger collection of data.
Tuple is an order sequence of elements yet here it does not mean that elements in the sequence are ordered meaning smallest to largest.
It means that the sequence itself has an order so that I can get to different parts of sequence by using simple indexing.
Just like a string, tuples are immutable. We can't change inner piece of tuples.

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

#### Exercise 1

```
x = (1, 2, (3, 'John', 4), 'Hi')
x[0] # returns 1
x[0:1] # returns (1,) as a tuple
2 in x # return True
3 in x # return False because sub-tuple does not count when using in to find elements, only main tuples are considered
```

#### Exercise oddTuples
```
def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''

    return aTup[::2]

```

### Lists
Lists are mutable and iterable, therefore it can be convenient but also brings challenges.

```
# Iterating over a alist
total = 0
 for i in L: # list
  total += 1
print(total)

```
#### Exercise 2
