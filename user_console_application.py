import psycopg2

#Header de connexion
HOST = "tuxa.sme.utc"
USER = "nf18a007"
PASSWORD = "5sOUz6Mq"
DATABASE = "dbnf18a007"

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#Espace Menu principal
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Main
def main():
    #Connexion à la base de donnée
    conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
    #print(conn)
    menu(conn)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Menu principal
def menu(conn):
    cursor = conn.cursor()
    continuer_programme = True                          #boolean de fin de programme
    while (continuer_programme):
      person_type = 0                                   #variable indiquant le type de connexion (membre, adhérent)
      while(person_type not in [1, 2, 3]):
        print("\n------Menu principal------")
        print('1 -- Adhérent ')
        print('2 -- Membre ')
        print('3 -- Quitter \n')
        person_type = int(input(''))
      if person_type == 1:
        menu_adherent(cursor, conn)                     #menu de l'adhérent
      elif person_type == 2:
        menu_membre(cursor, conn)                       #menu d'un membre
      else:                                             #quitter
        continuer_programme = False

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Espace Membre

#Fonction du menu du membre
def menu_membre(cursor, conn):
    connexion_access = False
    login = input("Entrer votre login :")              #login du membre
    mdp = input("Entrer votre mot de passe :")         #mot de passe du membre
    cursor.execute("SELECT mdp, Compte_user.login FROM Compte_user INNER JOIN Membre ON Membre.login = Compte_user.login WHERE Compte_user.login = '%s' and mdp = '%s'" % (login, mdp))
    raw = cursor.fetchone()
    if raw:                                            #validation du compte_user avec boolean connexion_access
      connexion_access = True
    else:
      print("Erreur : Login/mot de passe incorrect, ou vous n'êtes peut-être pas membre")
    if connexion_access:
      continuer = True
      while continuer :
        choice = 0
        while(choice not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]):
          print("\n------Menu membre------")
          print("1  -- Ajouter une ressource")
          print("2  -- Accéder à une ressource (possibilité de la modifier)")
          print("3  -- Ajouter un exemplaire")
          print("4  -- Rechercher un exemplaire (possibilité de le modifier)")
          print("5  -- Créer un emprunt")
          print("6  -- Retour d’un emprunt")
          print("7  -- Rechercher un adhérent")
          print("8  -- Statistiques")
          print("9  -- Créer un compte adhérent")
          print("10 -- Gestion sanction")
          print("11 -- Revenir au menu principal")
          choice = int(input(''))
        if (choice == 1):                               #Choix utilisateur
            ajout_ressource(cursor, conn)
        if (choice ==  2):
            access_ressource_membre(cursor, conn)
        if (choice == 3):
            ajout_exemplaire(cursor, conn)
        if (choice == 4):
            access_exemplaire(cursor)
        if (choice == 5):
            creer_emprunt(cursor, conn)
        if (choice == 6):
            retour_emprunt(cursor,conn)
        if (choice == 7):
            access_adherent(cursor)
        if (choice == 8):
            statistiques(cursor)
        if (choice == 9):
            creer_compte_adherent(cursor, conn)
        if (choice == 10):
            gestion_sanction(cursor,conn)
        if (choice == 11):
            continuer = False

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Ajout d'une ressource
def ajout_ressource(cursor, conn):
    print("-----AJOUT RESSOURCE-----")
    titre_saisi = input("Entrez le titre : ")
    date_saisi = input("Entrez la date d’apparition (format YYYY-MM-DD) : ")
    editeur_saisi = input("Entrez l’éditeur : ")
    code_class_saisi = input("Entrez le code de classification de la ressource : ").upper()
    prix_saisi = float(input("Entrez le prix de la ressource : "))

    sql2 = "INSERT INTO Ressource VALUES (DEFAULT,%s,%s,%s,%s,%s);"
    data = (titre_saisi, date_saisi, editeur_saisi, code_class_saisi, prix_saisi)
    cursor.execute(sql2, data)
    #conn.commit()
    type_saisi = input("Entrez le type de la ressource (livre, film ou musique) : ")
    if type_saisi == "film":
        nom_realisateur_saisi = input("Entrez le nom du réalisateur : ")
        sqla = f"SELECT id_contributeur FROM Contributeur WHERE Contributeur.nom = '{nom_realisateur_saisi}';"
        cursor.execute(sqla)
        retour = cursor.fetchall()
        rowCount = len(retour)
        if rowCount == 0:  # il faut créer le réalisateur
            print("> Le réalisateur n'existe pas. Il sera ajouté. \n")
            print("-----AJOUT REALISATEUR-----")
            date_naiss_saisi = input("Entrez la date de naissance (format YYYY-MM-DD) : ")
            nationalite_saisi = input("Entrez la nationalité : ").lower()
            sqlaa = f"INSERT INTO Contributeur VALUES (DEFAULT, '{nom_realisateur_saisi}', '{date_naiss_saisi}', '{nationalite_saisi}');"
            cursor.execute(sqlaa)
            sqlab = f"SELECT id_contributeur FROM Contributeur WHERE nom = '{nom_realisateur_saisi}' AND date_naiss = '{date_naiss_saisi}' AND nationalite = '{nationalite_saisi}';"
            cursor.execute(sqlab)
            id_realisateur = int(cursor.fetchone()[0])
            print("> Ajout du réalisateur terminé.")
            print("--------------------------")
        else:
            id_realisateur = int(retour[0][0])
        # récupération du code ressource
        sqlb = "SELECT code FROM Ressource WHERE titre = %s AND date_apparition = %s AND editeur = %s AND code_classification = %s AND prix = %s;"
        data = (titre_saisi, date_saisi, editeur_saisi, code_class_saisi, prix_saisi)
        cursor.execute(sqlb, data)
        code_saisi = int(cursor.fetchone()[0])
        synopsis_saisi = input("Entrez le synopsis :")
        langue_saisi = input("Entrez la langue : ").lower()
        duree_saisi = int(input("Entrez la durée (minutes) : "))
        sqlc = "INSERT INTO film (code,synopsis,langue,duree,realisateur) VALUES (%s, %s, %s, %s, %s);"
        data = (code_saisi, synopsis_saisi, langue_saisi, duree_saisi, id_realisateur)
        cursor.execute(sqlc, data)
    elif type_saisi == "livre":
        nom_auteur_saisi = input("Entrez le nom de l'auteur : ")
        sqla = f"SELECT id_contributeur FROM Contributeur WHERE Contributeur.nom = '{nom_auteur_saisi}';"
        cursor.execute(sqla)
        retour = cursor.fetchall()
        rowCount = len(retour)
        if rowCount == 0:  # il faut créer l'auteur
            print("-----AJOUT AUTEUR-----")
            print("> L'auteur n'existe pas. Il sera ajouté. \n")
            date_naiss_saisi = input("Entrez la date de naissance (format YYYY-MM-DD) : ")
            nationalite_saisi = input("Entrez la nationalité : ").lower()
            sqlaa = f"INSERT INTO Contributeur VALUES (DEFAULT, '{nom_auteur_saisi}', '{date_naiss_saisi}', '{nationalite_saisi}');"
            cursor.execute(sqlaa)
            sqlab = f"SELECT id_contributeur FROM Contributeur WHERE nom = '{nom_auteur_saisi}' AND date_naiss = '{date_naiss_saisi}' AND nationalite = '{nationalite_saisi}';"
            cursor.execute(sqlab)
            id_auteur= int(cursor.fetchone()[0])
            print("> Ajout de l'auteur terminé.")
            print("--------------------------")
        else:
            id_auteur = int(retour[0][0])
        sqlb = "SELECT code FROM Ressource WHERE titre = %s AND date_apparition = %s AND editeur = %s AND code_classification = %s AND prix = %s;"
        data = (titre_saisi, date_saisi, editeur_saisi, code_class_saisi, prix_saisi)
        cursor.execute(sqlb, data)
        code_saisi = int(cursor.fetchone()[0])
        isbn_saisi = input("Entrez l'ISBN : ")
        resume_saisi = input("Entrez le résumé : ")
        langue_saisi = input("Entrez la langue : ").lower()
        nb_pages_saisi = int(input("Entrez le nb de pages : "))
        sqlc = "INSERT INTO livre (code,isbn,resume,langue,nb_pages,auteur) VALUES (%s, %s, %s, %s, %s, %s);"
        data = (code_saisi, isbn_saisi, resume_saisi, langue_saisi, nb_pages_saisi, id_auteur)
        cursor.execute(sqlc, data)
    if type_saisi == "musique":
        nom_compositeur_saisi = input("Entrez le nom du compositeur : ")
        sqla = f"SELECT id_contributeur FROM Contributeur WHERE Contributeur.nom = '{nom_compositeur_saisi}';"
        cursor.execute(sqla)
        retour = cursor.fetchall()
        rowCount = len(retour)
        if rowCount == 0:  # il faut créer le compositeur
            print("-----AJOUT COMPOSITEUR-----")
            print("> Le compositeur n'existe pas. Il sera ajouté. \n")
            date_naiss_saisi = input("Entrez la date de naissance (format YYYY-MM-DD) : ")
            nationalite_saisi = input("Entrez la nationalité : ").lower()
            sqlaa = f"INSERT INTO Contributeur VALUES (DEFAULT, '{nom_compositeur_saisi}', '{date_naiss_saisi}', '{nationalite_saisi}');"
            cursor.execute(sqlaa)
            sqlab = f"SELECT id_contributeur FROM Contributeur WHERE nom = '{nom_compositeur_saisi}' AND date_naiss = '{date_naiss_saisi}' AND nationalite = '{nationalite_saisi}';"
            cursor.execute(sqlab)
            id_compositeur = int(cursor.fetchone()[0])
            print("> Ajout de l'auteur terminé.")
            print("--------------------------")
        else:
            id_compositeur = int(retour[0][0])
        # récupération du code ressource
        sqlb = "SELECT code FROM Ressource WHERE titre = %s AND date_apparition = %s AND editeur = %s AND code_classification = %s AND prix = %s;"
        data = (titre_saisi, date_saisi, editeur_saisi, code_class_saisi, prix_saisi)
        cursor.execute(sqlb, data)
        code_saisi = int(cursor.fetchone()[0])
        duree_saisi = int(input("Entrez la durée (secondes) : "))
        style_saisi = input("Entrez le style : ").lower()
        sqlc = f"INSERT INTO musique (code,duree,style,compositeur) VALUES ({code_saisi}, {duree_saisi},'{style_saisi}',{id_compositeur});"
        cursor.execute(sqlc)
    print("\n > Ajout de la ressource terminé.")
    conn.commit()


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Accès aux informations concernant une ressource (toutes les informations)
def access_ressource_membre(cursor, conn):
    code_classification_saisi = input("Entrez le code de classification de la ressource que vous souhaitez consulter : ")
    sql1 = f"SELECT * FROM Ressource WHERE code_classification = '{code_classification_saisi}';"
    cursor.execute(sql1)
    raw = cursor.fetchone()
    if not raw:
        print("Cette ressource n'existe pas.")
        quit()
    else:
        code_saisi = raw[0]
        print("-----AFFICHAGE DES INFORMATIONS-----")
        print(f"Titre : {raw[1]}")
        print(f"Date d'apparition : {raw[2]}")
        print(f"Editeur : {raw[3]}")
        print(f"Code de classification : {raw[4]}")
        print(f"Prix : {raw[5]}")
        print("------------------------------------")
        want_edit = input("Souhaitez-vous modifier une de ces informations (y/n) ? ")
        if want_edit == 'y':
            print("Vous avez choisi de modifier une de ces informations.")
            nb_edit = int(input(
                "Quelle information souhaitez-vous modifier (1 : Titre, 2 : Date d'apparition, 3 : Editeur, 4 : Code de classification, 5 : Prix) ? "))
            if nb_edit == 1:
                new_titre = input("Entrez le nouveau titre : ")
                sqla = "UPDATE ressource SET titre = %s WHERE code = %s;" #gestion single quote
                data = (new_titre, code_saisi)
                cursor.execute(sqla, data)
            elif nb_edit == 2:
                new_date = input("Entrez la nouvelle date d'apparition (format YYYY-MM-DD) : ")
                sqlb = f"UPDATE ressource SET date_apparition = '{new_date}' WHERE code = {code_saisi};"
                cursor.execute(sqlb)
            elif nb_edit == 3:
                new_editeur = input("Entrez le nouvel éditeur : ")
                sqlc = "UPDATE ressource SET editeur = %s WHERE code = %s;" #gestion single quote
                data = (new_editeur, code_saisi)
                cursor.execute(sqlc, data)
            elif nb_edit == 4:
                new_code = input("Entrez le nouveau code de classification : ")
                sqld = f"UPDATE ressource SET code_classification = '{new_code}' WHERE code = {code_saisi};"
                cursor.execute(sqld)
            elif nb_edit == 5:
                new_prix = float(input("Entrez le nouveau prix : "))
                sqle = f"UPDATE ressource SET prix = {new_prix} WHERE code = {code_saisi};"
                cursor.execute(sqle)
    type_saisi = input(
        "Entrez le type de la ressource (livre, film ou musique) : ")

    if type_saisi == "film":
        sql2 = f"SELECT * FROM film WHERE code = {code_saisi};"
        cursor.execute(sql2)
        retour = cursor.fetchall()
        rowCount = len(retour)
        if rowCount == 0:
            print(f"Erreur, cette ressource n'est pas un {type_saisi}.")
            quit("Par sécurité, aucune information n'a été modifiée.")
        else:
            print("-----AFFICHAGE DES INFORMATIONS-----")
            print(f"Synopsis: {retour[0][1]}")
            print(f"Langue : {retour[0][2]}")
            print(f"Durée (minutes) : {retour[0][3]}")
            sql2bis = f"SELECT nom FROM Contributeur WHERE id_contributeur = {retour[0][4]}"
            cursor.execute(sql2bis)
            nom_compo = cursor.fetchone()[0]
            print(f"Id du réalisateur : {retour[0][4]} (Nom : {nom_compo})")
            print("------------------------------------")
            want_edit = input("Souhaitez-vous modifier une de ces informations (y/n) ? ")
            if want_edit == 'y':
                print("Vous avez choisi de modifier une de ces informations.")
                nb_edit = int(input("Quelle information souhaitez-vous modifier (1 : Synopsis, 2 : Langue , 3 : Durée, 4 : Id du réalisateur) ? "))
                if nb_edit == 1:
                    new_synopsis = input("Entrez le nouveau synopsis : ")
                    sqla = "UPDATE film SET synopsis = %s WHERE code = %s;"
                    data = (new_synopsis, code_saisi)  # gestion single quote
                    cursor.execute(sqla, data)
                elif nb_edit == 2:
                    new_langue = input("Entrez la nouvelle langue : ")
                    sqlb = f"UPDATE film SET langue = '{new_langue}' WHERE code = {code_saisi};"
                    cursor.execute(sqlb)
                elif nb_edit == 3:
                    new_duree = int(input("Entrez la nouvelle durée (minutes) : "))
                    sqlc = f"UPDATE film SET duree = {new_duree} WHERE code = {code_saisi};"
                    cursor.execute(sqlc)
                elif nb_edit == 4:
                    print("-----RAPPEL REALISATEURS (id | nom)-----")
                    sqlpred = f"SELECT DISTINCT id_contributeur, nom FROM Contributeur JOIN Film ON id_contributeur = realisateur ORDER BY id_contributeur;"
                    cursor.execute(sqlpred)
                    res = cursor.fetchall()
                    for raw in res:
                        print(f"{raw[0]} | {raw[1]}")
                    print("----------------------------------------")
                    new_idrea = int(input("Entrez le nouvel id du réalisateur : "))
                    sqld = f"UPDATE film SET realisateur = {new_idrea} WHERE code = {code_saisi};"
                    cursor.execute(sqld)
    elif type_saisi == "livre":
        sql2 = f"SELECT * FROM livre WHERE code = {code_saisi};"
        cursor.execute(sql2)
        retour = cursor.fetchall()
        rowCount = len(retour)
        if rowCount == 0:
            print(f"Erreur, cette ressource n'est pas un {type_saisi}.")
            quit("Par sécurité, aucune information n'a été modifiée.")
        else:
            print("-----AFFICHAGE DES INFORMATIONS-----")
            print(f"Isbn: {retour[0][1]}")
            print(f"Résumé : {retour[0][2]}")
            print(f"Langue : {retour[0][3]}")
            print(f"Nombre de pages : {retour[0][4]}")
            sql2bis = f"SELECT nom FROM Contributeur WHERE id_contributeur = {retour[0][5]}"
            cursor.execute(sql2bis)
            nom_compo = cursor.fetchone()[0]
            print(f"Id de l'auteur : {retour[0][5]} (Nom : {nom_compo})")
            print("------------------------------------")
            want_edit = input("Souhaitez-vous modifier une de ces informations (y/n) ? ")
            if want_edit == 'y':
                print("Vous avez choisi de modifier une de ces informations.")
                nb_edit = int(input("Quelle information souhaitez-vous modifier (1 : Isbn, 2 : Résumé , 3 : Langue, 4 : Nombre de pages, 5 : Id de l'auteur) ? "))
                if nb_edit == 1:
                    new_isbn = input("Entrez le nouveau isbn : ")
                    sqla = f"UPDATE livre SET isbn = '{new_isbn}' WHERE code = {code_saisi};"
                    cursor.execute(sqla)
                elif nb_edit == 2:
                    new_resume = input("Entrez le nouveau résumé : ")
                    sqlb = f"UPDATE livre SET resume = %s WHERE code = %s;"
                    data = (new_resume, code_saisi)
                    cursor.execute(sqlb, data)
                elif nb_edit == 3:
                    new_langue = input("Entrez la nouvelle langue : ")
                    sqlc = f"UPDATE livre SET langue = '{new_langue}' WHERE code = {code_saisi};"
                    cursor.execute(sqlc)
                elif nb_edit == 4:
                    new_nbpages = int(input("Entrez le nouveau nombre de pages : "))
                    sqld = f"UPDATE livre SET nb_pages = {new_nbpages} WHERE code = {code_saisi};"
                    cursor.execute(sqld)
                elif nb_edit == 5:
                    print("-----RAPPEL AUTEURS (id | nom)-----")
                    sqlpree = f"SELECT DISTINCT id_contributeur, nom FROM Contributeur JOIN Livre ON id_contributeur = auteur ORDER BY id_contributeur;"
                    cursor.execute(sqlpree)
                    res = cursor.fetchall()
                    for raw in res:
                        print(f"{raw[0]} | {raw[1]}")
                    print("----------------------------------------")
                    new_idauteur = int(input("Entrez le nouvel id de l'auteur : "))
                    sqle = f"UPDATE livre SET auteur = {new_idauteur} WHERE code = {code_saisi};"
                    cursor.execute(sqle)
    elif type_saisi == "musique":
        sql2 = f"SELECT * FROM musique WHERE code = {code_saisi};"
        cursor.execute(sql2)
        retour = cursor.fetchall()
        rowCount = len(retour)
        if rowCount == 0:
            print(f"Erreur, cette ressource n'est pas un {type_saisi}.")
            quit("Par sécurité, aucune information n'a été modifiée.")
        else:
            print("-----AFFICHAGE DES INFORMATIONS-----")
            print(f"Durée (secondes): {retour[0][1]}")
            print(f"Style : {retour[0][2]}")
            sql2bis = f"SELECT nom FROM Contributeur WHERE id_contributeur = {retour[0][3]}"
            cursor.execute(sql2bis)
            nom_compo = cursor.fetchone()[0]
            print(f"Id du compositeur : {retour[0][3]} (Nom : {nom_compo})")
            print("------------------------------------")
            want_edit = input("Souhaitez-vous modifier une de ces informations (y/n) ? ")
            if want_edit == 'y':
                print("Vous avez choisi de modifier une de ces informations.")
                nb_edit = int(input("Quelle information souhaitez-vous modifier (1 : Durée, 2 : Style, 3 : Id du compositeur) ? "))
                if nb_edit == 1:
                    new_duree = int(input("Entrez la nouvelle durée (en secondes) : "))
                    sqla = f"UPDATE musique SET duree = {new_duree} WHERE code = {code_saisi};"
                    cursor.execute(sqla)
                elif nb_edit == 2:
                    new_style = input("Entrez le nouveau style : ")
                    sqlb = f"UPDATE musique SET style = '{new_style}' WHERE code = {code_saisi};"
                    cursor.execute(sqlb)
                elif nb_edit == 3:
                    print("-----RAPPEL COMPOSITEURS (id | nom)-----")
                    sqlprec = f"SELECT DISTINCT id_contributeur, nom FROM Contributeur JOIN Musique ON id_contributeur = compositeur ORDER BY id_contributeur;"
                    cursor.execute(sqlprec)
                    res = cursor.fetchall()
                    for raw in res:
                        print(f"{raw[0]} | {raw[1]}")
                    print("----------------------------------------")
                    new_idcompo = int(input("Entrez le nouvel id du compositeur : "))
                    sqlc = f"UPDATE musique SET compositeur = {new_idcompo} WHERE code = {code_saisi};"
                    cursor.execute(sqlc)
    conn.commit()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Ajout d'une ressource de la part d'un membre
