from os import getenv
import json

# Gunicorn config variables
loglevel = "info"
workers = 1
bind = f"0.0.0.0:{getenv('WS_PORT', 80)}"
errorlog = "-"
worker_tmp_dir = "/dev/shm"
accesslog = "-"
graceful_timeout = 120
timeout = 120
keepalive = 5


# For debugging and testing
log_data = {
    "loglevel": loglevel,
    "workers": workers,
    "bind": bind,
    "graceful_timeout": graceful_timeout,
    "timeout": timeout,
    "keepalive": keepalive,
    "errorlog": errorlog,
    "accesslog": accesslog
}

print(json.dumps(log_data, indent="\t"))
