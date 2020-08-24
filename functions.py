# Chapter 8 Problems.
# Problem 8-1: Write a function that accepts the name of your favorite radio station & 
# Prints a message saying something like "Let me tune in <inputted radio station>."
# Then, ask the user for their favorite radio station and store the inputted value in a variable.
# Call the function you wrote above and pass the value that was inputted.
 
def favorite_radio(station):
    """ Takes favorite radio station name as input.
 
        Returns 'Let me tune in < radio station > radio station'.
        """
    return('Let me tune in ', + (station) + ' radio station.')
 
 
 
# Problem 8-2: Write a function called "print_business_cards" that accepts name, quantity, and tag line information as parameters.
 
# The function should print out a message stating how many business cards you are printing, who they are for, and the tag line that will appear on each card.
 
# Call the function three times passing different arguments to it.
 
def print_business_cards(name, quantity, tagline):
 
    """ Function takes 3 arguments.
 
         Function prints out message detailing how many business cards
         you are printing, who they are for, and the tag line that will
         appear on each card.
 
         Parameters:
                             <name>, <quantity>, <tagline>
 
         """
    return('You re printing ' + str(quantity) + ' cards for ' + name +  ' with tagline: ' + str(tagline))
 
 
 
# Problem 8-3: Re-write the function in problem 8-2 so that the default quantity of business cards ordered by default is 100.
 
# Call the re-written function twice, once by passing a quantity of 150 and once by not passing quantity information.
 
def hundred_business_cards(name, tagline, quantity=100):
 
    """ Function takes 3 arguments.
 
         Function prints out message detailing how many business cards
         you are printing, who they are for, and the tag line that will
         appear on each card.
 
         Parameters:
                             <name>, <quantity>, <tagline>
 
         """
    return('You re printing ' + str(quantity) + ' cards for ' + name + ', with tagline: ' + tagline)
 
business_cards = print_business_cards("Mo'd Karim", 150, 'Writing good code is my long time goal.')
hundred_cards = hundred_business_cards('Richard Branson', 'Projecting the travel industry to the next level.')
print('Printing an instance of print_business_card function:' + '\n'+ business_cards)
print('Printing an instance of hundred_cards function:' + '\n'+ hundred_cards)
 
# Problem 8-4: Write a function that accepts song information specifically song title and artist.
#
# Make the default artist set to "Unknown" by default.
#
# This function should return a formatted string that looks like this: 
# 
#"<song name> by <artist name>."
#
# Call the function you just created three times.
#
# Make sure that at least one of the times, you don't pass artist information.
#
# Print out the result you get from each function.
 
 
def song_info(title, artist = 'Unknown'):
    """song_info:
          
            Function takes 2 arguments.
        Return:
                neatly formatted string <song title> by <artist_name>.                
 
        Parameters:
                <title>, <artist>
 
            """
 
    if title:
        try:
            return (str(title) + ' by ' + artist)
        except:
            return ('Please enter a string')
    else:
        return ('You entered a blank string.')
 
 
# Calls to function
title_unknownartist = song_info('Walk it Talk it')
print('Making an instance of the song_info function supplying 1.:\n' + title_unknownartist)
 
title_artist = song_info('Hallo', 'Beyonce')
another_title_artist = song_info('Cold', 'Maroon 5')
print('Making other instances of the song_info function and printing.:\n' + title_artist + '\n' + another_title_artist)
 
# Problem 8-5:
# Modify the program you created in problem 8-4.
# So that it returns a dictionary item in the format we've studied instead of a string.
 
def a_song_dictionary(title, artist_name = 'Unknown'):
    """ display_song_dict:
          
            Function takes 2 arguments.
 
            Second argument  set to Unknown as default.
                                                                        
            Function prints out song title and artist information.
 
        Parameters:
            <title>, <artist_name>
 
            """
    if title:
            try:
                # Return a dictionary.
                return_output = {'Title': str(title), 'Artist': artist_name}
                return return_output
            except:
                return ('Please enter a string')
    else:
        return ('Title cannot be left blank.')
 
# Introduce a function that will loop through a list of dictionaries  
# containing song information and print out each entry 
# (note: you may not print dictionary items directly).
 
def loop_through_list_of_dictionaries(list_of_dictionaries):
 
     ''' NAME:
             loop_through_list_of_dictionaries:
        Arguments:
            Takes 1 Argument
        Parameter: 
            <A list of dictionaries> .
                                                                                                
        Return:
            < key : value > objects as a string.
          '''
     if list_of_dictionaries and type(list_of_dictionaries) == list:
        for dictionary in list_of_dictionaries:
            print(dictionary['Title'] + ' by ' + dictionary['Artist'])
     else:
        return
 
# Next, create an empty list called "playlist" and introduce a while loop 
# where users are asked for items to add to the playlist.
# Be sure to ask for artist and song information.
# Store them as a dictionary using your function.
# and add them to your playlist.
# Create empty list
playlist = []
 
# While loop flag to keep things from getting out of control.
active = True
 
# While condition is True.
while active:
 
    #  Ask for song title and artist information
    song_title = input('Enter title: ')
    artist = input('Enter artist info: ')
 
    # Create an instance of a_song_dictionary.
    # Pass it the user input from  while loop.
    song_dict =  a_song_dictionary(song_title, artist)
 
    # Append instance of a_song_dictionary to empty list.
    playlist.append(song_dict)
 
    # Offer user a chance to save more music or exit the program.
    save_more_songs = input('Add more songs to playlist (Y/N): ')
    if save_more_songs.lower() == 'y':
        active = True
    else:
        active = False
 
 
 
print(playlist, '\n')
 
print('Looping through dictionaries:')
loop_through_dictionary = loop_through_list_of_dictionaries(playlist)


