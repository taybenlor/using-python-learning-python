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
    if population == 0:
        return 'Extinct'
    elif population > 0 and population < 51:
        return 'Critically Endangered'
    elif population > 50 and population < 251:
        return 'Endangered'
    elif population > 250 and population < 1001:
        return 'Vulnerable'
    else:
        return 'Lower Risk'


if __name__ == "__main__":
  import doctest
  doctest.testmod()
