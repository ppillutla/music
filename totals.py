# todo: dont hardcode these next few lines; get this from the dataset
listens = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1] # fixme: this should be a generated list from maxListens to 1
listens_to_num_albums = {12: 1,
                         11: 1,
                         10: 0,
                         9: 3,
                         8: 2,
                         7: 2,
                         6: 3,
                         5: 5,
                         4: 18,
                         3: 47,
                         2: 295,
                         1: 375, } # fixme: this should all come from calculations based off the data set (aka the listening log)

total_albums = sum(listens_to_num_albums.values())

# copy the listens to albums map to initialize the percents of listens map because we want the same keys
pct_of_total_listens = listens_to_num_albums.copy()

start = max(listens_to_num_albums.keys()) # fixme: if we have a maxListens val that we use on line 2, we can eliminate this calculation
# this line inits the base case for the pcts map
pct_of_total_listens[start] = 100 * (listens_to_num_albums[start] / total_albums)

# loop through the listens values to calculate the percent of total listens for each listen count 
for i in range(start - 1, 0, -1):
    pct_of_total_listens[i] = 100 * ((listens_to_num_albums[i] + listens_to_num_albums[i + 1]) / total_albums)
