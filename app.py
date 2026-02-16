from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>🚀 Flask App Deployed from GitHub via AWS CodeBuild</h1>
    <p>CI/CD Working Successfully!</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
