from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__, template_folder=".")


@app.route("/body.css")
def style():
    return send_from_directory(app.root_path, "body.css")

@app.route("/", methods=["GET", "POST"])
def home():
    cgpa = None
    if request.method == "POST":
        sgpas = request.form.getlist("sgpa")
        sgpas = [float(value) for value in sgpas if value]
        if len(sgpas) > 0:
            cgpa = round(sum(sgpas) / len(sgpas), 2)
    return render_template("body.html", cgpa=cgpa)

if __name__ == "__main__":
    app.run(debug=True)