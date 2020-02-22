"""
A smart dominion board game randomizer.
"""
import toga
from toga.style.pack import CENTER, COLUMN, RIGHT, LEFT
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import csv
from random import randint, sample


class DominionApp(toga.App):

    def startup(self):
        self.main_window = toga.MainWindow(title=self.name, size=(250, (240*10)+(40*20)))
        self.outer_box = toga.Box()
        self.outer_box.style.padding = 40
        self.outer_box.style.update(direction=COLUMN)
        self.button = toga.Button('Choose Game', on_press=self.decide_game, style=Pack(alignment=CENTER, padding=40))
        self.button.enabled = True;
        self.outer_box.add(self.button)
        box = toga.Box(style=Pack(padding=40,alignment=CENTER, direction=COLUMN))
        # initializing the space
        self.outer_box.add(box)
        self.scroller = toga.ScrollContainer(content=self.outer_box)
        #self.scroller.content = self.outer_box
        # image from local path
        # We set the style width/height parameters for this one
        self.main_window.content = self.scroller
        self.main_window.show()


    async def decide_game(self, widget):
        # widget.label = 'pressed'
        games = ['Dominion', 'Intrigue']
        total_cards = 10
        max_cost = 6
        csv_file = 'cards.csv'
        full_df = [[] for sub in range(max_cost + 1)]
        key_dict = {}
        csvfile = csv.DictReader(open('app/dominionapp/resources/' + csv_file))
        for row in csvfile:
            for game in games:
                if row['Expansion'] == game:
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
            if num:
                char_sample = sample(range(0, len(characters)), int(num))

                for s in char_sample:
                    final_characters[counter] = characters[s]
                    counter += 1
        print(final_characters)

        picture_box = toga.Box(style=Pack(direction=COLUMN))
        for i in range(1,11):
            image_from_path = toga.Image('./resources/images/' + (final_characters[i-1]['Name'].lower().replace(" ", "-") + ".jpg"))
            imageview_from_path = toga.ImageView(image_from_path, style=Pack(direction=COLUMN, alignment=CENTER,
                                                                             padding=40, width=150, height=240))
            picture_box.add(imageview_from_path)

        if len(self.outer_box.children) > 1:
           self.outer_box.children[1] = picture_box
        else:
           self.outer_box.add(picture_box)
        self.scroller.content = self.outer_box
        widget.enabled = True;
        self.main_window.content = self.scroller


def main():
    return DominionApp('DominionApp')

if __name__ == '__main__':
    app = main()
    app.main_loop()
