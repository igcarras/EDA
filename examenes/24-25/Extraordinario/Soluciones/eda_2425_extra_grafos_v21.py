class Friends:
  def __init__(self,friends:list):
    self._friends={}
    for f in friends:
      self._friends[f]=[]    
  def addConnection(self, friend1, friend2):
    if friend1 not in self._friends.keys():
      print(friend1,' does not exist!')
      return
    if friend2 not in self._friends.keys():
      print(friend2,' does not exist!')
      return
    self._friends[friend1].append(friend2)
    self._friends[friend2].append(friend1)

  def getConnections(self,p,steps):
    result=[]
    visited=[p]
    queue=[(p,0)]
    while queue[0][1]<steps:
      vertex=queue.pop(0)
      friend=vertex[0]
      dist=vertex[1]
      for adj in self._friends[friend]:
        if adj not in visited:
          queue.append((adj,dist+1))
          visited.append(adj)
          result.append(adj)
    return result      

  def __str__(self) -> str:
    result = ''
    for friend in self._friends.keys():
        result += '\n' + str(friend) + ': '
        if self._friends[friend] is not None:
            for connection in self._friends[friend]:
                result += str(connection) + ", "
        if result.endswith(", "):
            result = result[:-2]
    return result
L=['Isa','Bea','Ana','Joe','Cris','Jose','Leo','Mia','Ruth','Blas','Fran']
F=Friends(L)    
print(F)
F.addConnection("Isa","Bea")
F.addConnection("Isa","Ana")
F.addConnection("Isa","Cris")
F.addConnection("Bea","Cris")
F.addConnection("Ana","Leo")
F.addConnection("Cris","Jose")
F.addConnection("Cris","Joe")
F.addConnection("Cris","Fran")
F.addConnection("Mia","Jose")
F.addConnection("Mia","Leo")
F.addConnection("Mia","Ruth")
F.addConnection("Ruth","Blas")
print(F)
print('Isa, 1:',F.getConnections('Isa',1))
print('Isa, 2:',F.getConnections('Isa',2))
print('Isa, 3:',F.getConnections('Isa',3))
print('Cris, 1:',F.getConnections('Cris',1))
print('Cris, 2:',F.getConnections('Cris',2))
print('Cris, 3:',F.getConnections('Cris',3))
print('Mia, 1:',F.getConnections('Mia',1))
print('Mia, 2:',F.getConnections('Mia',2))
print('Blas, 1:',F.getConnections('Blas',1))
print('Blas, 2:',F.getConnections('Blas',2))