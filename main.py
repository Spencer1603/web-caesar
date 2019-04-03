from flask import Flask, request
from caesar import rotate_string


app = Flask(__name__)
app.config['DEBUG'] = True

form = """
    <!DOCTYPE html>

    <html>
        <head>
            <style>
                form {{

                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }}
                textarea {{
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }}
            </style>
        </head>
        <body>
            <form method="POST">
                <label for="rotation">Rotate by:</label>
                <input type="text" name="rot" id="rotation" />
                <textarea name="text">{0}</textarea>
                <input type="submit" />
            </form>
        </body>
    </html>
"""

def is_integer(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

@app.route("/", methods=["POST"])
def encrypt():
    rot = request.form['rot']
    text = request.form['text']

    """
    if not is_integer(rot):
        return error
    """
    rot = int(rot)
    encrypted = rotate_string(text, rot)
    #encrypt_wrap = "<h1>encrypted</h1>"
    return form.format(encrypted)

@app.route("/")
def index():
    return form.format("")

app.run()