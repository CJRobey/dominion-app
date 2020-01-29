import random as rand
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    games = ['Dominion', 'Intrigue']
    total_cards = 10
    df = pd.read_csv('characters.csv')
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
    nums = nums.astype(int)
    final_characters = []*10
    for i, num in enumerate(nums):
        characters = np.array(df[df['Value'] == (i+2)]['Name'])
        if num:
            final_characters[np.sum(nums[:i]):np.sum(nums[:i])+int(num)] = characters[rand.sample(range(0, len(characters)), int(num))]
    print(final_characters)
    print(nums)

    for i in range(1,11):
        image = plt.imread('./beeware-app/dominionapp/src/dominionapp/resources/images/' + (final_characters[i-1].lower().replace(" ", "-") + ".jpg"))
        plt.subplot(2,5,i); plt.imshow(image); plt.axis("off")

    plt.show()

if __name__ == '__main__':
    main()
