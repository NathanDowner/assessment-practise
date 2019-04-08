"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app
from flask import render_template, request, redirect, url_for, flash
from app.models import Staff, Project


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')
    
@app.route('/assign/')
def assign():
    devs = Staff.query.all()
    projects = Project.query.all()
    return render_template('assignment.html', devs=devs, projects=projects)

@app.route('/members/')
def staffMembers():
    """Render the website's about page."""
    mem = Staff.query.all()
    return render_template('members.html', members = mem)
    
    
@app.route('/members/<int:memberid>')
def staff(memberid):
    member = Staff.query.get(userid)
    return render_template('member.html', member=member)
    
@app.route('/projects/')
def projects():
    p = Project.query.all()
    return render_template('projects.html',projects=p)
    
@app.route('/projects/<int:projectId>')
def project(projectId):
    project = Project.query.get(projectId)
    return render_template('project.html', project = project)
    
    
###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
