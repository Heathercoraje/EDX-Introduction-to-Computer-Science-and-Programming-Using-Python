# problem 1 : write a program that counts up the number of vowels contained the string s (variable 's' is defined)
numVowels = 0
for char in s:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        numVowels+=1
print(numVowels)


# problem 2: write a program that prints the number of times the string 'bob' occurs in s.

count = 0
index = 1
for char in s:
    if (char + s[index:index+2] == 'bob'):
        count+=1
    index+=1
print('Number of times ' + "'bob '"+ 'occors is ' + str(count))

# problem 3 : write a program that prints the longest substring of s in which the letters occurts in alphabetic order.

current = ''
result = ''

for char in s:
    if (current == ''):
        current = char
    elif (current[-1] <= char):
        current += char
    elif (current[-1] > char):
        if (len(result) < len(current)):
            result = current
            current = char
        else:
            current = char
if (len(result) < len(current)):
    result = current
print('Longest substring in a alphabetical order is ' + result)
