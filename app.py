from flask import Flask, render_template, redirect, url_for
from forms import FileForm
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'waduhek'
@app.route('/',methods=['GET','POST'])
def index():
    form = FileForm()
    if form.validate_on_submit():
        filename = secure_filename(form.file.data.filename)
        print(filename)
        form.file.data.save('uploads/' + filename)
        return redirect(url_for('index'))
    return render_template('index.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)