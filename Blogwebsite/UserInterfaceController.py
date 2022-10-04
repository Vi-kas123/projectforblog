from django.shortcuts import render
from . import pool
import json
from django.http import JsonResponse
from urllib.parse import unquote  # url decode


def User_Index(request):
    return render(request,"UserInterface.html")

def Fetch_All_blogs(request):
    try:
        DB, CMD = pool.ConnectionPooling()
        Q = "select * from addblog"
        CMD.execute(Q)
        blogs = CMD.fetchall()
        #print(records)
        DB.close()
        return JsonResponse({'data': blogs}, safe=False)

    except Exception as e:
        return JsonResponse({'data': []}, safe=False)


def BlogDescription(request):
    blog=unquote(request.GET['blog'])
    blog=json.loads(blog)
    # print("zzzzz",product,type(product))
    return render(request,"blogdescription.html",{'blog': blog})