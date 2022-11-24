import os

try:
	import aminofix
except ModuleNotFoundError:
	os.system("pip install Amino.fix")

try:
	import threading
except ModuleNotFoundError:
	os.system("pip install threading")

import aminofix,requests
from threading import Thread as t
print('                القائد ياور      \033[12;32m           جيش البحر         ')

print("""
○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○●○
.
""")

print('         محمد    \033[1;36m⇣❂الـــتــོ͢༗ۦـٰۣؒۦོ᷼ـا❂بـۦ᭄꙰ــོ͢𖡹ـوت❂⇣ ‌           ')
print("""
‏❖༶———﴾༶❖༶﴿———༶❖☆❋──❁❃──❋❃──❋─❁❃──❋❃──❋‏❖༶————﴾༶❖༶﴿————༶❖☆❋──❁❃──❋❃──❋
.
""")

print('      سامر \033[1;31m⇣❂الـــ༗ۦـٰۣؒۦོ᷼ـ❂ـۦ᭄꙰ـحــོ͢𖡹ـوت❂⇣                   ')
print("""
[C]•─━─━─━─━─━─━─━─━─━─[C]•─━─━─━─━─━─━─━─━─━─[C]•─━─━─━─━─━─━─━─━─━─
""")
print('   ياور \033[1;33m⇣❂الــ༗ۦـٰۣؒدفـ❂ـۦ᭄꙰ـــོ͢ا𖡹ـن❂⇣                      ')
print("""
) •♥•.¸¸.•♥•.¸¸.) •♥•.¸¸.•♥•.¸¸.•♥•.¸¸.•♥•(•♥•.¸¸.•♥•(•♥•.¸¸.•♥•(
""")
print('\033[1;36minstagram.   :      tab_ot.9')
print("""
amino    :    http://aminoapps.com/p/jy8wrqx
""")
email=input("email : ")
password=input("password : ")

clint=aminofix.Client()
clint.login(email=email,password=password)
headers=clint.headers
x=clint.get_from_code(input("Group link : "))
com=[]
x1=clint.get_from_code(input("Community link : "))
comId=x.path[1:x.path.index('/')]
chatId=x.objectId
subclint=aminofix.SubClient(comId=comId,profile=clint.profile)
subclin=aminofix.SubClient(comId=x1.path[1:x1.path.index('/')],profile=clint.profile)
userI=[]
s=0
size=100
while (s!=200):
		user=subclin.get_online_users(start=s,size=size).profile.userId
		for o in user:
			userI.append(o)
		s+=100
		size+=100
print(userI)
def send():
	for i in range(100):
			try:
				subclint.edit_chat(chatId=chatId,coHosts=userI)
			except:
				print("التابوت محمد وسامر الحوت وياور العراقي ازيلء خجاب'\033[1;34m'")
def all():
	while True:
		t(target=send).start()
all()
