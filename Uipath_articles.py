#!/usr/bin/env python
# coding: utf-8

# In[29]:


import xml.etree.ElementTree as ET
from PIL import Image,ImageDraw,ImageFont
import requests
from bs4 import BeautifulSoup
import urllib
import urllib.request
import requests
import bs4
import io
from xml.dom.minidom import parse
import xml.dom.minidom

DOMTree = xml.dom.minidom.parse("xml_config.xml")
collection = DOMTree.documentElement
q=0

font = ImageFont.truetype('arial.ttf', size=23)
color = 'rgb(95,158,60)'
name = collection.getElementsByTagName("title")
li=[line for line in open('hello2.csv')]
iimg = Image.new('RGB', (1000,1000), color = 'white')
iimg.save('white100.png')

g=0
for m in name:
 
    if m.hasAttribute("url"):
        type = m.getElementsByTagName('image')[0]
        app=m.getElementsByTagName('div')[0]
        a=m.getAttribute("url")
        print(str(a))
        if( str(a) in li[0] ):
            alt=type.getAttribute("class")
            hyper=app.getAttribute("id")
            with urllib.request.urlopen(li[0])as f:
                soup=bs4.BeautifulSoup(f)
                data = soup.find('div',attrs={'class':alt})
                o=data['style']
                print(data['style'])
                x=o.find("https")
                y=o.find(".jpg")
#                     print(o.find(".jpg"))
#                     print(o[x:y+4])
                img_url=o[x:y+4]
                print(img_url)
               
                imge = Image.open(requests.get(img_url, stream = True).raw)
                imge.save('one.png')
                imge=Image.open('one.png')
                width = 300
                height = 300
                im2 = imge.resize((width, height))
                im2.save('one1.png')
                    
            image = Image.open('white100.png')
            draw = ImageDraw.Draw(image)
            font = ImageFont.truetype('arial.ttf', size=23)
            color = 'rgb(95,158,60)'
            i=352;j=10;p=0;q=58
            name= '"'+"  "
            g=0
            k=soup.findAll('p')
            l="s"
            for i in k:
                am=i.text
                g=g+1
                if(g==16):
                    l=am
#     
            print(l)
            
                
            h=soup.find('h1')
            for i in h:
                am=i.text
                 
            print(am)
            draw.text((340, 10),name, fill=color, font=font)
            draw.text((352,10), am, fill=color, font=font) 
            name='"'
            draw.text((895, 10),name, fill=color, font=font)
            color = 'rgb(0,0,0)'
            
            
            i=350;j=70;p=0;q=58
            while(j<275):

                (x,y)=(i,j)
                m=l[p:q]
                draw.text((x, y), m, fill=color, font=font)
                j=j+35
                p=p+58
                q=q+58
            image.save('final.png')

            large=Image.open('final.png')
            
            small=Image.open('one1.png') 
           
            large.paste(small,(0,0))

            
            large.save('jnk.png')
        if(str(a) in li[1]):
            print(str(a))
            print(li[1])
            print(9090)
            alt=type.getAttribute("class")
            hyper=app.getAttribute("id")
            with urllib.request.urlopen(li[1])as f:
                soup=bs4.BeautifulSoup(f)
                data = soup.find('div',attrs={'class':alt})
                o=data['style']
                print(data['style'])
                x=o.find("https")
                y=o.find(".jpg")

                img_url=o[x:y+4]
                print(img_url)
               
                imge = Image.open(requests.get(img_url, stream = True).raw)
                imge.save('one.png')
                imge=Image.open('one.png')
                width = 300
                height = 300
                im2 = imge.resize((width, height))
                im2.save('two.png')
            image = Image.open('jnk.png')
            draw = ImageDraw.Draw(image)
            font = ImageFont.truetype('arial.ttf', size=23)
            
            color = 'rgb(95,158,60)'
            new=soup.find('h1')
            am=new.text
            name='"'    
            
            draw.text((340,320), name, fill=color, font=font)
            draw.text((350,320), am, fill=color, font=font)
            name='"'
            draw.text((885,320), name, fill=color, font=font)
            love="dadasd"
            f=soup.findAll('p')
            g=0
            for pu in f:               
                g=g+1
                
                if(g==4):
                    print(pu.text)
                    love=pu.text
#                     
            print(love)
            m=love
            color = 'rgb(0,0,0)'
            i=345;j=380;p=0;q=58
            while(j<600):

                (x,y)=(i,j)
                name=m[p:q]
                draw.text((x, y), name, fill=color, font=font)
                j=j+35
                p=p+58
                q=q+58
            image.save('jnk2.png')
            large=Image.open('jnk2.png')
            print(large.size)
            small=Image.open('two.png') 
            print(small.size)
            large.paste(small,(0,310))
           
            large.save('jnk3.png')
        if(str(a) in li[2]):
            alt=type.getAttribute("class")
            hyper=app.getAttribute("id")
            with urllib.request.urlopen(li[2])as f:
                soup=bs4.BeautifulSoup(f)
                data = soup.find('div',attrs={'class':alt})
                o=data['style']
                print(data['style'])
                x=o.find("https")
                y=o.find(".jpg")

                img_url=o[x:y+4]
                print(img_url)
               
                imge = Image.open(requests.get(img_url, stream = True).raw)
                imge.save('one.png')
                imge=Image.open('one.png')
                width = 300
                height = 300
                im2 = imge.resize((width, height))
                im2.save('three3.png')
        image = Image.open('jnk3.png')
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype('arial.ttf', size=23)
        color = 'rgb(95,158,60)'
        data = soup.findAll('div',attrs={'class':hyper})
        h=soup.find('h1')
        play=h.text
       
        i=355;j=650;p=0;q=55
        name='"'+"  "
        draw.text((345,650), name, fill=color, font=font)
        draw.text((355,650), play, fill=color, font=font) 
        name='"'
        draw.text((835,650), name, fill=color, font=font)
        color = 'rgb(0,0,0)'
        k = soup.findAll('p')
        g=0
        for goal in k:
            g=g+1
            if(g==15):
                balel=goal.text
        last=balel
        i=352;j=720;p=0;q=60
        while(j<930):

            (x,y)=(i,j)
            names=last[p:q]
            draw.text((x, y), names, fill=color, font=font)
            j=j+35
            p=p+60
            q=q+60

        image.save('jnk4.png')
        large=Image.open('jnk4.png')
        print(large.size)
        small=Image.open('three3.png') 

        print(small.size)
        large.paste(small,(0,650))
       
        large.save('UIPath_article.png')

            

          
                            
                

        


# In[ ]:





# In[ ]:





# In[ ]:




