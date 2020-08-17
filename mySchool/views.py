
from django.http import HttpResponse
from django.shortcuts import render, redirect


def all_class(request):
    # 班级列表
    if request.method == "GET":
        import pymysql
        conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="123456", db="my_school")
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 括号内容 说明以字典方式获取数据
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


def del_class(request):
    # 删除班级
    val = request.GET.get('nid')
    import pymysql
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='my_school')
    cursor = conn.cursor()
    cursor.execute("delete from all_class where id = (%s)", [val, ])
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/all-class')


def edit_class(request):
    # 编辑班级
    if request.method == "GET":
        nid = request.GET.get('nid')
        import pymysql
        conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="123456", db="my_school")
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 括号内容 说明以字典方式获取数据
        cursor.execute("select id, title from all_class where id = %s", [nid, ])
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return render(request, "edit-class.html", {"result": result})
    else:
        nid = request.POST.get('id')
        title = request.POST.get('title')
        import pymysql
        conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="123456", db="my_school")
        cursor = conn.cursor()
        cursor.execute("update all_class set title = (%s) where id = (%s)", [title, nid, ])
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/all-class')




