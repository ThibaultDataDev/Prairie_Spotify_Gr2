####################### CREATION DE LA BDD ET AJOUT DES DATAS #########################

## IMPORT DES LIBRAIRIES
import os, sys, sqlite3

## SUPPRESSION DE LA BDD EXISTANTE
path = os.path.dirname(sys.argv[0])
bdd = sqlite3.connect(path + "/bddSpotify.db")
bdd.close()
os.remove(path + "/bddSpotify.db")

## CREATION DE LA BDD
bdd = sqlite3.connect(path + "/bddSpotify.db")
cur = bdd.cursor()

## CREATION TABLES
cur.execute('CREATE TABLE artiste (id_artiste INTEGER PRIMARY KEY, nom_artiste TEXT);')
cur.execute('CREATE TABLE titre (id_titre INTEGER PRIMARY KEY, nom_titre TEXT, durée REAL, bpm REAL, energie REAL, intensité REAL);')
cur.execute('CREATE TABLE playlist (id_playlist INTEGER PRIMARY KEY, nom_playlist TEXT);')
cur.execute('CREATE TABLE artiste_titre (titre_id INTEGER, artiste_id INTEGER, FOREIGN KEY (titre_id) REFERENCES titre(id_titre), FOREIGN KEY (artiste_id) REFERENCES artiste(id_artiste), PRIMARY KEY (titre_id, artiste_id));')
cur.execute('CREATE TABLE playlist_titre (playlist_id INTEGER, titre_id INTEGER, FOREIGN KEY (playlist_id) REFERENCES paylist(id_playlist), FOREIGN KEY (titre_id) REFERENCES titre(id_titre), PRIMARY KEY (playlist_id, titre_id));')
print("Création des tables effectuée.")

## AJOUT DE DONNEES
cur.execute('INSERT INTO artiste VALUES (1,"Claude Francois"),(2,"Madonna"),(3,"Lorie");')
cur.execute('INSERT INTO titre VALUES (1,"Cette année là",3.49,202,3.54,5.65),(2,"Like a virgin",3.32,120,6.33,8.76),(3,"Frozen",4.88,72,5.44,5.65);')
cur.execute('INSERT INTO artiste_titre VALUES (1,1),(2,2),(3,2);')
cur.execute('INSERT INTO playlist VALUES (1,"Planete Rap 1964"),(2,"Chansons Paillardes d''ici et d''ailleurs"),(3,"Love Night"),(4,"L''intégrale de JUL en Fa Mineur");')
cur.execute('INSERT INTO playlist_titre VALUES (2,2),(3,1),(3,2),(4,1),(4,2),(4,3);')
print("Ajout des datas OK.")

## SAUVEGARDE DE LA BDD
bdd.commit()
print("BDD sauvegardée.")

## FERMETURE BDD
bdd.close()
