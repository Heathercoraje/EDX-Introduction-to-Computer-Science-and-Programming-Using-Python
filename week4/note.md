# Good programming practice

## Testing and debugging

In a analogy of making a pot of soup, imagine bugs keep falling down from the ceiling when you are making a pot of soup. First, checking soup for bugs is testing. Second, keeping the lid close is practicing defensive programming, lastly cleaning kitchen is eliminating source of bugs, debugging.

**Defensive programming** comes down to defining what I expect to come in, what I will deliver and ensuring that I actually do that. It is to write specifications for functions (docs) for example "Here is what I   am expected to be an input and here is what I will deliver if I get things that are of the right form", to modularize programs instead of writing a huge single function, break it up into obvious pieces because later on we want to test functions by small pieces in turn and to check conditions on inputs and outputs(assertions).

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
  + SyntaxError: using invalid syntax

let the error messages guide what you are looking for in terms of bugs.

**Logic errors** are harder. *think* before writing new codes and *draw* pictures of code, *explain* to a rubber ducky and walk through the codes. Make sure that you have a backup of current codes and experiment with a new version so that you can always recover it to the previous code.

#### Handling exceptions
By clarifying what to do when expected exception occurs, we can handle exceptions.

#### Control the flow
By ```raise:```, we can control the flow of program.

```
try:
exception:
else:
finally:

```
