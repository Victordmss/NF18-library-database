DROP TABLE IF EXISTS Emprunt ;
DROP TABLE IF EXISTS Sanction ;
DROP TABLE IF EXISTS Pret ;
DROP TABLE IF EXISTS Exemplaire ;
DROP TABLE IF EXISTS Musique_interprete ;
DROP TABLE IF EXISTS Film_acteur ;
DROP TABLE IF EXISTS Musique ;
DROP TABLE IF EXISTS Film ;
DROP TABLE IF EXISTS Livre ;
DROP TABLE IF EXISTS Contributeur ;
DROP TABLE IF EXISTS Ressource ;
DROP TABLE IF EXISTS Adherent ;
DROP TABLE IF EXISTS Membre ;
DROP TABLE IF EXISTS Compte_user ;

CREATE TABLE Compte_user(
  login varchar,
  mdp varchar,
  PRIMARY KEY (login)
);

CREATE TABLE Membre(
  id_membre SERIAL,
  prenom varchar,
  nom varchar,
  adresse varchar,
  adresse_mail varchar,
  login varchar UNIQUE NOT NULL,
  PRIMARY KEY (id_membre),
  FOREIGN KEY (login) REFERENCES Compte_user
);

CREATE TABLE Adherent(
  id_adherent SERIAL,
  nom varchar,
  prenom varchar,
  adresse varchar,
  telephone varchar,
  nombre_pret integer,
  blacklist boolean,
  actif boolean,
  login varchar UNIQUE NOT NULL,
  PRIMARY KEY (id_adherent),
  FOREIGN KEY (login) REFERENCES Compte_user
);

CREATE TABLE Ressource(
  code SERIAL,
  titre varchar,
  date_apparition date,
  editeur varchar,
  code_classification varchar,
  prix float,
  PRIMARY KEY (code)
);

CREATE TABLE Contributeur(
  id_contributeur SERIAL,
  nom varchar,
  date_naiss date,
  nationalite varchar,
  PRIMARY KEY (id_contributeur)
);

CREATE TABLE Livre(
  code integer,
  ISBN Varchar UNIQUE NOT NULL,
  resume Varchar,
  langue varchar,
  nb_pages integer,
  auteur integer NOT NULL,
  PRIMARY KEY (code),
  FOREIGN KEY (code) REFERENCES Ressource,
  FOREIGN KEY (auteur) REFERENCES Contributeur
);

CREATE TABLE Film(
  code integer,
  synopsis varchar,
  langue varchar,
  duree integer,
  realisateur integer NOT NULL,
  PRIMARY KEY (code),
  FOREIGN KEY (code) REFERENCES Ressource,
  FOREIGN KEY (realisateur) REFERENCES Contributeur
);

CREATE TABLE Musique(
  code integer,
  duree integer,
  style varchar,
  compositeur int NOT NULL,
  PRIMARY KEY (code),
  FOREIGN KEY (code) REFERENCES Ressource,
  FOREIGN KEY (compositeur) REFERENCES Contributeur
);

CREATE TABLE Film_acteur(
  id_contributeur integer,
  code_film integer,
  PRIMARY KEY (id_contributeur, code_film),
  FOREIGN KEY (id_contributeur) REFERENCES Contributeur,
  FOREIGN KEY (code_film) REFERENCES Film
);

CREATE TABLE Musique_interprete(
  id_contributeur integer,
  code_musique integer,
  PRIMARY KEY (id_contributeur, code_musique),
  FOREIGN KEY (id_contributeur) REFERENCES Contributeur,
  FOREIGN KEY (code_musique) REFERENCES Musique
);

CREATE TABLE Exemplaire(
  numero integer,
  code_ressource integer,
  etat varchar CHECK(etat IN ('neuf', 'bon', 'abime', 'perdu')),
  disponible boolean NOT NULL,
  PRIMARY KEY (numero, code_ressource),
  FOREIGN KEY (code_ressource) REFERENCES Ressource
);

CREATE TABLE Pret (
  id_pret SERIAL,
  date_pret date,
  duree_pret integer,
  numero_ressource integer NOT NULL,
  code_ressource integer NOT NULL,
  etat_pret boolean NOT NULL,
  PRIMARY KEY (id_pret),
  FOREIGN KEY (numero_ressource, code_ressource) REFERENCES Exemplaire
);

CREATE TABLE Sanction(
  id_sanction SERIAL,
  id_adherent integer,
  etat_sanction boolean,
  type_sanction varchar CHECK(type_sanction IN ('retard', 'deterioration')),
  prix float,
  duree_retard int,
  PRIMARY KEY (id_sanction, id_adherent),
  FOREIGN KEY (id_adherent) REFERENCES Adherent,
  CHECK(((duree_retard IS NOT NULL) AND (type_sanction = 'retard')) OR ((prix IS NOT NULL) AND (type_sanction='deterioration')))
);

CREATE TABLE Emprunt(
  id_pret integer,
  id_adherent integer,
  PRIMARY KEY (id_pret, id_adherent),
  FOREIGN KEY (id_pret) REFERENCES Pret,
  FOREIGN KEY (id_adherent) REFERENCES Adherent
);
