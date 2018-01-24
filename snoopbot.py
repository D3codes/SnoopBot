import praw
import sqlite3
import time
import snoopsnoo

USERNAME = 'snoop-bot'

print('Opening snoop-bot database')
sql = sqlite3.connect('snoop.db')
cur = sql.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS oldposts(ID TEXT)')
sql.commit()

def handle_ratelimit(func, *args, **kwargs):
    while True:
        try:
            func(*args, **kwargs)
            break
        except praw.errors.RateLimitExceeded as error:
            print('\tSleeping for %d seconds' % error.sleep_time)
            time.sleep(error.sleep_time)
