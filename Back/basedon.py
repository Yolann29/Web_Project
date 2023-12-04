import os, django, subprocess
from django.contrib.auth.hashers import make_password
color = '\033[92m'

command = "python3 manage.py flush"
user_input = "yes"

try:
    # Exécute la commande avec une entrée utilisateur simulée
    completed_process = subprocess.run(
        command,
        input=user_input,  # Encode l'entrée utilisateur en bytes
        shell=True,
        text=True,  # Spécifie que l'entrée et la sortie sont des chaînes de texte
        check=True
    )

    # Affiche la sortie de la commande
    print("Toutes les tables ont été vidées !")
except subprocess.CalledProcessError as e:
    print(f"Erreur lors de l'exécution de la commande : {e}")


#########################
# Populate the database #
#########################
os.environ['DJANGO_SETTINGS_MODULE'] = 'Back.settings'

django.setup()

from django.contrib.auth.models import User
# Créez un super utilisateur
User.objects.create_superuser(
    username='ADMIN',
    email='victor.morellet@epitech.eu',
    password='ADMIN31'
)
print(color + "Superuser created !")

from utilisateur.models import cmp, advertisement, JobApplication, companies, permissions

#Insert new rows in the table permissions

# New rows :

permissions.objects.create(name="Admin") #id = 1
permissions.objects.create(name="User") #id = 2
permissions.objects.create(name="Superadmin") #id = 3
print(color + "Success creating new objects in companies !")

#Insert new rows in the table companies

# New rows :

companies.objects.create(name="No Companies") #id = 1
companies.objects.create(name="CAPGEMINI") #id = 2
companies.objects.create(name="TALAN") #id = 3
companies.objects.create(name="LYRA") #id = 4
companies.objects.create(name="CGX AERO") #id = 5
print(color + "Success creating new objects in companies !")

#Insert new rows in the table cmp

# New rows :

cmp.objects.create(first_name="Victor", surname="Morellet", username="Yolann", password="Ardwina29!", permissions_id=3, email="victor.morellet@epitech.eu",) #id = 1
cmp.objects.create(first_name="Andrew", surname="Smith", username="Andrew31", password="user", email="andrew.smith@gmail.com",) #id = 2
cmp.objects.create(first_name="Simon", surname="Marton", username="Simon", password="simon", email="simon.marton@yahoo.fr",) #id = 3
cmp.objects.create(first_name="Monique", surname="Durand", username="Monique", password="29091970", email="monique.durand@mail.com",) #id = 4
cmp.objects.create(first_name="Anaïs", surname="Dulac", username="AnaïsDulac", password="Montesquieu300", email="anaïs.dulac@mail.com",) #id = 5
cmp.objects.create(first_name="Marie", surname="Algans", username="Marie", password="HYuidh!LOI9", email="marie.algans@cloud.com",) #id = 6
cmp.objects.create(first_name="Maëlys", surname="Leroy", username="Maëlys", password="1234", permissions_id=1, companies_id=2, email="maëlys.leroy@mail.com",) #id = 7
cmp.objects.create(first_name="Sarah", surname="Wandeu", username="SW", password="mmmmmmm", permissions_id=1, companies_id=3, email="sarah.wandeu@toulouse.com",) #id = 8
cmp.objects.create(first_name="Luc", surname="Vidal", username="Luc000", password="admin", permissions_id=1, companies_id=4, email="luc.vidal@mail.com",) #id = 9
cmp.objects.create(first_name="Emma", surname="Louis", username="EmmaL", password="em456Lou", permissions_id=1, companies_id=5, email="emma.louis@mail.fr",) #id = 10
cmp.objects.create(first_name="Superadmin", surname="Superadmin", username="admin", password="admin", permissions_id=3, email="admin@epitech.eu",) #id = 11
cmp.objects.create(first_name="Xavier", surname="Cannere", username="Xav65", password="Epitech31", permissions_id=3, email="xavier.cannere@epitech.eu",) #id = 12
print(color + "Success creating new objects in cmp !")

#New rows for advertisement :

