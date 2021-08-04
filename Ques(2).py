"""
2.Develop a python code to read the contents of file and find how many upper case letters,
lower cas letters and digits are existed in the file?
"""

f2=open("text.txt","r")
data=f2.read()
uc=0
lc=0
dig=0
for ch in data:
    if ch.isupper():
        uc+=1
    elif ch.islower():
        lc+= 1
    elif ch.isdigit():
        dig+=1
print("UPPER CASE LETTERS=",uc,"LOWER CASE LETTERS=",lc,"DIGITS=",dig)
f2.close()

"""
contents in text.txt:
AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz  
1 2 3 4 5 6 7 8 9 1
Output:
UPPER CASE LETTERS= 26 LOWER CASE LETTERS= 26 DIGITS= 10
"""
