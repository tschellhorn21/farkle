from view import *


def roll_one(self, dice1) -> None:
    """
    This function sets the picture in the gui for dice one.
    :param self: self
    :param dice1: The value of dice1 from controller is needed to select the right picture.
    """
    if dice1 == 1:
        self.dice_one.setPixmap(QtGui.QPixmap("pictures/one.png"))
    elif dice1 == 2:
        self.dice_one.setPixmap(QtGui.QPixmap("pictures/two.png"))
    elif dice1 == 3:
        self.dice_one.setPixmap(QtGui.QPixmap("pictures/three.png"))
    elif dice1 == 4:
        self.dice_one.setPixmap(QtGui.QPixmap("pictures/four.png"))
    elif dice1 == 5:
        self.dice_one.setPixmap(QtGui.QPixmap("pictures/five.png"))
    elif dice1 == 6:
        self.dice_one.setPixmap(QtGui.QPixmap("pictures/six.png"))


def roll_two(self, dice2) -> None:
    """
    This function sets the picture in the gui for dice two.
    :param self: self
    :param dice2: The value of dice2 from controller is needed to select the right picture.
    """
    if dice2 == 1:
        self.dice_two.setPixmap(QtGui.QPixmap("pictures/one.png"))
    elif dice2 == 2:
        self.dice_two.setPixmap(QtGui.QPixmap("pictures/two.png"))
    elif dice2 == 3:
        self.dice_two.setPixmap(QtGui.QPixmap("pictures/three.png"))
    elif dice2 == 4:
        self.dice_two.setPixmap(QtGui.QPixmap("pictures/four.png"))
    elif dice2 == 5:
        self.dice_two.setPixmap(QtGui.QPixmap("pictures/five.png"))
    elif dice2 == 6:
        self.dice_two.setPixmap(QtGui.QPixmap("pictures/six.png"))


def roll_three(self, dice3):
    """
    This function sets the picture in the gui for dice three.
    :param self: self
    :param dice3: The value of dice3 from controller is needed to select the right picture.
    """
    if dice3 == 1:
        self.dice_three.setPixmap(QtGui.QPixmap("pictures/one.png"))
    elif dice3 == 2:
        self.dice_three.setPixmap(QtGui.QPixmap("pictures/two.png"))
    elif dice3 == 3:
        self.dice_three.setPixmap(QtGui.QPixmap("pictures/three.png"))
    elif dice3 == 4:
        self.dice_three.setPixmap(QtGui.QPixmap("pictures/four.png"))
    elif dice3 == 5:
        self.dice_three.setPixmap(QtGui.QPixmap("pictures/five.png"))
    elif dice3 == 6:
        self.dice_three.setPixmap(QtGui.QPixmap("pictures/six.png"))


def roll_four(self, dice4):
    """
    This function sets the picture in the gui for dice four.
    :param self: self
    :param dice4: The value of dice4 from controller is needed to select the right picture.
    """
    if dice4 == 1:
        self.dice_four.setPixmap(QtGui.QPixmap("pictures/one.png"))
    elif dice4 == 2:
        self.dice_four.setPixmap(QtGui.QPixmap("pictures/two.png"))
    elif dice4 == 3:
        self.dice_four.setPixmap(QtGui.QPixmap("pictures/three.png"))
    elif dice4 == 4:
        self.dice_four.setPixmap(QtGui.QPixmap("pictures/four.png"))
    elif dice4 == 5:
        self.dice_four.setPixmap(QtGui.QPixmap("pictures/five.png"))
    elif dice4 == 6:
        self.dice_four.setPixmap(QtGui.QPixmap("pictures/six.png"))


def roll_five(self, dice5):
    """
    This function sets the picture in the gui for dice five.
    :param self: self
    :param dice5: The value of dice5 from controller is needed to select the right picture.
    """
    if dice5 == 1:
        self.dice_five.setPixmap(QtGui.QPixmap("pictures/one.png"))
    elif dice5 == 2:
        self.dice_five.setPixmap(QtGui.QPixmap("pictures/two.png"))
    elif dice5 == 3:
        self.dice_five.setPixmap(QtGui.QPixmap("pictures/three.png"))
    elif dice5 == 4:
        self.dice_five.setPixmap(QtGui.QPixmap("pictures/four.png"))
    elif dice5 == 5:
        self.dice_five.setPixmap(QtGui.QPixmap("pictures/five.png"))
    elif dice5 == 6:
        self.dice_five.setPixmap(QtGui.QPixmap("pictures/six.png"))


def roll_six(self, dice6):
    """
    This function sets the picture in the gui for dice six.
    :param self: self
    :param dice6: The value of dice6 from controller is needed to select the right picture.
    """
    if dice6 == 1:
        self.dice_six.setPixmap(QtGui.QPixmap("pictures/one.png"))
    elif dice6 == 2:
        self.dice_six.setPixmap(QtGui.QPixmap("pictures/two.png"))
    elif dice6 == 3:
        self.dice_six.setPixmap(QtGui.QPixmap("pictures/three.png"))
    elif dice6 == 4:
        self.dice_six.setPixmap(QtGui.QPixmap("pictures/four.png"))
    elif dice6 == 5:
        self.dice_six.setPixmap(QtGui.QPixmap("pictures/five.png"))
    elif dice6 == 6:
        self.dice_six.setPixmap(QtGui.QPixmap("pictures/six.png"))


def reset_dice(self):
    """
    This function resets the pictures of the dice to 1 - 6.
    :param self: self
    """
    self.dice_one.setPixmap(QtGui.QPixmap("pictures/one.png"))
    self.dice_two.setPixmap(QtGui.QPixmap("pictures/two.png"))
    self.dice_three.setPixmap(QtGui.QPixmap("pictures/three.png"))
    self.dice_four.setPixmap(QtGui.QPixmap("pictures/four.png"))
    self.dice_five.setPixmap(QtGui.QPixmap("pictures/five.png"))
    self.dice_six.setPixmap(QtGui.QPixmap("pictures/six.png"))
    self.checkbox_one.setChecked(True)
    self.checkbox_two.setChecked(True)
    self.checkbox_three.setChecked(True)
    self.checkbox_four.setChecked(True)
    self.checkbox_five.setChecked(True)
    self.checkbox_six.setChecked(True)
