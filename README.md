PRÀCTICA DE CERCA LOCAL

Fitxers implementats:
- problemes/el_meu_problema.py
- algoritmes/hill_climbing.py

Fitxer principal:
- p1.py
Aquest fitxer ve donat pel professor i no s’ha modificat.

DESCRIPCIÓ DE LA IMPLEMENTACIÓ

1) el_meu_problema.py
S’ha implementat la classe ElMeuProblema, que hereta de ProblemaCercaLocal.

L’estat es representa com una llista de 0 i 1 de longitud n:
- 1 indica que la persona està seleccionada
- 0 indica que la persona no està seleccionada

S’han implementat els mètodes:
- estat_inicial(): genera un estat inicial aleatori
- veinat(estat): genera tots els veïns canviant una única posició de l’estat
- cost(estat): calcula el cost total com la suma de:
  * costos unitaris de les persones seleccionades
  * penalitzacions per parelles incompatibles seleccionades
  * penalització per diferència respecte al nombre ideal de persones

2) hill_climbing.py
S’ha implementat l’algoritme Hill Climbing amb reinici aleatori.

Funcionament:
- es parteix d’un estat inicial aleatori
- es genera el veïnat de l’estat actual
- es selecciona el veí amb menor cost
- si aquest veí millora l’estat actual, es continua des d’aquest veí
- si no millora, es fa un reinici aleatori

Criteri d’aturada:
- L’algoritme s’atura si en la meitat d'iteracions restants no s'ha trobat una millora
- Si arriba al màxim d’iteracions establert

EXECUCIÓ

Per executar el programa:
python p1.py

OBSERVACIONS

- La implementació funciona correctament amb el fitxer p1.py subministrat.

