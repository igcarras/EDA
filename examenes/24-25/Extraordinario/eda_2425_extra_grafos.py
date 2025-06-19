
class Friends():
    def __init__(self):
        self.people=[]
        self.connections=[]

    def addPerson(self,p):
        self.people.append(p)
        self.connections.append([])

    def addConnection(self,p1,p2):
        #print('new connection:',p1,p2)
        if p1 not in self.people:
            print(str(p1) + ' does not exist!!!')
            return
        if p2 not in self.people:
            print(str(p2) + ' does not exist!!!')
            return
        i1=self.people.index(p1)
        i2=self.people.index(p2)
        self.connections[i1].append(p2)
        self.connections[i2].append(p1)

    def __str__(self):
        result=''
        for p in self.people:
            result+=str(p)+':\n'
            i=self.people.index(p)
            for friend in self.connections[i]:
                result+='\t'+str(friend)
            result+='\n'
        return result


    def getConnections(self, p, steps):
      visited=[p]
      result=[]
      Q=[[p,0]]
      while len(Q)>0 and Q[0][1]<steps:
        contact=Q.pop(0)
        person=contact[0]
        dist=contact[1]
        ind=self.people.index(person)
        for friend in self.connections[ind]:
          if friend not in visited:
            visited.append(friend)
            Q.append((friend,dist+1))
            result.append(friend)
      return result





#we use this dictionary to represent the vertices with numbers:
labels=['Isa','Bea','Ana','Joe','Cris','Jose','Leo','Mia','Ruth','Blas']
g=Friends()

g.addPerson("Isa")
g.addPerson("Bea")
g.addPerson("Ana")
g.addPerson("Cris")
g.addPerson("Joe")
g.addPerson("Jose")
g.addPerson("Leo")
g.addPerson("Mia")
g.addPerson("Ruth")
g.addPerson("Blas")
g.addPerson("Fran")

g.addConnection("Isa","Bea")
g.addConnection("Isa","Ana")
g.addConnection("Isa","Cris")
g.addConnection("Bea","Cris")
g.addConnection("Ana","Leo")
g.addConnection("Cris","Jose")
g.addConnection("Cris","Joe")
g.addConnection("Cris","Fran")
g.addConnection("Mia","Jose")
g.addConnection("Mia","Leo")
g.addConnection("Mia","Ruth")
g.addConnection("Ruth","Blas")




print(g)
print('g.getConnections("Isa",1):',g.getConnections("Isa",1))
print('g.getConnections("Isa",2):',g.getConnections("Isa",2))
print('g.getConnections("Isa",3):',g.getConnections("Isa",3))
print('g.getConnections("Cris",1):',g.getConnections("Cris",1))
print('g.getConnections("Cris",2):',g.getConnections("Cris",2))
print('g.getConnections("Cris",3):',g.getConnections("Cris",3))
print('g.getConnections("Mia",1):',g.getConnections("Mia",1))
print('g.getConnections("Mia",2):',g.getConnections("Mia",2))
print('g.getConnections("Blas",1):',g.getConnections("Blas",1))
print('g.getConnections("Blas",2):',g.getConnections("Blas",2))