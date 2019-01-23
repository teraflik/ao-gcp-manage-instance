import os

def auth(key_path):
    KEY_PATH = key_path
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = KEY_PATH