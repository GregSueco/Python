def show_progress(how_many,character = '*'):
    while how_many:
        print(character)
        how_many -= 1

show_progress(10)
show_progress(15)
show_progress(30)
 
show_progress(10, '-')
show_progress(15, '+')