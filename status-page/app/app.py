from flask import Flask, render_template
import requests

app = Flask(__name__)

SERVICES = [
    {"name": "Proxmox", "url": "https://proxmox.costantino.es"},
    {"name": "Adguard", "url": "https://adguard.costantino.es"},
    {"name": "Vikunja", "url": "https://vikunja.costantino.es"},
    {"name": "Grafana", "url": "https://grafana.costantino.es"},
    {"name": "Prometheus", "url": "https://prometheus.costantino.es"},
    {"name": "Gitlab", "url": "https://gitlab.costantino.es"},
    {"name": "Stirling", "url": "https://stirling.costantino.es"},
]

def check_services(url):
    try:
        r = requests.get(url, timeout=5, verify=False)
        return r.status_code < 500
    except:
        return False

@app.route("/")
def index():
    services = []
    for s in SERVICES:
        services.append({
            "name": s["name"],
            "url": s["url"],
            "online": check_services(s["url"])
        })
    return render_template("index.html", services=services)

@app.route("/health")
def health():
    return {"status":"ok"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)