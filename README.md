# Projet d'économie et de sociologie, ENSAE 3A

### Lilou Soulas, Maëlie Perier et Lucien Chaudron

## Contexte

Ce repository GitHub contient le code que nous avons produit au cours de notre projet de 3e année pour le cours "Projet en économie, sociologie et science des données". <br>
Notre projet porte sur l'étude du processus de gentrification et de ses effets sur la fermeture des commerces, en interrogeant notamment deux hypothèes : <br>
* Les effets de **l'accessibilité** des commerces, à savoir leur proximités avec les réseaux de transports, les parcs, etc... <br>
* Le maintien ou non des **effets d'agglomération**, qui permettent à certains commerces hors contexte de gentrification de profiter d'externalités positives liées à la concentration dans un même lieu (mutualisation de la clientèle, des coûts de livraisons des ingrédients.

## Organisation du repo

### Récupération de la donnée initiale

Les différents scripts contenus dans *preprocessing/data_retrieval/* permettent de récupérer les différentes données de diverses sources nécessaires à la constitution de nos bases de données (les données SIRENE, les données de conjoncture économique, et les données sur les IRIS).

### Constitution des géométries des commerces 

Afin de mener notre analyse spatiale, nous devons constituer pour chaque commerce deux polygones, qui représente chacun une zone accessible à 3 et à 5 minutes à pied. Ces scripts sont situés dans *preprocessing/geometry/*.

### Calculs des densités de points d'intérêt

Notre analyse repose sur l'accessibilité des commerces et la concentration de commerces de même type au sein du même espace. Nous devions donc calculer, pour chaque commerce, la densité de commerce du même type dans leur polygone, ainsi que le nombre de parcs et d'arrêts de transports. Ces scripts sont disponibles dans *preprocessing/density_calculation/*.

### Analyse de survie des commerces

L'analyse de la survie des commerces se fait via un modèle de Cox, dont le script est situé à l'emplacement *analysis/cox.qmd*

### Stockage des données

Les données manipulées sont trop volumineuses pour être stockées sur un repo GitHub. Nous les conservons sur une instance séparée, et pouvons les rendre disponibles à la demande.
