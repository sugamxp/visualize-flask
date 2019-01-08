from flask import Flask, render_template, redirect, url_for,flash
from forms import FileForm
from werkzeug.utils import secure_filename
import os
import pandas as pd

app = Flask(__name__)
app.config['SECRET_KEY'] = 'waduhek'
ALLOWED_EXT = {'csv','xlsx'}


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
        return redirect(url_for('index'))
    return render_template('index.html', form=form)

@app.route('/pandas')
def pand():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(dir_path, 'uploads')
    data = os.listdir(data_path)[0]
    print(type(data))
    df = read_ext(data).head(5)
    return render_template('pandas.html',filename=data,df = df.to_html(classes=['table table-dark']))



def read_ext(data):
    if (data.split('.'))[1] == 'csv':
        return pd.read_csv('uploads/'+data)

    if (data.split('.'))[1] == 'xlsx':
        return pd.read_excel('uploads/'+data)
if __name__ == "__main__":
    app.run(debug=True)