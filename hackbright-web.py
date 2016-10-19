from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github', 'jhacks')
    first, last, github = hackbright.get_student_by_github(github)
    # return "%s is the GitHub account for %s %s" % (github, first, last)
    project_grades = hackbright.get_grades_by_github(github)

    html = render_template("student_info.html", 
                            first=first,
                            last=last,
                            github=github,
                            grades=project_grades)
    return html

@app.route("/student-search")
def get_student_form():
    """Display student search form"""
    return render_template("student_search.html")

@app.route("/newstudent")
def show_add_form():
    """Display add student form"""
    return render_template("student_add.html")

@app.route("/student-add", methods=['POST'])
def student_add():
    """Add student to Students database and show user student had
    been added"""
    first_name = request.form.get('first-name')
    last_name = request.form.get('last-name')
    github = request.form.get('github')

    hackbright.make_new_student(first_name, last_name, github)

    return render_template("added_student.html", 
                           first=first_name, last=last_name, github=github)

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
