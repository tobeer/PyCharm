# %%

import re

ss = 'I love you, do you?'
res = re.match(r'((\w)+(\W))+', ss)
print("group() ", res.group())
print("groups() ", res.groups())  # ????
print("group(1) ", res.group(1))
print("group(2) ", res.group(2))
print("==============")
res = re.match(r'((\w)+(\W))', ss)
print("group() ", res.group())
print("groups() ", res.groups())
print("group(1) ", res.group(1))
print("group(2) ", res.group(2))
