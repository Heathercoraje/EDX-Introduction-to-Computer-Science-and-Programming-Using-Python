# Algorithmic complexity
### Complexity of algorithms
Though computers are fast and getting faster, data sets can be very large.
There are time and space efficiency of a program and it is tradeoff relation. In the program we focus on time efficiency. A program can be implemented in many different ways and we want to understand the efficiency of solution. When evaluating efficiency of programs, abstract notion of **order to growth** is the most appropriate way of assessing the impact of choices of algorithms in solving a problem.

#### Order of growth (Big 0 notation)
+ Evaluate algorithms
+ Evaluate scalability
+ Evaluate in terms of input size

## Sort algorithms and their complexity
+ Monkey sort(also called bogo sort): because it is unbounded it can be O(?)

+ Bubble sort: bubble sort basically bubble two items each time and swap to put smaller before bigger. This solution has to go through each elements in len(L) and until there is no more item to swap so it is quadratic class of complexity

+ Selection sort: Extract the min element and swap it with element at index 0 until list is fully sorted. Time-wise it is a little more efficient than bubble sort but it still has a quadratic class of complexity  

+ Merge sort: use divide and conquer method and it has O(n log(n)) complexity.
