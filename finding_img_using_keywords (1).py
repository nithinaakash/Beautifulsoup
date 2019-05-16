#!/usr/bin/env python
# coding: utf-8

# In[5]:


from PIL import Image
import requests
import bs4
import urllib 
import urllib.request
import io
import ssl
url = 'https://blog.scrapinghub.com/'
ssl._create_default_https_context = ssl._create_unverified_context
with urllib.request.urlopen(url)as f:

    soup=bs4.BeautifulSoup(f)
    l=0
    for i in soup.findAll('img'):
        try:

            print(i)
            print(i['alt'])

            print(i['src'])
            temp=i['alt']

            if("Blog featured image" in temp ):  
                print(i['src'])
                img_url=i['src']
                if(img_url[:1]=="/"):
                    img_url="https:"+img_url

                imge = Image.open(requests.get(img_url, stream = True).raw)

                imge.save(str(l)+'.png')
                l=l+1

        except KeyError:
            pass
#     if(i['alt']=="HubSpot Logo"):
#          print(i['alt'])
        
# im.save('out.png')

# imge = Image.open(requests.get(image_url, stream = True).raw)


# In[ ]:





# In[ ]:





# In[ ]:




