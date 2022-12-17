<h1> Notes pour la compréhension du document </h2>

Les requêtes sont parfois écrites de la forme : nom = requête. Bien que cette écriture ne soit pas valide au niveau sql, elle permet de mieux comprendre ce qui est récupéré par la requête puis ce qui est utilisé dans les requêtes suivantes. 

Les attributs de type : attribut_saisi sont des attributs entrés par l'utilisateur. 

<h2>Authentification : vérifier que mdp correspond au nom d'utilisateur</h2>

    - on possède login_saisi et mdp_saisi qui ont été entrés par l'utilisateur
    - On fait une jointure sur adhérent car on considère qu'on recherche le compte user d'un adhérent. On a juste à mettre membre si l'utilisateur a précisé qu'il était membre via le menu python

```sql
SELECT mdp, Compte_user.login FROM Compte_user 
INNER JOIN adherent ON Adherent.login = Compte_user.login 
WHERE login = login_saisi and mdp = mdp_saisi

--Exemple avec notre BDD
SELECT Compte_user.login, mdp FROM Compte_user 
INNER JOIN adherent ON Adherent.login = Compte_user.login 
WHERE Compte_user.login = 'thierryh' and mdp = 'vivEZesfA2';

--Renvoie le login 'thierryh' et le mdp 'vivEZesfA2' si le compte existe et qu'il appartient à un adhérent
```

<h2>Ajouter un document à la table</h2>

    - Demander le type de document
    - Puis, demander les bonnes infos selon le type et envoyer la requête avec les données entrées par l’utilisateur

**Peu importe le type de document que l'on créé, on créé une ressource**
```sql
INSERT INTO Ressource VALUES (DEFAULT,'titre_saisi','date_saisi','editeur_saisi','code_class_saisi','prix_saisi');

--Exemple avec notre BDD
INSERT INTO Ressource VALUES (DEFAULT,'titre_test','2022-11-15','editeur_test','code_class_test',20);
```
**Si on veut ajouter un film :**

Récupération de l'id du réalisateur à partir de son nom (on suppose qu'il n'y a pas d'homonymes) : 
```sql
id_realisateur = SELECT id_contributeur FROM Contributeur
WHERE Contributeur.nom = nom_realisateur_saisi; 

--Exemple avec notre BDD
SELECT id_contributeur FROM Contributeur
WHERE Contributeur.nom = 'George Lucas';
--Renvoie 9

--Si le réalisateur n'existe pas on le créé :
INSERT INTO Contributeur VALUES (DEFAULT, nom_saisi, date_naiss_saisi, nationalite_saisi);

--Exemple avec notre BDD
INSERT INTO Contributeur VALUES (DEFAULT, 'nom_test', '2022-11-15', 'nationalite_test');
```
Insertion: 
```sql
INSERT INTO film (code,synopsis,langue,duree,realisateur) VALUES (code_saisi, synopsis_saisi,langue_sasi,duree_saisi,id_realisateur);

--Exemple avec notre BDD
INSERT INTO film (code,synopsis,langue,duree,realisateur) VALUES (10, 'synopsis_test','langue_test',2,11);
```

**Pour les livres et les musiques, le fonctionnement est similaire: créer les ressources correspondantes avant**

**Si on veut ajouter un livre :**

Récupération de l'id de l'auteur à partir de son nom:
```sql 
id_auteur = SELECT id_contributeur FROM Contributeur
WHERE Contributeur.nom = nom_saisi;
```
Insertion : 
```sql
INSERT INTO livre (code,isbn,resume,langue,nb_pages,auteur) VALUES ('code_saisi', 'resume_saisi', 'langue_saisi', 'nb_pages_saisi', 'id_auteur');
```
**Si on veut ajouter une musique :**

Récupération de l'id du compositeur:
```sql
id_compositeur = SELECT id_contributeur FROM Contributeur
WHERE Contributeur.nom = nom_saisi;
```
Insertion : 
```sql
INSERT INTO musique (code,duree,style,compositeur) VALUES ('code_saisi', 'duree_saisi','style_saisi', 'id_compositeur');
```
<h2>Modifier la description d’un document</h2>

    - Demander le type de document
    - Demander le code de la ressource : code_saisi
    - Demander ce que la personne veut modifier : nouveau_resume

Exemple: nous cherchons à modifier le résumé d'un livre 
```sql
UPDATE Livre 
SET resume = nouveau_resume 
WHERE livre.code = code_saisi;

--Exemple avec notre BDD
UPDATE Livre 
SET resume = 'resume test pour le rendu4'
WHERE livre.code = 4;
```
Dans le cas où nous voulons modifier le titre par exemple, il faudra UPDATE la table ressource. A adapter selon les besoins !

