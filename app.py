from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import Config


# Create application
app = Flask(__name__)

# Load configuration
app.config.from_object(Config)


# Database
db = SQLAlchemy(app)


# ==========================
# MAIN ROUTES
# ==========================

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/marketplace")
def marketplace():
    return "AI Marketplace Coming Soon"


@app.route("/creator-studio")
def creator_studio():
    return "AI Creator Studio Coming Soon"


@app.route("/prompt-generator")
def prompt_generator():
    return "Prompt Generator Coming Soon"


# ==========================
# START APPLICATION
# ==========================

if __name__ == "__main__":

    with app.app_context():
        db.create_all()

    app.run(debug=True)
