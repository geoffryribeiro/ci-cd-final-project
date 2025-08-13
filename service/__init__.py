"""
Service Package
"""
from flask import Flask

app = Flask(__name__)

# These must be imported after the Flask app is created
from service import routes  # pylint: disable=wrong-import-position, cyclic-import
from service.common import log_handlers  # pylint: disable=wrong-import-position

log_handlers.init_logging(app, "gunicorn.error")

separator = "*" * 70
status_message = "  S E R V I C E   R U N N I N G  ".center(70, "*")

app.logger.info(separator)
app.logger.info(status_message)
app.logger.info(separator)
