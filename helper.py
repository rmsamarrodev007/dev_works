import sqlite3 
import configparser
import csv

CONFIG = configparser.ConfigParser()
CONFIG.read('config.ini')

def get_connection():
    connection = sqlite3.connect(CONFIG['SQLITE_CONFIG']['database']) 
    return connection

def generate_csv(columns,rows):
    with open(CONFIG['SQLITE_CONFIG']['sql_csv_filename'], 'w', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(columns)
        writer.writerows(rows)
