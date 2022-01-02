# poolbooru_gelscraper
a simple python script for scraping images off gelbooru pools.

by default saves files without extensions so for windows you will need to set whatever file type you want in the code, the file names will be the image ID gelbooru uses by defualt

use forward slashes (just for consistency, I hate how windows uses backslashes)

wont make directories recursively (might fix this in later versions) so for /home/user/Desktop/waifus/emilia_re_zero it will only make the last emilia_re_zero folder and start downloading all the pool images in there.

if all your folders go in waifus folder in your Desktop you can set pwd in the code to /home/user/Desktop/waifus

ja ne!
