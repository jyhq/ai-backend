#!/bin/bash
set -e

SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
PID_FILE="${PROJECT_BASE}/gun.pid"
GUNICORN_CMD="gunicorn -c ${APP_ROOT}/gunicorn.conf.py main:app"

init_app() {
    source "${SCRIPT_DIR}/init_project_env.sh"
}

check_process() {
    if [ -f "${PID_FILE}" ]; then
        local pid
        pid=$(cat "${PID_FILE}")
        if ps -p "${pid}" > /dev/null 2>&1; then
            echo "${pid}"
            return 0
        else
            rm -f "${PID_FILE}"
            return 1
        fi
    fi
    return 1
}

start_app() {
    echo "[INFO] Starting application..."

    if check_process >/dev/null; then
        echo "[ERROR] Application is already running (PID: $(check_process))"
        return 1
    fi

    nohup "${GUNICORN_CMD}" > "${PROJECT_BASE}"/log/boot.log 2>&1 &
    echo $! > "${PID_FILE}"
    sleep 3

    if check_process >/dev/null; then
        echo "[INFO] Application started successfully (PID: $(check_process))"
        return 0
    else
        echo "[ERROR] Failed to start application"
        return 1
    fi
}

stop_app() {
    echo "[INFO] Stopping application..."

    if ! check_process >/dev/null; then
        echo "[INFO] Application is not running"
        return 0
    fi

    local pid
    pid=$(check_process)
    kill -TERM "${pid}" 2>/dev/null
    sleep 5

    if ! check_process >/dev/null; then
        echo "[INFO] Application stopped gracefully"
        return 0
    fi

    echo "[WARNING] Force stopping application..."
    kill -9 "${pid}" 2>/dev/null
    sleep 2

    if ! check_process >/dev/null; then
        echo "[INFO] Application force stopped"
        return 0
    else
        echo "[ERROR] Failed to stop application (PID: ${pid})"
        return 1
    fi
}

status_app() {
    if check_process >/dev/null; then
        echo "[INFO] Application is running (PID: $(check_process))"
        return 0
    else
        echo "[INFO] Application is not running"
        return 1
    fi
}

case "$1" in
    init)
        init_app
        ;;
    start)
        init_app
        start_app
        ;;
    stop)
        init_app
        stop_app
        ;;
    restart)
        init_app
        stop_app
        start_app
        ;;
    status)
        init_app
        status_app
        ;;
    *)
        echo "Usage: $0 {start|stop|restart|status}"
        exit 1
esac

exit $?