<h2>Ajouter des exemplaires</h2>

    - Demander code ressource
    - Demander l’état
    - Chercher le dernier numéro d’exemplaire pour ce code_ressource avec le premier SELECT. On considère que dans l'application python nous stockerons ce max dans une variable max_num_exemplaire après avoir fouillé dans le fetchone.

On récupère d'abord le nombre d'exemplaire de la ressource en question
```sql
max_num_exemplaire = SELECT MAX(numero) FROM exemplaire 
WHERE code_ressource = code_ressource; 

--Exemple appliqué à notre BDD: 
SELECT MAX(numero) FROM exemplaire WHERE code_ressource = 4;
--Renvoie 2 --> Il y a 2 exemplaires de la ressource 4

INSERT INTO exemplaire (numero,code_ressource,etat,disponible) VALUES (max_num_exemplaire+1, code_ressource, etat, true);

--Exemple appliqué à notre BDD:
INSERT INTO exemplaire (numero,code_ressource,etat,disponible) VALUES (2+1, 4, 'bon', true); 
```

<h2>Recherche de documents</h2>
    - Recherche en fonction du type: livre, film ou musique → Le SELECT ne s’appliquera pas sur ressource mais sur livre, film ou musique dans ce cas

**Recherche avec titre**
```sql
SELECT code, titre, date_apparition, editeur, code_classification, prix FROM Ressource 
WHERE ressource.titre = titre_saisi;

--Exemple sur notre BDD
SELECT code, titre, date_apparition, editeur, code_classification, prix FROM Ressource 
WHERE ressource.titre = 'Candide';
```

**Recherche avec Auteur**
(on parle alors de livre)
```sql
SELECT R.titre, R.date_apparition FROM Ressource R
JOIN Livre L ON R.code = L.code
JOIN Contributeur C ON L.auteur = C.id_contributeur
WHERE C.nom = nom_auteur_saisi;

--Exemple avec notre BDD

SELECT R.titre, R.date_apparition FROM Ressource R
JOIN Livre L ON R.code = L.code
JOIN Contributeur C ON L.auteur = C.id_contributeur
WHERE C.nom = 'Voltaire';
```		
//_Qui sélectionne le titre et la date d’apparition des livres dont l’auteur est Voltaire_

**Recherche pour un acteur**
```sql
SELECT R.titre, R.date_apparition FROM Ressource R
JOIN Film F ON R.code = F.code 
JOIN Film_acteur FA ON F.code = FA.code_film 
JOIN Contributeur C ON FA.id_contributeur = C.id_contributeur
WHERE C.nom = nom_acteur_saisi;

--Exemple avec notre BDD
SELECT R.titre, R.date_apparition FROM Ressource R
JOIN Film F ON R.code = F.code 
JOIN Film_acteur FA ON F.code = FA.code_film 
JOIN Contributeur C ON FA.id_contributeur = C.id_contributeur
WHERE C.nom = 'Harrison Ford';
```
//_Qui sélectionne le titre et la date d’apparition des films dans lesquels l’acteur Harrison Ford a joué_

**Recherche pour un compositeur**
```sql
SELECT R.titre, R.date_apparition, M.duree, M.style FROM Ressource R
JOIN Musique M ON R.code = M.code
JOIN Contributeur C ON M.compositeur = C.id_contributeur
WHERE C.nom = nom_compositeur_saisi;

--Exemple avec notre BDD
SELECT R.titre, R.date_apparition, M.duree, M.style FROM Ressource R
JOIN Musique M ON R.code = M.code
JOIN Contributeur C ON M.compositeur = C.id_contributeur
WHERE C.nom = 'Johnny Hallyday';
```
//_Qui sélectionne le titre, la date d’apparition, la durée et le style des musiques dont le compositeur est Johnny Hallyday_

**Recherche avec style d’une musique**
```sql
SELECT R.titre, R.date_apparition, M.duree FROM Ressource R
JOIN Musique M ON R.code = M.code
WHERE M.style = style_musique_saisi;

--Exemple avec notre BDD
SELECT R.titre, R.date_apparition, M.duree FROM Ressource R
JOIN Musique M ON R.code = M.code
WHERE M.style = 'rock';
```
//_Qui sélectionne le titre, la date d’apparition et la durée de toutes les musiques dont le style est rock._

<h2>Gestion des emprunts</h2>

    - Lors d’un prêt vérifier si l’adhérent possède des sanctions actives, on considere qu’on a l’id de l'adhérent dans la variable id