def ajout_exemplaire(cursor, conn):

    code_classification = input("Insérer le code de classification de l'exemplaire à ajouter : ")

    cursor.execute("Select code FROM ressource WHERE code_classification = '%s'" % (code_classification))
    code_ressource = cursor.fetchone()

    if code_ressource:

        etat = input("Insérer l'état de l'exemplaire : ")

        cursor.execute("SELECT MAX(numero) FROM exemplaire WHERE code_ressource = '%s';" % (code_ressource[0]))
        max_num_exemplaire = cursor.fetchone()[0]

        ##si c'est le premier exemplaire de la ressource
        if not max_num_exemplaire:
            max_num_exemplaire = 0

        cursor.execute("INSERT INTO exemplaire(numero, code_ressource, etat, disponible) VALUES (%i, '%s', '%s', 'true');" % (max_num_exemplaire+1, code_ressource[0], etat))
    else:
        print(f"ERROR no ressource associated to {code_classification}")
    conn.commit()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Accès d'un membre aux informations concernant un exemplaire
def access_exemplaire(cursor):
    code_classification = input("Insérer le code de classification de l'exemplaire à rechercher : ")
    cursor.execute("Select code FROM ressource WHERE code_classification = '%s';" % (code_classification))
    code_ressource = cursor.fetchone()
    if code_ressource:
        cursor.execute("SELECT exemplaire.numero, exemplaire.etat, exemplaire.disponible FROM exemplaire WHERE exemplaire.code_ressource = '%s';" % (code_ressource[0]))
        for elem in cursor.fetchall():
            if elem[2] == False:
                print(f"Numéro : {elem[0]} | Etat : {elem[1]} | Disponible : non ")
            else:
                print(f"Numéro : {elem[0]} | Etat : {elem[1]} | Disponible : oui")
    else:
        print(f"ERROR no ressource associated to {code_classification}")

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Création d'un nouvel emprunt
def creer_emprunt(cursor, conn):
    login_saisi = input("Insérer le login de l'adhérent : ")
    cursor.execute("SELECT id_adherent FROM Adherent WHERE login = '%s';" % (login_saisi))
    id_ad = cursor.fetchone()
    if id_ad:
        cursor.execute("SELECT etat_sanction FROM sanction WHERE id_adherent = '%s' and etat_sanction = true;" % (id_ad[0]))
        sanction = cursor.fetchall()
        if sanction:                    #est ce que adhérent a des sanctions actives
            print("L'adhérent possède au moins une sanction, il ne peut pas emprunter")
        else:
            cursor.execute("SELECT count(Pret.id_pret) FROM pret INNER JOIN Emprunt ON Emprunt.id_pret=Pret.id_pret WHERE Emprunt.id_adherent = '%s' AND Pret.etat_pret='true';" % (id_ad[0]))
            nb_pret = cursor.fetchone()
            if nb_pret[0] >= 4:         #est ce qu'il n'a pas dépassé le nb de pret max autorisé
                print("L'adhérent a trop de prêts en cours, il ne peut pas emprunter")
            else:                       ##vérifier la dispo de la ressource
                code_classification = input("Insérer le code de classification de l'exemplaire à emprunter : ")
                cursor.execute("Select code FROM ressource WHERE code_classification = '%s';" % (code_classification))
                code_ressource = cursor.fetchone()
                if code_ressource:
                    numero_exemplaire = input("Insérer le numéro d'exemplaire à emprunter : ")
                    cursor.execute(f"""SELECT disponible, numero, etat FROM exemplaire WHERE numero = {numero_exemplaire} AND code_ressource = {code_ressource[0]};""")
                    exemplaire = cursor.fetchone()
                    numero_pret = 0
                    if exemplaire:
                        if exemplaire[0] == True and (exemplaire[2] in ['neuf', 'bon']):
                            numero_pret = exemplaire[1]
                            ##on créé l'emprunt

                            ##insertion dans la table pret
                            cursor.execute(f"""INSERT INTO pret VALUES (DEFAULT, CURRENT_DATE, 30, {numero_pret}, {code_ressource[0]}, 'true');""")
                            conn.commit()

                            ##insertion dans la table emprunt
                            cursor.execute(f"""SELECT id_pret FROM pret WHERE date_pret = CURRENT_DATE AND duree_pret = 30 AND numero_ressource = {numero_pret} AND code_ressource = {code_ressource[0]} AND etat_pret = 'true';""")
                            pret = cursor.fetchone()

                            cursor.execute("INSERT INTO emprunt VALUES ('%s', '%s');" % (pret[0], id_ad[0]))

                            ##MAj de la table exemplaire
                            cursor.execute(f"""UPDATE exemplaire SET disponible = 'false' WHERE numero = {numero_pret} AND code_ressource = {code_ressource[0]};""")

                            ##MAJ de la table Adherent
                            cursor.execute("UPDATE adherent SET nombre_pret = nombre_pret + 1 WHERE id_adherent = '%s';" % (id_ad[0]))

                            print("\nEmprunt enregistré\n")
                        else:
                            print("Ressource indisponible")
                    else:
                            print(f"Exemplaire {numero_exemplaire} introuvable")
                else:
                    print(f"Ressource {code_classification} introuvable")
    else:
        print("Utilisateur introuvable ")
    conn.commit()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Gestion du retour d'un emprunt
