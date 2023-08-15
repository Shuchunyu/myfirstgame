from django.http import HttpResponse

def index(request):
    line1 = '<h1 style = "text-align: center">狂扁小朋友</h1>'
    line4 = '<hr>'
    line3 = '<a href = "/play/"> 开始游戏 </a>'
    line2 = '<img src = "https://i.ssjz8.com/upload/1/img2.baidu.com%2Fit%2Fu%3D137719425%2C2773523159%26amp%3Bfm%3D253%26amp%3Bfmt%3Dauto%26amp%3Bapp%3D138%26amp%3Bf%3DJPEG%3Fw%3D480%26amp%3Bh%3D272" width = 1700>'
    return HttpResponse(line1 + line3 + line2)

def play(request):
    line1 = '<h1 style = "text-align: center">游戏界面</h1>'
    line3 = '<a href = "/"> 返回主界面 </a>'
    line2 = '<img src = "https://www.xiaohei.com/d/file/zhuantiheji/haowan/2019-09-21/46de7021e3f869eb6c0ad3850b2c8591.jpg" width = 1700>'
    return HttpResponse(line1 + line3 + line2)
