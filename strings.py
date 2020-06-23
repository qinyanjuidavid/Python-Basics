

'''def approximate_size(size,a_kilobyte_is_1024_bytes=True):
    """

    :param size:
    :param a_kilobyte_is_1024_bytes:
    :return:
    """
    suffixes = {
        1000: ['KB', "MB", "GB", "TB", "PB", "ZB", "YB"],
        1024: ['KiB', "MiB", "GiB", "TiB", "PiB", "ZiB", "YiB"]
    }
    if size<0:
        raise ValueError("Numbers must be non-negative.")
    multiple= 1024 if a_kilobyte_is_1024_bytes else 1000
    for suffixes in suffixes[multiple]:
        size/=multiple
        if size<multiple:
            print(f"{size}:{suffixes}")
    raise ValueError("number too large")

if __name__=="__main__":
    approximate_size(1000)'''


username="David"
password="keepitclean"
print(f"{username} password is {password}")
print("{0}'s password is {1}".format(username,password))
# Other string methods
s="""Finished files are the re-
sult of years of scientif-
ic study combined with the
experience of years"""
print(s.split())
print(s.splitlines())
print(s.lower())
print(s.upper())
print(s.capitalize())
print(s.count("f"))
query="user=Day&database=postgresql&password=keepitclean"
print(query.split("&"))
name="Da vi dk in ya nju i"
print(name.split(" "))
num="1.2.3156.256.9"
print(num.split("."))

a_string="My alphabet starts where your alphabet ends"
print(a_string[3:9])
print(a_string[3:-3])
print(a_string[0])
print(a_string[:19])
print(len(a_string))
print(a_string.index("a"))
print(a_string.index("s"))
print(a_string[6])
print(a_string.count("a"))