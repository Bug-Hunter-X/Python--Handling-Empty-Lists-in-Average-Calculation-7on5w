# Python: Handling Empty Lists in Average Calculation

This code snippet showcases a common error in Python: attempting to calculate the average of an empty list, which leads to a `ZeroDivisionError`.  The improved version demonstrates how to elegantly handle this case.

## The Problem

Directly calculating the average of an empty list results in division by zero.  The original `calculate_average` function doesn't account for this possibility.

## The Solution

The improved version checks for an empty list using `if not numbers:` and returns 0 in that specific case, avoiding the division-by-zero error.