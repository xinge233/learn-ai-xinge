import re
email=input("请输入你的邮箱：")
pattern=re.compile("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9_.+-]+\.com$")
result=re.match(pattern.email.group())
if result:
    print("1")
else:
    print("0")