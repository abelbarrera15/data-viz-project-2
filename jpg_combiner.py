import json
import pandas as pd
from PIL import Image

with open("./data/match.json") as f:
    df_unique_match_ups = pd.json_normalize(json.load(f))[
        ['home_team_api_id', 'away_team_api_id']].drop_duplicates()

team_names = pd.read_csv(
    './data/team.csv', sep=',')[['team_api_id', 'team_long_name']]

team_names.rename(
    columns={'team_api_id': 'home_team_api_id'}, inplace=True)


df_unique_names_combos = df_unique_match_ups.merge(
    team_names, on='home_team_api_id', how='left')

team_names.rename(
    columns={'home_team_api_id': 'away_team_api_id'}, inplace=True)

df_unique_names_combos.rename(
    columns={'team_long_name': 'home_team_name'}, inplace=True
)

df_unique_names_combos = df_unique_names_combos.merge(
    team_names, on='away_team_api_id', how='left')

df_unique_names_combos.rename(
    columns={'team_long_name': 'away_team_name'}, inplace=True
)

for iter in df_unique_names_combos[['home_team_name', 'away_team_name']].values.tolist():

    images = [Image.open(x) for x in ['./team_logos/' +
                                      iter[0]+'.png', './team_logos/'+iter[1]+'.png']]
    widths, heights = zip(*(i.size for i in images))

    total_width = sum(widths)
    max_height = max(heights)

    new_im = Image.new('RGBA', (total_width, max_height))

    x_offset = 0
    for im in images:
        new_im.paste(im, (x_offset, 0))
        x_offset += im.size[0]

    new_im.save('./match_banners/'+str(iter[0])+str(iter[1])+'.png')
