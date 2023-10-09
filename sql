POSTGRES

Installation :
sudo apt update
sudo apt install postgresql postgresql-contrib

Lancement de postgres :
sudo service postgresql start
sudo -i -u postgres
psql (accès menu général)
psql bdd (accès a la bdd "bdd")

Lister les bdd > \l
Se connecter a une bdd > \c jobboardbdd

Créer la base de données (une fois postgres lancé) :
CREATE DATABASE jobboardbdd;

Créer les tables (une fois dans la bdd) :



---------------------------------------------------------------------------
