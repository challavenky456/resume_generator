from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def form():
    return render_template("form.html")

@app.route('/resume', methods=['POST'])
def resume():
    name = request.form['name']
    email = request.form['email']
    skills = request.form['skills']
    education = request.form['education']

    return render_template("resume.html",
                           name=name,
                           email=email,
                           skills=skills,
                           education=education)

if __name__ == "__main__":
    app.run(debug=True)