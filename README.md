
# Projet API Django - Gestion des Trades

## Description du Projet

Ce projet est une **API Django REST** permettant de gérer un inventaire de Trades. Il fournit une interface permettant de manipuler les données des Trades via des requêtes HTTP telles que **GET**, **POST**, **PUT**, **PATCH**, et **DELETE**. L'API est conçue pour offrir une gestion facile des Trades dans une base de données, avec des fonctionnalités permettant d'ajouter, consulter, mettre à jour et supprimer des Trades.

### Objectif du projet
L'objectif de ce projet est de créer une **API RESTful** capable de gérer une base de données de Trading. Chaque trade dispose des champs suivants :
- **Asset** : Nom du produit (string)
- **Price** : Description détaillée du produit (string)
- **Quantity** : Prix du produit (float)

Cette API peut être utilisée pour une application de commerce électronique, une gestion d'inventaire ou tout autre type d'application nécessitant la gestion d'une liste de produits.

### Fonctionnalités
- **CRUD (Create, Read, Update, Delete)** : Les utilisateurs peuvent créer de nouveaux produits, les lire, les mettre à jour ou les supprimer.
- **Autres fonctionnalités** : 
  - Validation des entrées via des sérialiseurs pour garantir l'intégrité des données.
  - Sécurisation de l'API avec des mécanismes d'authentification (le cas échéant).
  - Pagination des résultats pour les appels `GET` afin de gérer les grandes listes de produits.

## Technologies utilisées

Ce projet utilise les technologies suivantes :
- **Django** : Framework web Python pour la création de l'API.
- **Django Rest Framework** : Pour la gestion des API RESTful et la sérialisation des données.
- **SQLite** : Base de données légère, idéale pour les petites applications ou le développement.
- **Conda** : Gestion de l'environnement virtuel et des dépendances.
- **Postman** : Outil de test des API.

## Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants installés sur votre machine :
- **Python 3.8+**
- **Conda** (pour la gestion des environnements virtuels, recommandé pour l'isolation des dépendances).
