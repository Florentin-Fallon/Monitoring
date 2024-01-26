#!/usr/bin/env python3

import json
import os
import psutil
import logging
from datetime import datetime, timedelta
import socket
import time

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

def save_report(report):
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
    reports = [f for f in os.listdir(DATA_DIR) if f.startswith(REPORT_FILE_PREFIX)]
    return reports

def get_last_report():
    reports = list_reports()
    if reports:
        latest_report = max(reports)
        with open(os.path.join(DATA_DIR, latest_report)) as report_file:
            last_report = json.load(report_file)
        return last_report
    else:
        return None

def get_average_values(last_x_hours):
    reports = list_reports()
    relevant_reports = [r for r in reports if datetime.now() - datetime.fromtimestamp(int(r.split('_')[1].split('.')[0])) < timedelta(hours=last_x_hours)]
    
    if relevant_reports:
        total_values = {'ram_usage': 0, 'disk_usage': 0, 'cpu_usage': 0}
        total_reports = len(relevant_reports)
        
        for report in relevant_reports:
            with open(os.path.join(DATA_DIR, report)) as report_file:
                report_data = json.load(report_file)
            total_values['ram_usage'] += report_data['ram_usage']
            total_values['disk_usage'] += report_data['disk_usage']
            total_values['cpu_usage'] += report_data['cpu_usage']
        
        avg_values = {key: total_values[key] / total_reports for key in total_values}
        return avg_values
    else:
        return None

def is_port_open(port):
    try:
        socket.create_connection(("localhost", port), timeout=1)
        return True
    except (socket.timeout, ConnectionRefusedError):
        return False

if __name__ == "__main__":
    setup_directories()
    setup_logging()
    
    log_command('monit.py check')
    check()
    
    reports_list = list_reports()
    print("List of reports:")
    for report in reports_list:
        print(f'- {report}')

    last_report = get_last_report()
    print("\nLast report:")
    if last_report:
        for key, value in last_report.items():
            print(f'{key}: {value}')

    avg_values_last_24_hours = get_average_values(24)
    print("\nAverages for the last 24 hours:")
    if avg_values_last_24_hours:
        for key, value in avg_values_last_24_hours.items():
            print(f'{key}: {value}')
    
    logging.info(f"monit.py ended at {datetime.now()}")

