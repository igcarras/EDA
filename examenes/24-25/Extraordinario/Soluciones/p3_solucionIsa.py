class Friends:
  def __init__(self,friends:list) -> None:
    self._friends={}
    for f in friends:
      self._friends[f]=[]

  def add_connection(self, friend1: str, friend2: str) -> None:
    if friend1 not in self._friends.keys():
      print(friend1,' does not exist!')
      return
    if friend2 not in self._friends.keys():
      print(friend2,' does not exist!')
      return
    self._friends[friend1].append(friend2)
    self._friends[friend2].append(friend1)

  def get_connections(self, p: str, steps: int) -> list:
    # lista que almacena los amigos de p con una distancia <= steps
    result=[]

    # diccionario para controlar los amigos que vamos visitando
    visited = dict.fromkeys(self._friends.keys(), False)

    # cola que nos permite hacer un recorrido por niveles. Cada vez guardamos una persona y su distancia a p
    # Inicializamos la cola con la persona p y su distancia a ella misma que es 0.
    queue=[(p,0)]
    # marcamos p como visitado
    visited[p] = True

    while len(queue) > 0:
      first_element=queue.pop(0)
      # recuperamos la persona
      current_friend=first_element[0]
      # recuperamos su distancia a p
      current_distance=first_element[1]
      # recuperamos los vecinos de friend
      if current_distance < steps:
        for neighbour in self._friends[current_friend]:
          if visited[neighbour] == False:
            # Si neigbour no ha sido visitado, lo añadimos a la cola.
            # Su distancia es una más que la distancia de current_friend
            queue.append((neighbour,current_distance+1))
            # marcamos como visitado
            visited[neighbour] = True
            # y lo añadimos a la lista de resultados
            result.append(neighbour)

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


if __name__=='__main__':

  people=['Isa','Bea','Ana','Joe','Cris','Jose','Leo','Mia','Ruth','Blas','Fran']
  f=Friends(people)
  print(f)
  f.add_connection("Isa", "Bea")
  f.add_connection("Isa", "Ana")
  f.add_connection("Isa", "Cris")
  f.add_connection("Bea", "Cris")
  f.add_connection("Ana", "Leo")
  f.add_connection("Cris", "Jose")
  f.add_connection("Cris", "Joe")
  f.add_connection("Cris", "Fran")
  f.add_connection("Mia", "Jose")
  f.add_connection("Mia", "Leo")
  f.add_connection("Mia", "Ruth")
  f.add_connection("Ruth", "Blas")
  print(f)
  print('Isa, 1:', f.get_connections('Isa', 1))
  print('Isa, 2:', f.get_connections('Isa', 2))
  print('Isa, 3:', f.get_connections('Isa', 3))
  print('Cris, 1:', f.get_connections('Cris', 1))
  print('Cris, 2:', f.get_connections('Cris', 2))
  print('Cris, 3:', f.get_connections('Cris', 3))
  print('Mia, 1:', f.get_connections('Mia', 1))
  print('Mia, 2:', f.get_connections('Mia', 2))
  print('Blas, 1:', f.get_connections('Blas', 1))
  print('Blas, 2:', f.get_connections('Blas', 2))