def retour_emprunt(cursor,conn):
    print("\n------Retour d'emprunt------\n")

    continuer = True

    while continuer:

        login = input("Login de la personne qui rend: ")
        code_class = input("Code classification de la ressource (écrite sur la ressource): ")
        num_exemplaire = int(input("Numéro d'exemplaire (écrit sur la ressource): "))

        #Récupération de l'id de l'adherent qui rend
        sql = f"""SELECT A.id_adherent FROM Adherent A
            WHERE A.login = '{login}'""";
        cursor.execute(sql)
        raw = cursor.fetchone()
        if raw:
            id_ad = raw[0]
        else:
            print("Erreur: login introuvable")

        #Récupération du code de la ressource qui correspond à l'exemplaire à rendre
        sql1 = f"""SELECT R.code, R.prix FROM Ressource R
            WHERE R.code_classification = '{code_class}'""";
        cursor.execute(sql1)

        raw1 = cursor.fetchone()

        if raw1:
            code_ress = raw1[0]
            prix_ress = raw1[1]
            continuer = False
        else:
            print("Erreur: le code de classification ne correspond à aucune ressource")

    #Récupération des informations concernant le prêt en question
    sql2 = f"""SELECT * , CURRENT_DATE - (P.date_pret+P.duree_pret) AS nb_jours_retard FROM Pret P
        JOIN Emprunt E ON P.id_pret = E.id_pret
        WHERE P.code_ressource = {code_ress} AND E.id_adherent = {id_ad} AND P.etat_pret = True AND P.numero_ressource = {num_exemplaire};"""
    cursor.execute(sql2)
    raw2 = cursor.fetchone()

    if raw2:
        print("\n---Récapitulatif des informations concernant le prêt---\n")
        print(f"ID prêt: {raw2[0]}\nDate de prêt: {raw2[1]}\nDurée prêt: {raw2[2]}\nNuméro de l'exemplaire: {num_exemplaire}\nCode de la ressource: {raw2[4]}")

        jours_retard = raw2[8]
        #Si la ressource est rendue en avance, on met les jours de retards à 0
        if jours_retard < 0:
            jours_retard = 0

        print(f"Jours de retard: {jours_retard}")

        sql3 = f"""SELECT etat FROM Exemplaire WHERE code_ressource = {code_ress} AND numero = {num_exemplaire};"""
        cursor.execute(sql3)
        raw3 = cursor.fetchone()

        print(f"Etat de la ressource avant prêt: {raw3[0]}")

        etat_rendu = input("Dans quel état est l'exemplaire au moment du retour (neuf,bon,abime,perdu): ")

        if jours_retard > 0:
            print("La ressource est rendue en retard, une sanction va être appliquée")
            sql4 = f"""INSERT INTO Sanction
                VALUES(DEFAULT,{id_ad},true,'retard',NULL,{jours_retard})""";
            cursor.execute(sql4)

        if raw3[0] != etat_rendu and (etat_rendu == 'abime' or etat_rendu == 'perdu'):
            print("La ressource a été dégradée/perdue, une sanction va être appliquée")
            print(f"L'utilisateur doit rembourser la somme de {prix_ress} euros")
            sql5 = f"""INSERT INTO Sanction
                VALUES(DEFAULT,{id_ad},true,'deterioration',{prix_ress},NULL);"""
            cursor.execute(sql5)

        #Si l'exemplaire est perdu, il faut mettre l'exemplaire indisponible
        if etat_rendu == 'perdu':
            sql6 = f"UPDATE Exemplaire SET disponible = False WHERE numero = {num_exemplaire} AND code_ressource = {code_ress};"
            cursor.execute(sql6)
        else:
            sql7 = f"UPDATE Exemplaire SET disponible = True WHERE numero = {num_exemplaire} AND code_ressource = {code_ress};"
            cursor.execute(sql7)

        #Check si on doit blacklist l'adhérent au vu de son nombre de sanctions
        sql8 = f"""SELECT COUNT(*) AS nb_sanctions FROM SANCTION WHERE id_adherent = {id_ad} AND etat_sanction = true;"""
        cursor.execute(sql8)
        raw8 = cursor.fetchone()

        if raw8[0] >= 5:
            print("Vous venez de dépasser le nombre de sanctions tolérées, vous allez être blacklisté")
            sql9 = f"""UPDATE Adherent SET blacklist = true WHERE id_adherent = {id_ad};"""
            cursor.execute(sql9)
        else:
            print(f"Vous avez {raw8[0]} sanction(s). Au bout de 5 vous serez blacklisté")

        #----Fin du prêt----
        #On met l'état prêt à False

        sql8 = f"UPDATE Pret SET etat_pret = False WHERE numero_ressource = {num_exemplaire} AND code_ressource = {code_ress};"
        cursor.execute(sql8)

    else:
        print("Aucun prêt actif n'est enregistré pour cette ressource et cet adhérent")

    conn.commit()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Accès aux informations concernant un adhérent de la part d'un membre
