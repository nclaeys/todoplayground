from flask import Flask
import os

file_path = os.path.abspath(os.getcwd()) + "/todo.db"

app = Flask(__name__)

