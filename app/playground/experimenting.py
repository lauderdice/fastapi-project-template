"""
File for trying stuff and experimenting with code, usually in .gitignore in production
"""
import string
from app.common.helpers import get_random_string

[print(i,letter,get_random_string()) for i, letter in enumerate(string.ascii_uppercase)]
