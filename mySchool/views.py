
from django.http import HttpResponse
from django.shortcuts import render, redirect


def all_class(request):
    # 班级列表
    if request.method == "GET":
        import pymysql
        conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="123456", db="my_school")
        cursor = conn.cursor()
        cursor.execute("select * from all_class")
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return render(request, "all-class.html", {"msg": result})


def add_class(request):
    # 添加班级
    if request.method == "GET":
        return render(request, "add-class.html")
    else:
        print(request.POST)
        val = request.POST.get('title')
        import pymysql
        conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="123456", db="my_school")
        cursor = conn.cursor()
        cursor.execute("insert into all_class(title) values (%s)", [val, ])
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/all-class')
