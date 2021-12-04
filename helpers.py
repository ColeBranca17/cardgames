import os
import requests
import urllib.parse

from flask import redirect, render_template, request, session
from functools import wraps


def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


def usd(value):
    """Format value as USD."""
    return f"${value:,.2f}"


def deck():
    # deck structured so that it is a list of cards, which are represented by a list (in the order of [value, type, suit])
    deck = []
    # fills deck with numbered 2-9 cards
    for i in range(32):
        card = []
        card.append(2 + (i // 4))
        card.append(str(2 + (i // 4)))
        if i % 4 == 0:
            card.append("H")
        elif i % 4 == 1:
            card.append("D")
        elif i % 4 == 2:
            card.append("C")
        else:
            card.append("S")
        deck.append(card)
    # fills deck with face cards (and 10's)
    for i in range(16):
        card = []
        card.append(10)
        if i // 4 == 0:
            card.append("10")
        if i // 4 == 1:
            card.append("Jack")
        if i // 4 == 2:
            card.append("Queen")
        else:
            card.append("King")
        if i % 4 == 0:
            card.append("H")
        elif i % 4 == 1:
            card.append("D")
        elif i % 4 == 2:
            card.append("C")
        else:
            card.append("S")
        deck.append(card)
    # fills deck with aces
    for i in range(4):
        card = []
        # must remember to ask user whether to play as 1 or 11
        card.append(11)
        card.append("Ace")
        if i % 4 == 0:
            card.append("H")
        elif i % 4 == 1:
            card.append("D")
        elif i % 4 == 2:
            card.append("C")
        else:
            card.append("S")
        deck.append(card)
    return deck