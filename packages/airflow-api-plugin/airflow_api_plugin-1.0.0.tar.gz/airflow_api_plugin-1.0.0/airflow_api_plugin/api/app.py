from flask import Blueprint

import airflow_api_plugin.utils as utils

# setup blueprint
blueprint = Blueprint("airflow_api", __name__, url_prefix=utils.get_api_endpoint())

# setup api
from airflow_api_plugin.api import api_setup
