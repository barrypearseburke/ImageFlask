from flask import Flask,request
from flask import send_file
from werkzeug.utils import secure_filename
import  os
app = Flask(__name__)

UPLOAD_FOLDER = 'C:/Users/Barry/PycharmProjects/untitled/tmp'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/',methods=['POST'])
def hello_world():
    #sends cat pic if no file sent
    if request.method == 'POST':
        file = request.files['cat']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # return redirect(url_for('upload_file', filename=filename))
        greycat = do_image_crap(filename)
        return send_file('C:/Users/Barry/PycharmProjects/untitled/tmp/blackcat.png', mimetype='image/png')


def do_image_crap(cat):
#    pass
    from PIL import Image

    import numpy as np
    im = Image.open("C:/Users/Barry/PycharmProjects/untitled/tmp/cat.png").convert('L')
    im.save('C:/Users/Barry/PycharmProjects/untitled/tmp/blackcat.png')
if __name__ == '__main__':
    app.run(debug=True)
#runs on port 5000
#access by going to 127.0.0.1:5000