from area import Area
map = {
"PLA01" : Area("place de l'Ephec",
             "PLA01",
             ["Parking", "HAL01"],
              ["personnage1"],
             ["objects"],
             "La place de l'Ephec,devant le bâtiment",
             "Y a pleins d'élèves la"),

"HAL01" : Area("Hall d'entrée",
             "HAL01",
             ["PLA01", "Ancienne aile RDC", "Nouvelle aile RDC"],
             ["personnage1"],
             ["objects"],
             "Le hall d'entrée de l'Ephec",
             "Gildas attend le secrétariat"),

"AIL01" : Area("Ancienne aile du rez de chaussée",
             "AIL01",
             ["Toilettes" , "Cafétéria" , "Escalier principal" , "HAL01", "Zone distributeur" , "Locaux RDC" , "Learning Lab"],
             ["personnage1"],
             ["objects"],
             "L'endroit ou on cours les enculés de market",
             "Local on est 40 dedans"),

"AIL02" : Area("Nouvelle aile du rez de chaussée",
             "AIL01",
             ["LA01", "LA02", "Logette bois", "Escalier secondaire", "Secrétariat", "HAL01"],
             ["personnage1"],
             ["objects"],
             "Nouvelle aile",
             "ça pue y PA"),

"LOC01" : Area("Les locaux du rez de chaussée",
             "LOC01",
             ["LR01", "LR02", "LR03", "LR04", "LR05", "AIL01"],
             ["personnage1"],
             ["objects"],
             "Les locaux de l'ancienne aile",
             "ça pue y PA"),

}