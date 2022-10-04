from django.shortcuts import render
from . import pool
import json
from . import AdminLoginController
from urllib.parse import unquote
from django.http import JsonResponse
adminemail=''
def AddBlog(request):
    try:
      admindata = unquote(request.GET['admindata'])
      # admindata = admindata.replace("27", "\"")
      # admindata = json.loads(admindata)
      global adminemail
      adminemail=admindata[1:]
      print('xxxx : ',adminemail)
      return render(request,'Addblog.html')
    except Exception as e:
      print(e)
      return render(request,'Adminlogin.html')

def Submit_Blog(request):
  try:
    DB,CMD=pool.ConnectionPooling()
    blogtype=request.POST['blogtype']
    description=request.POST['description']
    blogimage=request.FILES['blogimage']
    title=request.POST['title']
    print('xxx',adminemail)
    email=str(adminemail)
    print('bbb',email)
    Q="insert into addblog(blogtype,description,title,emailid,blogimage) values('{0}','{1}','{2}','{3}','{4}')".format(blogtype,description,title,email,blogimage.name)
    F = open("e:/Blogwebsite/assets/" + blogimage.name, 'wb')
    for chunk in blogimage.chunks():
      F.write(chunk)
    F.close()
    CMD.execute(Q)
    DB.commit()
    DB.close()
    return render(request,'Addblog.html',{'message':'Record Submitted'})

  except Exception as e:
      print("Error",e)
      return render(request, 'Addblog.html', {'message': 'Fail to Submit record'})

def Display_All_Blog(request):
    try:
      DB, CMD = pool.ConnectionPooling()
      email = str(adminemail)
      print('xxxx',adminemail)
      Q = "select * from addblog where emailid='{0}'".format(email)
      print(Q)
      CMD.execute(Q)
      records = CMD.fetchall()
      # print(records)
      DB.close()
      return render(request, 'DisplayBlog.html', {'records': records})

    except Exception as e:
      return render(request, 'DisplayBlog.html', {'records', None})


def Edit_Blog(request):
  try:
    DB, CMD = pool.ConnectionPooling()
    id = request.GET['id']
    print(id)
    description = request.GET['description']
    title = request.GET['title']
    blogtype= request.GET['blogtype']
    email = str(adminemail)
    Q ="update addblog set description='{0}',title='{1}',blogtype='{2}',emailid='{3}' where id='{4}'".format(description,title,blogtype,email,id)
    print(Q)
    CMD.execute(Q)
    DB.commit()
    DB.close()
    return JsonResponse({'result': True}, safe=False)
  except Exception as e:
    print("Error :", e)
    return JsonResponse({'result': False}, safe=False)

def Delete_Blog(request):
  try:
    DB,CMD=pool.ConnectionPooling()
    id = request.GET['id']

    Q="delete from addblog where id={0}".format(id)
    #print(Q)
    CMD.execute(Q)
    DB.commit()
    DB.close()
    return JsonResponse({'result':True},safe=False)
  except Exception as e:
    print("Error:",e)
    return JsonResponse({'result':False},safe=False)
