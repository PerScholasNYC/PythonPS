#creating a class
class Song(object):
#creating the attributes
    def _init_(self, lyrics):
        self.lyrics = lyrics
#creating the methods
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
#intializing instance for that class
happy_bday = Song(["Happy birthday to you",
                    " I don't want to get sued",
                    "So I'll stop right there"])
#intializing instance for that class
bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full or shells"])

#calling the function for that instance
happy_bday.sing_me_a_song()

#calling the function for that instance
bulls_on_parade.sing_me_a_song()
