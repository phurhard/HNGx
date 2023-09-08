#!/usr/bin/python
from flask import Flask, jsonify, request, Blueprint
from os import getenv
from datetime import timedelta, datetime


app = Flask(__name__)
app_views = Blueprint("app_views", __name__, url_prefix="")
app.json.sort_keys = False


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """ GET /api/v1/status
    Return:
      - the status of the API
    """
    return jsonify({"status": "OK"})


@app_views.route('/api', methods=['GET'], strict_slashes=False)
def stats() -> str:
    """ GET /api/v1/stats
    Return:
      - the parameters of the user and track
    """

    name = request.args.get('slack_name')
    day = datetime.utcnow().strftime("%A")
    time = datetime.utcnow()
    current_time = time.strftime('%Y-%m-%dT%H:%M:%SZ')
    Track = request.args.get('track')
    github_url_file = 'https://github.com/
    phurhard/HNGx/blob/main/Stage_1/task1.py'
    github_url_repo = 'https://github.com/
    phurhard/HNGx/tree/main'
    status_code = 200
    stats = {'slack_name': name,
             'current_day': day,
             'utc_time': current_time,
             'track': Track,
             'github_file_url': github_url_file,
             'github_repo_url': github_url_repo,
             'status_code': status_code
             }
    return jsonify(stats)


app.register_blueprint(app_views)


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port, debug=1)
