from flask import Flask

app = Flask(__name__)

VERSION = "v1.0"

@app.route("/")
def home():
    return f"DevOps CI/CD Platform Running - Version {VERSION}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
