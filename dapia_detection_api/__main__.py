#!/usr/bin/env python3

import connexion
from flask_cors import CORS

from dapia_detection_api import encoder


def main():
    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    CORS(app.app)
    app.add_api('openapi.yaml',
                arguments={'title': 'API Flask Server for Anomaly Detection'},
                pythonic_params=True)

    app.run(port=3033)


if __name__ == '__main__':
    main()
