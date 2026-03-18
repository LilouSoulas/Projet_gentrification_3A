
#On importe les graphs et verts de 2025 pour ne pas le faire à chaque fois dans la fonction
if(TRUE){
  graphs_list <- list()
  verts_list  <- list()
  annees <- 2025
  
  for(annee in annees){
    graph_file <- file.path("graphs", paste0("graph_", annee, ".rds"))
    if(file.exists(graph_file)) {
      g <- readRDS(graph_file)
      graphs_list[[as.character(annee)]] <- g
      verts_list[[as.character(annee)]] <- dodgr_vertices(g)
    } else {
      warning("Graph non trouvé pour l'année ", annee)
    }
  }
  
  
}




# FONCTION POUR FAIRE LES POLYGONES (en fait le vrai nom c'est isochrone askip) AUTOUR DES COMMERCES
isochrone_walk_fast <- function(point_sf, graph, verts, temps_minutes = 4, debug = TRUE) {
  
  #point_sf: point geometry du commerce
  # graph et verts, verticale et graph déja calculé pour 2025 pour eviter de le refaire tout le temps
  #temps_minutes: temps a pieds jusquau bord du polygone, faut mettre +1
  #debug: si TRUE affiche une petite carte avec le commerce en rouge et le polygone autour, pour verifier si ya des bugs
  
  print("go")
  
  
  # 1. Snap du point au graphe
  pt <- st_coordinates(point_sf)
  d <- (verts$x - pt[1])^2 + (verts$y - pt[2])^2
  start <- verts$id[which.min(d)]
  
  # 2. Calculer les distances depuis le vertex le plus proche
  dist <- dodgr_dists(graph, from = start)
  
  
  
  # 3. Filtrer vertices accessibles
  seuil <- temps_minutes * 60
  accessibles <- verts[!is.infinite(dist[1,]) & dist[1,] <= seuil, ]
  accessibles <- accessibles[!is.na(accessibles$x) & !is.na(accessibles$y), ]
  
  # 4. Vérifier qu'il y a assez de points
  if(nrow(accessibles) < 3) return(NA)
  
  # 5. Convertir en sf POINT
  acc_sf <- st_as_sf(accessibles, coords = c("x","y"), crs = st_crs(point_sf))
  
  # 6. Créer le polygone concave
  iso <- tryCatch({
    concaveman(acc_sf)
  }, error = function(e) NA)
  
  
  # 8. Debug visuel
  if(debug && !is.na(iso)) {
    cat("Nombre de vertices accessibles :", nrow(acc_sf), "\n")
    print(
      ggplot() +
        geom_sf(data = acc_sf, color="green", size=0.5, alpha=0.5) +
        geom_sf(data = point_sf, color="red", size=3) +
        geom_sf(data = iso, fill=adjustcolor("green", alpha.f=0.2), color="darkgreen") +
        ggtitle(paste("Isochrone à", temps_minutes, "min - année", annee))
    )
  }
  
  
  return(iso)
}
