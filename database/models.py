from datetime import datetime
from app import db


# ==========================
# USERS
# ==========================

class User(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(200),
        nullable=False
    )

    account_type = db.Column(
        db.String(50),
        default="USER"
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


# ==========================
# AI CREATORS
# ==========================

class Creator(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id")
    )

    company_name = db.Column(
        db.String(150)
    )

    verified = db.Column(
        db.Boolean,
        default=False
    )


# ==========================
# AI AGENTS
# ==========================

class AIAgent(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    creator_id = db.Column(
        db.Integer,
        db.ForeignKey("creator.id")
    )

    name = db.Column(
        db.String(150),
        nullable=False
    )

    description = db.Column(
        db.Text
    )

    category = db.Column(
        db.String(100)
    )

    system_prompt = db.Column(
        db.Text
    )

    price = db.Column(
        db.Float,
        default=0
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


# ==========================
# CHAT CONVERSATIONS
# ==========================

class Conversation(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer
    )

    ai_id = db.Column(
        db.Integer
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


# ==========================
# CHAT MESSAGES
# ==========================

class Message(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    conversation_id = db.Column(
        db.Integer
    )

    sender = db.Column(
        db.String(50)
    )

    content = db.Column(
        db.Text
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )


# ==========================
# PAYMENTS
# ==========================

class Payment(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer
    )

    amount = db.Column(
        db.Float
    )

    provider = db.Column(
        db.String(50)
    )

    status = db.Column(
        db.String(50)
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )
