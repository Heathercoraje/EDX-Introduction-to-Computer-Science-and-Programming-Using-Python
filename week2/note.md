# Simple programs
----
### Simple Algorithms
In this lecture, we are introduced to three different classes of Algorithms and with these, we've got a lot of tools for doing numerical computation.

### Functions
It is important to have a good structure in code. Decomposition is an idea of breaking a bit chunk of code into pieces, a module that are self-contained, intended to be reusable, used to break up codes, keep code organized and coherent. For early weeks we learn how to do decomposition with functions and later after a few weeks, we will learn how to do decomposition with classes. Abstraction is an idea that one once I've built something, I don't need to know what is inside as long as it works. In other words, abstraction comes with a contract which says if you give me an appropriate answer, I am going to behave in an appropriate way.

### Specification

It is recommended to write a docstring below a function one create so that a user of the function what to put as input and what to expect as output. Also it is helpful for future oneself to understand which thought she had when building the function before.

### Iteration vs Recursion
The idea of a recursive function is to break it down into a small version of the same problem, plus some operations I want to do and figure out when can I stop breaking it down into smaller version of the same problem. The code below is an example of an recursive function.
It might help to [read further on a recursive function] (https://pythonspot.com/en/recursion/) to fully understand its concept. A recursive function must call itself and has to have a terminate condition. By repetitively calling itself, it creates a new scope with a returned value, which not resolved yet pending, once the terminate condition is met, it returns to pending function to return value and continue returning pending functions until the end.

### Inductive reasoning
How do we know a recursive code is going to work? In this case, we use a mathematical tool called mathematical induction. The idea of behind induction is that if I want to prove that statement is true for all values, then I just need to prove that statement is true when n has the smallest value.

### Tower of Hanoi
Recursion is a powerful tool and sometimes there are problems which cannot be solve otherwise if you don't think about it recursively, for example a classic problem called Towels of Hanoi. This is a problem that the professor suggests is really hard to solve iteratively but elegantly easy to solve recursively. The important thing to understand is the notion of breaking it down into a smaller version of the same problem, assume that can be solve, build your solution with that and other simple operations and then let the recursion unwind it until it gets to the solution you want.

  ```
  def printMove(fr, to):
      print('move from' + str(fr) + ' to ' + str(to))

  def Towers(n, fr, to, spare):
      if n == 1:
          printMove(fr, to)
      else:
          Towers(n-1, fr, spare, to)
          Towers(1, fr, to, spare)
          Towers(n-1, spare, to, fr)
  ```

### Fibonacci
Fibonacci is an example of having multiple base cases and calling two invocation of the function itself
```
def fib(x):
  if(x == 0) or (x ==1):
    return 1
  else:
    return fib(x-1) + fix(x-2)
```
### Recursion on non-numerics
We can also use recursive function on string, for example palindrome, a string that read the same in backward.
```
def isPalindrome(s):
    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans

  def isPal(s):
      if len(s) <= 1:
          return True
      else:
          return s[0] == s[-1] and isPal(s[1:-1])
  return isPal(toChars(s))        
```
This is an elegant piece of code and is an example of what we call **divide and conquer algorithm.** I solve a hard problem by breaking it into a set of other sub-problems that have the property that they are easier to solve than the original and that solution of sub-problems get
combined to solve the original-hard problem.  
