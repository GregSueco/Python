colours = ["red", "orange", "green", "violet", "blue", "yellow"]

def pick_colours(palette,number_of_colours):
    chosen_palette = []
    counter = 0
    while counter < number_of_colours:
        chosen_palette.append(palette[counter])
        counter += 1
    return chosen_palette

print(pick_colours(colours,-1))~