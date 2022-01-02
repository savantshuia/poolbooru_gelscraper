import os
from requests_html import HTML, HTMLSession

pwd = '' 
#enter a dir if you are storing all your images in one dir with different folders, if not enter full path of the location in the input dir_name
dir_name = input(' enter the name of the folder/directory')
pool_id = int(input(' enter gelbooru pool id'))
page_id = 0
extension = '' # '.png' '.jpeg' '.jpg'
i = j = 1
images_downloaded = 0

if os.path.isdir(pwd + dir_name):
    pass
else:
    os.mkdir(pwd + dir_name)

session = HTMLSession()

req = session.get(f"https://gelbooru.com/index.php?page=pool&s=show&id={pool_id}&pid={page_id}")

req_html = req.html

thumbnails_div = req_html.find('.thumbnail-container', first=True)


while i + j != 0:
    j*= -1
    for span in thumbnails_div.find('span'):
        i*= -1
        image_id = span.attrs['id'][1::] #p2826155 --> 2826155 to be able to use &id=2826155
        post = session.get(f"https://gelbooru.com/index.php?page=post&s=view&id={image_id}")    
        post_html = post.html
        for hyperlink in post_html.find('a'):
            if hyperlink.text.lower() == "original image":
                image = hyperlink.attrs['href']
                image_content = session.get(image)
                with open(dir_name + f'/{image_id}{extension}', 'wb') as f:
                    f.write(image_content.content)
                    images_downloaded += 1

    page_id += images_downloaded

    req = session.get(f"https://gelbooru.com/index.php?page=pool&s=show&id={pool_id}&pid={page_id}")

    req_html = req.html

    thumbnails_div = req_html.find('.thumbnail-container', first=True)