```sql
sanction = SELECT etat_sanction FROM sanction 
WHERE id_adherent = id and etat_sanction = true;

--Exemple avec notre BDD
SELECT etat_sanction FROM sanction 
WHERE id_adherent = 2 and etat_sanction = true;
--Renvoie quelque chose, ce qui signifie qu'il possède au moins une sanction active

--Si sanction existe (sanction != null), alors l'emprunt n'est pas possible
```
Ce qui donne en python : 
```python
sql = f"SELECT etat_sanction FROM sanction WHERE id_adherent = {id} and etat_sanction = true"
    cur.execute(sql)
    res = cur.fetchone()[0]
    if res != None:
        print("Emprunt impossible : il y a une sanction en cours")
        exit()

```
    - Vérifier que le nombre de prêt en cours < nb_pret_max = 4
On considère qu'on a défini la variable nb_pret_max représentant le nombre de prêt max par adhérent avant.
```sql
nb_pret = SELECT nombre_pret FROM adherent WHERE id_adherent = id;

--Exemple avec notre BDD
SELECT nombre_pret FROM adherent WHERE id_adherent = 4;

--Si nb_pret >= nb_pret_max alors le prêt est interdit
```

Ce qui donne en python : 
```python
sql = f"SELECT nombre_pret FROM adherent WHERE id_adherent = {id}"
cur.execute(sql)
nb_pret_encours = int(cur.fetchone()[0])
if nb_pret_encours >= nb_pret_max:
    print("Emprunt impossible : vous avez atteint le nb maximal d’emprunt en simultané")
    exit()
```

    - Vérifier la disponiblité de la ressource demandée
on considere que le numero de l’exemplaire est écrit sur la ressource, on le demande donc à l’utilisateur (variable numero_saisi)
On demande code_classification stocké dans la variable code_saisi, lui aussi écrit sur le livre pour récupérer son code ressource dans la base de données
```python
sql = f"SELECT code FROM ressource WHERE code_classification = {code_saisi}"
cur.execute(sql)
code_ressource = int(cur.fetchone()[0])
sql = f"SELECT etat_pret from pret WHERE code_ressource = {code_ressource} AND numero_ressource = {numero}"
cur.execute(sql)
if cur.fetchone()[0] == 'true':
    print("Emprunt impossible : la ressource est déjà empruntée par qqun d’autre")
    exit()

```
**Après succès du pret, on met à jour les tables:**

    - Insertion du pret dans la table Pret
    - Insertion du pret dans la table Emprunt après Récupération
        de l'id_adherent et id_pret
    - Mise à jour de la table exemplaire (attribut disponible mis à false)
    - Mise à jour de la table adherent (incrémenter son nombre de prêt en cours)

```sql
--Insertion dans la table Pret
INSERT INTO pret VALUES (DEFAULT, CURRENT_DATE, {duree}, {numero}, {code}, true)

--Insertion dans la table Emprunt
    -- Récupération de idpret
    idpret = SELECT id_pret FROM pret 
    WHERE date_pret = CURRENT_DATE AND duree_pret = {duree} AND numero_ressource = {numero} AND code_ressource = {code} AND etat_pret = true

    -- Récupération de idadherent
    idadherent = SELECT id_adherent FROM Adherent 
    WHERE login = login_saisi;

INSERT INTO emprunt VALUES ({idpret}, {idadherent})

--MAJ de la table exemplaire
UPDATE exemplaire SET (disponible = false) WHERE numero = {numero} AND code_ressource = {code}

--MAJ de la table adherent
UPDATE adherent SET (nombre_pret = nombre_pret + 1) WHERE id_adherent = idadherent
```
<h2>Gestion des prêts, des retards, et des réservations</h2>

**Récupérer tous les prêts d’un adhérent**
```sql
adherent = SELECT id_adherent FROM Adherent 
WHERE login = login_saisi;

SELECT id_prêt FROM Emprunt WHERE Emprunt.id_adherent = adherent;
```
**Connaitre le nombre de prêt d'un adherent qu'ils soient en cours ou terminés (TOUS)**
```sql
SELECT COUNT(*) AS nb_prets_total FROM Emprunt 
WHERE Emprunt.id_adherent = id_adherent 
GROUP BY Emprunt.id_adherent;
```

**Ajout d'une sanction retard**

    - Vérification du retard : on considère que code_ressource et numéro ressource sont écrit sur le livre qui est en train d'être rendu

