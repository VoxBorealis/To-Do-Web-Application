from app import app
from flask import redirect, render_template, request, session
import users
import tasks

@app.route("/", methods=["GET","POST"])
def index():
    return render_template("index.html", tasks=tasks.get_all_tasks())

@app.route("/login", methods=["GET", "POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    if users.login(username,password):
        return redirect("/")
    else:
        return render_template("error.html",message="Invalid username or password.")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/new_task", methods=["GET", "POST"])
def new_task():
    print("tultiin routes -> new task metodiin")
    task = request.form["new_task"]
    priority = request.form["priority"]
    print(task, priority)
    tasks.new_task(users.user_id(), task, priority)
    return redirect("/")

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.register(username, password):
            return redirect("/")
        else:
            return render_template("error.html", message="There was an error while creating your account.")
    