"""
File for storing various helper functions used throughout all other project modules
"""
from typing import List
import requests, random
from requests import Response
import app.common.constants as C

def get_random_string() -> str:
    try:
        word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
        response: Response = requests.get(word_site)
        word_list: List[bytes] = response.content.splitlines()
        return str(random.choice(word_list).decode("UTF-8")) + str(random.randint(1, 10000))
    except:
        return "RandomWord" + str(random.randint(1, 10000))

def is_apikey_valid(apikey: str) -> bool:
    if apikey == C.CORRECT_APIKEY:
        return True
    return False



