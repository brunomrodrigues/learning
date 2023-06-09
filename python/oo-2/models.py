class Program:
    def __init__(self, name, year):
        self._name      = name.title()
        self.year       = year
        self._likes     = 0

    @property
    def name(self):
        return self._name

    @name.setter
    def nome(self, new_name):
        self._name = new_name.title()

    @property
    def likes(self):
        return self._likes
    
    def give_like(self):
        self._likes += 1

class Movie(Program):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration   = duration
 
class Serie(Program):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons    = seasons

avengers = Movie("avengers - infinite war", 2023, 160)
avengers.give_like()
print(f'Name: {avengers.name} - {avengers.duration} - Likes: {avengers.likes}')

breakingbad = Serie("breaking bad", 2023, 8)
breakingbad.give_like()

print(f'Name: {breakingbad.name} - {breakingbad.seasons} - Likes: {breakingbad.likes}')