advertisement.objects.create(cmp_id=7, companies_id=companies.objects.get(pk=2).id, title="Développeur DevOps", description="En tant que développeur DevOps, vous ferez partie de notre équipe de développement et de gestion des opérations (DevOps) et jouerez un rôle clé dans la création, le déploiement et la maintenance de nos applications logicielles. Vous collaborerez étroitement avec les développeurs, les administrateurs système et les ingénieurs en sécurité pour automatiser les processus de développement et de déploiement, améliorer la stabilité des systèmes et accélérer la livraison de logiciels de haute qualité. Nous recherchons un développeur exceptionnel pour rejoindre notre équipe dynamique et innovante. En tant que membre clé de notre équipe de développement, vous serez chargé de concevoir, développer et déployer des solutions logicielles de pointe pour résoudre des problèmes complexes. Vous aurez l'opportunité de travailler sur une variété de projets stimulants, de la conception de nouvelles fonctionnalités à l'optimisation des systèmes existants. Vous serez constamment encouragé à repousser les limites de la technologie et à explorer de nouvelles approches pour résoudre les défis techniques. Votre rôle comprendra la collaboration étroite avec les équipes multidisciplinaires pour comprendre les besoins des clients et concevoir des applications qui offrent une expérience utilisateur exceptionnelle. Vous serez responsable de l'écriture de code propre, efficace et bien documenté, tout en veillant à ce que les normes de qualité et de performance soient respectées. En tant que développeur, vous serez encouragé à rester à jour avec les dernières avancées technologiques et à participer activement à la recherche et au développement de nouvelles solutions. Vous aurez également l'occasion de contribuer à l'amélioration continue de nos processus de développement. Si vous êtes passionné par la programmation, curieux, créatif et que vous avez un désir ardent de repousser les limites du possible, alors vous pourriez être le candidat idéal pour rejoindre notre équipe. Rejoignez-nous pour faire partie d'une aventure passionnante, où l'innovation est au cœur de notre culture d'entreprise et où vous aurez la possibilité de laisser votre empreinte dans le monde de la technologie.") #id = 1
advertisement.objects.create(cmp_id=8, companies_id=companies.objects.get(pk=3).id, title="Développeur Logiciel", description=" En tant que développeur logiciel au sein de notre entreprise fictive, vous jouerez un rôle essentiel dans la conception, le développement et la maintenance de nos applications logicielles. Vous collaborerez avec une équipe de développement dynamique pour créer des solutions logicielles de haute qualité répondant aux besoins de nos clients. Nous recherchons un développeur exceptionnel pour rejoindre notre équipe dynamique et innovante. En tant que membre clé de notre équipe de développement, vous serez chargé de concevoir, développer et déployer des solutions logicielles de pointe pour résoudre des problèmes complexes. Vous aurez l'opportunité de travailler sur une variété de projets stimulants, de la conception de nouvelles fonctionnalités à l'optimisation des systèmes existants. Vous serez constamment encouragé à repousser les limites de la technologie et à explorer de nouvelles approches pour résoudre les défis techniques. Votre rôle comprendra la collaboration étroite avec les équipes multidisciplinaires pour comprendre les besoins des clients et concevoir des applications qui offrent une expérience utilisateur exceptionnelle. Vous serez responsable de l'écriture de code propre, efficace et bien documenté, tout en veillant à ce que les normes de qualité et de performance soient respectées. En tant que développeur, vous serez encouragé à rester à jour avec les dernières avancées technologiques et à participer activement à la recherche et au développement de nouvelles solutions. Vous aurez également l'occasion de contribuer à l'amélioration continue de nos processus de développement. Si vous êtes passionné par la programmation, curieux, créatif et que vous avez un désir ardent de repousser les limites du possible, alors vous pourriez être le candidat idéal pour rejoindre notre équipe. Rejoignez-nous pour faire partie d'une aventure passionnante, où l'innovation est au cœur de notre culture d'entreprise et où vous aurez la possibilité de laisser votre empreinte dans le monde de la technologie.") #id = 2
advertisement.objects.create(cmp_id=9, companies_id=companies.objects.get(pk=4).id, title="Développeur Web", description = "Nous recherchons un développeur web talentueux pour rejoindre notre équipe. Vous serez chargé de concevoir et de mettre en œuvre des applications web innovantes, de la conception de l'interface utilisateur à la gestion de la base de données. Si vous êtes passionné par le développement web, que vous maîtrisez les dernières technologies et que vous êtes prêt à relever des défis techniques, nous aimerions vous avoir dans notre équipe. Nous recherchons un développeur exceptionnel pour rejoindre notre équipe dynamique et innovante. En tant que membre clé de notre équipe de développement, vous serez chargé de concevoir, développer et déployer des solutions logicielles de pointe pour résoudre des problèmes complexes. Vous aurez l'opportunité de travailler sur une variété de projets stimulants, de la conception de nouvelles fonctionnalités à l'optimisation des systèmes existants. Vous serez constamment encouragé à repousser les limites de la technologie et à explorer de nouvelles approches pour résoudre les défis techniques. Votre rôle comprendra la collaboration étroite avec les équipes multidisciplinaires pour comprendre les besoins des clients et concevoir des applications qui offrent une expérience utilisateur exceptionnelle. Vous serez responsable de l'écriture de code propre, efficace et bien documenté, tout en veillant à ce que les normes de qualité et de performance soient respectées. En tant que développeur, vous serez encouragé à rester à jour avec les dernières avancées technologiques et à participer activement à la recherche et au développement de nouvelles solutions. Vous aurez également l'occasion de contribuer à l'amélioration continue de nos processus de développement. Si vous êtes passionné par la programmation, curieux, créatif et que vous avez un désir ardent de repousser les limites du possible, alors vous pourriez être le candidat idéal pour rejoindre notre équipe. Rejoignez-nous pour faire partie d'une aventure passionnante, où l'innovation est au cœur de notre culture d'entreprise et où vous aurez la possibilité de laisser votre empreinte dans le monde de la technologie.") #id = 3
advertisement.objects.create(cmp_id=10, companies_id=companies.objects.get(pk=5).id, title="Développeur Web", description = "Nous recherchons un développeur web talentueux pour rejoindre notre équipe. Vous serez chargé de concevoir et de mettre en œuvre des applications web innovantes, de la conception de l'interface utilisateur à la gestion de la base de données. Si vous êtes passionné par le développement web, que vous maîtrisez les dernières technologies et que vous êtes prêt à relever des défis techniques, nous aimerions vous avoir dans notre équipe. Nous recherchons un développeur exceptionnel pour rejoindre notre équipe dynamique et innovante. En tant que membre clé de notre équipe de développement, vous serez chargé de concevoir, développer et déployer des solutions logicielles de pointe pour résoudre des problèmes complexes. Vous aurez l'opportunité de travailler sur une variété de projets stimulants, de la conception de nouvelles fonctionnalités à l'optimisation des systèmes existants. Vous serez constamment encouragé à repousser les limites de la technologie et à explorer de nouvelles approches pour résoudre les défis techniques. Votre rôle comprendra la collaboration étroite avec les équipes multidisciplinaires pour comprendre les besoins des clients et concevoir des applications qui offrent une expérience utilisateur exceptionnelle. Vous serez responsable de l'écriture de code propre, efficace et bien documenté, tout en veillant à ce que les normes de qualité et de performance soient respectées. En tant que développeur, vous serez encouragé à rester à jour avec les dernières avancées technologiques et à participer activement à la recherche et au développement de nouvelles solutions. Vous aurez également l'occasion de contribuer à l'amélioration continue de nos processus de développement. Si vous êtes passionné par la programmation, curieux, créatif et que vous avez un désir ardent de repousser les limites du possible, alors vous pourriez être le candidat idéal pour rejoindre notre équipe. Rejoignez-nous pour faire partie d'une aventure passionnante, où l'innovation est au cœur de notre culture d'entreprise et où vous aurez la possibilité de laisser votre empreinte dans le monde de la technologie.") #id = 4
print(color + "Success creating new objects in advertisement !")

