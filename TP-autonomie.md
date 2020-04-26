# TP-Autonomie

Création d'un blog en Python avec le framework Flask.

* Créez un nouveau projet Python, mettez en place l'environnement virutel python (venv), installez Flask et Flask-SQLAlchemy
* Créez un Modèle Post (avec id, titre, résumé, contenu, date de création, et statut (publié ou brouillon))
* Créez votre page d'accueil qui affiche la liste des posts publiés (en affichant uniquement titre, résumé et date de création) (vous pouvez créer vos post via un logiciel de gestion de BDD comme DBBrowser pour le moment)
* Créez une page de détails d'un post (où l'on affichera titre, résumé, date et contenu)
* Créez un modèle User (avec id, email, mot de passe et nom)
* Modifiez le modèle du post pour créer un lien entre un post et un utilisateur (son auteur)
* Créez une page pour s'enregistrer (création d'un utilisateur)
* Créez une page de login
* Créer une page d'administration (accessible uniquement par un utilisateur connecté) qui liste tous les posts existants (même les brouillons)
* Depuis cette page d'administration donnez la possibilité de Créer un post
* Créez également la page d'édition d'un post (accessible uniquement depuis la page d'administration)
