"""
pip install apscheduler
"""
# will allow the database to fill tables with lower granularity
from datetime import datetime
import os

from apscheduler.schedulers.background import BackgroundScheduler


def BDD AGREG():
    

if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(tick, 'interval', minutes=10)
    print('woof'.format('Break' if os.name == 'nt' else 'C'))

scheduler.start()
