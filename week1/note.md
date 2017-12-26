# Python and programming basics

### Basics of computer

+ A fixed program computer is designed to compute precisely one computation
+ A stored program computer is designed to run any computation, by interpreting a sequence of instructions that are read into it
+ A program counter points the computer to the next instruction to execute in the program
+ Computer executes the instructions mostly in a linear sequence, except sometimes it jumps to a different place in the s sequence
+ There are 6 primitives but with modern programming language, one can create primitives by abstracting methods
+ The difference of an algorithm and a program is that an algorithm is conceptual idea and a program is an concrete instantiation of algorithm
+ A computational mode of thinking means that everything can be viewed as a math problem involving numbers and formulas
+ Computer Science is not just about building efficient machines to run programs.
+ Remembering results and performing calculation are two things that every computer can do   
+ Turing complete means equivalent in power to a universal tuning machine which says anything you can compute in one language can be compute in any other.

### Expressions
With a simple set of primitives, one should be able to compute anything. Yet modern programming languages have more convenient set of primitives and also one can abstract methods to create new primitives(note that this is where a power of computational thinking comes in).

### Type
There are different type of object(Data) and they are int, float, boolean and nonetype. While performing operations, when inputs are integers then result is always int. If either or both numbers are floats then result is always float.

### Variables
By using assignment ```=``` one assign a value to a variable.
By storing value as a variable, one can reuse it later without doing calculation

### Core elements of programming
It is important not to lose bindings because once lost, you cannot get it back.
Therefore, in such case, one can use a new variable temp to store a value

### Comparison between for loop and while loop
In case of for loops, we know number of iterations. It can end early using ```break```. Also it uses a counter. One can rewrite a for loop using while loop. On the other hand, in case of while loop, it executes unbounded number of iterations. It can use a counter but must initialize before loop and increment it inside the loop. Also one sometimes cannot rewrite a while loop using a for loop.
In short, one tends to use for loop when knowing what we are going to do as computation and one tends to use while loop, when there is a condition that he cannot predict
