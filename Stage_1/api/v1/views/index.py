#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort
from api.v1.views import app_views
from datetime import datetime, timedelta
import random


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """ GET /api/v1/status
    Return:
      - the status of the API
    """
    return jsonify({"status": "OK"})


@app_views.route('/<slack_name>/<track>', methods=['GET'], strict_slashes=False)
def stats(slack_name, track) -> str:
    """ GET /api/v1/stats
    Return:
      - the parameters of the user and track
    """
    
    name = slack_name
    day = datetime.now().strftime("%A")
    # day = Day.day
    time = datetime.utcnow()
#    window = random.randint(-120, 120)
#    current_time = time + timedelta(seconds=window)
    current_time = time.strftime('%Y-%m-%dT%H:%M:%SZ')
    Track = track
    github_url_file = 'https://github.com/phurhard/HNGx/blob/main/Stage_1/api/v1/views/index.py'
    github_url_repo = 'https://github.com/phurhard/HNGx/tree/main'
    status_code = 200
    stats = {'slack_name': name, 'current_day':day, 'utc_time': current_time, 'track': Track, 'github_file_url':github_url_file, 'github_repo_url':github_url_repo, 'status_code': status_code}
    return jsonify(stats)
