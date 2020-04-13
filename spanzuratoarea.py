class Spanzuratorea:
    """A class representing the game 'spanzuratoarea'"""

    def __init__(self):
        self.word = ''
        self.word_displayed = []
        self.aux_word = []
        self.tries = 3
        self.game_active = True

    def game(self):
        while self.game_active:
            self.play()


    def play(self):
        """The main loop of the game."""
        self._get_word()
        while True:
            print(*self.word_displayed)
            letter = input("Enter a letter:")
            if letter in self.word_displayed:
                print(f"You have already entered the letter {letter}")
            elif letter in self.word:
                self._fit_letter(letter)
            else:
                print("Try again!")
            if self._check_win():
                choice = input("Want to play again?'y' for yes and 'n' for no.\n")
                if choice.lower() == 'y':
                    break
                elif choice.lower() == 'n':
                    print("Thanks for playing!")
                    self.game_active = False
                    break


    def _check_win(self):
        """Checks if the word has been guessed."""
        if self.word_displayed == list(self.word):
            print(f"{self.word} was the word.")
            print("You won!!")
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
        print("Try to guess the word by entering a letter that could fit.")


sp = Spanzuratorea()
sp.game()