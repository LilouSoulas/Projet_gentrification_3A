Note à moi même (M) : 

avec la base de lilou et lucien (siret - polygone) --> faire tourner le code reconstruction_base_pour_comptage.R
Pour mettre les 3 bases ensemble, associer les polygones aux commerces_annee de la base finale_dtb 
Ce même code permet aussi d'ajouter les infos IRIS de chaque commerce 

A la fin de ce code, t'as une base par siret_annee avec les infos d'IRIS et les polygones 3 / 5 par commerce (dupliqué sur les années)

Ensuite faire tourner le code de focntion_densite qui fait d'abord le comptage des arrêts RATP _par année_ 
Puis comptage des autres commerces aussi apr année (lorsqu'ils sont encore ouverts)
