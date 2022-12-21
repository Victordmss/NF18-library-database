INSERT INTO compte_user VALUES ('mbellamy','couCoU1234');
INSERT INTO compte_user VALUES ('thierryh','vivEZesfA2');
INSERT INTO compte_user VALUES ('isabellebel','bbBAdf*');
INSERT INTO compte_user VALUES ('ales','shtougdsasmA');
INSERT INTO compte_user VALUES ('albertbe','ABbHnEé');
INSERT INTO compte_user VALUES('vdemessa','pixou60');
INSERT INTO compte_user VALUES('slebreto','pirate!');
INSERT INTO compte_user VALUES('mmouchet','testblack');
INSERT INTO compte_user VALUES('ielyahya','ninirugby');
INSERT INTO compte_user VALUES('cbauvais', 'CjH5fT');
INSERT INTO compte_user VALUES('jrouet', 'GAdt5i');
INSERT INTO compte_user VALUES('dmeto', 'JoP5za');
INSERT INTO compte_user VALUES ( 'aamarger', 'azerty123');
INSERT INTO compte_user VALUES('adupont', 'HuY6f7');

ALTER SEQUENCE adherent_id_adherent_seq RESTART WITH 1 ;
INSERT INTO adherent VALUES(DEFAULT, 'bauvais', 'camille', 'rue notre dame de bon secours', '0789916609', 0, False, True, 'cbauvais');
INSERT INTO adherent VALUES(DEFAULT, 'dupont', 'arthur', 'avenue de la republique', '0645322787', 0, False, True, 'adupont');
INSERT INTO adherent VALUES(DEFAULT, 'bellamy', 'mathis', 'rue de la poste', '0647342721', 0, False, True, 'mbellamy');
INSERT INTO adherent VALUES(DEFAULT, 'rouet', 'justine', 'rue du poussin', '0625332684', 2, False, True, 'jrouet');
INSERT INTO adherent VALUES(DEFAULT, 'meto', 'daphne', 'rue des cerises', '0725239685', 0, False, True, 'dmeto');
INSERT INTO adherent VALUES(DEFAULT, 'bella', 'isabelle', 'rue du temps', '0625666784', 0, False, True, 'isabellebel');
INSERT INTO adherent VALUES(DEFAULT, 'hermes', 'thierry', 'rue de la libération', '0622232684', 0, False, True, 'thierryh');
INSERT INTO adherent VALUES(DEFAULT, 'les', 'alexandre', 'rue du petit mouton', '0625535584', 1, False, True, 'ales');
INSERT INTO adherent VALUES(DEFAULT, 'betz', 'albert', 'rue de michel', '0695392684', 1, False, True, 'albertbe');
INSERT INTO adherent VALUES(DEFAULT, 'demessance', 'victor', 'rue de la cour', '0685392981', 0, False, False, 'vdemessa');
INSERT INTO adherent VALUES(DEFAULT, 'lebreton', 'sylvie', 'rue de paris', '0694337884', 0, False, True, 'slebreto');
INSERT INTO adherent VALUES(DEFAULT, 'mouchet', 'mathilde', 'avenue rostand', '0695412624', 0, True, True, 'mmouchet');

ALTER SEQUENCE membre_id_membre_seq RESTART WITH 1 ;
INSERT INTO membre VALUES (DEFAULT, 'iel', 'yahya', '2 rue de la paix, paris', 'ielyahya@gmail.com', 'ielyahya');
INSERT INTO membre VALUES (DEFAULT, 'axel', 'amarger', 'rue de la rue', 'axel.amarger@gmail.com', 'aamarger');

ALTER SEQUENCE ressource_code_seq RESTART WITH 1 ;
INSERT INTO ressource VALUES (DEFAULT, 'Star Wars IV',  '1977-05-22',  'lucasfilm',  '241LUC',  19.99);
INSERT INTO ressource VALUES (DEFAULT, 'Star Wars V',  '1980-10-02',  'lucasfilm',  '242LUC',  19.99);
INSERT INTO ressource VALUES (DEFAULT, 'Star Wars VI', '1983-04-23',  'lucasfilm',  '243LUC', 19.99);
INSERT INTO ressource VALUES (DEFAULT, 'Candide', '1959-01-20', 'magnard', '211VOL', 2.95);
INSERT INTO ressource VALUES (DEFAULT, 'Le rouge et le Noir', '1830-08-30', 'hatier', '221STE', 6.99);
INSERT INTO ressource VALUES (DEFAULT, 'Tintin au pays des Soviets', '1987-11-16', 'Herge', '311HER', 5);
INSERT INTO ressource VALUES (DEFAULT, 'La marseillaise', '1789-07-14', 'NULL', '111MAR', 2.99);
INSERT INTO ressource VALUES (DEFAULT, 'Allumez le feu', '1998-01-16', 'Universal', '121HAL', 5);
INSERT INTO ressource VALUES (DEFAULT, 'Debout', '1998-01-16', 'Universal', '122HAL', 5);

