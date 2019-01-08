from song import Song
from operator import attrgetter
import csv

class SongList:
    song = Song()

    def __init__(self):
        self.song_list = []

    def add_songs(self, new_song):
        self.song_list.append(new_song)
        return self.song_list

    def load_songs(self, csv_file):
        with open('songs.csv', 'r') as file:
            song_csv = csv.reader(file)
            for row in song_csv:
                if row[3] == 'n':
                    row[3] = True
                else:
                    row[3] = False
                song = Song(row[0], row[1], row[2], row[3])
                self.song_list.append(song)
        return self.song_list

    def sort_songs(self, sort_id):
        if sort_id == 0:
            attr_sort = 'title'
        elif sort_id == 1:
            attr_sort = 'artist'
        elif sort_id == 2:
            attr_sort = 'year'
        # sort list with key

        self.song_list.sort(key=attrgetter(attr_sort))
        return self.song_list # Returns the sorted list to the calling function

    def calculate_songs(self):
        song_amount = len(self.song_list)
        self.root.ids.song_count.rows = int(song_amount)
        return song_amount

    def mark_as_learned(self, input):
        for song in self.song_list:
            validate = song.__eq__(input)
            if validate == True:
                song.mark_learned()

    def calculate_song_learned(self):
        learn_count = 0
        for song in self.song_list:
            if song.learned == False:
                learn_count += 1
        return learn_count

    def calculate_song_not_learned(self):
        not_learn_count = 0
        for song in self.song_list:
            if song.learned == True:
                not_learn_count += 1
        return not_learn_count

    def save_songs(self):
        with open ('songs.csv', 'w') as out_file:
            for song in self.song_list:
                if song.learned == True:
                    learn_write = 'n'
                else:
                    learn_write = 'y'
                str_out = [song.title, song.artist, str(song.year), learn_write]
                csv_write = ','.join(str_out)
                out_file.write(str(csv_write)+'\n')
            out_file.close()

    def give_songs(self):
        return self.song_list

    def __eq__(self, btn_id):
        equal_check = '{}_{}'.format(self.song.title, self.song.year)
        result = (btn_id == equal_check)
        return result

    def __str__(self):
        print_str = ''
        for song in self.song_list:
            str_out = '{}, {}, {}, {}\n'.format(song.title, song.artist, song.year, song.learned)
            print_str += str_out
        return print_str