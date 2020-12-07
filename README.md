Note for development:

We think we can visualize multiple seasons but not multiple leagues at the same time.

This means at the beginning of the visualization initialization, we have to have users tell us what season(s) and leage they want to visualize.

The data is in "points" form -- which means there is no elimination. This is good news because it means we don't have to handle consollation rounds.

There doesn't have to be order to the point placement and movement.

Each rectangular node would be the same color across all other matches during that season to present it as the same in case they choose multiple seasons to visualize.

We need some indication of a win -- whether that is to make a line longer, bold the line, or something in the rectangle. We need to visually see WHO won.

For people that are going to use the tool, they're likely to be soccer people -- so we need for them a way to follow the team(s) they're interested in analyzing.

How to visually show one team? Either a filter or within the visual they should be relatively easily spottable. Perhaps we can do logos as cirlces inside of the rectangles.

Potentially we can do a number for a line to represent the margin of win, but this may make it too busy.

Also potentially -- we could do left to right representation such that the team that is at the top most line of the graph has won the most and the match at the bottom has lost
the most. We need to think about this more.

FINAL NOTE:

matches.json and player_attr.csv are either incomplete or don't exist plesae downlaod from the sql lite db that the documentation tells you the data is avalilable in for the visual to fully work
