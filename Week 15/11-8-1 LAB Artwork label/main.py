# Define the Artist class in Artist.py with a constructor to initialize an artist's information. The constructor '
# 'should by default initialize the artist')s name to "unknown" and the years of birth and death to -1.
#
# Define the Artwork class in Artwork.py with a constructor to initialize an artwork('s information. '
# ('The constructor should by default initialize the title to "unknown", the year created to -1, and the artist to use '
# 'the Artist default constructor parameter values. Add an import statement to import the Artist class.))
#
# Add import statements to main.py to import the Artist and Artwork classes.


from Artist import Artist
from Artwork import Artwork

# TODO: Import Artist from Artist.py and Artwork from Artwork.py

if __name__ == "__main__":
    user_artist_name = input()
    user_birth_year = int(input())
    user_death_year = int(input())
    user_title = input()
    user_year_created = int(input())

    user_artist = Artist(user_artist_name, user_birth_year, user_death_year)

    new_artwork = Artwork(user_title, user_year_created, user_artist)

    new_artwork.print_info()
