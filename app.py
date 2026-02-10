from flask import Flask

app = Flask(__name__)

@app.get("/")
def home():
    return "Hello from Azure VM (Docker + ACR + Azure DevOps)!\n"

@app.get("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    # IMPORTANT: bind to 0.0.0.0 so it is reachable outside the container
    app.run(host="0.0.0.0", port=5001)
