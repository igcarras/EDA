from graph import AdjacentVertex
from graph import Graph

class Queue:
      
      def __init__(self):
        """Create an empty queue"""
        self.items=[]
      
      def __len__(self):
        """Return the number of elements in the queue"""
        return len(self.items)
      
      def isEmpty(self):
        """Return True if the queue is empty"""
        return len(self)==0
     
      def __str__(self):
        return str(self.items)
      
        
      def enqueue(self,e):
        """Add the element e to the tail of the queue"""
        self.items.append(e)
        
      def dequeue(self):
        """Remove and return the first element in the queue"""
        if self.isEmpty():
          print('Error: Queue is empty')
          return None
        return self.items.pop(0) 
      
       
class Graph2(Graph): 
    def min_number_edges(self, start: str, end: str) -> int:
        """returns the minimum number of edges from start to end"""
         
        if start not in self._vertices.keys() or end not in self._vertices.keys():
            return
        
        if start == end or len(self._vertices[start]) == 0:
            return 0
        camino_corto = len(self.camino_corto(start,end))
        
        return camino_corto -1
    
    def camino_corto(self,start,end,camino = []):
        camino = camino + [start] 
        if start == end: 
            return camino  
        cami_cortito = None
        for adj in self._vertices[start]: 
            if adj.vertex not in camino: 
                camino_nuevo = self.camino_corto(adj.vertex, end, camino)
                if camino_nuevo: 
                    if not cami_cortito or len(camino_nuevo) < len(cami_cortito): 
                        cami_cortito = camino_nuevo 
        if cami_cortito:   
            return cami_cortito
    
    
    def transpose(self) -> 'Graph2':
        """ returns a new graph that is the transpose graph of self"""
        herma_graphe = Graph(self._vertices)
        for dentro_verti in self._vertices:
         for dent_verti in self._vertices[dentro_verti]:
	         herma_graphe.add_edge(dent_verti.vertex, dentro_verti, dent_verti.weight)
        return herma_graphe
                  

    def is_strongly_connected(self) -> bool:
        """ This function checks if the graph is strongly connected.
        A directed graph is strongly connected when for any
        pair of vertices u and v, there is always a path from u to v.
        If the graph is undirected, the function returns True if the graph is
        connected, that is, there is a path from any vertex to any other vertex
        in the graph.
        """
        lista_vertices = []
        if self._directed:
            je_controle = 0  
        else:
            je_controle = len(self._vertices.items())-1
        while je_controle < len(self._vertices.items()):
            for den_verti in self._vertices.items():
                vertex = den_verti[0]
                lista_vertices.append(vertex) 

            queue = Queue()
            queue.enqueue(lista_vertices[je_controle][0])
            diccio_visitado = {}
            for h in self._vertices: 
                diccio_visitado[h] = False

            while queue.isEmpty() == False:

                actual = queue.dequeue()

                if not diccio_visitado[actual]:
                    diccio_visitado[actual] = True

                    for adyacente in self._vertices[actual]:
                        queue.enqueue(adyacente.vertex)

            je_controle += 1

            if False in diccio_visitado.values():
             
                return False
        return True
       
            
        
    
        
         
        
        
        
        
        
        
        
        
        
        
        
        

