#Tuples are immutable list,
a_tuple=('a','b','mpligrim','z','example','a')
print(a_tuple)
print(a_tuple[0])
print(a_tuple[-1])
print(a_tuple[0:3])
print(a_tuple.index("b"))
print(a_tuple.count("a"))
print(len(a_tuple))
print(a_tuple)
print("example" in a_tuple)

#Tuples in a boolean
def is_it_true(anything):
    """

    :param anything:
    :return:
    """
    if anything:
        print("Yes, it\'s true.")
    else:
        print('No, it\'s False.')

if __name__ == "__main__":
    is_it_true(())
    is_it_true(("a","b"))
    is_it_true((False,))
    # is_it_true((False)) This is not a tuple
# Assigning Multiple Values At Once
v=("a",2,True)
(x,y,z)=v
print(x)
print(y)
print(z)
(MONDAY,TUESDAY,WEDNESDAY,THURSDAY,FRIDAY,SATURDAY,SUNDAY)=range(7)
print(MONDAY)
print(TUESDAY)
print(SUNDAY)
