class Spanzuratorea:
    """A class representing the game 'spanzuratoarea'"""

    def __init__(self):
        self.word = ''
        self.word_displayed = []
        self.aux_word = []
        self.tries = 3
        self.game_active = True
        self.rounds = 1

    def game(self):
        print("Welcome to Spanzuratoarea\nIn this game you have to guess a word letter by letter\n"
              "You only have 3 tries so Good luck!")
        while self.game_active:
            self.play()


    def play(self):
        """The main loop of the game."""
        self._get_word()
        while True:
            print(*self.word_displayed)
            letter = input("Enter a letter:")
            if len(letter) > 1:
                print("Please enter just a single letter.")
            elif letter in self.word_displayed:
                print(f"You have already entered the letter {letter}")
            elif letter in self.word:
                self._fit_letter(letter)
            else:
                print("Try again!")
                self.tries -= 1
                print("Tries left: {}".format(self.tries))
            if self._check_win_lose():
                self._play_again()
                break

    def _play_again(self):
        choice = input("Want to play again?'y' for yes and 'n' for no.\n")
        while choice.lower() != 'y' and choice.lower() != 'n':
            choice = input("Please enter a suitable character:\n")
        if choice.lower() == 'y':
            self.rounds += 1
            print(f"Beggining Round {self.rounds}\n")
            self.tries = 3
        elif choice.lower() == 'n':
            print("Thanks for playing!")
            self.game_active = False

    def _check_win_lose(self):
        """Checks if the word has been guessed."""
        if self.word_displayed == list(self.word):
            print(f"'{self.word}' was the word.")
            print("You won!!")
            return True
        elif self.tries <= 0:
            print(f"'{self.word}' was the word.")
            return True

    def _fit_letter(self,letter):
        """Puts in a letter that was guessed correctly"""
        while self.aux_word.count(letter):
            index = self.aux_word.index(letter)
            self.word_displayed[index] = letter
            self.aux_word[index] = '_'

    def _get_word(self):
        """Asks the user for a word to be guessed."""
        self.word = input("Enter a word that someone has to guess:\n")
        self.word_displayed = list(len(self.word) * '_')
        self.aux_word = list(self.word)
        self._convert_spaces()
        print("Try to guess the word by entering a letter that could fit.")

    def _convert_spaces(self):
        while " " in self.aux_word:
            index = self.aux_word.index(" ")
            self.word_displayed[index] = " "
            self.aux_word[index] = "_"
            print(self.aux_word)

sp = Spanzuratorea()
sp.game()