import pandas as pd


words = pd.read_csv('src/assets/words.csv')
words = words.squeeze()
words = words[words.str.len() == 5]
words = words.str.lower()
words.drop_duplicates(inplace=True)

yellows = ''

while True:
    current_greens = input('Correct: ').split()
    current_yellows = input('ElseWhere: ').split()
    current_grays = input('Absent: ')
    print()

    if len(current_greens) > 0:
        current_greens = pd.DataFrame({'char': list(current_greens[0]), 'pos': map(int, current_greens[1])})
    if len(current_yellows) > 0:
        yellows += current_yellows[0]
        current_yellows = pd.DataFrame({'char': list(current_yellows[0]), 'pos': map(int, current_yellows[1])})
    if current_grays != '':
        current_grays = pd.DataFrame({'char': list(current_grays)})

    for i in range(len(current_greens)):
        row = current_greens.loc[i]
        words = words[words.str[row.pos - 1] == row.char]
    for i in range(len(current_yellows)):
        row = current_yellows.loc[i]
        words = words[words.str.contains(row.char) & (words.str[row.pos - 1] != row.char)]
    for i in range(len(current_grays)):
        row = current_grays.loc[i]
        count_in_yellows = yellows.count(row.char)
        if count_in_yellows == 0:
            words = words[~words.str.contains(row.char)]
        else:
            words = words[words.str.count(row.char) == count_in_yellows]

    print(words.to_string())
    print('\n')
