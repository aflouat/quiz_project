🧠 Django Mini-Quiz MVP
Ce projet est un MVP (Produit Minimum Viable) d'une application de quiz développée avec Django 6.0. Il permet aux utilisateurs connectés de répondre à une série de questions aléatoires et de suivre leurs scores.

🚀 Fonctionnalités actuelles
Génération aléatoire : Sélection de 5 questions parmi la base de données à chaque session.

Système de score : Calcul automatique des résultats et enregistrement par utilisateur.

Historique : Consultation des résultats précédents via une page dédiée.

Données d'exemple : Un point de terminaison (/create_sample/) pour peupler rapidement la base de données.

🛠️ Installation et Onboarding
1. Cloner le dépôt
Bash
git clone https://github.com/aflouat/quiz_project.git
cd quiz_project
2. Créer l'environnement virtuel
Bash
python -m venv venv
# Sur Windows
.\venv\Scripts\activate
# Sur Mac/Linux
source venv/bin/activate
3. Installer Django
Bash
pip install django
4. Appliquer les migrations
Le projet utilise SQLite par défaut. Créez la base de données locale :

Bash
python manage.py makemigrations
python manage.py migrate
5. Créer un compte administrateur
Essentiel pour accéder au quiz car la vue est protégée par @login_required.

Bash
python manage.py createsuperuser
🚦 Démarrage rapide
Lancer le serveur :

Bash
python manage.py runserver
Initialiser les questions :
Visitez http://127.0.0.1:8000/create_sample/ pour injecter les 5 questions par défaut (Capitale, Océan, Art, etc.).

Jouer :
Allez sur http://127.0.0.1:8000/quiz/.

📂 Structure du projet
quiz_app/models.py : Définit les modèles Question, Choice, QuizResult et UserAnswer.

quiz_app/views.py : Contient la logique de sélection aléatoire et de calcul du score.

quiz_project/settings.py : Configuration globale (langue en fr-fr, gestion des fichiers statiques).

📝 Roadmap (Prochaines étapes)
[ ] Corriger le calcul du pourcentage de score dans le template.

[ ] Ajouter une interface d'administration personnalisée dans admin.py.

[ ] Implémenter un compte à rebours pour chaque quiz.

[ ] Ajouter des tests unitaires dans tests.py.