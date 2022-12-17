<h1>Note de clarification projet Bibliothèque</h1>

<h2>Classes et attributs</h2>

**Ressource**: code (string) clé, titre (string), date_apparition (date), editeur (string), code_classification (string), prix (float), nombre_pret (int)

    - association d’héritage avec Livre, Film et Musique 

    - classe mère abstraite

**Contributeur:** nom (string), prenom (string), date_naissance (date), nationalité (string)

    - Peut écrire plusieurs Livres; relation 1 - *
    - Peut réaliser plusieurs Films; relation 1 - *
    - Peut jouer dans plusieurs Films; relation * - *
    - Peut composer plusieurs musiques; relation 1 - *
    - Peut interpréter plusieurs musiques; relation * - *


**Livre:** ISBN (string), résumé (string), langue (string), nb_pages (integer)

    - Hérite de Ressource
    - A un seul auteur

**Film:** synopsis (string), langue (string), durée  (int)
	
    - Hérite de Ressource
    - A un seul réalisateur (* - 1)
    - A plusieurs acteurs (* - *)

**Musique:** durée (integer), style (string)

    - Hérite de Ressource
    - A un seul compositeur (* - 1)
    - A un ou plusieurs interprètes (1..* - *)

**Exemplaire:** etat (Neuf | Bon | Abimé | Perdu), numéro (integer), disponible (boolean)

    - Composition avec Ressource. Une ressource peut être composée de 1 ou plusieurs exemplaires (1..*).

**Adhérent:** nom (string), prenom (string), adresse (string), adresse_mail (mail), num_tel (integer), nombre_pret (integer), blacklist (boolean), actif (boolean)

    - Possède un compte utilisateur; relation avec compte_user (1 - 1)

    - réalise de 0 à n_pret_max prêts (0..n - 0...n_pret_max)

**Membre:** nom (string), prenom (string), adresse (string), mail (string)

    - Possède un compte utilisateur; relation avec compte_user (1-1)

**Compte_user:** login (string) clé, mdp (string)

**Prêt:** date_prêt (date), durée (int)

    - Contient 1 exemplaire, relation avec Exemplaire (1 - 0..1)


**Sanction:** etat_sanction (boolean)

    - Association d'héritage avec Deterioration et Retard
    - Est possédée par un seul adhérent

**Retard:** duree_retard (string)

    - Hérite de sanction

**Deterioration:** prix (float)

    - Hérite de sanction

<h2>Contraintes</h2>

Durée d’un prêt compris entre 1 et nombre de jour de prêt maximum

Réaliser un prêt que si la ressource est disponible et en bon état (état = {neuf, bon})

Un adhérent effectue un nombre de prêt simultané limité : n_pret_max

Un adhérent est sanctionné si retard dans le retour ou dégradation d’un exemplaire

    Retard => suspension du droit de prêt = nb de jours de retard
    Perte/Déterioration grave => suspension du droit de prêt jusqu’au remboursement

<h2>Rôles des utilisateurs</h2>

Un membre du personnel de la bibliothèque peut accéder aux fonctions d’administration du système. Il gèrera les adhérents: création, blacklist, modification des données… Un membre peut aussi ajouter des documents, les modifier, ajouter des exemplaires etc…

Ce sont les membres du personnel qui géreront les prêts: vérification des retards, application des sanctions, gestion des réservations.

Les adhérents pourront rechercher des documents et consulter leurs emprunts (notamment les dates de prêt).

Les comptes utilisateurs seront générés informatiquement, les membres et adhérents ne seront pas à l’initiative de cela.

<h2>Notes pour la compréhension de la NDC et du MCD</h2>

L’attribut Prix (float) dans Ressource correspond au prix de base de la Ressource.

L’attribut Actif (boolean) dans Adhérent permet de savoir s’il s’agit d’un adhérent actuel ou s’il a été adhérent par le passé mais ne l’est plus.

On considère qu'un livre ne peut être écrit par un seul auteur, un film n'a qu'un seul réalisateur et une musique un seul compositeur. 

L'attribut Prix dans Deterioration correspond au prix à payer pour un adhérent qui déteriore une ressource.

