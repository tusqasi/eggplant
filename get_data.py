import pandas as pd
import random

SECONDS_IN_A_MINTUE = 60
genres  = [
    "happy",
    "groovy",
    "slow",
    "instrumental",
    "dramatic",
    "energetic",
    "melancholic", 
]
"""
songs list
1 id
2 name
3 genre
4 length
---
user list
1 id
2 name
3 song history 
"""
songs_df = pd.read_csv("./public_songs_export_2023-10-12_213331.csv")
n_songs,_  = songs_df.shape

songs_df.rename(columns={'uploaded_user_id':'genre'})
songs_df['length'] = [random.randint(120, SECONDS_IN_A_MINTUE*5) for _ in range(n_songs)]
exit()
users_df = pd.read_csv("./public_users_export_2023-10-12_212940.csv")
print(users_df)


