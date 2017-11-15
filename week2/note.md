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

#### Exercise Guess my number
With the idea of bisection search throwing away half of possible values at every stage, it takes way less guesses than before.
bisection search really radically reduces computation time and it should work on any problem we would call an ordering property as in the value of function being solved varies monotonically, that is, it increases as the input value increases.

```
# by having done, we can break out of loop
print('Please thnk of a number between 0 and 100!')
high = 100
low = 0
done = False

# loop until guess is correct
while (not done):
  guess = (high+low)//2
  print("Is your secret number " + str(guess) + "?")
  user_input = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

  if user_input == 'c':
    done = True
  elif user_inout == 'h':
    high = guess
  elif user_input == 'l':
    low = guess
  else:
    print('Sorry, I did not understand your input.')

print('Game over. Your secret number was: ' + str(guess))
# while False: will escape the iteration
```
#### Exercise 4
A set of simple true/false questions
+ It is false that internal computer representation of any number is always an approximation
+ 1011 is binary of decimal 11
+ It is true that the internal representation of the decimal number 1/10 = 0.1 requires an infinite number of digits
+ After many computation, you get two floating numbers stored in variables a and b. In comparing the numbers with a == b, it sometimes lead to a correct answer but not always.  


In this lecture, we are introduced to three different classes of Algorithms and with these, we've got a lot of tools for doing numerical computation.
