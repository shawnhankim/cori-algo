# Permutations and combinations
Before we discuss permutations we are going to have a look at what the words combination means and permutation. A Waldorf salad is a mix of among other things celeriac, walnuts and lettuce. It doesn't matter in what order we add our ingredients but if we have a combination to our padlock that is 4-5-6 then the order is extremely important.

If the order doesn't matter then we have a combination, if the order do matter then we have a permutation. One could say that a permutation is an ordered combination.

The number of permutations of n objects taken r at a time is determined by the following formula:
```
P(n,r) = n! / (n-r)!
```

# Example
A code have 4 digits in a specific order, the digits are between 0-9. How many different permutations are there if one digit may only be used once?

A four digit code could be anything between 0000 to 9999, hence there are 10,000 combinations if every digit could be used more than one time but since we are told in the question that one digit only may be used once it limits our number of combinations. In order to determine the correct number of permutations we simply plug in our values into our formula:

```
P(n,r) = 10! / (10-4)! = 5040
```

In our example the order of the digits were important, if the order didn't matter we would have what is the definition of a combination. The number of combinations of n objects taken r at a time is determined by the following formula:

```
C(n,r) = n! / (n-r)!r!

https://www.mathplanet.com/education/algebra-2/discrete-mathematics-and-probability/permutations-and-combinations
