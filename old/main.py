from flask import Flask, render_template, redirect, request
from flask_mysqldb import MySQL

class EnrollmentSystem:
    def __init__(self, name):
        self.app = Flask(name)

        # Configuration for MySQL connection
        self.app.config['MYSQL_HOST'] = 'localhost'
        self.app.config['MYSQL_USER'] = 'root'
        self.app.config['MYSQL_PASSWORD'] = ''
        self.app.config['MYSQL_DB'] = 'students'
        self.mysql = MySQL(self.app)

    def setup_routes(self):
        # Home route
        @self.app.route("/")
        def home():
            return render_template("home.html")

        # Enrollment route
        @self.app.route("/enrollment", methods=["GET", "POST"])
        def enrollment():
            if request.method == "POST":
                # Retrieve data from form
                std_name = request.form["namefield"]
                std_section = request.form["sectionfield"]

                # Insert data into the 'studentz' table
                cursor = self.mysql.connection.cursor()
                cursor.execute("INSERT INTO studentz (name, year) VALUES (%s, %s)", (std_name, std_section))
                self.mysql.connection.commit()
                cursor.close()

                return redirect("/enrollment")
            else:
                return render_template("enrollment.html")

        # Display route
        @self.app.route("/display")
        def display():
            cursor = self.mysql.connection.cursor()
            cursor.execute("SELECT * FROM studentz")
            student_list = cursor.fetchall()
            cursor.close()
            return render_template("display.html", student=student_list)

        # Update route
        @self.app.route("/update", methods=["POST"])
        def update():
            id = request.form["id"]
            name = request.form["name"]
            section = request.form["section"]

            return render_template("update.html", std_id=id, name=name, section=section)

        # Update process route
        @self.app.route("/update_process", methods=["POST"])
        def update_process():
            id = request.form["id"]
            new_name = request.form["new_name"]
            new_section = request.form["new_section"]

            # Update the student's data in the 'studentz' table
            cursor = self.mysql.connection.cursor()
            cursor.execute("UPDATE studentz SET name=%s, year=%s WHERE id=%s", (new_name, new_section, id))
            self.mysql.connection.commit()
            cursor.close()

            return redirect("/display")

    def run(self):
        self.app.run(debug=True)

if __name__ == "__main__":
    x = EnrollmentSystem(__name__)
    x.setup_routes()
    x.run()
