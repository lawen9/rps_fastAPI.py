from typing import Optional
from enum import Enum
import random
from fastapi import FastAPI

app = FastAPI()

class Move(str, Enum):
    rock = "rock"
    paper = "paper"
    scissors = "scissors"

moves = list(Move)

scores = {"player": 0, "computer": 0}

def determine_winner(player_move: Move, computer_move: Move) -> str:
    if player_move == computer_move:
        return "draw"
    if (player_move == Move.rock and computer_move == Move.scissors) or \
       (player_move == Move.paper and computer_move == Move.rock) or \
       (player_move == Move.scissors and computer_move == Move.paper):
        return "player"
    return "computer"
@app.get("/")
def read_root():
    return {"Welcome to Rock-Paper-Scissors game"}

@app.get("/play/{player_move}")
def play(player_move: Move):
    computer_move = random.choice(moves)
    winner = determine_winner(player_move, computer_move)

    if winner == "player":
        scores["player"] += 1
    elif winner == "computer":
        scores["computer"] += 1

    return {
        "player_move": player_move,
        "computer_move": computer_move,
        "winner": winner,
        "scores": scores
    }
@app.get("/scores")
def get_scores():
    return scores
