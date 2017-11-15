# Week2
----
## 3. Simple Algorithms
string is a immutable type, as in one cannot change a piece of a string for example, by using index, rather one must redefine the string

#### Exercise 1

```
iteration = 0
count = 0
while iteration < 5:
    # the variable 'letter' in the loop stands for every
    # character, including spaces and commas!
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1
```
The code above prints out:
```
iteration 0; count is 12
iteration 1; count is 24
iteration 2; count is 36
iteration 3; count is 48
iteration 4; count is 60
```

```
iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1
```

The code above prints out:
```
iteration 0; count is 12
iteration 1; count is 12
iteration 2; count is 12
iteration 3; count is 12
iteration 4; count is 12
```
This is because variable count is reassign to 0 every time it repeats the while loop

```
iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
        if iteration % 2 == 0:
            break
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1

```
The code above prints out:

+ ``` print ``` will be executed 5 times.
+ The largest value of ```iteration``` to be printed will be 4
+ The largest value of ```count``` to be printed is 12
+ the smallest value of ```count``` to be printed is 1

#### Exercise 2
As you make changes to the code, you need to think about the consequences. The case win the video was one where my test wasn't capturing all of the cases because the step was too big so that it skips the answer

#### Exercise 3
With the idea of bisection search throwing away half of possible values at every stage, it takes way less guesses than before.
bisection search really radically reduces computation time and it should work on any problem we would call an ordering property as in the value of function being solved varies monotonically, that is, it increases as the input value increases.
