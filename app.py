from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask inside Docker!"

if __name__ == "__main__":
    # Run on all interfaces so Docker can expose it
    app.run(host="0.0.0.0", port=5000)

