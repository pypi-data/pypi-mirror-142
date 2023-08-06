# class cov:
#     def __init__(self, cvv, cd):
#             self.name = cvv
#             self.intros = cd
#     def intro(self):
#         print(self.name)
        
        
        
# asosiy = cov('Islam','turkey')

# asosiy.intro()

# class Solution:
    
#     def solve(self, s):
#         for i in range(1,len(s)):
#             vv = []
#             if s[0] != s[1]:
#                 if s[i] != s[i+1]: 
#                     del s[i]
#             else:
#                     vv.append(s[i])
            
#             print(vv)

# c = Solution()
# print(c.solve(['11000']))

import datetime
import dateutil.tz

now = datetime.datetime.now()

tz = dateutil.tz.gettz("Asia/Bishkek")
utc = dateutil.tz.tzutc()

con = datetime.datetime(2222,10,23,2,30, tzinfo=tz)
con.replace(fold=1).astimezone(utc)

print(con)