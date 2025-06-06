from flask import Flask, render_template, request
import os

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        filename = request.form['filename'].strip()

        user_text = request.form['user_text']
        file=request.files['file']
        file.save(f"files/{file.filename}")
        # Ensure safe filename
        if request.form['filename'].strip()!='' and request.form['user_text']!='':
            if not filename.endswith('.txt'):
                filename += '.txt'

        # Save to the file
            with open(f"files/{filename}", 'w') as f:
                f.write(user_text)

        return f'Text saved successfully to {filename}!'

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=4444)
