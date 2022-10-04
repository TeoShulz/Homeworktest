# (function(){
#   function downloadString(text, fileType, fileName) {
#     var blob = new Blob([text], { type: fileType });
#     var a = document.createElement('a');
#     a.download = fileName;
#     a.href = URL.createObjectURL(blob);
#     a.dataset.downloadurl = [fileType, a.download, a.href].join(':');
#     a.style.display = "none";
#     document.body.appendChild(a);
#     a.click();
#     document.body.removeChild(a);
#   }
#   downloadString(Array.from(document.querySelectorAll('.audio_row')).map(el => {
#       const title = el.querySelector('.audio_row__title_inner');
#       const artist = el.querySelector('.audio_row__performers');
#       return `${artist.innerText} - ${title.innerText}`
#   }).join('\n'), 'text', 'audio.txt');
# })();
# Парсинг вк

# Парсинг спотика через бс
# Type__TypeElement-goli3j-0 jsusuc VrRwdIZO0sRX1lsWxJBe
import bs4
from bs4 import BeautifulSoup

with open('spisok', encoding='utf-8') as file:
    src = file.read()
    # try:
    #     print(src)
    # except UnicodeDecodeError:
    #     pass
soup = BeautifulSoup(src, 'lxml')
name_of_song = soup.find_all('div', class_='Type__TypeElement-goli3j-0 gwYBEX t_yrXoUO3qGsJS4Y6iXX standalone-ellipsis-one-line')
# print(name_of_song)

name_of_artist = soup.find_all('span', class_='Type__TypeElement-goli3j-0 eDbSCl rq2VQ5mb9SDAFWbBIUIn standalone-ellipsis-one-line')
# print(name_of_artist)
name_of_song_clear = []
name_of_artist_clear = []
for item in name_of_song:
    name_of_song_clear.append(item.text)

for item in name_of_artist:
    name_of_artist_clear.append(item.text)

songs_list = zip(name_of_song_clear, name_of_artist_clear)
count = 0
for i in songs_list:
    count += 1
    print('{} - {}'.format(i[0], i[1]))


# class ="Type__TypeElement-goli3j-0 eDbSCl rq2VQ5mb9SDAFWbBIUIn standalone-ellipsis-one-line" > < a draggable="true" dir="auto" href="/artist/44L2bdEufrpXM5S7yn30JJ" tabindex="-1" > Кишлак < / a > < / span >
#

# songs = dict()
#
# for i in range(len(name_of_song)):
# #     songs.values()
#
# print(songs)

# <div dir="auto" class="Type__TypeElement-goli3j-0 gwYBEX t_yrXoUO3qGsJS4Y6iXX standalone-ellipsis-one-line" aria-expanded="false">УБРАЛО (prod. by UnKnown)</div>