def getdate():
  import datetime
  return datetime.datetime.now()
def fileeditor():
  a=input("Please choose 'd' for Diet and 'e' for Exercise : \n")
  if a=='d':
    with open('adityadiet.txt','a') as f:
      b=input("Enter your diet : ")
      f.write(str([str(getdate())])+" : "+b+"\n")
      print("Entered Successfully")
  elif a=='e':
    with open('adityaexe.txt','a') as f:
      b=input("Enter your exercise : ")
      f.write(str([str(gettime())])+" : "+b+"\n")
      print("Entered Successfully")
  else:
      print("**INVALID INPUT*")
  return
def filereader():
  a=input("Please choose 'd' for Diet and 'e' for Exercise : \n")
  if a=='d':
      with open('adityadiet.txt') as f:
        print(f.read())
  elif a=='e':
      with open('adityaexe.txt') as f:
        print(f.read())
  else:
      print("*INVALID INPUT*")
  return
print("    ---->>>HEALTH MANAGEMENT SYSTEM<<<----\n Developed by :- Aditya Pandey")
s=input("Please choose 'w' for entering diet and 'r' for reading your progress : \n")
if s=='w':
      fileeditor()
      print("THANK YOU! Have a nice day")
elif s=='r':
 filereader()
      print("THANK YOU! Have a nice day")
else:
      print("INVALID INPUT***please check")
      print("THANK YOU! Have a nice day")
