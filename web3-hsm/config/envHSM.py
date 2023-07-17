import os
from dotenv import load_dotenv
load_dotenv();
def Config(name :str):
    return os.getenv(name);