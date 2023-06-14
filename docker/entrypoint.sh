#!/bin/bash

set -e

case $1 in

    run-devel)
        echo "→ Running as development mode"
        DEBUGPY="${DEBUGPY:-false}"
        exec bash -c 'if [ "${DEBUGPY}" == "True" ]; then python -u -m debugpy --listen 0.0.0.0:5678 -m uvicorn application.asgi:app --host 0.0.0.0 --port 80 --reload --log-config logging.dev.yaml; else uvicorn application.asgi:app --host 0.0.0.0 --port 80 --reload --log-config logging.dev.yaml; fi'
        ;;

    run)
        echo "→ Running as prod mode"
        exec ddtrace-run uvicorn application.asgi:app --host 0.0.0.0 --port 80 --workers 3 --log-config logging.yaml
        ;;

    *)
        exec "$@"
        ;;
esac
