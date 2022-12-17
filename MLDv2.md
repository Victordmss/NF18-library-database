<h1>MLD v2</h1>


**Membre** (#id_membre : int , prenom: varchar(), nom: varchar(), adresse: varchar, adresse_mail: varchar, login => compte_user), avec login key

- *Contrainte avancée: Projection(Membre,login) = Projection(Compte_user,login)*

**Adhérent** (#id_adherent: int, nom: varchar(), prenom: varchar(), adresse: varchar(), telephone: varchar(),: nombre_pret: int, blacklist: boolean, actif: boolean, login => compte_user), avec login KEY

- *Contrainte avancée: Projection(Adhérent,login) = Projection(Compte_user,login)*

**Compte_user** (#login: varchar(), mdp: varchar())


**Ressource** (#code : int, titre : varchar(), date_apparition : date, editeur : varchar(), code_classification : varchar(), prix : float)


<h3>Transformation de l’héritage avec Ressource: par référence</h3>

*Ressource est une classe mère abstraite, l’héritage est non complet et les classes filles sont impliquées dans des relations avec d’autres tables. L’héritage par les classe filles n’est donc pas vraiment pertinent ici. De même pour l’héritage par classe mère. De plus, à cause des associations sur les classes filles, l’héritage par la classe mère poserait problème. On choisit donc l’héritage par référence.*

- **Livre** (#code => Ressource.code, ISBN: varchar(), resume: varchar(), langue : varchar(), nb_pages int, auteur => Contributeur.id_contributeur), avec ISBN key, auteur NOT NULL

- **Film** (#code => Ressource.code, synopsis: varchar(), langue : varchar(), duree: integer, realisateur => Contributeur.id_contributeur), realisateur NOT NULL

- **Musique** (#code => Ressource.code, durée int, style varchar(), compositeur => Contributeur.id_contributeur), compositeur NOT NULL

*Contrainte avancée: Projection(Ressource,code) = Projection(Livre,code) UNION Projection(Film,code) UNION Projection(Musique,code)*

**Contributeur** (#id_contributeur : int, nom : varchar(), date : date, nationalite : Varchar())


**Film_acteur** (#id_contributeur => Contributeur.id_contributeur, #code_film => Film.code) 


**Musique_interprete** (#id_contributeur => Contributeur.id_contributeur, #code_musique => Musique.code)


**Exemplaire** (#numero : int, #code_ressource => Ressource.code, etat : {“neuf”|“bon”|“abime”|“perdu”} , disponible : boolean), avec disponible NOT NULL

*Contrainte avancée: Projection(Exemplaire.numero) = Projection(Ressource.numero)*


**Pret** (#id_pret : int, date_pret : date, duree_pret : integer, etat_pret: boolean, numero_ressource => Exemplaire.numero, code_ressource => Exemplaire.code_ressource), avec numero_ressource KEY et code_ressource KEY

- *Prêt est référençante dans l’association avec Exemplaire car elle porte la cardinalité 0..1*

**Emprunt** (#id_pret => Pret, #id_adherent => Adherent)

<h3>Transformation de l’héritage de Sanction: par classe mère</h3>

*L'héritage est presque complet (1 seul attribut dans chacune des classes Détérioration et Retard). L’héritage par la classe mère semble être le plus efficace ici.*

**Sanction** (#id_sanction : int, id_adherent => Adherent.id_adherent, etat_sanction : boolean, type_sanction : {retard|deterioration}, prix : float, duree_retard : int)

- *Contrainte avancée : (duree_retard NOT NULL AND type_sanction=retard) OR (prix NOT NULL AND type_sanction=deterioration)*