def access_adherent(cursor):
    login_adherent = input("Veuillez entrer le login de l'adhérent à rechercher : ")
    cursor.execute("SELECT Compte_user.login, blacklist, actif FROM Compte_user INNER JOIN Adherent ON Adherent.login = Compte_user.login WHERE Compte_user.login = '%s'" % (login_adherent))
    raw1 = cursor.fetchone()
    if raw1:                                             #validation du compte_user avec boolean connexion_access
        print("Voici le profil de : ",login_adherent, "\n")
        if raw1[1]==True:
            print("/!\ Utilisateur blacklisté /!\ ")
        if raw1[2]==False:
            print("/!\ Utilisateur inactif /!\ ")
        cursor.execute("SELECT COUNT(*) AS nb_prets_total FROM Emprunt INNER JOIN Adherent ON Emprunt.id_adherent = Adherent.id_adherent WHERE Adherent.login = '%s' GROUP BY Emprunt.id_adherent" %(login_adherent))
        raw2 = cursor.fetchone()
        if raw2:
            print(f"Nombre de prêts : {raw2[0]}\n")
            cursor.execute("SELECT Pret.duree_pret, Pret.date_pret, Pret.numero_ressource, Ressource.titre, Pret.etat_pret FROM Emprunt INNER JOIN Pret on Emprunt.id_pret = Pret.id_pret INNER JOIN Ressource ON Pret.code_ressource=Ressource.code INNER JOIN Adherent ON Emprunt.id_adherent = Adherent.id_adherent WHERE Adherent.login = '%s'" % (login_adherent))
            tab = cursor.fetchall()
            if tab:
                i = 1
                for raw3 in tab:
                    print(f"-- Emprunt n° {i}\n")
                    if (raw3[4]):
                        etat_pret = "En cours"
                    else:
                        etat_pret = "Terminé"
                    print(f"Titre : {raw3[3]}")
                    print(f"Exemplaire n° : {raw3[2]}")
                    print(f"Date de prêt : {raw3[1]}")
                    print(f"Durée du prêt : {raw3[0]}")
                    print(f"Etat : {etat_pret}\n")
                    i+=1
            else:
                print("Cet adhérent n'a jamais effectué aucun prêt")
        else:
            print("Cet adhérent n'a jamais effectué aucun prêt")
        print('\n')
        cursor.execute("SELECT COUNT(*) FROM Sanction INNER JOIN Adherent ON Sanction.id_adherent=Adherent.id_adherent WHERE Adherent.login = '%s' GROUP BY Adherent.login" %(login_adherent))
        raw4 = cursor.fetchone()
        if raw4:
            if raw4[0]==1:
                print("Cet utilisateur possède 1 sanction")
            else:
                print(f"Cet utilisateur possède {raw4[0]} santions")
            cursor.execute("SELECT type_sanction, prix, duree_retard, etat_sanction FROM Sanction INNER JOIN Adherent ON Sanction.id_adherent=Adherent.id_adherent WHERE Adherent.login = '%s'" %(login_adherent))
            tab2 = cursor.fetchall()
            if tab2:
                i = 1
                for raw5 in tab2:
                    if (raw5[3]):
                        etat_sanction = "En attente (Emprunt interdit)"
                    else:
                        etat_sanction = "Réglée"
                    if (raw5[0]=="deterioration"):
                        print(f"-- Sanction n° {i} : {raw5[0]} | Prix : {raw5[1]}€ | Etat : {etat_sanction}")
                    else:
                        print(f"-- Sanction n° {i} : {raw5[0]} | Durée : {raw5[2]} | Etat : {etat_sanction}")
                    i+=1
        else:
            print("Cet utilisateur ne possède aucune sanction")
    else:
        print("Erreur, login introuvable")

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Accès aux statistiques de prêts
def statistiques(cursor):
    continuer = True
    while continuer:
        choix = 0
        while choix not in [1,2,3]:
            print("\n------Statistiques------")
            print("1 -- Classement des ressources les plus empruntées")
            print("2 -- CLassement des adhérents qui empruntent le plus")
            print("3 -- Retour au menu")
            choix = int(input(''))

        if choix == 1:

            sql = """SELECT R.code, R.titre, COUNT(P.id_pret) AS nb_prets FROM Ressource R
                JOIN Pret P ON R.code = P.code_ressource
                GROUP BY R.code, R.titre
                ORDER BY nb_prets DESC;"""
            cursor.execute(sql)
            raw = cursor.fetchone()

            if raw:
                print("%-20s" % "Code", "%-20s" % "Titre", "%-20s" % "Nombre de prêts\n")
                while raw:

                    print("%-20s" % raw[0], "%-20s" % raw[1], "%-20s" % raw[2])
                    raw = cursor.fetchone()
            else:
                print("Aucun prêt n'est enregistré dans la BDD\n")

        if choix == 2:

            sql = """SELECT  A.id_adherent, A.nom, A.prenom, A.login, A.nombre_pret FROM Adherent A
                WHERE A.nombre_pret > 0
                ORDER BY A.nombre_pret DESC;"""

            cursor.execute(sql)
            raw = cursor.fetchone()
            if raw:
                print("%-20s" % "ID", "%-20s" % "Nom", "%-20s" % "Prenom", "%-20s" % "Login", "%-20s" % "Nombre de prêts\n")
                while raw:
                    print("%-20s" % raw[0], "%-20s" % raw[1], "%-20s" % raw[2], "%-20s" % raw[3], "%-20s" % raw[4])
                    raw = cursor.fetchone()
            else:
                print("Aucun adhérent n'a fait de prêt")

        if choix == 3:
            continuer=False

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def creer_compte_adherent(cursor, conn):
    try:
        print("Ajout d'un adhérent.")
        username = input("Entrez un nom d'utilisateur : ")
        password = input("Entrez un mot de passe : ")
        if not username or not password:
            raise ValueError("Le nom d'utilisateur ou le mot de passe ne peuvent pas être vides.")
        sql1 = "INSERT INTO compte_user VALUES (%s, %s)"
        data = (username, password)
        cursor.execute(sql1, data)
        nom = input("Entrez le nom : ")
        prenom = input("Entrez le prénom : ")
        adresse = input("Entrez l'adresse : ")
        tel = input("Entrez l'numéro de téléphone : ")
        sql2 = "INSERT INTO adherent VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s, %s)"
        data = (nom, prenom, adresse, tel, 0, False, True, username)
        cursor.execute(sql2, data)
        print(f"L'adhérent {username} a bien été ajouté.")
        conn.commit()
    except psycopg2.errors.UniqueViolation as u:
        print("Erreur : ce nom d'utilisateur est déjà pris.")
    except ValueError as e:
        print(e)

