import random as rand
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    games = ['Dominion', 'Intrigue']
    total_cards = 10
    # csv_file = 'characters.csv'
    csv_file = 'cards.csv'
    full_df = pd.read_csv(csv_file)

    if (csv_file == 'cards.csv'):
        action_bools = (full_df['Action'] == float(1))
        df = full_df[action_bools]
        bools = [[],[]]
        for i,game in enumerate(games):
            bools[i] = (df['Expansion'] == game)
        final_bools = np.array(bools[0]) | np.array(bools[1])

        # final_bools = [(bools[0][i] or bools[1][i]) for i in range(len(bools[0]))]

        df = df[final_bools]

    nums = np.zeros(5)
    nums[0] = rand.randint(0, 3)
    # this should be rare that we get 3 "2"s. Guess again, but at least 1
    if nums[0] == 3:
        nums[0] = rand.randint(1, 3)
    if nums[0] == 0:
        nums[1] = rand.randint(1, 3)
    else:
        nums[1] = rand.randint(0, 3)

    while np.sum(nums) != total_cards:
        nums[2] = rand.randint(2, 5)
        nums[3] = rand.randint(2, 5)
        nums[4] = rand.randint(0, 2)
        if nums[4] == 2:
            nums[4] = rand.randint(0, 2)

    nums = nums.astype(int)
    final_characters = []*10
    for i, num in enumerate(nums):
        if csv_file == 'cards.csv':
            char_bools = (df['Cost'] == float(i+2))
            characters = np.array(df[char_bools]['Name'])
        else:
            characters = np.array(df[df['Cost'] == (i+2)]['Name'])
        if num:
            sample = rand.sample(range(0, len(characters)), int(num))
            rng_min = np.sum(nums[:i])
            rng_max = np.sum(nums[:i])+int(num)
            final_characters[rng_min:rng_max] = characters[sample]
    print(final_characters)
    print(nums)

    for i in range(1,11):
        image = plt.imread('./beeware-app/dominionapp/src/dominionapp/resources/images/' + (final_characters[i-1].lower().replace(" ", "-") + ".jpg"))
        plt.subplot(2,5,i); plt.imshow(image); plt.axis("off")

    #plt.savefig('final_plot')
    plt.show()

if __name__ == '__main__':
    main()
