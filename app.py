from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Welcome to Jenkins</title>
        <style>
            body {
                background-color: #1e1e2f;
                font-family: Arial, sans-serif;
                color: #ffffff;
                text-align: center;
                padding-top: 100px;
            }
            h1 {
                color: #00ffcc;
                font-size: 3em;
                margin-bottom: 20px;
                text-shadow: 2px 2px 5px #000000;
            }
            p {
                color: #ffcc00;
                font-size: 1.5em;
            }
            .container {
                background: linear-gradient(135deg, #2a2a72, #009ffd);
                padding: 50px;
                border-radius: 15px;
                display: inline-block;
                box-shadow: 0px 0px 20px rgba(0,0,0,0.5);
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1> Welcome to Jenkins </h1>
            <p>Your CI/CD pipeline is running successfully!</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

