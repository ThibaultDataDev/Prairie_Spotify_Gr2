# SUPPRESSION DE LA BDD POUR EXECUTION A LA CHAINE
import os, sys
path = os.path.dirname(sys.argv[0])
# print("Le répertoire courant est : " + path)
os.remove(path + "/bddSpotify.db")

# CREATION DE LA BDD
import sqlite3
bdd = sqlite3.connect(path + "/bddSpotify.db")
cur = bdd.cursor()

# CREATION TABLES
cur.execute('CREATE TABLE artiste (id_artiste INTEGER PRIMARY KEY, nom_artiste TEXT);')
cur.execute('CREATE TABLE titre (id_titre INTEGER PRIMARY KEY, nom_titre TEXT, durée REAL, bpm REAL, energie REAL, intensité REAL);')
cur.execute('CREATE TABLE playlist (id_playlist INTEGER PRIMARY KEY, nom_playlist TEXT);')
cur.execute('CREATE TABLE artiste_titre (titre_id INTEGER, artiste_id INTEGER, FOREIGN KEY (titre_id) REFERENCES titre(id_titre), FOREIGN KEY (artiste_id) REFERENCES artiste(id_artiste), PRIMARY KEY (titre_id, artiste_id));')
cur.execute('CREATE TABLE playlist_titre (playlist_id INTEGER, titre_id INTEGER, FOREIGN KEY (playlist_id) REFERENCES paylist(id_playlist), FOREIGN KEY (titre_id) REFERENCES titre(id_titre), PRIMARY KEY (playlist_id, titre_id));')

# AJOUT DE DONNEES
cur.execute('INSERT INTO artiste VALUES (1,"Claude Francois"),(2,"Madonna"),(3,"Lorie");')
cur.execute('INSERT INTO titre VALUES (1,"Cette année là",3.49,9.32,3.54,5.65),(2,"Like a virgin",3.32,4.34,6.33,8.76),(3,"Frozen",4.88,6.54,5.44,5.65);')
cur.execute('INSERT INTO artiste_titre VALUES (1,1),(2,2),(3,2);')

# REQUETE
# Temps moyen des morceaux :
cur.execute('SELECT AVG(durée) FROM titre;')
view = cur.fetchall()
for i in view :
    print ("Le temps moyen des morceaux est de " +str(i))
# Nombre de titres par artiste :
cur.execute('SELECT nom_artiste, COUNT(titre_id) FROM artiste INNER JOIN artiste_titre WHERE artiste.id_artiste = artiste_titre.artiste_id GROUP BY nom_artiste')
view = cur.fetchall()
for i in view :
    print (i)

# # AFFICHAGE RESULTAT
# view = cur.fetchall()
# for i in view :
#     print (i)

# FERMETURE BDD
bdd.close()
