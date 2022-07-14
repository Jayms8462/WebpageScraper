## Importing Necessary Modules
import requests # to get image from the web
import shutil # to save it locally
import time

## Set up the image URL and filename
image_url = [
]

def main(url, idx):
    filename = url.split("/")[-1]

    # Open the url image, set stream to True, this will return the stream content.
    r = requests.get(url, stream = True)

    # Check if the image was retrieved successfully
    if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True
        
        # Open a local file with wb ( write binary ) permission.
        with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)
            
        print('Image sucessfully Downloaded: ',filename)
    else:
        print('Hit issue with URL sending to issueUrl.txt: ' + url)
        with open('issueUrl.txt', 'a') as f:
            f.write(url + '\n')
        f.close()

def tryAgain(url, idx):
    idx += 1
    if idx < 4:
        print('Hit issue with ', url, '. Trying again')
        time.sleep(10)
        main(url, idx)
    else:
        print('Hit issue with URL sending to issueUrl.txt: ' + url)
        with open('issueUrl.txt', 'a') as f:
            f.write(url + '\n')
        f.close(url)

for url in image_url:
    idx = 0
    try:
        main(url, idx)
    except:
        tryAgain(url, idx)