ALTER SEQUENCE contributeur_id_contributeur_seq RESTART WITH 1 ;
INSERT INTO contributeur VALUES (DEFAULT, 'Brad Pitt', '1963-12-18', 'americain');
INSERT INTO contributeur VALUES (DEFAULT, 'Mark Hamill', '1951-09-25', 'americain');
INSERT INTO contributeur VALUES (DEFAULT, 'Harrison Ford', '1694-11-21', 'americain');
INSERT INTO contributeur VALUES (DEFAULT, 'Voltaire', '1972-08-18', 'francais');
INSERT INTO contributeur VALUES (DEFAULT, 'Kalouchkov', '1963-12-18', 'russe');
INSERT INTO contributeur VALUES (DEFAULT, 'Johnny Hallyday', '1943-06-15', 'francais');
INSERT INTO contributeur VALUES (DEFAULT, 'Herge', '1907-05-22', 'belge');
INSERT INTO contributeur VALUES (DEFAULT, 'Rouget de Lisle', '1760-05-10', 'francais');
INSERT INTO contributeur VALUES (DEFAULT, 'George Lucas', '1944-05-14', 'francais');
INSERT INTO contributeur VALUES (DEFAULT, 'Henri Beyle', '1753-05-14', 'francais');

INSERT INTO livre (code,isbn,resume,langue,nb_pages,auteur) VALUES (4,  '978-2-01-169169-9',  'Candide est un jeune homme naïf qui vit dans le château du baron de Thunder-Ten-Tronckh. Il est chassé de ce petit bout de paradis parce qu’il est surpris avec Cunégonde, la fille du baron, dont il est amoureux. Il quitte alors sa bien-aimée et Pangloss, le précepteur de la maison qui a enseigné à Candide que tout est au mieux dans le meilleur des mondes.',  'francais',  '192',  4);
INSERT INTO livre (code,isbn,resume,langue,nb_pages,auteur) VALUES (5,  '978-3-11-125672-9',  'Julien Sorel est le troisième fils du vieux Sorel, scieur, qui n’a que mépris pour les choses intellectuelles et donc pour Julien, qui se révèle très tôt doué pour les études. Au contraire de ses frères, le garçon n’est pas taillé pour les travaux de force, et sa curiosité le pousse à s’instruire par tous les moyens possibles.',  'francais',  '556',  10);
INSERT INTO livre (code,isbn,resume,langue,nb_pages,auteur) VALUES (6,  '178-2-01-169169-9',  'Au temps de l’URSS de Staline, le reporter Tintin et son fox-terrier Milou sont envoyés à Moscou par Le Petit Vingtième afin d’y effectuer un reportage. Informés de son départ et des raisons de sa venue, les Soviétiques dépêchent un agent secret afin de le tuer, et font exploser son train, alors en Allemagne.',  'francais',  '36',  7);

INSERT INTO musique VALUES(7, 210, 'hymne', 8);
INSERT INTO musique VALUES(8, 225, 'rock', 6);
INSERT INTO musique VALUES(9, 250, 'rock', 6);

INSERT INTO film (code,synopsis,langue,duree,realisateur) VALUES ( 1,
'Dix-neuf années se sont écoulées depuis La Revanche des Sith. Mais l’Empire Galactique dirigé par Palpatine et son homme de main Dark Vador doit aujourd’hui faire face aux Rebelles. L’une d’entre elles, la Princesse Leia, est capturée et missionne deux droïdes de retrouver un vieil ermite. Sur leurs routes, ils font la connaissance d’un ouvrier agricole, un certain Luke Skywalker, qui se révèle être un puissant détenteur de la Force Jedi. Rejoints par un duo de contrebandiers, ils vont tenter de libérer la Princesse et de détruire l’arme ultime de l’Empire : l’Étoile noire.',
 'anglais',  132,  9);
