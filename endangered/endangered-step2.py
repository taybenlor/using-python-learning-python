def categorise(population):
    """
    This function takes the population of an animal.
    It then returns the endangered category,
    based off the table above.

    >>> categorise(55)
    'Endangered'

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
    """
    return 'Endangered'


if __name__ == "__main__":
  import doctest
  doctest.testmod()
