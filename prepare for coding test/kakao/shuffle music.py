# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import codecs
import random
from collections import defaultdict



def shuffleSong(song):
        
    lineup = {}

    variation = .25 


    for artist in song:
    
        songs = song[artist]
        random.shuffle(songs)
   
        spread = 1/len(songs)
 
        artist_variation = random.uniform(0, spread-variation)

        for i,j in enumerate(songs):
            
            song_variation = random.uniform(0,spread*variation)
            
            lineup[j] = i*(spread) + artist_variation + song_variation
            
    return sorted(lineup, key = lineup.get)

#################################################################################################

lines = codecs.getreader('utf-8')(sys.stdin.detach()).readlines()

data = []

t = int(lines.pop(0))

for _ in range(t):
    
    music = lines.pop(0)
    music_list = [i.replace('\n','') for i in music.split('\t')]
    
    artist = lines.pop(0)
    artist_list = [i.replace('\n','') for i in artist.split('\t')]
    
    songs = defaultdict(list)
    
    for i,j in zip(music_list,artist_list):
    
        songs[j].append(i)
    
    

    playlist = '\t'.join([''.join(i) for i in shuffleSong(songs)])
    sys.stdout.write(playlist)
    sys.stdout.write('\n')