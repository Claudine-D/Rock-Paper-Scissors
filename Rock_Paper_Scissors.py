#!/usr/bin/env python3

# Importing necessary modules
import random
import time

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


# Parent class
class Player:
    # Picks the move the player will make
    def move(self):
        pass

    # For the player to learn from the previous move in order to choose the
    # following move
    def learn(self, my_move, their_move):
        pass

    # Defines which moves beat others
    def beats(one, two):
        # If True one beats two (or draw), if False two beats one
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))


# Only plays rock
class RockPlayer(Player):
    def move(self):
        return rock


# Plays a move at random
class RandomPlayer(Player):
    def move(self):
        move_choice = random.choice([moves])
        return move_choice


# Plays the opponent's previous move
class ReflectPlayer(Player):
    # Picks the opponent's previous move as the next move
    def learn(self, my_move, their_move):
        self.next_move = their_move
        return self.next_move

    def move(self):
        # Picks the first move at random
        if game.round == 0:
            self.move_choice = random.choice([moves])
        # Picks the opponent's previous move as the next move
        else:
            self.move_choice = self.next_move
        return self.move_choice


# Plays through all the moves in order
class CyclePlayer(Player):
    # Picks following move based on previous move
    def learn(self, my_move, their_move):
        self.my_move = my_move
        if self.my_move == "rock":
            self.next_move = "paper"
        elif self.my_move == "paper":
            self.next_move = "scissors"
        else:
            self.next_move = "rock"

    def move(self):
        # Picks the first move at random
        if game.round == 0:
            self.move_choice = random.choice([moves])
        # Picks following move based on previous move
        else:
            self.move_choice = self.next_move
        return self.move_choice


# So  a person can play :)
class HumanPlayer(Player):
    # Input so that the human player can type in their move choice
    def move(self):
        move_choice = input("Rock, paper, scissors? > ").lower()
        if move_choice in [moves]:
            return move_choice
        else:
            self.move()


# The game itself
class Game:
    # Needs 2 players and sets scores + rounds
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score_p1 = 0
        self.score_p2 = 0
        self.round = 0

    def print_pause(self, text):
        print(text)
        time.sleep(2)

    # Choosing how many rounds to play in 1 game
    def number_rounds(self):
        try:
            self.rounds = int(input("How many rounds do you want to play? > "))
            return self.rounds
        # Account for invalid user input (if not an integer)
        except ValueError:
            print("Please enter a number")
            game.play_game()

    # Displaying the final scores at the end of the game
    # and announcing the winner
    def final_scores(self):
        game.print_pause("Final Scores:")
        game.print_pause(f"Player 1: {self.score_p1}\t"
                         "Player 2: {self.score_p2}")
        if self.score_p1 > self.score_p2:
            game.print_pause("~PLAYER 1 WINS!~")
        elif self.score_p1 < self.score_p2:
            game.print_pause("~PLAYER 2 WINS!~")
        else:
            game.print_pause("~It's a draw~")

    # For playing each round and keeping score
    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        game.print_pause(f"Player 1: {move1}  Player 2: {move2}")
        if move1 == move2:
            game.print_pause("It's a draw")
        else:
            if beats(move1, move2):
                game.print_pause("Player 1 wins")
                self.score_p1 += 1
            else:
                game.print_pause("Player 2 wins")
                self.score_p2 += 1
        game.print_pause(f"Score: {self.score_p1} - {self.score_p2}\n")
        # For when the players need to keep track of previous moves
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    # Playing the whole game from start to finish
    def play_game(self):
        game.number_rounds()
        game.print_pause("Game start!")
        for round in range(self.rounds):
            game.print_pause(f"-- Round {round} --")
            self.play_round()
            self.round += 1
        game.print_pause("Game over!")
        game.final_scores()


if __name__ == '__main__':
    # Pick the class of players to use
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()
