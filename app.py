from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from cs50 import SQL
import os

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
db = SQL('sqlite:///database.db')
Session(app)

# main page
@app.route("/", methods=["GET", "POST"])
def index():
    roster = db.execute("SELECT * FROM Local_solution_details ORDER BY local_solution_id DESC LIMIT 5")
    if session.get("email", "password"):

        return render_template("index.html", roster=roster)
    return render_template("index.html", roster=roster)

# dashboard only for admins
@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    return render_template("dashboard.html")

# edit solution page
@app.route("/editsolution", methods=["GET", "POST"])
def editsolution():
    return render_template("editsolution.html")

# route to covid solutions page
@app.route("/covidprojects", methods=["GET", "POST"])
def covidprojects():

    # search for spesific solutions based on the name
    if request.method == "POST":
        search_box = request.form.get("search")

        roster = db.execute("SELECT * FROM Local_solution_details WHERE type_of_the_local_solution='covid' AND local_solution_name LIKE ?", "%" + search_box + "%")
        return render_template("covid.html", roster=roster)

    roster = db.execute("SELECT * FROM Local_solution_details WHERE type_of_the_local_solution='covid'")
    return render_template("covid.html", roster=roster)

# route to climate solutions page
@app.route("/climateprojects", methods=["GET", "POST"])
def climateprojects():

    # search for spesific solutions based on the name
    if request.method == "POST":
        search_box = request.form.get("search")

        roster = db.execute("SELECT * FROM Local_solution_details WHERE type_of_the_local_solution='climate' AND local_solution_name LIKE ?", "%" + search_box + "%")
        return render_template("climate.html", roster=roster)
    roster = db.execute("SELECT * FROM Local_solution_details WHERE type_of_the_local_solution='climate'")
    return render_template("climate.html", roster=roster)

# route to solution page
@app.route("/solutionsprojects", methods=["GET", "POST"])
def solutionsprojects():

    # search for spesific solutions based on the name
    if request.method == "POST":
        search_box = request.form.get("search")

        roster = db.execute("SELECT * FROM Local_solution_details WHERE type_of_the_local_solution='solution' AND local_solution_name LIKE ?", "%" + search_box + "%")
        return render_template("solutions.html", roster=roster)
    roster = db.execute("SELECT * FROM Local_solution_details WHERE type_of_the_local_solution='solution'")
    return render_template("solutions.html", roster=roster)

# route to miscellaneous solutions page
@app.route("/miscprojects", methods=["GET", "POST"])
def miscprojects():

    # search for spesific solutions based on the name
    if request.method == "POST":
        search_box = request.form.get("search")

        roster = db.execute("SELECT * FROM Local_solution_details WHERE type_of_the_local_solution='miscellaneous' AND local_solution_name LIKE ?", "%" + search_box + "%")
        return render_template("misc.html", roster=roster)
    roster = db.execute("SELECT * FROM Local_solution_details WHERE type_of_the_local_solution='miscellaneous'")
    return render_template("misc.html", roster=roster)

