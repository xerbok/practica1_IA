import random
from problemes.problema import ProblemaCercaLocal

class ElMeuProblema(ProblemaCercaLocal):
    def __init__(self, n, costs_unitaris, penal_parelles, nombre_ideal, alpha):
        self.n = n
        self.costs_unitaris = costs_unitaris
        self.penal_parelles = penal_parelles
        self.nombre_ideal = nombre_ideal
        self.alpha = alpha

    def estat_inicial(self):
        estat = []
        for i in range(self.n):
            estat.append(random.choice([0, 1])) 
        return estat

    def veinat(self, estat):
        veins = []

        for i in range(self.n):
            nou_estat = estat.copy()  
            if nou_estat[i] == 0:
                nou_estat[i] = 1
            else:
                nou_estat[i] = 0      
            veins.append(nou_estat)

        return veins

    def cost(self, estat):
        # Has de calcular el cost total de l'estat sumant:
        cost_total = 0
        
        # 1. Cost individual de les persones seleccionades
        for i in range(self.n):
            if estat[i] == 1:
                cost_total += self.costs_unitaris[i]
        
        # 2. Penalitzacions per incompatibilitats
        for (i, j), penal in self.penal_parelles.items():
            if estat[i] == 1 and estat[j] == 1:
                cost_total += penal
        
        # 3. Penalització per la diferència de mida amb l'ideal * alpha
        nombre_actual = sum(estat)

        cost_total += self.alpha * abs(nombre_actual - self.nombre_ideal)
        return cost_total