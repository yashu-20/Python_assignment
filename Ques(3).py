"""
3.Create a file and insert the records in the following format(Read the records from the user)
SNo      Name      Game
1	 Rahul	  Cricket
2.       David 	  Chess
3.       Ram 	  Volly Ball
"""

fp=open("GamesRecord.txt","w")
t=["SNo\t","Name\t","Game\n"]
fp.writelines(t)
n=int(input("Enter number of rows: "))
for i in range(n):
    fp.writelines([input(),"\t",input(),"\t",input()])
    fp.write("\n")
fp.close()
fp1=open("GamesRecord.txt","r")
data=fp1.read()
print(data)
fp1.close()

"""
Enter number of rows: 3
1.
Rahul
Cricket
2.
David
Chess
3.
Ram
VollyBall
SNo	Name	Game
1.	Rahul	Cricket
2.	David	Chess
3.	Ram     VollyBall
"""
