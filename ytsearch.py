# install by 'pip install youtube-search-python'
from youtubesearchpython import SearchVideos

menoob = input("What to search? \n")
search = SearchVideos(f"{menoob}", offset = 1, mode = "dict", max_results = 10)
mi = search.result()
noob = ""
most = mi['search_result']
for mio in most:
    kek = mio['link']
    stark_name = mio['title']
    fridayz = mio['id']
    total_stark = mio['duration']
    starks = mio['views']
    stark_chnnl = mio['channel']
    noob += (f"VIDEO-TITLE ➠ {stark_name} \n" 
                     f"LINK ➠ {kek} \n" 
                     f"CHANNEL ➠ {stark_chnnl} \n" 
                     f"DURATION ➠ {total_stark} \n"
                     f"TOTAL-VIEWS ➠ {starks} \n\n")
print(noob)
