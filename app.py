from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__, template_folder=".")


@app.route("/body.css")
def style():
    return send_from_directory(app.root_path, "body.css")


@app.route("/", methods=["GET", "POST"])
@app.route("/body.html", methods=["GET", "POST"])
def home():
    cgpa = None

    if request.method == "POST":
        sgpas = request.form.getlist("sgpa")
        credits = request.form.getlist("credit")

        sgpas = [float(s) if s else 0 for s in sgpas]
        credits = [float(c) if c else 0 for c in credits]

        # If no credits are entered, calculate the simple average.
        if sum(credits) == 0:
            valid_sgpas = [s for s in sgpas if s > 0]
            if valid_sgpas:
                cgpa = round(sum(valid_sgpas) / len(valid_sgpas), 2)
        else:
            # Calculate the credit-weighted CGPA.
            total_points = sum(
                sgpas[i] * credits[i]
                for i in range(min(len(sgpas), len(credits)))
            )
            total_credits = sum(credits)

            if total_credits > 0:
                cgpa = round(total_points / total_credits, 2)

    return render_template("body.html", cgpa=cgpa)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
