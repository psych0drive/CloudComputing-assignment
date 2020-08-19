class subject:
    def __init__ (self,subname,subid):
        self.subname=subname
        self.subid=subid
    def __repr__(self):
        return self.subid

subjectlist=[]
selectlist=[]
def sublist():
    f=open("subject.txt","r")
    for line in f:
        name,id=line.split(",")
        subjectlist.append(subject(name,id))
    f.close()

def selectsubject(student):
    num=1
    for sub in subjectlist:
        if int(sub.subid[2])==int(student[3]):
            print("{}: {} {}".format(num,sub.subname,sub.subid))
            num+=1

print('welcome. enter your details')

sublist()

name = input('Enter your name:')
roll = input('enter roll no.')
sem =input('enter semester')

if(int(sem)%2==0):
    year=int(int(sem)/2)
else:
    year=int(int(sem)/2 + 1)

student=[name,roll,sem,year]

print('select subject')
while(len(selectlist)<2):
    print('choose atleast 2 subject')
    selectlist.clear()
    selectsubject(student)
    selectlist=[x for x in input().split()]

f=open("studentinfo.txt","a")
f.write("\n{},{},{}\n\nregistered courses:\n\n".format(name,roll,sem))
for x in selectlist:
    f.write("{},{}".format(subjectlist[int(x)].subname,subjectlist[int(x)].subid))
f.close()
