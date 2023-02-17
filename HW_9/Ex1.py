import time
from progress.bar import IncrementalBar
import emoji

mylist = [1, 2, 3, 4, 5, 6, 7, 8]

bar = IncrementalBar('Countdown', max=len(mylist))

for item in mylist:
    bar.next()
    time.sleep(0.2)

bar.finish()

print(emoji.emojize('Python is :thumbs_up:'))