from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)

def db():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="rootpass",
        database="testdb",
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]

        conn = db()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO users (name, email) VALUES (%s, %s)",
            (name, email)
        )
        conn.commit()
        conn.close()

        return "Saved!"

    return render_template("form.html")

# IMPORTANT: no app.run needed when using gunicorn
