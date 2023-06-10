# voici un programme python qui vérifie si une année entré par l'utilisateur
# est bissextile ou pas
user_int= input("veuillez entrer une année: ")
user_int= int(user_int)

if((user_int % 4) == 0 | (user_int % 400)==0):
    print("l'année que vous avez entré est une année bissextile.")
else:
    print("l'année que vous avez entré n'est pas une année bissextile.")
