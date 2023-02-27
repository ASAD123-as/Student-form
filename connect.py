from flask import *
import sqlite3
connect = Flask(__name__)
@connect.route("/")
def index():
    return render_template("index.html");
@connect.route("/stdinsert")
def startinsert():
    return render_template("insert.html");
@connect.route("/stdupdate")
def startupdate():
    return render_template("update.html");
@connect.route("/stddelete")
def startdelete():
    return render_template("delete.html");

@connect.route("/detailsinsert", methods=["POST", "GET"])
def insert():
    msg = "cannot insert"
    if request.method == "POST":
        try:
            a = request.form["num"]
            b = request.form["name"]
            c = request.form["location"]
            d = request.form["number"]
            with sqlite3.connect(r"C:\Users\ELCOT\studentinformation.db") as con:
                cur = con.cursor()
                cur.execute("insert into student(studentid,name,location,number) values (?,?,?,?)", (a,b,c,d))
                con.commit()

        except:
            con.rollback()
            msg = "We can not insert list"
        finally:
            return render_template("join.html", msg=msg)
            con.close()

@connect.route("/detailsupdate", methods=["POST", "GET"])
def update():
    msg = "cannot update"
    if request.method == "POST":
        try:
            a = request.form["studentid"]
            b = request.form["name"]
            c = request.form["location"]
            d = request.form["number"]
            with sqlite3.connect(r"C:\Users\ELCOT\studentinformation.db") as con:
                cur = con.cursor()
                print("jiiiii")
                sql=(f"update student set name='{b}',location='{c}',number={d} where studentid={a}")
                print("jiiiiiii")
                cur.execute(sql)
                con.commit()
        except:
            con.rollback()
            msg = "We can not update list"
        finally:
            return render_template("join.html", msg=msg)
            con.close()

@connect.route("/detailsdelete", methods=["POST", "GET"])
def delete():
    msg = "cannot delete"
    if request.method == "POST":
        try:
            a = request.form["num"]
            with sqlite3.connect(r"C:\Users\ELCOT\studentinformation.db") as con:
                cur = con.cursor()
                cur.execute(f"delete from student where studentid={a}")
                con.commit()
                msg="successfully deleted"
        except:
            con.rollback()
            msg = "We can not delete list"
        finally:
            return render_template("join.html", msg=msg)
            con.close()

@connect.route("/viewinsert")
def insertview():
    con = sqlite3.connect(r"C:\Users\ELCOT\studentinformation.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from student")
    rows = cur.fetchall()
    return render_template("view.html", rows=rows)

@connect.route("/viewupdate")
def updateview():
    con = sqlite3.connect(r"C:\Users\ELCOT\studentinformation.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from student")
    rows = cur.fetchall()
    return render_template("view.html", rows=rows)

@connect.route("/viewdelete")
def deleteview():
    con = sqlite3.connect(r"C:\Users\ELCOT\studentinformation.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from student")
    rows = cur.fetchall()
    return render_template("view.html", rows=rows)

if __name__ == "__main__":
    connect.run(debug=True,port=1111)