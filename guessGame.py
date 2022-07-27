import random
import string
import sys

class Gaming:
    def __init__(self):
        try:
            option = int(input('''Welcome to Guess Game.
            Select an option to continue:
            1. Start Game
            2. Exit
            '''))
        except ValueError:
            print('Invalid selected option, try again')
            game = Gaming()
        
        if option == 1:
            self.startGame()
        elif option == 2:
            sys.exit()
        else:
            print('Invalid selected option, try again')
            game = Gaming()
    
    def startGame(self):
        player1 = input('Enter player 1 name >> ')
        player2 = input('Enter player 2 name >> ')
        self.players = [player1, player2]

        try:
            gameOption = int(input('''What Guess game do you want to play?
            Select an option to continue >>
            1. Text Guess
            2. Number Guess
            '''))
        except ValueError:
            print('Invalid selected option, try again')
            self.startGame()
            
        if gameOption == 1:
            self.textGame()
        elif gameOption == 2:
            self.numGame()
        else:
            print('Invalid selected option, try again')
            self.startGame()
        
    def textGame(self):
        systemText = random.choice(string.ascii_uppercase)
        self.currentScore = {}
        for player in self.players:
            playerGuess = input('{} enter the character for your guess >> '.format(player.upper()))
            if playerGuess.upper() == systemText:
                self.currentScore[player] = 10
                  
        self.displayWinner('Text', systemText)
        
    def numGame(self):
        systemNum = random.randint(0, 9)
        self.currentScore = {}
        for player in self.players:
            try:
                playerGuess = int(input('{} enter your guess number between 0 to 9 >> '.format(player.upper())))
            except ValueError:
                print('Invalid selected guess, your guess must be a number')
                self.numGame()
            if playerGuess == systemNum:
                self.currentScore[player] = 10
        self.displayWinner('Number', systemNum)
    
    def displayWinner(self, gameType, guess):
        if len(self.currentScore) > 1 or not self.currentScore:
            print('The game is a draw')
            for player, score in self.currentScore.items():
                print('{} has {} points'.format(player, score))
        else:
            for player, score in self.currentScore.items():
                print('The winner is {} with {} points'.format(player.upper(), score))
                
        print('The Guess {} is {}'.format(gameType, guess))
        self.endGame(gameType)
        
    def endGame(self, gameType):
        try:
            option = int(input('''Select an option to continue
        1. Restart New Game
        2. Reset Game
        3. Exit
        '''))
        except ValueError:
            print('Invalid selected option')
            self.endGame()
        
        if option == 1:
            if gameType == 'Text':
                self.textGame()
            else:
                self.numGame()
        elif option == 2:
            self.startGame()
        elif option == 3:
            sys.exit()
        else:
            print('Invalid selected option')
            game = Gaming()
                
game = Gaming()