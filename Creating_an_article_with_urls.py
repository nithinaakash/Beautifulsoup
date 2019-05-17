#!/usr/bin/env python
# coding: utf-8

# In[31]:


from PIL import Image,ImageDraw,ImageFont
import requests
from bs4 import BeautifulSoup
import urllib
import urllib.request
import requests
import bs4
import io
url = 'https://blog.scrapinghub.com/'
with urllib.request.urlopen(url)as f:

    soup=bs4.BeautifulSoup(f)
    l=0

    for i in soup.findAll('img'):
        
        try:
            
            
            temp=i['alt']

            if("Blog featured image" in temp ): 
                
                print(i['src'])
                img_url=i['src']
                if(img_url[:1]=="/"):
                    img_url="https:"+img_url
                play=img_url
                imge = Image.open(requests.get(img_url, stream = True).raw)

                imge.save('one.png')
                imge=Image.open('one.png')
                width = 300
                height = 300

                im2 = imge.resize((width, height))
                im2.save('one1.png')
                break;
            break;
        
        except KeyError:
            pass
    iimg = Image.new('RGB', (1000,1000), color = 'white')
    iimg.save('white.png')
    print(iimg.size)
    k= soup.findAll('p')
    m=k[1].string
    image = Image.open('white.png')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('arial.ttf', size=23)
    color = 'rgb(0,0,0)'
    i=350;j=10;p=0;q=60
    while(j<200):
        
        (x,y)=(i,j)
        name=m[p:q]
        draw.text((x, y), name, fill=color, font=font)
        j=j+35
        p=p+60
        q=q+60
    h=soup.findAll('a')
    play=h[33].string
    i=351;j=220;p=0;q=58
    print("ASda")
    name= '"'
    draw.text((340, 220),name, fill=color, font=font)
    while(j<300):
        print("asdfas")
        (x,y)=(i,j)
        j=j+25
        name=play[p:q]
        draw.text((x, y), name, fill=color, font=font) 
        p=p+58
        q=q+58
    name='"'
    draw.text((430, 247),name, fill=color, font=font)
    image.save('final.png')
#     (x, y) = (350,10)
#     l=k[1].string
#     p=l[:70]
#     m=l[70:140]
#     print(p)
#     name = p
#     ' # white color
#     draw.text((x, y), name, fill=color, font=font)
#     draw.text((350,35), m, fill=color, font=font)
#     (x, y) = (350,150)
#     l=play
#     p=l[:40]
#     print(p)
#     name = p
#     color = 'rgb(0,0,0)' # white color
#     draw.text((x, y), name, fill=color, font=font)    
#     image.save('final.png')    
       
        
    large=Image.open('final.png')
    print(large.size)
    small=Image.open('one1.png') 
    print(small.size)
    large.paste(small,(0,0))
   
    print(play)
    large.save('jnk.png')
    print(23123)
    

url ='https://en.wikipedia.org/wiki/MS_Dhoni'
with urllib.request.urlopen(url)as f:
    soup=bs4.BeautifulSoup(f)
    h=soup.findAll('img')
    for i in h:
        
         if("Mahendra Singh Dhoni January 2016 (cropped).jpg"in i['alt']): 
                img_url=i['src']
                if(img_url[:1]=="/"):
                    img_url="https:"+img_url
                print(img_url)
                play2=img_url
                imge = Image.open(requests.get(img_url, stream = True).raw)
                imge.save('two.png')
                imge=Image.open('two.png')
                width = 300
                height = 300

                im2 = imge.resize((width, height))
                im2.save('two2.png')
    
    k=soup.findAll('p')
    m=k[46].string
    image = Image.open('jnk.png')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('arial.ttf', size=23)
    i=352;j=310;p=0;q=60
    while(j<510):
        
        (x,y)=(i,j)
        name=m[p:q]
        draw.text((x, y), name, fill=color, font=font)
        j=j+35
        p=p+60
        q=q+60
    h=soup.findAll('a')
    play=h[1152].string
    m=play
    i=345;j=520;p=0;q=58
    while(j<910):
        
        (x,y)=(i,j)
        name=m[p:q]
        draw.text((x, y), name, fill=color, font=font)
        j=j+35
        p=p+60
        q=q+60    
  
#     (x, y) = (350,350)
#     l=b.string
#     p=l[:45]
#     print(p)
#     name = p
#     color = 'rgb(0,0,0)' # white color
#     draw.text((x, y), name, fill=color, font=font)
#     (x, y) = (350,450)
#     l=play2
#     p=l[:40]
#     print(p)
#     name = p
#     color = 'rgb(0,0,0)' # white color
#     draw.text((x, y), name, fill=color, font=font)
    image.save('jnk2.png')
    large=Image.open('jnk2.png')
    print(large.size)
    small=Image.open('two2.png') 
    print(small.size)
    large.paste(small,(0,310))
    print(play2)
    large.save('jnk3.png')
    
    print(23123)
url ='https://www.forbes.com/sites/jaysondemers/2017/03/06/the-8-requirements-for-any-blog-to-be-successful/#1069ca3272ad'

with urllib.request.urlopen(url)as f:

    soup=bs4.BeautifulSoup(f)

    try:
        h=soup.findAll('img')
       
        
       
        for i in h:
           
            if("Jayson DeMers" in i['alt']):
                
                img_url=i['src']
                if(img_url[:1]=="/"):
                    img_url="https:"+img_url
                print(img_url)
                play3=img_url
                imge = Image.open(requests.get(img_url, stream = True).raw)
                imge.save('three.png')
                imge=Image.open('three.png')
                width = 300
                height = 300

                im2 = imge.resize((width, height))
                im2.save('three3.png')
    
                
                break;
            break;
                   
    except KeyError:
        pass

    k = soup.findAll('p')
    m=k[4].string
    image = Image.open('jnk3.png')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('arial.ttf', size=23)
    i=352;j=650;p=0;q=60
    while(j<810):
        
        (x,y)=(i,j)
        name=m[p:q]
        draw.text((x, y), name, fill=color, font=font)
        j=j+35
        p=p+60
        q=q+60
#     draw.text((350,650), name, fill=color, font=font)
#     (x, y) = (350,750)
    k=soup.findAll('a')
    m=k[141].string
    i=346;j=850;p=0;q=55
    name='"'+" "
    draw.text((337,850), name, fill=color, font=font)
    while(j<960):
        (x,y)=(i,j)
        name=m[p:q]
        draw.text((x, y), name, fill=color, font=font)
        j=j+35
        p=p+55
        q=q+55
    name='"'
    draw.text((550,880), name, fill=color, font=font)
    
    image.save('jnk4.png')
    large=Image.open('jnk4.png')
    print(large.size)
    small=Image.open('three3.png') 
    
    print(small.size)
    large.paste(small,(0,650))
    print(play3)
    large.save('finale3.png')
    large.show()
  
      


# In[ ]:





# In[ ]:




