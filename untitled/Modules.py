# import os
#
# print (os.name)
#
# print(os.environ)
#
# print(os.getlogin())
#
# print(os.getppid())
#
#
# import math
#
# print(math.ceil(11.98788))
#
# import random
# print(random.randrange(0,122222,253))
#
#

import  sys
try:
    a=10
    b=0
    c=a/b
    print(c)
except Exception:
    print("Oops!",sys.exc_info(),"occured" )