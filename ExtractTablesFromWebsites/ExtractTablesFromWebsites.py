import pandas as pd

simpsons = pd.read_html('https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1%E2%80%9320)')

# Getting the first 5 rows of the table "Season 1" (second table), and export to csv
simpsons[1].head().to_csv('wikiTable.csv')

