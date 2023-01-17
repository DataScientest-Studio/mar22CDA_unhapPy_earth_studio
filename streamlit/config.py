"""

Config file for Streamlit App

"""

from member import Member


TITLE = "UnhapPy Earth"

TEAM_MEMBERS = [
    Member(name = "Olga Fedorova", 
           linkedin_url = "https://www.linkedin.com/in/olga-fedorova-665a4b63/", 
           github_url = "https://github.com/OlgaFedorovaKukk"),
    Member(name = "Boris Baldassari", 
           linkedin_url = "https://www.linkedin.com/in/borisbaldassari/", 
           github_url = "https://github.com/borisbaldassari"),
    Member(name = "Nicolas Cristiano", 
           linkedin_url="https://www.linkedin.com/in/nicolas-cristiano-7b8a23171/", 
           github_url="https://github.com/Nic0C")]

PROMOTION = "Promotion Continue Data Analyst - Mars 2022"

# liste de fichiers
globales_file = '../data/unhappy_earth/temperatures_globales.csv'
hemispheres_file = '../data/unhappy_earth/temperatures_hemispheres.csv'
countries_file = '../data/unhappy_earth/temperatures_countries.csv'

co2_global = '../data/unhappy_earth/co2_global.csv'
co2_countries = '../data/unhappy_earth/co2_countries.csv'

temperatures_globales_file = '../data/unhappy_earth/temperatures_globales.csv'
temperatures_hemispheres_file = '../data/unhappy_earth/temperatures_hemispheres.csv'
temperatures_countries_file = '../data/unhappy_earth/temperatures_countries.csv'