#New rows for JobApplication :

JobApplication.objects.create(applicant_id=cmp.objects.get(pk=2).id, advert_id=advertisement.objects.get(id=1).id, first_name=cmp.objects.get(pk=2).first_name, surname=cmp.objects.get(pk=2).surname, email=cmp.objects.get(pk=2).email) #id = 1
JobApplication.objects.create(applicant_id=cmp.objects.get(pk=3).id, advert_id=advertisement.objects.get(id=2).id, first_name=cmp.objects.get(pk=3).first_name, surname=cmp.objects.get(pk=3).surname, email=cmp.objects.get(pk=3).email) #id = 2
JobApplication.objects.create(applicant_id=cmp.objects.get(pk=3).id, advert_id=advertisement.objects.get(id=3).id, first_name=cmp.objects.get(pk=3).first_name, surname=cmp.objects.get(pk=3).surname, email=cmp.objects.get(pk=3).email) #id = 3
JobApplication.objects.create(applicant_id=cmp.objects.get(pk=4).id, advert_id=advertisement.objects.get(id=1).id, first_name=cmp.objects.get(pk=4).first_name, surname=cmp.objects.get(pk=4).surname, email=cmp.objects.get(pk=4).email) #id = 4
JobApplication.objects.create(applicant_id=cmp.objects.get(pk=4).id, advert_id=advertisement.objects.get(id=1).id, first_name=cmp.objects.get(pk=4).first_name, surname=cmp.objects.get(pk=4).surname, email=cmp.objects.get(pk=4).email) #id = 5
JobApplication.objects.create(applicant_id=cmp.objects.get(pk=4).id, advert_id=advertisement.objects.get(id=2).id, first_name=cmp.objects.get(pk=4).first_name, surname=cmp.objects.get(pk=4).surname, email=cmp.objects.get(pk=4).email) #id = 6
JobApplication.objects.create(applicant_id=cmp.objects.get(pk=5).id, advert_id=advertisement.objects.get(id=1).id, first_name=cmp.objects.get(pk=5).first_name, surname=cmp.objects.get(pk=5).surname, email=cmp.objects.get(pk=5).email) #id = 7
JobApplication.objects.create(applicant_id=cmp.objects.get(pk=5).id, advert_id=advertisement.objects.get(id=2).id, first_name=cmp.objects.get(pk=5).first_name, surname=cmp.objects.get(pk=5).surname, email=cmp.objects.get(pk=5).email) #id = 8
JobApplication.objects.create(applicant_id=cmp.objects.get(pk=5).id, advert_id=advertisement.objects.get(id=3).id, first_name=cmp.objects.get(pk=5).first_name, surname=cmp.objects.get(pk=5).surname, email=cmp.objects.get(pk=5).email) #id = 9
print(color + "Success creating new objects in JobApplication !")
