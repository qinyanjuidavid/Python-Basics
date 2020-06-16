import fractions
def is_it_true(anything):
    """
    if anything is 1 is it True returns True,
    But if anything is 0 anything returns False.
    :param anything:
    :return:
    The non-Zero integers are true
    """
    if anything:
        print("yes, it's true")
    else:
        print('No, it\'s not true.')

if __name__ == "__main__":
    is_it_true(1+0)
    is_it_true(fractions.Fraction(1,2))
    is_it_true(-1)
    is_it_true(0)
    is_it_true(0.0)
    is_it_true(0.1)
    is_it_true(fractions.Fraction(0,1))