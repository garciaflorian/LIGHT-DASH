"""
pip install apscheduler
"""
# will allow the database to fill tables with lower granularity
from datetime import datetime
import os

from apscheduler.schedulers.background import BackgroundScheduler

# from .models import 

def Bdd10Min():
    
def BddHour():
    
def BddDay():
    
def BddWeek():
    
def BddMonth():
    
if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(Bdd10min, 'interval', minutes=10)
    scheduler.add_job(BddHour, 'interval', minutes=60)
    scheduler.add_job(BddDay, 'interval', minutes=1440)
    scheduler.add_job(BddWeek, 'interval', minutes=10080)
    scheduler.add_job(BddMonth 'interval', minutes=43200)

scheduler.start()
