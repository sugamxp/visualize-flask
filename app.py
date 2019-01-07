from flask import Flask, render_template, redirect, url_for,flash
from forms import FileForm
from werkzeug.utils import secure_filename
import os
import pandas as pd


app = Flask(__name__)
app.config['SECRET_KEY'] = 'waduhek'
ALLOWED_EXT = {'csv','tsv', 'xlsx'}
@app.route('/',methods=['GET','POST'])
def index():
    form = FileForm()
    if form.validate_on_submit():
        filename = secure_filename(form.file.data.filename)
        print(filename)
        if filename.split('.')[1] in ALLOWED_EXT:
            form.file.data.save('uploads/' + filename)
        else:
            flash('Incorrect format selected, please try again!')
        return redirect(url_for('pand'))
    return render_template('index.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)