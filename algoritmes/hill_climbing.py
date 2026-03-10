from algoritmes.algoritme_cerca_local import AlgoritmeCercaLocal


class HillClimbing(AlgoritmeCercaLocal):
    """
    Hill climbing amb reinici aleatori.

    Estratègia:
    - parteix d'un estat inicial aleatori
    - es mou al millor veí que millori l'actual
    - si no hi ha millora, fa reinici aleatori
    - s'atura després de K iteracions totals
      o si arriba a cost 0
    """

    def __init__(self, max_iter=1000):
        self.max_iter = max_iter

    def executa(self, problema):
        # Inicialització
        estat_actual = problema.estat_inicial()
        cost_actual = problema.cost(estat_actual)

        millor_estat = estat_actual
        millor_cost = cost_actual

        historia = [millor_cost]
        iteracions = 0
        iteracionsSenseMillora = 0

        while iteracions < self.max_iter and iteracionsSenseMillora < (self.max_iter - iteracions) // 2:
            # Criteri d'aturada si ja hem arribat al millor cost possible
            if millor_cost == 0:
                break

            veins = problema.veinat(estat_actual)

            # Triar el millor veí
            millor_vei = None
            millor_cost_vei = float("inf")

            for vei in veins:
                c = problema.cost(vei)
                if c < millor_cost_vei:
                    millor_cost_vei = c
                    millor_vei = vei

            iteracions += 1
            iteracionsSenseMillora += 1

            # Si el millor veí millora l'estat actual, avancem
            if millor_cost_vei < cost_actual:
                estat_actual = millor_vei
                cost_actual = millor_cost_vei

                # Actualitzar millor global
                if cost_actual < millor_cost:
                    millor_estat = estat_actual
                    millor_cost = cost_actual
                    iteracionsSenseMillora = 0
                
            else:
                # Òptim local -> reinici aleatori
                estat_actual = problema.estat_inicial()
                cost_actual = problema.cost(estat_actual)
                
                # També pot passar que el reinici sigui millor
                if cost_actual < millor_cost:
                    millor_estat = estat_actual
                    millor_cost = cost_actual

            historia.append(millor_cost)

        return millor_estat, historia