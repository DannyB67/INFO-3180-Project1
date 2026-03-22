"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""

from app import app
from app import db
from flask import flash, render_template, request, redirect, url_for
from app.forms import PropertyForm
from werkzeug.utils import secure_filename
import os
from app.models import Property


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/properties/<int:property_id>')
def property_detail(property_id):
    pass

@app.route('/properties')
def properties():
    pass

@app.route('/properties/create', methods=['GET', 'POST'])
def create_property():
    
    form = PropertyForm()
    if request.method == "GET":
        return render_template('create.html', form=form)
    if request.method == "POST":
        if form.validate_on_submit():
            title=form.title.data
            ptype=form.type.data
            no_of_bedrooms=form.no_of_bedrooms.data
            no_of_bathrooms=form.no_of_bathrooms.data
            location=form.location.data
            description=form.description.data
            price=form.price.data
            picture=form.picture.data
            if picture:
                file = secure_filename(picture.filename)
                picture.save(os.path.join(app.config['UPLOAD_FOLDER'], file))

            new_property = Property(title=title, type=ptype, no_of_bedrooms=no_of_bedrooms, no_of_bathrooms=no_of_bathrooms, location=location, description=description, price=price, image_filename=file)
            db.session.add(new_property)
            db.session.commit()
            flash('Property created successfully!', 'success')
            return redirect(url_for('properties'))
            # Save property to database

        return render_template('create.html', form=form)

###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

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
