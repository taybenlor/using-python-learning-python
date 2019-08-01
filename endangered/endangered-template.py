"""
There are many criteria that determine whether an animal is "Endangered".

One of the simplest is based on the population of "Mature Individuals".
This criteria is used if the population is stable.
If the population is decreasing then a different criteria is used.

In this project we'll write tools that help us classify endangered animals.
Based off the criteria here:

Population | Category
------------------------------
         0 | Extinct
      1-50 | Critically Endangered
    51-250 | Endangered
  251-1000 | Vulnerable
     1000+ | Lower Risk


Following are a number of tests to make sure your program is working.

You can run these tests with:

python endangered.py -v


First we'll test the categorise function. Checking each category:

>>> categorise(0)
'Extinct'
>>> categorise(8)
'Critically Endangered'
>>> categorise(105)
'Endangered'
>>> categorise(352)
'Vulnerable'
>>> categorise(1200)
'Lower Risk'


Then we'll test the boundaries:

>>> categorise(1)
'Critically Endangered'
>>> categorise(50)
'Critically Endangered'
>>> categorise(51)
'Endangered'
>>> categorise(250)
'Endangered'
>>> categorise(251)
'Vulnerable'
>>> categorise(1000)
'Vulnerable'
>>> categorise(1001)
'Lower Risk'

Good luck!
"""


def categorise(population):
    """
    This function takes the population of an animal.
    It then returns the endangered category,
    based off the table above.
    """
    pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
