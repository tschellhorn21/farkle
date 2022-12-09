from PyQt5.QtWidgets import *
from view import *
import random
from collections import Counter
from modules import dice as d

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs) -> None:
        """
        Function is to set up everything for the program
        """
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.player_one_score = 0
        self.player_two_score = 0
        self.score = 0
        self.x = 6
        self.y = 6
        self.roll_button.clicked.connect(lambda: self.roll_dice())
        self.endTurn_button.clicked.connect(lambda: self.end_turn())
        self.restart_button.clicked.connect(lambda: self.restart())

    def roll_dice(self) -> None:
        """
        This function handles rolling the dice when the Roll Dice button is clicked.
        :return: None
        """
        trio = 0
        pair = 0
        num = 0
        one_six = 0
        dice = []
        self.score = 0
        self.what_label.setText('')

        if self.checkbox_one.isChecked():
            dice1 = random.randint(1, 6)
            d.roll_one(self, dice1)
            dice.append(dice1)
        if self.checkbox_two.isChecked():
            dice2 = random.randint(1, 6)
            d.roll_two(self, dice2)
            dice.append(dice2)
        if self.checkbox_three.isChecked():
            dice3 = random.randint(1, 6)
            d.roll_three(self, dice3)
            dice.append(dice3)
        if self.checkbox_four.isChecked():
            dice4 = random.randint(1, 6)
            d.roll_four(self, dice4)
            dice.append(dice4)
        if self.checkbox_five.isChecked():
            dice5 = random.randint(1, 6)
            d.roll_five(self, dice5)
            dice.append(dice5)
        if self.checkbox_six.isChecked():
            dice6 = random.randint(1, 6)
            d.roll_six(self, dice6)
            dice.append(dice6)
        print(dice)
        dicenum = Counter(dice)
        print(dicenum)

        for x in dicenum:
            if dicenum[x] == 6:
                self.what_label.setText('Six of a kind!')
                self.score += 3000
                break
            if dicenum[x] == 5:
                self.what_label.setText('Five of a kind!')
                self.score += 2000
                break
            if dicenum[x] == 4:
                self.what_label.setText('Four of a kind!')
                self.score += 1000
                break
            if dicenum[x] == 3:
                trio += 1
                num = x
            if dicenum[x] == 2:
                pair += 1
            if dicenum[x] == 1:
                one_six += 1

        if one_six == 6:
            self.what_label.setText('One through Six!')
            self.score += 1500
        elif trio == 2:
            self.what_label.setText('Two Triplets!')
            self.score += 2500
        elif pair == 3:
            self.what_label.setText('Three Pairs!')
            self.score += 1500
        elif trio == 1:
            self.what_label.setText('Three of a kind!')
            if num == 1:
                self.score += 300
            else:
                self.score += (num * 100)
        elif dicenum[1] > 0 and dicenum[5] > 0:
            ones = dicenum[1] * 100
            fives = dicenum[5] * 50
            self.score += ones + fives
        elif dicenum[1] > 0:
            ones = dicenum[1] * 100
            self.score += ones
        elif dicenum[5] > 0:
            fives = dicenum[5] * 50
            self.score += fives
        elif dicenum[1] == 0 and dicenum[5] == 0:
            self.possible_score.setText('0')
            self.score = 0
            self.end_turn()
            self.what_label.setText("Oh no,  you scored nothing.  Next player's turn")

        self.possible_score.setText(f'{self.score}')
        print(f'trio {trio}')
        print(f'pair {pair}')

    def end_turn(self) -> None:
        """
        This function handles switching to the other player and setting the score when the end turn button is clicked.
        :return: None
        """
        player_num = self.playerNum_label.text()
        if player_num == '1':
            self.player_one_score += self.score
            self.playerOne_score.setText(f'{self.player_one_score}')
            self.playerNum_label.setText('2')
        else:
            self.player_two_score += self.score
            self.playerTwo_score.setText(f'{self.player_two_score}')
            self.playerNum_label.setText('1')
        d.reset_dice(self)
        self.what_label.setText('')
        self.possible_score.setText('0')
        self.score = 0

    def restart(self) -> None:
        """
        This function handles resetting everything in the game to restart.
        :return: None
        """
        d.reset_dice(self)
        self.playerNum_label.setText('1')
        self.what_label.setText('')
        self.possible_score.setText('0')
        self.playerOne_score.setText('0')
        self.playerTwo_score.setText('0')
        self.score = 0
