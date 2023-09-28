#!/usr/bin/env python3

import connexion

from openapi_server import encoder


def main():
    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': 'API Flask Server for Anomaly Detection'},
                pythonic_params=True)

    app.run(port=3033, debug=True)


if __name__ == '__main__':
    main()
