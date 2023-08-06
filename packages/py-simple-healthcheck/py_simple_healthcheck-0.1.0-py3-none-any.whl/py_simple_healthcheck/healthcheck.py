from time import time

class UnhealthyException(Exception):
    pass

def health_check(timeout):
    with open('healthcheck', 'w+') as file:
        file.write(f'{str(int(time()))},{str(timeout)}')

def is_healthy():
    try:
        with open('healthcheck', 'r') as file:
            content = file.read()
            timestamp, timeout = content.split(',')
            if time() > int(timestamp) + int(timeout):
                raise UnhealthyException()
    
    except FileNotFoundError as e:
        print('Healthcheck file not found', flush=True)
