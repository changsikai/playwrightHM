import ddddocr
from wx.lib.agw.ribbon import panel

ocr = ddddocr.DdddOcr()
with open('3.jpg', 'rb') as f:
    img_bytes = f.read()
result = ocr.classification(img_bytes)
print(result)
import wx

app = wx.App(False) #创建1个APP，禁用stdout/stderr重定向
frame = wx.Frame(None, wx.ID_ANY, "Hello, World!")  #这是一个顶层的window
frame.Show(True)    #显示这个frame
bmp = wx.Bitmap('3.jpg')
sb = wx.StaticBitmap(panel, -1, bmp, pos=(280, 10))
app.MainLoop()