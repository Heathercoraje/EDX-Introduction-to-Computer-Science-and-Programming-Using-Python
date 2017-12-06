# Week4: Good programming practice

## Testing and debugging

In a analogy of making a pot of soup, imagine bugs keep falling down from the ceiling when you are making a pot of soup. First, checking soup for bugs is testing. Second, keeping the lid close is practicing defensive programming, lastly cleaning kitchen is eliminating source of bugs, debugging.

**Defensive programming** comes down to defining what I expect to come in, what I' ll deliver and ensuring that I actually do that. It is to write specifications for functions (docs) for example "Here is what I   am expected to be an input and here is what I will deliver if I get things that are of the right form", to modularize programs instead of writing a huge single function, break it up into obvious pieces because later on we want to test functions by small pieces in turn and to check conditions on inputs and outputs(assertions).

**testing and validation** is to compare input/output pairs to specifications we have given before for the function. Also, tests need to be built in a way that they cover all of different cases to make sure the program is doing what I want it to dos.

**debugging** is to study what events lead to an error and to come up with solution to fix the bug.

+ For easy testing and debugging:
  + From the start, design code to ease this part
  + Break program into modules that can be tested and debugged *individually*
  + Create habits of writing documents constraints well: what do you expect the input to be? the output to be?
  + Document assumptions behind the code: what are you thinking when creating this code? why is this built in a particular way?

+ Classes of testing
  + Unit testing: validate each piece/each function separately.
  + Regression testing: add test for bugs then catch reintroduced errors
  + Integrated testing: does overall program work?

In fact, they all go back and forth (unit testing > regression testing > unit > regression > integrated > unit et al).

+ Testing approaches
  + intuition about natural boundaries

  + random testing

  + black-box testing: explore all the paths through specifications without looking at the code.

  + glass-box testing: explore paths through code (making sure test hits all of possible paths) but sometimes you might miss some paths so you may have to add other approaches
  ```
  def union(set1, set2):
   """
   set1 and set2 are collections of objects, each of which might be empty.
   Each set has no duplicates within itself, but there may be objects that
   are in both sets. Objects are assumed to be of the same type.

   This function returns one set containing all elements from
   both input sets, but with no duplicates.
   """

  ```

  A good black box test suite would contain tests for all of the given conditions! Black-box testing tests the functionality of an application, by looking at the paths through its *specifications.* According to the specifications, the possibilities for set1 and set2 are as follows:
   + set1 is an empty set and set2 is an empty set
   + set1 is an empty set an set2 is of size greater than or equal to 1
   + set1 is of size greater than or equal to 1 and set2 is an empty set correct
   + set1 and set2 are both nonempty sets which do not contain any objects in common
   + set1 and set2 are both nonempty sets which contain objects in common.

### Exercise 4

```
def foo(x, a):
   """
   x: a positive integer argument
   a: a positive integer argument

   returns an integer
   """
   count = 0
   while x >= a:
      count += 1
      x = x - a
   return count

```
Consider the following function definition, Please select the best glass box test suite for the function foo from the following options.

In glass box testing: we try to sample as many paths through the code as we can. In case of loops, we cant to sample three general cases:
+ not executing the loop at all
+ executing the loop exactly once
+ executing the loop multiple times

+ Types of bug
  + overt bug has an obvious indication, code crashes or runs forever
  + covert bug returns incorrect value, harder to determine
  + persistent occurs every time code is run
  + intermittent only occurs sometimes even with same input, it tends to depend on other factors  

Over and persistent bugs are obvious to detect. Good programmers use defensive programming to try to ensure that if error is made, bug will fall into this category. Overt and intermittent bugs are frustrating but if you know in which condition an error occurs, then it allows you to isolate where to go back to fix the bug. Covert bugs are difficult and dangerous because you will not know where to go back and the code could have been running for a long time.

## Debugging
Debugging has a steep learning curve. There are tools to help you such as print statements, python tutor and formulating hypothesis and test your own experiments.

+ print statement: when to print, enter function, parameters, expected output. Also, put print statement in half way of program to make sure where bug is at

+ error message:
  + IndexError: trying to acess beyond the limits of a list
  + TypeError: trying to convert an inappropriate type (int([1,2])
  + NameError: referencing a non-existent variable
  + TypeError: mixing data types without appropriate coercion ('3'/4)
+ SyntaxError

let the error messages guide what you are looking for in terms of bugs.

**Logic errors** are harder. *think* before writing new codes and *draw* pictures of code, *explain* to a rubber ducky and walk through the codes. Make sure that you have a backup of current codes and experiment with a new version so that you can always recover it to the previous code.

## Exceptions and Assertion
