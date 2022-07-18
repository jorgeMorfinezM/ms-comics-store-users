'''Intention: Start mongodb engine'''
from __future__ import annotations

from config import MONGO_CLUSTER_CONN
from src.adapters.persistence.mongo import MongoDatabaseSession
from src.adapters.persistence.utils import singleton


@singleton
def start_engine():
    '''Initialize unique mongo session'''

    db_environment = MongoDatabaseSession(MONGO_CLUSTER_CONN)
    db_environment.connect()
    session = db_environment.get_session()
    return session