def gestion_sanction(cursor, conn):
    login = input("Entrez le login de l'adhérent : ")
    sql1 = f"SELECT id_adherent from adherent where login = '{login}';"
    cursor.execute(sql1)
    raw = cursor.fetchone()
    if raw:
        id = raw[0]
        sql2 = f"SELECT * FROM Sanction where sanction.id_adherent = {id} and etat_sanction = True and type_sanction = 'deterioration';"
        cursor.execute(sql2)
        res = cursor.fetchall()

        if res:
            print("\n---Sanctions de détérioration actives---\n")
            for line in res:
                print(f"\nId sanction : {line[0]} | Id adhérent : {line[1]} | Etat de la sanction : {line[2]} | Type de la sanction : {line[3]} | Prix : {line[4]}\n")

            id_remb = int(input("\nSaisissez l'id de la sanction à rembourser: "))
            sql3 = f"SELECT prix FROM Sanction WHERE id_sanction={id_remb};"
            cursor.execute(sql3)
            raw = cursor.fetchone()

            print(f"Le prix à rembourser est: {raw[0]} euros")

            argent_rendu = float(input("Saisir le montant donné par l'adhérent (montant exact sinon rien): "))

            if argent_rendu == raw[0]:
                sql4 = f"UPDATE Sanction SET etat_sanction = False WHERE id_sanction = {id_remb};"
                cursor.execute(sql4)
                print("\nSanction désactivée\n")
            else:
                print("\nRepassez plus tard avec le montant exact ! ")

        else:
            print("L'adhérent n'a pas de sanction détérioration en cours")
    else:
        print("Le login n'existe pas.")
    conn.commit()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Espace Adhérent

