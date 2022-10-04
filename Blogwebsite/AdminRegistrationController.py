from django.shortcuts import render
from . import pool
from django.http import JsonResponse


def Admin_Registration(request):
    return render(request,"AdminRegistration.html")

def SubmitAdminData(request):
    try:
        DB, CMD = pool.ConnectionPooling()
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        gender = request.POST['gender']
        number= request.POST['number']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        adminimage = request.FILES['adminimage']
        Q = "insert into adminregistration(firstname,lastname,number,gender,password,cpassword,email,adminimage) values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}')".format(fname,lname,number,gender,password,cpassword,email,adminimage.name)
        F = open("e:/Blogwebsite/assets/" + adminimage.name, 'wb')
        for chunk in adminimage.chunks():
            F.write(chunk)
        F.close()
        CMD.execute(Q)
        DB.commit()
        DB.close()
        return render(request, 'AdminRegistration.html', {'message': 'Record Submitted'})

    except Exception as e:
        print("Error", e)
        return render(request, 'AdminRegistration.html', {'message': 'Fail to Submit record'})

