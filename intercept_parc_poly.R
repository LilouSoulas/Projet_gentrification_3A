library(sf)
library(osmextract)
library(dplyr)
library(ggplot2)
library(tidyr)
library(osrm)
library(dodgr)
library(concaveman)
#il manque peut etre des packages, ca fait deux jours que je suis sur R je ne sais plus ce que j'ai chargé oupsi

#INTERCEPT DES JARDINS ET DES POYGONES DES COMMERCES

#POUR MAELIE:
#Nécessite que le df de nos commerces s'apelle data_clean et que les colonnes des polygones soient poly_3 et poly_5 (tu peux changer dans mon code)
data_clean <- readRDS("data_clean_polygones.rds")


#Base des parcs
data_parc <- st_read("data_parc.gpkg")

#Vérifier que c'est bien sf les deux (si TRUE c'est okkkkk)
same_crs <- st_crs(data_clean) == st_crs(data_parc)
same_crs

#Juste pour voir combien on a de polygones invalides à reparer
sum(!st_is_valid(data_parc))         # combien de parcs invalides (normalement 7)
sum(!st_is_valid(data_clean$poly_5)) # combien de poly_5 invalides
sum(!st_is_valid(data_clean$poly_5)) # combien de poly_3 invalides

#Réparation des polygones
data_parc <- st_make_valid(data_parc)
data_clean$poly_3 <- st_make_valid(data_clean$poly_3)
data_clean$poly_5 <- st_make_valid(data_clean$poly_5)

#Nouvelles colonnes indicatrices
data_clean <- data_clean %>%
  rowwise() %>%
  mutate(
    parc_3 = ifelse(any(st_intersects(poly_3, data_parc, sparse = FALSE)), 1, 0),
    parc_5 = ifelse(any(st_intersects(poly_5, data_parc, sparse = FALSE)), 1, 0)
  ) %>%
  ungroup()
