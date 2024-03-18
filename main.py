
import random


class Dice:

    def __init__(self):
        self._dice = []
        self.roll()

    def roll(self):
        self._dice = []
        for i in range(5):
            self._dice.append(random.randrange(1,6))

    def print(self):
        print(self._dice)

    def sum_all(self, value):
        return self._dice.count(value) * value


class Result:
    def __init__(self, name):
        self.is_set = False
        self.score = '-'
        self.name = name

class ResultBoard:

    def __init__(self):
        self._result = {}
        self._result["ettor"] = Result("ettor")
        self._result["tvåor"] = Result("tvåor")

    def set_result(self, choice, score):
        if choice in self._result.keys():
            if not self._result[choice].is_set:
                self._result[choice].is_set = True
                self._result[choice].score = score
    def __str__(self):
        answer = ""
        for key in self._result:
            answer += key + ": " + str(self._result[key].score) +"\n"
        return answer


class Game:

    def __init__(self):
        self.dice = Dice()
        self.player_one_result_board = ResultBoard()

    def run(self):
        print(self.player_one_result_board)
        self.dice.roll()
        self.dice.print()       
        self.player_one_result_board.set_result("ettor", self.dice.sum_all(1))
        self.dice.roll()
        self.dice.print()
        self.player_one_result_board.set_result("tvåor", self.dice.sum_all(2))

        print(self.player_one_result_board)

game = Game()
game.run()
 