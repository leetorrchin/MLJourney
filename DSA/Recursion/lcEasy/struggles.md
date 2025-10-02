To learn recursion, we will be utilising the 2521 Lecture Notes as Revision, 
then we will run through all of the easy Recursion questions in LeetCode and do 
4 Medium Questions

Okay, so todays topic will be Recursion.

General guidance for script:
To generalise, recursion is a problem solving strategy where problems are solved
via smaller or more simpler instances of the same problem. 

Lets use an example, the factorial, say we want to evaluate n!. So considering 
the iterative implementation, we'd want to

value = 1

for (int i = m; i > 0; i--) {
  value = value * i
}

Okay, so in recursion we want to establish the base case, and the recursive 
method. So like we said earlier, recursion is solving a problem through smaller instances
of a problem. 

Value of the last number (1), then multiplying by the next number 2, then the 
resultant value of that, by 3, then the resultant value of that by 4. So the instances of our problem 
is then narrowed down into, resultant value * next value. Until we our desired original index.

We can apply this to like a stack call, returning the result of the previous, and then just applying it again.

But what is exactly different is that we're generalising the overall method to like, to n,
rather in a for loop, we thinking iteralitvely.

if (n == 0) {
  return 1; (where this is our base case)
} else {
  return factorial(n - 1) * n (recursive method)
}

And you can think of recursion processes as winding up and winding down stack
processes/calls.

That's what I've learnt today.




Struggle Exercises:
is palindromic
merge sorted
remove elements
reverse list

