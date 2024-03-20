
import random
"""Object oriented Yatzy

Add code to complete the game.
"""


class Dice:
    """The five die used in the game."""

    def __init__(self):
        """Call constructor to create a Dice, containing five die."""
        self._dice = []
        self.roll()

    def roll(self):
        """Roll not saved dice."""
        for i in range(5 - len(self._dice)):
            self._dice.append(random.randrange(1,6))

    def print(self):
        """Print dice values to console."""
        print(self._dice)

    def sum_all(self, value):
        """Return the sum of the selected value.
        
        For example sum_all(5) returns 15 with the folowing dice: 1, 5, 3, 5, 5."""
        return self._dice.count(value) * value
    
    def save(self, list_of_numbers_to_save):
        """Include a list of numbers to save. 
        
        For examle [6, 6] will save two sixes, if exists.
        """
        saved_dice = []
        for number in list_of_numbers_to_save:
            if number in self._dice:
                saved_dice.append(number)
                self._dice.remove(number)
        self._dice = saved_dice
    
    def discard_all(self):
        """Discard all five dice."""
        self._dice = []


class Result:
    """One cell in the score board."""

    def __init__(self, name):
        """Call constructor to create a Result-object."""
        self.is_set = False
        self.score = '-'
        self.name = name

class ResultBoard:
    """All results for one player in one game."""

    def __init__(self):
        """Call constructor to create a ResultBord-object."""
        self._result = {}
        self._result["ettor"] = Result("ettor")
        self._result["tvåor"] = Result("tvåor")
        self._result["treor"] = Result("treor")

    def set_result(self, choice, score):
        """Set score in the choicen cell."""
        if choice in self._result.keys():
            if not self._result[choice].is_set:
                self._result[choice].is_set = True
                self._result[choice].score = score

    def __str__(self):
        """Returns string representation of the result board."""
        answer = ""
        for key in self._result:
            answer += key + ": " + str(self._result[key].score) +"\n"
        return answer


class Game:
    """A class to hold the game."""

    def __init__(self):
        """Call constructor to create an object of the Game."""
        self.dice = Dice()
        self.player_one_result_board = ResultBoard()

    def run(self):
        """Start the game."""
        print(self.player_one_result_board)
        
        # round one
        self.dice.roll()
        self.dice.print() 
        self.dice.save([1, 1, 1, 1, 1]) # TODO input from user
        self.dice.print()
        # Roll a second time.    
        self.dice.roll()
        self.dice.print()
        self.dice.save([1, 1, 1, 1, 1]) # TODO input from user
        self.dice.print()
        # Roll a third time.
        self.dice.roll()
        self.dice.print()
        print("save as 1")
        self.player_one_result_board.set_result("ettor", self.dice.sum_all(1))
        print(self.player_one_result_board)
        self.dice.discard_all()

        # round two
        self.dice.roll()
        self.dice.print()
        print("save as 3")
        self.player_one_result_board.set_result("treor", self.dice.sum_all(3))

        # round three
        self.dice.roll()
        self.dice.print()
        print("save as 2")
        self.player_one_result_board.set_result("tvåor", self.dice.sum_all(2))

        print(self.player_one_result_board)

game = Game()
game.run()
 