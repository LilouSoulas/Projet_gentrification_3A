library(sf)
library(osmextract)
library(dplyr)
library(ggplot2)
library(tidyr)
library(osrm)
library(dodgr)
library(concaveman)
library(purrr)



#Importation de la fonction isochrone_walk_fast_final qui determine les polygones
source("fonction_polygone_base.R")


# Importation de la base de données netooyée de lucien
data_clean <- read.csv("data/final_dtb_nettoye.csv")

# On repare la colonne geometry
data_clean$geometry <- st_as_sfc(data_clean$geometry, crs = 4326)  # WGS84

#Base de données 2025:
data_2025 <- data_clean[data_clean$annee == 2025, ]


#--------------------------------------------------------------------------
#Polygones pour 5min
graphe_2025 <- graphs_list[["2025"]]
verts_2025 <- verts_list[["2025"]]
data_2025 <- data_2025 %>%
  mutate(
    poly_5 = map(
      geometry,
      ~ sf::st_geometry(isochrone_walk_fast(.x, graphe_2025, verts_2025, 6, FALSE))[[1]]
    )
  )

data_2025$poly_5 <- st_sfc(data_2025$poly_5, crs = st_crs(data_2025))
#--------------------------------------------------------------------------


#--------------------------------------------------------------------------
#Polygones pour 3min
graphe_2025 <- graphs_list[["2025"]]
verts_2025 <- verts_list[["2025"]]
data_2025 <- data_2025 %>%
  mutate(
    poly_3 = map(
      geometry,
      ~ sf::st_geometry(isochrone_walk_fast(.x, graphe_2025, verts_2025, 4, FALSE))[[1]]
    )
  )

data_2025$poly_3 <- st_sfc(data_2025$poly_3, crs = st_crs(data_2025))
#--------------------------------------------------------------------------