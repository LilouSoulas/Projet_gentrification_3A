Pour lucien : 



Ensuite il faut faire tourner le code "fonction.densite" avec dedans la fonction de comptage, une qui compte tout et une qui compte par année. Dans les bouts de codes suivants c'est pour faire le comptage du nmb de métro/tram/bus à 3 minute, puis à 5 minute et enfin le nombre de commerces. 
Je pense qu'il y a moyen d'optimiser la fonction, ou faire des tests sur des plus petits bouts pour voir le temps que ça prend en tout pcq là quand j'ai essayé de faire tourner ça m'a paru longuet (car bcp bcp de lignes dans la base par année)
Et il faudrait enregistrer à la fin du code pour avoir une base avec toutoutout enfin lol 


Dictionnaire des bases de données : 
- Les bases "dtb_poly_annee.df" et "dtb_poly_annee.rds" (dispos dans le [drive]([url](https://drive.google.com/drive/folders/1N78gUPq_8SJUNV36S1BMPPUjwvVEPbaa))) sont les bases avec une ligne par commerce_annee et : 
  - leur localisation (pour le df, c'est juste les coordonnées écrites et pour le .rds c'est une géométrie)
  - Leur polygone 3 minute et polygone 5 minute
  - L'iris qui lui est associé / le type d'iris (gentrifié / pas etc.)
  - Et les indicatrices : parc dans les 3 minutes et parc dans les 5 minutes
 
- La base "densite_cmt_p3" et p5 sont les bases qui à chaque commerce-année associe le nombre de commerces de même type (cmt) dans son polygone de 3/5 minutes => Ces bases sont produites par le code "densite_cmt.qmd" et enregistrées [dans]([url](https://drive.google.com/drive/folders/1LhKBaxnAyDxeNqv6nRNEpw4dZNI8-uOk)) 
