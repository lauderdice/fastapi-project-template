"""
File for storing enums used throughout the project
"""
import enum

class Environment(enum.Enum):
    Development = "development"
    Production = "production"
    Beta = "beta"
    Local = "local"

class SampleCarEnum(str, enum.Enum):
    BMW = "bmw"
    Mercedes = "mercedes"
