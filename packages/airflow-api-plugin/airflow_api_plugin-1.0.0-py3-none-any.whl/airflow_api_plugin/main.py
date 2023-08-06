from airflow.plugins_manager import AirflowPlugin

import airflow_api_plugin.utils as utils
from airflow_api_plugin.api import app
import airflow_api_plugin.config as config

api_blueprint = app.blueprint


class AgguaApi(AirflowPlugin):
    name = config.PLUGIN_NAME
    operators = []
    hooks = []
    executors = []
    menu_links = []

    if utils.get_config_aggua_api_disabled():
        flask_blueprints = []
        appbuilder_views = []
    else:
        flask_blueprints = [api_blueprint]
        appbuilder_views = []
