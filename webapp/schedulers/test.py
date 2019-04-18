"""
pip install apscheduler
"""
# donne l'heure toutes les secondes, c'est un test
from datetime import datetime
import os
# on prend un plannificateur qui tourne en fond (background) à l'opposé de bloquant (blocking)
from apscheduler.schedulers.background import BackgroundScheduler


def tick():
    print('il est : %s' % datetime.now())


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(tick, 'interval', seconds=1)
    #lance le plannificateur
    scheduler.start()
