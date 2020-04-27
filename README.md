# Exercise 6.11 Averages

The exercise base includes the previously constructed program to store grades. In this exercise you will further develop the class `GradeRegister` so that it can calculate the average of grades and exam results.

## Average grade

Create the method `average_of_grades()` for the class `GradeRegister`. It should return the average of the grades. If the register contains no grades, the method should return `-1`. Use the `grades` list to calculate the average.

Example:

```python
register = GradeRegister()
register.add_grade_based_on_points(93)
register.add_grade_based_on_points(91)
register.add_grade_based_on_points(92)
register.add_grade_based_on_points(88)

print(register.average_of_grades())
```

```plaintext
4.75
```

## Average points

Give the class `GradeRegister` a new object variable: a list where you will store the exam points every time that the method `add_grade_based_on_points` is called. After this addition, create a method `average_of_points()` that calculates and returns the average of the exam points. If there are no points added to the register, the method should return the number `-1`.

Example:

```python
register = GradeRegister()
register.add_grade_based_on_points(93)
register.add_grade_based_on_points(91)
register.add_grade_based_on_points(92)

print(register.average_of_points())
```

```plaintext
92.0
```

## Prints in the user interface

As a final step, add the methods implemented above as parts of the user interface. When the program prints the grade distribution, it should also print the averages of the points and the grades.

```plaintext
Points: **82**
Points: **83**
Points: **96**
Points: **51**
Points: **48**
Points: **56**
Points: **61**
Points:

5: \*
4: \*\*
3:
2: \*
1: \*\*
0: \*
The average of points: 68.14285714285714
The average of grades: 2.4285714285714284
```
