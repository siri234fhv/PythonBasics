#Program for Removing the File name
import os
try:
    os.remove("C:\\HYD\\python1")
    print("File Name removed")
except FileNotFoundError:
    print("File does not exist")