```sql
dates = SELECT date_prêt, durée FROM Pret 
INNER JOIN Emprunt ON Pret.id_pret = Emprunt.id_pret 
WHERE Pret.code_ressource = code_ressource and Pret.numero_ressource and Emprunt.id_adherent = adherent;

-- date_retour_prevu = date_pret + durée

-- Si date_retour_prevu < date_ajourdhui alors on crée une SANCTION
INSERT INTO Sanction (id_adherent, etat_sanction, duree_retard) VALUES (adherent, true, date_ajourdhui - date_retour_prevu)
```

**Ajout d'une sanction détérioration**

    - Vérification de l'état
    - Récupérer le prix d'une ressource
    - Ajouter la sanction détérioration

```sql
-- Si etat_retour dans (abime, perdu) alors on crée une SANCTION

--On cherche le prix de la ressource abimée
Prix_ressource = SELECT prix FROM Ressource 
WHERE Ressource.code = code_ressource_saisi;

--Ajout de la sanction
INSERT INTO Sanction (id_adherent, etat_sanction, prix) VALUES (adherent, true, prix_ressource);
```

**Retours**

    - Lors d'un retour, on met à jour la table adherent (décrémentation de l'attribut nombre_pret)
    - Mise à jour de la table exemplaire (mettre disponible à true)
    - Mise à jour de la table Pret (mettre etat_pret à false)
```sql
--Pour la table Adherent:
    --Récupération de idadherent
    SELECT id_adherent FROM Adherent 
    WHERE login = login_saisi;

UPDATE adherent SET (nombre_pret = nombre_pret - 1) WHERE id_adherent = idadherent;

--Pour la table exemplaire
UPDATE exemplaire SET (disponible = true) WHERE numero = {numero} AND code_ressource = {code};

--Récupération de idpret pour la table Pret
idpret = SELECT id_pret FROM pret WHERE numero_ressource = {numero} AND code_ressource = {code} AND etat_pret = true;

-- Pour la table Pret
UPDATE pret SET (etat_pret = false) WHERE id_pret = {idpret};

```

<h2>Gestion des utilisateurs et leurs données</h2>

**Compter toutes les sanctions actives et inactives d’un adhérent et mettre à jour blacklist si trop important**

    - A partir de login_saisi récupérer id_adherent
    - Compter le nombre de sanctions pour id_adherent

```sql
id_adherent = SELECT id_adherent FROM Adherent 
WHERE login = id_adherent;

Nb_sanction = SELECT COUNT(*) FROM Sanction 
WHERE sanction.id_adherent = id_adherent 
GROUP BY id_adherent;

-- Nb_Sanctions_Max = 5

-- Si nb_sanction >= Nb_Sanctions_Max alors on met à jour blacklist:
UPDATE Adherent 
SET blacklist = True 
WHERE Adherent.id_adherent = id_adherent;
```

**Lors du remboursement d’une sanction détérioration, si montant donné= montant désiré alors mettre la sanction à inactif**

    - montant_donné par adhérent
    - récuperer id_adherent à partir du login

```sql
montant_desire = SELECT prix, id_sanction FROM Sanction 
WHERE sanction.id_adherent = id_adherent and sanction.etat_sanction = true and type_sanction = détérioration;

--Si le montant_donné est équivalent au montant_desire (montant_desire[0])
UPDATE Sanction 
SET etat_sanction = FALSE 
WHERE sanction.id_sanction = montant_desire[1];
```

<h2> Statistiques </h2>

**Faire un classement des emprunts pour trouver les ressources les plus empruntées**
```sql
SELECT pret.code_ressource, R.titre,COUNT(pret.code_ressource) AS nb_total_pret FROM pret 
JOIN Ressource R ON pret.code_ressource = R.code
GROUP BY pret.code_ressource, R.titre
ORDER BY nb_total_pret DESC;
```

**Ressource en cours d'emprunt par un adhérent**
```sql
SELECT Ressource.titre FROM Emprunt
INNER JOIN Pret on Emprunt.id_pret = Pret.id_pret
INNER JOIN Ressource on Ressource.code = Pret.code_ressource
WHERE Pret.etat_pret = true and Emprunt.id_adherent = (SELECT id_adherent FROM Adherent WHERE login = 'jrouet');
```


<h2> MENU PYTHON </h2>

**MENU GLOBAL :** 

membre ou adhérent

authentification/connection bdd

**MENU MEMBRE :**

Ajouter une ressource

Accéder à une ressource (possibilité de la modifier)

Ajouter un exemplaire

Rechercher un exemplaire (possibilité de le modifier)

Créer un emprunt

Retour d’un emprunt

Rechercher un adhérent (possibilité de le modifier, statistiques)

Statistiques 


**MENU ADHÉRENT :**

Rechercher une ressource (+voir ses exemplaires)

Visualiser son profil (emprunt, statistiques…)





