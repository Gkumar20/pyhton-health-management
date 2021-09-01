class Health:
    def gettime(self):
        import datetime
        return datetime.datetime.now()
    def manage(self,name,m,aname):
        self.name=name
        self.m=m
        self.aname=aname
        fname=str(self.name)+str(self.m)
        with open("{}.txt".format(fname),"a") as f:
            f.write("[{}]- {}\n".format(b.gettime(),self.aname))
        return fname 
n=["cliants name:","1.Ganesh","2.Rajesh","3.Luv"]
for i in n:
    print(i)
name=int(input("Enter cliant name no.: "))
print("1.excercise\n2.diat")
m=int(input("Enter a choice:= "))
if m==1:
    typ="excercise"
else:
    typ="diat"
aname=input("Enter {} NAME:= ".format(typ))
print("you entered cliant name= {}\n{} name= {}\n".format(n[name][2:],typ,aname))
b=Health()
r=b.manage(name,m,aname)
print("Health Management shadule")
with open("{}.txt".format(r)) as g:
    print(g.read())