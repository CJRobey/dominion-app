"""
A smart dominion board game randomizer.
"""
import toga
import asyncio
from toga.style.pack import CENTER, COLUMN, RIGHT, LEFT
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import csv
from random import randint, sample


class DominionApp(toga.App):

    def startup(self):
        self.main_window = toga.MainWindow(title=self.name)
        self.outer_box = toga.Box()
        self.outer_box.style.update(direction=COLUMN)

        self.choose_button = toga.Button('Choose Game', on_press=self.decide_game, style=Pack(alignment=CENTER, padding=40))
        self.outer_box.add(self.choose_button)

        # initializing the space
        self.scroller = toga.ScrollContainer(content=self.outer_box)
        self.init_menu()
        self.split = toga.SplitContainer()
        self.split.content = [self.scroller, self.game_dashboard]

        # image from local path
        # We set the style width/height parameters for this one
        self.main_window.content = self.split
        self.main_window.show()

    def init_menu(self):
        self.games = []
        csv_file = 'cards.csv'
        self.csvfile = csv.DictReader(open('app/dominionapp/resources/' + csv_file))
        expansion_buttons = []
        self.game_dashboard = toga.Box(style=Pack(direction=COLUMN, alignment=RIGHT))
        self.game_dashboard.add(toga.Label('Expansions to Use', style=Pack(text_align=CENTER, padding=10)))
        for row in self.csvfile:
            if row['Expansion'] not in expansion_buttons:
                button = toga.Button(row['Expansion'], on_press=self.button_callback, style=Pack(alignment=CENTER, padding=5))
                expansion_buttons.append(row['Expansion'])
                self.game_dashboard.add(button)

    def button_callback(self, widget):
        if widget.label[0] != '+':
            self.games += [widget.label]
            widget.label = '+ ' + widget.label
        else:
            self.games.remove(widget.label[2:])
            widget.label = widget.label[2:]
        print(self.games)

    def decide_game(self, widget):
        max_cost = 6
        full_df = [[] for sub in range(max_cost + 1)]
        total_cards = 10
        csv_file = 'cards.csv'
        self.csvfile = csv.DictReader(open('app/dominionapp/resources/' + csv_file))

        for row in self.csvfile:
            for game in self.games:
                if row['Expansion'] == game:
                    print(row['Cost'], row['Name'])
                    if row['Cost'] == '':
                        row['Cost'] = 0
                    cost = int(row['Cost'])
                    if bool(row['Action']) or (bool(row['Treasure']) and bool(row['Victory'])):
                        full_df[cost] += [row]

        nums = [0 for sub in range(5)]
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
            if nums[4] == 2:
                nums[4] = randint(0, 2)

        final_characters = ['filler_name' for i in range(total_cards)]
        counter = 0;
        for i, num in enumerate(nums):
            characters = full_df[i + 2]
            # print(len(characters), int(num))

            if num:
                char_sample = sample(range(0, len(characters)), int(num))
                for s in char_sample:
                    final_characters[counter] = characters[s]
                    counter += 1
        # print(final_characters)

        picture_box = toga.Box(style=Pack(direction=COLUMN))
        for i in range(1,11):
            image_from_path = toga.Image('./resources/images/' + (final_characters[i-1]['Name'].lower().replace(" ", "-") + ".jpg"))
            imageview_from_path = toga.ImageView(image_from_path, style=Pack(direction=COLUMN, alignment=CENTER,
                                                                             padding=40, width=150, height=240))
            picture_box.add(imageview_from_path)

        if (len(self.outer_box.children) > 1):
            self.outer_box.children[1] = picture_box
        else:
            self.outer_box.add(picture_box)

        self.scroller.content = self.outer_box


def main():
    return DominionApp('DominionApp')

if __name__ == '__main__':
    app = main()
    app.main_loop()
