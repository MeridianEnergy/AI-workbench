from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Create Flask application
app = Flask(__name__)

# Configuration
app.config["SECRET_KEY"] = os.getenv(
    "SECRET_KEY",
    "ai-workbench-development-key"
)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ai_workbench.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Database initialization
db = SQLAlchemy(app)


# ==========================
# MAIN WEBSITE ROUTES
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
