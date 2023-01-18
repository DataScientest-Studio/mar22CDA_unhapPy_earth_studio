# mar22CDA_unhapPy_earth_studio

Projet MAR22CDA - Earth Temperature

**Nom du projet:** UnhapPy_Earth

## Déploiement d'un projet sur le Studio

Une API permettant de déployer automatiquement des projets sur le studio a été développée par l'équipe DEV.

### **Ce qu'elle fait :**

* elle clone le repo du projet que tu lui donnes
* elle installe les requirements dans un venv
* elle te donne la possibilité de démarrer/arrêter le service du projet, de voir son status et de supprimer entièrement le projet

### Les prérequis pour que ça fonctionne:

3 conditions :

* :⚠️: **le repo doit être passé en PUBLIC** :⚠️:
* les requirements dans `requirements.txt` à la racine du repo
* Le fichier principal doit se nommer `app.py` ET **être situé à la racine du repo**

Exemple du repo actuel:

```
.
├── app.py
├── assets
│   ├── CO2.jpg
│   ├── earth_2.gif
│   ├── github-logo.png
│   ├── Global_Warming.jpg
│   ├── linkedin-logo-black.png
│   ├── linkedin-logo.png
│   ├── logo-datascientest.png
│   ├── rechauffement-climatique-illustration.webp
│   ├── Reftinsky_reservoir_of_Sverdlovsk_region.jpg
│   ├── sample-image.jpg
│   ├── starving_polar_bear.jpg
│   ├── station_meteo.jpg
│   ├── Unhappy_earth2.jpg
│   ├── Unhappy_earth.jpg
│   └── Unhappy_earth.png
├── config.py
├── data
│   ├── berkeley_earth
│   │   ├── Complete_TAVG_complete.txt
│   │   ├── data_all_countries.csv
│   │   └── Sets_by_hemisphere
│   │       ├── northern-hemisphere-TAVG-Trend.txt
│   │       └── southern-hemisphere-TAVG-Trend.txt
│   ├── co2
│   │   ├── global-co2-fossil-plus-land-use.csv
│   │   └── owid-co2-data.csv
│   └── unhappy_earth
│       ├── co2_countries.csv
│       ├── co2_global.csv
│       ├── temperatures_countries.csv
│       ├── temperatures_globales.csv
│       └── temperatures_hemispheres.csv
├── member.py
├── README.md
├── requirements.txt
├── structure_repo.txt
├── style.css
└── tabs
    ├── conclusion.py
    ├── correlation.py
    ├── donnees.py
    ├── existence.py
    ├── intro.py
    ├── prediction.py
```

### **Les appels et étapes de déploiement sur studio :**

consulter la documentation en interne pour laprcédure de déploiement
