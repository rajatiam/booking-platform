import csv, hashlib, io, json, math, re
from datetime import datetime, timezone
from urllib.request import Request, urlopen
from .validation import validate_input, http_url, unique

def now(): return datetime.now(timezone.utc).isoformat()
def validate(data,records): return initialize(validate_input(data,CONFIG['example']),records)

def initialize(row,records):
    try: start=datetime.fromisoformat(row['start']); end=datetime.fromisoformat(row['end'])
    except ValueError: raise ValueError('Use local ISO timestamps')
    if start.tzinfo or end.tzinfo: raise ValueError('Use local times without timezone offsets')
    if end<=start: raise ValueError('End must follow start')
    for existing in records:
        if existing['resource']==row['resource'] and start<datetime.fromisoformat(existing['end']) and end>datetime.fromisoformat(existing['start']): raise ValueError('Resource already booked during this interval')
    return row
def summary(rows): return {'bookings':len(rows),'resources':len({r['resource'] for r in rows})}
def transition(row,action): raise ValueError('Reservations are immutable; archive and create a replacement')
