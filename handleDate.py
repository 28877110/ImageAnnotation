#coding:utf-8
import json
from PIL import Image
import os


def loadjson(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
        return data

def writefile(date):
    with open('./date.txt','a',encoding= 'utf8') as f:
        f.write(date)

mark = 'car'
carmark = 'bentian'
path = './image'
parents = os.listdir(path)
parents.sort()
extensions = ['.jpeg', '.jpg', '.png', '.bmp']
imgjsons = []
img = []
allfilename =[]

i = 0
for parent in parents:
    if  parent.lower().endswith('.jpg'):
        filename = os.path.splitext(parent)[0]
        print(filename)
        fileimg = filename+'.jpg'
        print("文件名：",fileimg)
        filejson = filename+'.json'
        if os.path.exists(os.path.join(path,filejson)):
            img = Image.open(os.path.join(path,fileimg))

            # img.show()
            width  = img.size[0]
            height = img.size[1]
            widthscal  = 600/width
            heightscal = 600/height
            print("原始大小",width,height)
            scalTime = min(widthscal,heightscal)
            print('scalTime::',scalTime)
            jsondata = loadjson(os.path.join(path,filejson))
            startpointx = jsondata[mark]['startpointx']
            startpointy = jsondata[mark]['startpointy']
            endpointx   = jsondata[mark]['endpointx']
            endpointy   = jsondata[mark]['endpointy']
            print(startpointx,startpointy,endpointx,endpointy)
            x1 = round(min(startpointx,endpointx)/scalTime)
            x2 = round(max(startpointx,endpointx)/scalTime)
            y1 = round(min(startpointy,endpointy)/scalTime)
            y2 = round(max(startpointy,endpointy)/scalTime)
            print(int(x1),int(y1),int(x2),int(y2))
            writefile(fileimg+' ')
            writefile(mark +' ')
            writefile(str(x1)+' ')
            writefile(str(y1)+' ')
            w=x2-x1
            writefile(str(x2)+' ')
            h=y2-y1
            writefile(str(y2)+'\n')

