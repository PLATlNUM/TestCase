from flask import Flask, request, render_template
import os
from formJSON import form

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        img = request.files['image']
        img_path = os.path.join(app.config['UPLOAD_FOLDER'], 'uploaded_image.jpg')
        img.save(img_path)
        result = form()

        return render_template('result.html', result=result)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
