class Playlist:
    def __init__(self, name, programs):
        self.name      = name
        self._programs = programs

    @property
    def programs_list(self):
        return self._programs  

    def __len__(self):
        return len(self._programs)

    def __getitem__(self, item):
        return self._programs[item]

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

    def __str__(self):
        return ((f'Name: {self.name} - Likes: {self.likes}')) 

class Movie(Program):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration   = duration
    
    def __str__(self):
        return ((f'Name: {self.name} - Year: {self.year} - Duration: {self.duration} - Likes: {self.likes}')) 
 
class Serie(Program):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons    = seasons
    
    def __str__(self):
        return ((f'Name: {self.name} - Year: {self.year} - Seasons: {self.seasons} - Likes: {self.likes}')) 

avengers = Movie("avengers - infinite war", 2023, 160)
avengers.give_like()

breakingbad = Serie("breaking bad", 2023, 8)
breakingbad.give_like()

walkingdead = Serie("walking dead", 2020, 11)
walkingdead.give_like()

shining = Movie("shining", 1989, 120)
shining.give_like()

shining1 = Movie("shining", 1989, 120)
shining1.give_like()

movies_series = [avengers, breakingbad, shining, walkingdead, shining1]

playlist = Playlist("Weekend", movies_series)
print(f'Avenger is in playlist? {avengers in playlist}')
print(f'Playlist size {len(playlist)}')
for program in playlist:
    print(program)