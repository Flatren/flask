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
          port=os.environ["PORT"])


if __name__ == '__main__':
    app_flask .run(debug=True, port=os.getenv("PORT", default=5000))
