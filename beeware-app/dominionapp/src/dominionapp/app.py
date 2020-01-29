"""
A smart dominion board game randomizer.
"""
import toga
from toga.style.pack import CENTER, COLUMN
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from numpy import zeros, array, sum
from random import randint, sample
from pandas import read_csv
from cv2 import imread

box = toga.Box()


class DominionApp(toga.App):

    def startup(self):
        self.main_window = toga.MainWindow(title=self.name)

        box.style.padding = 40
        box.style.update(alignment=CENTER)
        box.style.update(direction=COLUMN)
        button1 = toga.Button('Choose Game', on_press=self.decide_game)
        box.add(button1)
        # image from local path
        # load brutus.png from the package
        # We set the style width/height parameters for this one

        self.main_window.content = box
        self.main_window.show()

    def decide_game(self, widget):
        games = ['Dominion', 'Intrigue']
        total_cards = 10
        df = read_csv('src/dominionapp/resources/characters.csv')
        nums = zeros(5)
        nums[0] = randint(0, 3)
        # this should be rare that we get 3 "2"s. Guess again, but at least 1
        if nums[0] == 3:
            nums[0] = randint(1, 3)
        if nums[0] == 0:
            nums[1] = randint(1, 3)
        else:
            nums[1] = randint(0, 3)

        while sum(nums) != total_cards:
            nums[2] = randint(2, 5)
            nums[3] = randint(2, 5)
            nums[4] = randint(0, 2)
        nums = nums.astype(int)
        final_characters = [] * 10
        for i, num in enumerate(nums):
            characters = array(df[df['Value'] == (i + 2)]['Name'])
            if num:
                final_characters[sum(nums[:i]):sum(nums[:i]) + int(num)] = characters[sample(range(0, len(characters)), int(num))]

        for i in range(1,11):
            image_from_path = toga.Image('./resources/images/' + (final_characters[i-1].lower().replace(" ", "-") + ".jpg"))
            imageview_from_path = toga.ImageView(image_from_path)
            imageview_from_path.style.update(width=150)
            imageview_from_path.style.update(height=240)
            imageview_from_path.style.update(direction=ROW)
            box.add(imageview_from_path)

        print(final_characters)
        print(nums)

        self.main_window.content = box
        self.main_window.show()


def main():
    return DominionApp()
