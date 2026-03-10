PRÀCTICA DE CERCA LOCAL

Fitxers implementats:
- problemes/el_meu_problema.py
- algoritmes/hill_climbing.py

Fitxer principal:
- executa_hill_climbing.py
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
- l’algoritme s’atura si troba una solució de cost 0
- o si arriba al màxim d’iteracions establert

EXECUCIÓ

Per executar el programa:
python executa_hill_climbing.py

OBSERVACIONS

- S’han utilitzat les llavors aleatòries fixades al fitxer principal:
  np.random.seed(31)
  random.seed(31)
  per tal que els resultats siguin reproduïbles.

- No s’han modificat els fitxers base proporcionats pel professor.

- La implementació funciona correctament amb el fitxer executa_hill_climbing.py subministrat.

POSSIBLES LIMITACIONS O MILLORABLES

- L’algoritme implementat és hill climbing bàsic amb reinici aleatori, de manera que no garanteix trobar l’òptim global, però sí una bona solució heurística.
- El rendiment depèn del nombre màxim d’iteracions i de l’estat inicial generat aleatòriament.
- No s’han afegit optimitzacions extra ni estratègies avançades de cerca local.

INCIDÈNCIES

- No s’ha detectat cap error de funcionament en les proves realitzades.
