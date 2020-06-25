import sys
print("Hello World")
suffixes={1000:['KB',"MB","GB","TB","PB","ZB","YB"],
          1024:['KiB','MiB','GiB','TiB','PiB','EiB','ZiB','YiB']}
def approximate_size(size,a_kilobytes_is_1024_bytes=True):
    """
    A Doc string should be the first thing that is defined in the  function
    :param size:
    :param a_kilobytes_is_1024_bytes:
    :return:
    """
    if size<0:
        raise ValueError('The number must be non-negative.')
    print(size)
if __name__ == "__main__":
    approximate_size(10000000,False)
try:
    import chardet
except ImportError:
    chardet=None
if chardet:
    print("Import Availble")
else:
    print("Import not Available.")
print("Hello Python!")

print(8,end="\n")
print("this is for separation","key",sep="%")
print("My name is","Day Qinyanjui",sep=": ")
print("I love Coding.", "I don\'t like movies.","I am hoping in God that one day i ll be a senior software engineer.",sep="\n",end="\n")
#Python uses indentations
if True:
    print("True")
else:
    print("False")
    
if True:
    print("Answer")
    print("True")
else:
    print("Answer")
    print("False")
    

















