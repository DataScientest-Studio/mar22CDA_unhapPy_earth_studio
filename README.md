# deploy_streamlit_on_studio

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

1. Cloner le projet et installer les requirements :

```
curl -X POST -H 'Content-Type: application/json' -i 'http://studio.datascientest.com:8899/project' --data '{"id": "NOM_DU_PROJET","repo": "https://github.com/DataScientest-Studio/NOM_DU_PROJET.git"}'
```

2. Démarrer le service :

```
curl -X PUT -i "http://studio.datascientest.com:8899/project/NOM_DU_PROJET/start"
```

3. Obtenir le status :

```
curl -X GET -i "http://studio.datascientest.com:8899/project/NOM_DU_PROJET/status"
```

**Une fois démarré, il est accessible via [https://studio.datascientest.com/project/NOM_DU_PROJET](https://studio.datascientest.com/project/NOM_DU_PROJET "https://studio.datascientest.com/project/NOM_DU_PROJET")**

### **Les étapes optionnelles (si besoin)):**

1. Arrêter le service (OPTIONNEL si besoin) :

```
curl -X PUT -i "http://studio.datascientest.com:8899/project/NOM_DU_PROJET/stop"
```

2. Le supprimer :

```
curl -X DELETE -i "http://studio.datascientest.com:8899/project/NOM_DU_PROJET"
```

### **Limitations :**

* Le git clone et l'installation des requirements peuvent prendre du temps. C'est normal si l'appel prend du temps à aboutir.
* Python 3.6. L'upgrade risque de casser tous les autres projets installés.
* Corollaire du point précédent : certaines dépendances dans le requirements.txt risquent de ne pas être satisfaites.
