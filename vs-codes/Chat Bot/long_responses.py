import random

#How to add longer responses.
R_EATING = "I don't like eating anything, because I'm a bot, obviously!"
R_HOBBIES = "I enjoy spending my time learning new things and helping people with their questions."
R_FEELINGS = "As a bot, I don't have feelings, but I'm here to assist you to the best of my abilities."
R_OUTFIT = "As a program, I just wear code."
R_TRAVEL = "I can't travel physically, but I'm knowledgeable about global destinations."
R_WEATHER = "I lack weather experiences, but I provide accurate forecasts."
R_BOOKS = "I recommend books and offer summaries across genres."
R_MUSIC = "I suggest music and discuss its cultural significance."
R_EXERCISE = "I advise on exercise routines and healthy practices."
R_RELATIONSHIPS = "I guide on communication and maintaining relationships."
R_HISTORY = "I explore historical events, figures, and eras."
R_FUTURE = "I discuss emerging tech, trends, and future possibilities."
R_LANGUAGES = "I teach, translate, and share language insights."
R_UNIVERSE = "I engage in cosmic discussions about space and astronomy."


def unknown():
    response = response = random.choice([
        "Could you please rephrase that?",
        "I'm not sure I understand your message.",
        "Sounds interesting, tell me more!",
        "What does that mean?",
        "......",
        "I'm here to chat and learn with you.",
        "That's intriguing, could you provide more details?"
    ])
    return response