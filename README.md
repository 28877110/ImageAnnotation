# Image Annotation Tool 

---
图像标定工具，主要针对一张图标定同一个标记，标完会在同级目录下生成json文件储存标记位置。   
用pyqt5写的。
---

在你使用之前,得先安装pyqt5和pillow
```
pip install pyqt5
pip install Pillow
```
运行程序

```
python3 main.py
```
快捷键：A是前一张图片，D是后一张图片   
标记完图片之后  
运行

```
python3 handleDate.py
```
得到data.txt 就是你所有图片的标注信息了。
