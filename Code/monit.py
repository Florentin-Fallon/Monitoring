import json
import os
import psutil
import logging
import time
from datetime import datetime, timedelta
from typing import Dict

LOG_DIR = '/var/log/moniteur_de_ressources/'
DATA_DIR = '/var/monit/'
CONFIG_FILE_PATH = '/etc/monit/config.json'

# Constantes
LOG_FILE = 'monit.log'
COMMANDS_LOG_FILE = 'monit_commands.log'
REPORT_FILE_PREFIX = 'report_'

def load_config():
    if os.path.exists(CONFIG_FILE_PATH):
        with open(CONFIG_FILE_PATH, 'r') as config_file:
            return json.load(config_file)
    return {}

def setup_directories():
    for directory in [LOG_DIR, DATA_DIR]:
        if not os.path.exists(directory):
            os.makedirs(directory)

def setup_logging():
    logging.basicConfig(filename=os.path.join(LOG_DIR, LOG_FILE), level=logging.INFO)
    logging.info(f"monit.py started at {datetime.now()}")

def log_command(command):
    with open(os.path.join(DATA_DIR, COMMANDS_LOG_FILE), 'a') as log_file:
        log_file.write(f"{datetime.now()} - {command}\n")

def save_report(report: Dict):
    report_file_path = os.path.join(DATA_DIR, f'{REPORT_FILE_PREFIX}{report["id"]}.json')
    with open(report_file_path, 'w') as file:
        json.dump(report, file)

def check():
    log_command('monit.py check')

    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    cpu_usage = psutil.cpu_percent()

    tcp_ports = load_config().get('tcp_ports', [])
    open_ports = [port for port in tcp_ports if is_port_open(port)]

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
    reports = [f for f in os.listdir('/var/monit') if f.startswith('monit_report_')]
    return reports

def get_last_report():
    reports = list_reports()
    if reports:
        latest_report = max(reports)
        with open(f'/var/monit/{latest_report}') as report_file:
            last_report = json.load(report_file)
        return last_report
    else:
        return None

def get_average_values(last_x_hours):
    reports = list_reports()
    relevant_reports = [r for r in reports if datetime.now() - datetime.fromtimestamp(int(r.split('_')[2].split('.')[0])) < timedelta(hours=last_x_hours)]
    
    if relevant_reports:
        total_values = {'ram_usage': 0, 'disk_usage': 0, 'cpu_usage': 0}
        total_reports = len(relevant_reports)
        
        for report in relevant_reports:
            with open(f'/var/monit/{report}') as report_file:
                report_data = json.load(report_file)
            total_values['ram_usage'] += report_data['ram_usage']
            total_values['disk_usage'] += report_data['disk_usage']
            total_values['cpu_usage'] += report_data['cpu_usage']
        
        avg_values = {key: total_values[key] / total_reports for key in total_values}
        return avg_values
    else:
        return None
    
def load_all_reports():
    
    reports = []
    for file in os.listdir(DATA_DIR):
        if file.startswith('report_'):
            with open(os.path.join(DATA_DIR, file), 'r') as report_file:
                report = json.load(report_file)
                reports.append(report)
    return reports

def is_within_last_x_hours(report, x):
    
    report_time = datetime.strptime(report['date'], '%Y-%m-%d %H:%M:%S.%f')
    x_hours_ago = datetime.now() - timedelta(hours=x)
    return report_time >= x_hours_ago

def is_port_open(port):
    return True

time.sleep(60)

logging.info(f"monit.py ended at {datetime.now()}")

if __name__ == "__main__":
    log_command('monit.py check')
    check()
    reports_list = list_reports()
    print(f"List of reports: {reports_list}")
    last_report = get_last_report()
    print(f"Last report: {last_report}")
    avg_values_last_24_hours = get_average_values(24)
    print(f"Averages for the last 24 hours: {avg_values_last_24_hours}")
