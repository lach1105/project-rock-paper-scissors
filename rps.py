# This program plays a game of Rock, Paper, Scissors between two Players, and
# reports both Player's scores each round.

import random
from os import system

moves = ['rock', 'paper', 'scissors']


# Checks user input value (prompt) against acceptable values (options)
def valid_input(prompt, options):
    while True:
        response = input(prompt).lower()
        if response in options:
            return response


class Player:
    my_move = None
    their_move = None

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


# Subclass whose move method makes a random choice
class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

    def learn(self, my_move, their_move):
        pass


# Subclass whose move method asks the human user what move to make
class HumanPlayer(Player):
    def move(self):
        response = valid_input("Player 1: Rock, Paper, or Scissors? > ", moves)
        return response

    def learn(self, my_move, their_move):
        pass


# Subclass whose move method remembers what move the HumanPlayer played last round, and plays that move this round
class ReflectPlayer(Player):
    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        else:
            return self.their_move

    def learn(self, my_move, their_move):
        self.their_move = their_move


# Subclass whose move mehtod remembers what move it played last round, and cycles through the different moves
class CyclePlayer(Player):
    def move(self):
        if self.my_move is None:
            return random.choice(moves)
        elif self.my_move == "rock":
            return "paper"
        elif self.my_move == "paper":
            return "scissors"
        else:
            return "rock"

    def learn(self, my_move, their_move):
        self.my_move = my_move


# Logic for determining winner
def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


# Prints the current score
def score(score1, score2):
    print(f"Score: Player One {score1}, Player Two {score2}\n")


# Prints the final score
def final_score(score1, score2):
    print("** FINAL SCORE **")
    print(f"** PLAYER 1: {score1}     PLAYER 2: {score2} **\n")


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score1 = 0
        self.score2 = 0

    # Code for one round
    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        winner = beats(move1, move2)
        if move1 == move2:
            print("** THAT ROUND IS A TIE **")
            score(self.score1, self.score2)
        elif winner is True:
            print("** PLAYER 1 WINS THAT ROUND**")
            self.score1 += 1
            score(self.score1, self.score2)
        else:
            print("** PLAYER 2 WINS THAT ROUND**")
            self.score2 += 1
            score(self.score1, self.score2)
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    # Game plays through 3 rounds
    def play_game(self):
        print("Game start!")
        for round in range(3):
            round_count = round + 1
            print(f"Round {round_count}:")
            self.play_round()
        if self.score1 > self.score2:
            print("** PLAYER 1 WINS:  CONGRATULATIONS HUMAN **\n")
            final_score(self.score1, self.score2)
        elif self.score1 < self.score2:
            print("** PLAYER 2 WINS:  BETTER LUCK NEXT TIME HUMAN **\n")
            final_score(self.score1, self.score2)
        else:
            print("** THE GAME WAS A TIME **\n")
            final_score(self.score1, self.score2)
        print("Game over!\n")


if __name__ == '__main__':
    while True:
        # Allow user to choose opponent type
        opponent = valid_input("What type of player do you want to play with "
                               "(Random, Reflect, or Cycle)? > ",
                               ["random", "reflect", "cycle"])
        if opponent == "random":
            player_type = RandomPlayer()
        elif opponent == "reflect":
            player_type = ReflectPlayer()
        else:
            player_type = CyclePlayer()
        game = Game(HumanPlayer(), player_type)
        game.play_game()
        #  Ask user if they want to play again
        play_again = valid_input("Would you like to play again (y/n)?",
                                 ["y", "n"])
        _ = system('cls')
        if play_again == "n":
            break
