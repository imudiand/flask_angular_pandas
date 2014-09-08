import os
import json
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False

import wise_io.controllers

