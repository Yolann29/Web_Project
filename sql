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
CREATE TABLE Companies(
   Id_Companies SERIAL,
   Name VARCHAR(50) NOT NULL,
   PRIMARY KEY(Id_Companies)
);

CREATE TABLE Advertisements(
   Id_Advertisements SERIAL,
   Id_Companies INT NOT NULL,
   PRIMARY KEY(Id_Advertisements),
   FOREIGN KEY(Id_Companies) REFERENCES Companies(Id_Companies)
);

CREATE TABLE Permissions(
   Id_Permissions SERIAL,
   Name VARCHAR(50),
   PRIMARY KEY(Id_Permissions)
);

CREATE TABLE Users(
   Id_Users SERIAL,
   Surname VARCHAR(50) NOT NULL,
   First_name VARCHAR(50) NOT NULL,
   Id_Permissions INT NOT NULL,
   Id_Companies INT,
   PRIMARY KEY(Id_Users),
   FOREIGN KEY(Id_Permissions) REFERENCES Permissions(Id_Permissions),
   FOREIGN KEY(Id_Companies) REFERENCES Companies(Id_Companies)
);

CREATE TABLE Job_Application(
   Id_Job_Application SERIAL,
   Id_Advertisements INT NOT NULL,
   Id_Users INT NOT NULL,
   PRIMARY KEY(Id_Job_Application),
   FOREIGN KEY(Id_Advertisements) REFERENCES Advertisements(Id_Advertisements),
   FOREIGN KEY(Id_Users) REFERENCES Users(Id_Users)
);


---------------------------------------------------------------------------
