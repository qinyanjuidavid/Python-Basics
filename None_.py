print(type(None))
print(None == False)
print(None ==0 )
print(None=="")
print(None==None)
x=None
print(x==None)
y=None
print(x==y)
# None in a boolean context
def is_it_true(anything):
    """

    :param anything:
    :return:
    """
    if anything:
        print("yes, it\'s true.")
    else:
        print("No, it\'s False")
if __name__=="__main__":
    is_it_true(None)
    is_it_true(not None)