#Menu d'un adhérent
def menu_adherent(cursor, conn):
    connexion_access = False
    login = input("Entrer votre login :")       #login de l'adhérent
    mdp = input("Entrer votre mot de passe :")  #mot de passe de l'adhérent
    cursor.execute("SELECT mdp, Compte_user.login, blacklist FROM Compte_user INNER JOIN Adherent ON Adherent.login = Compte_user.login WHERE Compte_user.login = '%s' and mdp = '%s'" % (login, mdp))
    raw = cursor.fetchone()
    if raw:
        if raw[2]:
            print("Vous êtes blacklisté, votre compte n'est plus accessible.")
        else:
            connexion_access = True                   #validation du compte_user avec boolean connexion_access
    else:
      print("Erreur : Login/mot de passe incorrect, ou vous n'êtes peut-être pas adhérent")
    if connexion_access:
      continuer = True                          #boolean de fin de menu
      while continuer :
        choice = 0
        while(choice not in [1, 2, 3]):
          print("\n------Menu adhérent------")
          print("1 -- Accéder à une ressource (+voir le nombre d'exemplaires disponibles)")
          print("2 -- Consulter son profil (pret, statistique)")
          print("3 -- Revenir au menu principal")
          choice = int(input(''))
        if choice == 1:                         #Choix utilisateur
            access_ressource_adherent(cursor)
        if choice == 2:
            access_monprofil(cursor,login)
        if choice == 3:
            continuer = False

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Accès d'un adhérent aux informations concernant son profil
def access_monprofil(cursor,login):

    print("\n\n--------------------")
    print(f"Profil de {login}")
    print("--------------------\n")

    print("---Voici vos emprunts en cours--- \n")

    #Récupération des titres des ressources empruntées, de la date du prêt et de la durée du prêt
    sql = f"""SELECT Ressource.titre, Pret.date_pret, Pret.duree_pret, Pret.date_pret + Pret.duree_pret FROM Emprunt
        INNER JOIN Pret on Emprunt.id_pret = Pret.id_pret
        INNER JOIN Ressource on Ressource.code = Pret.code_ressource
        WHERE Pret.etat_pret = true and Emprunt.id_adherent = (SELECT id_adherent FROM Adherent WHERE login = '{login}');"""

    cursor.execute(sql)

    raw = cursor.fetchone()
    while raw:
        print(f"Titre: {raw[0]}")
        print(f"Emprunté le {raw[1]}")
        print(f"Délais pour rendre la ressource: {raw[2]} jours")
        print(f"A rendre le: {raw[3]}\n")

        raw = cursor.fetchone()

    print("---Historique de vos prêts terminés---\n")

    #Récupération des titres des ressources ayant été empruntées ainsi que leur date de prêt (pour les prêts terminés)
    sql = f"""SELECT Ressource.titre, Pret.date_pret FROM Emprunt
        INNER JOIN Pret on Emprunt.id_pret = Pret.id_pret
        INNER JOIN Ressource on Ressource.code = Pret.code_ressource
        WHERE Pret.etat_pret = false and Emprunt.id_adherent = (SELECT id_adherent FROM Adherent WHERE login = '{login}');"""

    cursor.execute(sql)

    raw = cursor.fetchone()
    while raw:
        print(f"Titre: {raw[0]}")
        print(f"Emprunté le {raw[1]}\n")
        raw = cursor.fetchone()

    #Récupération du nombre de prêts réalisés
    sql = f"""SELECT COUNT(*) FROM Emprunt E
        WHERE E.id_adherent = (SELECT id_adherent FROM Adherent WHERE login = '{login}');"""

    cursor.execute(sql)
    raw = cursor.fetchone()
    print(f"---Nombre total de prêts réalisés---\n")
    print(f"> {raw[0]}\n")

    print(f"---Récap de vos sanctions---\n")

    #Récupération des sanctions
    sql = f"""SELECT S.type_sanction, S.etat_sanction, S.prix, S.duree_retard
        FROM Sanction S
        WHERE S.id_adherent = (SELECT id_adherent FROM Adherent WHERE login = '{login}');"""

    cursor.execute(sql)

    raw = cursor.fetchone()
    if raw:
        while raw:
            print(f"Type de sanction: {raw[0]}")
            if raw[1] == True:
                print("Etat de la sanction: active")
            else:
                print("Etat de la sanction: inactive")
            if raw[0] == 'retard':
                print(f"Durée du retard: {raw[3]}\n")
            if raw[0] == 'deterioration':
                print(f"Prix à rembourser: {raw[2]}\n")
            raw = cursor.fetchone()

    else:
        print("Aucune sanction")

    print("\n--------------------\n")

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Accès aux informations concernant une ressource (informations permises à l'adhérent)
def access_ressource_adherent(cursor):

    #ON considère que deux ressources différentes n'ont pas le même titre

    choix = 0
    while (choix not in [1,2,3]):
        print("\nQuelle type de ressource recherchez-vous ?")
        print("1 -- Livre")
        print("2 -- Film")
        print("3 -- Musique")
        choix = int(input(''))
    title = input("Titre à chercher: ")
    if choix == 1:  #On va chercher dans les livres

        sql = f"""SELECT R.titre, C.nom, R.editeur, L.resume, L.nb_pages, L.ISBN, R.code FROM Ressource R
            JOIN Livre L ON R.code = L.code
            JOIN Contributeur C ON L.auteur = C.id_contributeur
            WHERE R.titre = '{title}';"""
        cursor.execute(sql)

        raw = cursor.fetchone()
        if raw:
            print(f"\n- Titre: {raw[0]}\n- Auteur: {raw[1]}\n- Editeur: {raw[2]}\n- Nombre de pages: {raw[4]}\n- ISBN: {raw[5]}\n- Resume: {raw[3]} ")

        else:
            print("\nCe livre n'est pas dans notre bibliothèque")

    if choix == 2:  #On va chercher dans les films

        sql = f"""SELECT R.titre, R.date_apparition, F.synopsis, F.langue, F.duree, C.nom, R.code FROM Ressource R
            JOIN Film F ON R.code = F.code
            JOIN Contributeur C ON F.realisateur = C.id_contributeur
            WHERE R.titre = '{title}';"""
        cursor.execute(sql)

        raw = cursor.fetchone()
        if raw:

            print(f"\n- Titre: {raw[0]}\n- Réalisateur: {raw[5]}\n- Date de sortie: {raw[1]}\n- Langue: {raw[3]}\n- Durée: {raw[4]} min\n- Synopsis: {raw[2]}")

        else:
            print("\nCe film n'est pas dans notre bibliothèque")

    if choix == 3:  #On va chercher dans les musiques

        sql = f"""SELECT R.titre, R.date_apparition, M.duree, M.style, C.nom, R.editeur, R.code FROM Ressource R
            JOIN Musique M ON R.code = M.code
            JOIN Contributeur C ON M.compositeur = C.id_contributeur
            WHERE R.titre = '{title}';"""
        cursor.execute(sql)

        raw = cursor.fetchone()
        if raw:
            print(f"\n- Titre: {raw[0]}\n- Compositeur: {raw[4]}\n- Date de sortie: {raw[1]}\n- Style: {raw[3]}\n- Duree: {raw[2]}")

        else:
            print("\nCette musique n'est pas dans notre bibliothèque")

    #On cherche le nombre d'exemplaires disponible
    if raw:
        sql2 = f"""SELECT COUNT(*) FROM Exemplaire E
            WHERE E.code_ressource = {raw[6]} AND E.disponible=True;"""
        cursor.execute(sql2)
        raw2 = cursor.fetchone()
        print(f"\nIl y a {raw2[0]} exemplaire(s) disponibles")
        if raw2[0] != 0:
            print("Dirigez-vous vers l'accueil ou contactez un membre pour un éventuel prêt")


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Appel de fonction main
main()
