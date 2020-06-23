s="100 North Main Road"
print(s.replace('Road',"RD."))
import re
print(re.sub("Road$",'RD.',s))
print(re.sub('Road$',"RD.",s))
print(re.sub(r"/Road/b","RD",s))