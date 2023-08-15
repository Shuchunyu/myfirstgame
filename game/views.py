from django.http import HttpResponse

def index(request):
    line1 = '<h1 style = "text-align: center">狂扁小朋友</h1>'
    line2 = '<img src = "https://i.ssjz8.com/upload/1/img2.baidu.com%2Fit%2Fu%3D137719425%2C2773523159%26amp%3Bfm%3D253%26amp%3Bfmt%3Dauto%26amp%3Bapp%3D138%26amp%3Bf%3DJPEG%3Fw%3D480%26amp%3Bh%3D272" width = 1500>'
    return HttpResponse(line1 + line2)