INSERT INTO film (code,synopsis,langue,duree,realisateur) VALUES ( 2,
'Malgré la destruction de l’Étoile noire dans Un nouvel espoir, l’Empire galactique est toujours aussi puissant et continue à persécuter les rebelles. Ceux-ci ont élu domicile sur la planète des glaces, Hoth. Le jeune Luke Skywalker s’en va quant à lui trouver un nouveau maître Jedi afin de maîtriser la Force. De leur côté, Han Solo et Leia s’en vont trouver de l’aider dans une étrange cité perchée dans les nuages et retrouvent une vieille connaissance de Han.',
 'anglais',  129,  9);
INSERT INTO film (code,synopsis,langue,duree,realisateur) VALUES ( 3,
'Sur Tatooine, les rebelles tentent de libérer Han Solo, qui s’est fait cryogéniser et a échoué entre les mains du criminel Jabba Le Hutt. Après une rude bataille, Luke Skywalker part faire ses adieux à son maître Yoda, tandis que toute l’équipe de héros se retrouve sur la planète Endor, afin de tenter de faire exploser la nouvelle Étoile de la mort. Luke s’en va finalement combattre l’Empereur et tente de rallier à sa cause Dark Vador, qui n’est autre que son propre père.',
 'anglais',  133,  9);

INSERT INTO Film_acteur VALUES(2,1);
INSERT INTO Film_acteur VALUES(2,2);
INSERT INTO Film_acteur VALUES(2,3);
INSERT INTO Film_acteur VALUES(3,1);
INSERT INTO Film_acteur VALUES(3,2);
INSERT INTO Film_acteur VALUES(3,3);

INSERT INTO musique_interprete VALUES(6, 8);
INSERT INTO musique_interprete VALUES(6, 9);

INSERT INTO exemplaire VALUES (1, 1, 'bon', false);
INSERT INTO exemplaire VALUES (2, 1, 'neuf', true);
INSERT INTO exemplaire VALUES (3, 1, 'bon', true);
INSERT INTO exemplaire VALUES (1, 2, 'bon', true);
INSERT INTO exemplaire VALUES (2, 2, 'neuf', false);
INSERT INTO exemplaire VALUES (3, 2, 'abime', true);
INSERT INTO exemplaire VALUES (1, 3, 'bon', true);
INSERT INTO exemplaire VALUES (2, 3, 'neuf', true);
INSERT INTO exemplaire VALUES (3, 3, 'neuf', false);
INSERT INTO exemplaire VALUES (1, 4, 'bon', true);
INSERT INTO exemplaire VALUES (2, 4, 'bon', true);
INSERT INTO exemplaire VALUES (1, 5, 'bon', true);
INSERT INTO exemplaire VALUES (1, 6, 'bon', true);
INSERT INTO exemplaire VALUES (2, 6, 'neuf', true);
INSERT INTO exemplaire VALUES (1, 7, 'abime', true);
INSERT INTO exemplaire VALUES (2, 7, 'bon', true);
INSERT INTO exemplaire VALUES (1, 8, 'neuf', true);
INSERT INTO exemplaire VALUES (1, 9, 'bon', true);

ALTER SEQUENCE Pret_id_pret_seq RESTART WITH 1 ;
INSERT INTO Pret VALUES (DEFAULT, '2021-11-11',30,1,1, false);
INSERT INTO Pret VALUES (DEFAULT, '2022-12-11',30,1,1, true);
INSERT INTO Pret VALUES (DEFAULT, '2022-12-08',30,3,3, true);
INSERT INTO Pret VALUES (DEFAULT, '2022-12-14',30,2,2, true);

ALTER SEQUENCE Sanction_id_Sanction_seq RESTART WITH 1 ;
INSERT INTO Sanction VALUES (DEFAULT, 2, TRUE,'deterioration', 23,NULL);
INSERT INTO Sanction VALUES (DEFAULT, 12, TRUE,'deterioration', 20,NULL);
INSERT INTO Sanction VALUES (DEFAULT, 12, TRUE,'deterioration', 3,NULL);
INSERT INTO Sanction VALUES (DEFAULT, 12, TRUE,'deterioration', 19,NULL);
INSERT INTO Sanction VALUES (DEFAULT, 12, TRUE,'deterioration', 16,NULL);
INSERT INTO Sanction VALUES (DEFAULT, 12, TRUE,'deterioration', 5,NULL);

INSERT INTO Emprunt (id_pret,id_adherent) VALUES (1,4);
INSERT INTO Emprunt (id_pret,id_adherent) VALUES (2,8);
INSERT INTO Emprunt (id_pret,id_adherent) VALUES (3,9);
INSERT INTO Emprunt (id_pret,id_adherent) VALUES (4,4);
