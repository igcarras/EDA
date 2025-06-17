import math

class SubestacionAdyacente:
    def __init__(self, estacion: str, coste: int):
        self.estacion = estacion
        self.coste = coste

    def __repr__(self):
        return f"({self.estacion}, coste={self.coste})"


class RedElectrica:
    def __init__(self):
        # Diccionario que representa el grafo: subestacion -> lista de SubestacionAdyacente
        self.grafo = {}

    def anadir_subestacion(self, codigo: str):
        """Anade una subestacion a la red si no existe ya."""
        if codigo not in self.grafo.keys():
            self.grafo[codigo] = []
        else:
            print(f"Subestacion {codigo} ya existe. No se anade de nuevo.")

    def anadir_linea(self, estacion1: str, estacion2: str, coste: int):
        """
        Anade una linea de alta tension dirigida de estacion1 a estacion2 con el coste dado.
        Ambas subestaciones deben existir previamente.
        No se permiten duplicados.
        """
        if estacion1 not in self.grafo.keys() or estacion2 not in self.grafo.keys():
            print("Ambas subestaciones deben existir en la red.")
            return

        if estacion1 == estacion2:
            print("Las subestaciones deben ser distintas")
            return

        # Verificar si ya existe la conexion
        for adyacente in self.grafo[estacion1]:
            if adyacente.estacion == estacion2:
                print(f"La linea de {estacion1} a {estacion2} ya existe.")
                return

        self.grafo[estacion1].append(SubestacionAdyacente(estacion2, coste))

    def estaciones_proximas(self, estacion1: str):
        """
        Devuelve una lista con las subestaciones que pueden recibir electricidad desde estacion1.
        Si no existe la subestacion o no tiene conexiones, se devuelve una lista vacia.
        """
        if estacion1 not in self.grafo:
            return []

        return [adyacente.estacion for adyacente in self.grafo[estacion1]]

    def min_distancia(self, distancias: dict, visitados: dict) -> str:
        min_dist = math.inf
        min_estacion = None
        for estacion in self.grafo:
            if not visitados[estacion] and distancias[estacion] <= min_dist:
                min_dist = distancias[estacion]
                min_estacion = estacion
        return min_estacion

    def dijkstra(self, origen: str):
        visitados = {v: False for v in self.grafo}
        previos = {v: None for v in self.grafo}
        distancias = {v: math.inf for v in self.grafo}

        distancias[origen] = 0

        for _ in range(len(self.grafo)):
            u = self.min_distancia(distancias, visitados)
            #if u is None:
            #    break  # No quedan alcanzables

            visitados[u] = True

            for ady in self.grafo[u]:
                v = ady.estacion
                coste = ady.coste
                if not visitados[v] and distancias[v] > distancias[u] + coste:
                    distancias[v] = distancias[u] + coste
                    previos[v] = u

        return distancias, previos

    def ruta_minima(self, origen: str, destino: str):
        """
        Devuelve una tupla (coste_total, ruta como lista de subestaciones)
        usando Dijkstra. Si no hay ruta, devuelve (math.inf, []).
        """
        if origen not in self.grafo or destino not in self.grafo:
            return (math.inf, [])

        distancias, previos = self.dijkstra(origen)

        if distancias[destino] == math.inf:
            return (math.inf, [])

        # Reconstruir la ruta desde destino hacia origen
        ruta = []
        actual = destino
        while actual is not None:
            ruta.insert(0, actual)
            actual = previos[actual]

        return distancias[destino], ruta

# Ejemplo de uso:
if __name__ == "__main__":
    red = RedElectrica()

    # Añadir subestaciones A a J
    for codigo in "ABCDEFGHIJ":
        red.anadir_subestacion(codigo)

    # Añadir líneas (rutas con diferentes costes)
    red.anadir_linea("A", "B", 4)
    red.anadir_linea("A", "C", 2)
    red.anadir_linea("B", "D", 5)
    red.anadir_linea("C", "D", 8)
    red.anadir_linea("C", "E", 10)
    red.anadir_linea("D", "E", 2)
    red.anadir_linea("D", "F", 6)
    red.anadir_linea("E", "G", 3)
    red.anadir_linea("F", "G", 1)
    red.anadir_linea("G", "H", 1)
    red.anadir_linea("H", "I", 2)
    red.anadir_linea("I", "J", 4)
    red.anadir_linea("E", "J", 12)
    red.anadir_linea("F", "J", 10)

    # Casos de prueba desde distintas subestaciones
    casos = [
        ("A", "D"),
        ("A", "G"),
        ("D", "G"),

        ("A", "J"),
        ("C", "J"),
        ("B", "H"),
        ("A", "G"),
        ("D", "J"),
        ("F", "J"),
        ("E", "J"),
    ]

    for origen, destino in casos:
        coste, ruta = red.ruta_minima(origen, destino)
        print(f"Ruta de menor coste desde {origen} a {destino}: {ruta}, con coste total: {coste}")



