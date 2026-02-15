from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World from CI/CD Pipeline using AWS Codebuild and GitHub 🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
