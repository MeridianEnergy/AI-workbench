import os
from dotenv import load_dotenv

load_dotenv()


class Config:

    # Security
    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "ai-workbench-development-key"
    )


    # Database
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "sqlite:///ai_workbench.db"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False


    # AI Provider Settings
    OPENAI_API_KEY = os.getenv(
        "OPENAI_API_KEY",
        ""
    )


    # Payment Settings

    PAYPAL_CLIENT_ID = os.getenv(
        "PAYPAL_CLIENT_ID",
        ""
    )


    YOCO_SECRET_KEY = os.getenv(
        "YOCO_SECRET_KEY",
        ""
    )
