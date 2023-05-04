import logging
import json
from flask import Flask
from app import App
import os
from app.controllers.get_link_controller import controller_api as get_link_controller
from app.controllers.get_short_link_controller import controller_api as get_short_link_controller
app_flask = Flask(__name__)

app = App(dbname=os.environ["DBNAME"],
          host=os.environ["HOST"],
          user=os.environ["USER"],
          password=os.environ["PASSWORD"],
          port=os.environ["DBPORT"])

app_flask.route("/api/get_short_link", methods=['POST'])(get_short_link_controller(app))
app_flask.route("/api/get_link", methods=['POST'])(get_link_controller(app))
app_flask.run(host='0.0.0.0', port=int(os.environ["PORT"]))
