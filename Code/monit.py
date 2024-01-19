import json
import os
import psutil
import logging
from datetime import datetime
from typing import Dict

# Remplacez "moniteur_de_ressources" par le nom réel de votre programme
Monitoring = "moniteur_de_ressources"

# Répertoires dans le répertoire personnel de l'utilisateur
LOG_DIR = f'~/{Monitoring}/var/log/'
DATA_DIR = f'~/{Monitoring}/var/monit/'

# Assurez-vous que les répertoires existent
for directory in [LOG_DIR, DATA_DIR]:
    if not os.path.exists(directory):
        os.makedirs(directory)

# Définir le chemin complet des répertoires
LOG_DIR = os.path.expanduser(LOG_DIR)
DATA_DIR = os.path.expanduser(DATA_DIR)

# Configurer le logger
logging.basicConfig(filename=os.path.join(LOG_DIR, 'monit.log'), level=logging.INFO)

def log_command(command):
    logging.info(f"Command '{command}' called at {datetime.now()}")

def save_report(report: Dict):
    report_file = os.path.join(DATA_DIR, f'report_{report["id"]}.json')
    with open(report_file, 'w') as file:
        json.dump(report, file)

def check():
    log_command('monit.py check')

    # Exemple de collecte de données
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    cpu_usage = psutil.cpu_percent()

    # Vérifier les ports TCP
    tcp_ports = config.get('tcp_ports', [])
    open_ports = [port for port in tcp_ports if is_port_open(port)]

    # Enregistrer le rapport
    report = {
        'id': str(datetime.now().timestamp()),
        'date': str(datetime.now()),
        'ram_usage': ram_usage,
        'disk_usage': disk_usage,
        'cpu_usage': cpu_usage,
        'open_ports': open_ports
    }

    save_report(report)

def list_reports():
    log_command('monit.py list')

    # Afficher la liste des rapports
    reports = [file for file in os.listdir(DATA_DIR) if file.startswith('report_')]
    print("List of reports:")
    for report_file in reports:
        print(report_file)

def get_last_report():
    log_command('monit.py get last')

    # Obtenir le dernier rapport
    reports = [file for file in os.listdir(DATA_DIR) if file.startswith('report_')]
    if reports:
        last_report_file = max(reports)
        with open(os.path.join(DATA_DIR, last_report_file), 'r') as file:
            last_report = json.load(file)
            print("Last report:")
            print(json.dumps(last_report, indent=2))
    else:
        print("No reports available.")

# Ajoutez d'autres fonctions comme get_avg, etc.

def is_port_open(port):
    # Logique pour vérifier si le port est ouvert
    # Vous devez implémenter cette fonction en fonction de vos besoins.
    return True

if __name__ == "__main__":
    # Exemple d'utilisation des fonctions
    check()
    list_reports()
    get_last_report()