# redirects to creating a solution
@app.route("/newsolution", methods=["GET", "POST"])
def newsolution():
    if request.method == "POST":

        # gets the solutions info
        s1 = request.form.get("local_solution_name")
        s2 = request.form.get("owner_name") 
        s3 = request.form.get("type_of_the_local_solution")
        s4 = request.form.get("province_of_the_local_solution")
        s5 = request.form.get("date_of_finding_the_local_solution")
        s6 = request.form.get("stage_of_the_local_solution") 
        s7 = request.form.get("institution")
        s8 = request.form.get("phone_number")
        s9 = request.form.get("email")
        s10 = request.form.get("working_area_of_the_local_solution")
        s11 = request.form.get("institutions_the_solution_is_implemented_at")
        s12 = request.form.get("current_partners_of_the_solution")
        s13 = request.form.get("local_solution_description")
        s14 = request.form.get("local_solution_requirements") 
        s15 = request.form.get("social_media_links")
        
        image = request.files["image_of_local_solution"]
        image.save("static/solimage/"+s1+".png")
        s16 = ("../static/solimage/"+s1+".png")

        project = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16]

        # check if any box is blank
        for loop in project:
            if len(loop) == 0:
                project.clear()
                return redirect("/newsolution")

        # check the sdgs if checked or or not
        if len(request.form.getlist("sdg1")) == 1:
            sdg1 = 1
        else:
            sdg1 = 0

        if len(request.form.getlist("sdg2")) == 1:
            sdg2 = 1
        else:
            sdg2 = 0

        if len(request.form.getlist("sdg3")) == 1:
            sdg3 = 1
        else:
            sdg3 = 0

        if len(request.form.getlist("sdg4")) == 1:
            sdg4 = 1
        else:
            sdg4 = 0

        if len(request.form.getlist("sdg5")) == 1:
            sdg5 = 1
        else:
            sdg5 = 0

        if len(request.form.getlist("sdg6")) == 1:
            sdg6 = 1
        else:
            sdg6 = 0

        if len(request.form.getlist("sdg7")) == 1:
            sdg7 = 1
        else:
            sdg7 = 0
            
        if len(request.form.getlist("sdg8")) == 1:
            sdg8 = 1
        else:
            sdg8 = 0

        if len(request.form.getlist("sdg9")) == 1:
            sdg9 = 1
        else:
            sdg9 = 0

        if len(request.form.getlist("sdg10")) == 1:
            sdg10 = 1
        else:
            sdg10 = 0

        if len(request.form.getlist("sdg11")) == 1:
            sdg11 = 1
        else:
            sdg11 = 0

        if len(request.form.getlist("sdg12")) == 1:
            sdg12 = 1
        else:
            sdg12 = 0

        if len(request.form.getlist("sdg13")) == 1:
            sdg13 = 1
        else:
            sdg13 = 0

        if len(request.form.getlist("sdg14")) == 1:
            sdg14 = 1
        else:
            sdg14 = 0

        if len(request.form.getlist("sdg15")) == 1:
            sdg15 = 1
        else:
            sdg15 = 0

        if len(request.form.getlist("sdg16")) == 1:
            sdg16 = 1
        else:
            sdg16 = 0

        if len(request.form.getlist("sdg17")) == 1:
            sdg17 = 1
        else:
            sdg17 = 0

        # saves the solution in the database
        db.execute(
            "INSERT INTO Local_solution_details(local_solution_name, owner_name, type_of_the_local_solution, province_of_the_local_solution, date_of_finding_the_local_solution, stage_of_the_local_solution, institution, phone_number, email, working_area_of_the_local_solution, institutions_the_solution_is_implemented_at, current_partners_of_the_solution, local_solution_description, local_solution_requirements, social_media_links, image_of_local_solution) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16)

        sol = db.execute("SELECT local_solution_id from Local_solution_details WHERE local_solution_name=?", s1)
        sul = 0

        for loop in sol:
            sul = loop["local_solution_id"]

        db.execute(
            "INSERT INTO sdg_of_the_local_solution(local_solution_id, sdg1, sdg2, sdg3, sdg4, sdg5, sdg6, sdg7, sdg8, sdg9, sdg10, sdg11, sdg12, sdg13, sdg14, sdg15, sdg16, sdg17) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            sul, sdg1, sdg2, sdg3, sdg4, sdg5, sdg6, sdg7, sdg8, sdg9, sdg10, sdg11, sdg12, sdg13, sdg14, sdg15, sdg16, sdg17)

        return redirect("/")
    return render_template("submission.html")

# redirects to creating register a new user
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if any text field is empty
        if len(request.form.get("user_name")) == 0 or len(request.form.get("email")) == 0 or len(request.form.get("password")) == 0:
            return redirect("/register")

        # get the input and save it in the database
        user_name = request.form.get("user_name")
        email = request.form.get("email")
        password = request.form.get("password")
        
        db.execute("INSERT INTO users(user_name, email, password) VALUES(?, ?, ?)", user[0], user[1], user[2])

        session["admin"] = 0
        session["user_name"] = user_name
        session["email"] = email
        session["password"] = password

        return redirect("/")
    return render_template("register.html")
    

# redirects to login page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
    
        # check if input is null
        if len(request.form.get("email")) == 0 or len(request.form.get("password")) == 0:
            return redirect("/login")

        try:
            # get the inputs and check if it matches a valid user
            email = request.form.get("email")
            password = request.form.get("password")
            
            check = db.execute("SELECT user_name, email, password, admin_auth FROM users WHERE email = ?", email)
            if check is not None:
                for loop in check:
                    if password != loop["password"]:
                        return redirect("/login")
                    session["admin"] = loop["admin_auth"]
                    session["user_name"] = loop["user_name"]
                    session["email"] = loop["email"]
                    session["password"] = loop["password"]
                return redirect("/")
        except sqlite3.Error as error:
            return redirect("/login")
    return render_template("login.html")

# logsout the user
@app.route("/logout")
def logout():
    session["admin"] = None
    session["email"] = None
    session["password"] = None
    session["user_name"] = None
    return redirect("/")