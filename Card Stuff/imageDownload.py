## Importing Necessary Modules
import requests # to get image from the web
import shutil # to save it locally

def main(url):
    filename = url.split("/")[-1]

    # Open the url image, set stream to True, this will return the stream content.
    r = requests.get(url, stream = True)

    if r.status_code == 200:
        r.raw.decode_content = True
        
        with open(filename,'wb') as f:
            shutil.copyfile(r.raw, f)
            
        print('Image sucessfully Downloaded: ',filename)
    else:
        print('Hit issue with URL sending to issueUrl.txt: ' + url)
        with open('issueUrl.txt', 'a') as f:
            f.write(url + '\n')
        f.close()