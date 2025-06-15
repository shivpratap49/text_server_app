from flask import Flask, render_template, request,send_file
import os

app = Flask(__name__)

FILES_DIR = os.path.join(app.root_path, 'files')

@app.route('/files')
def list_files():
    files = os.listdir(FILES_DIR)
    return render_template('list_files.html', files=files)
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

        return f'File saved successfully to {filename}!'

    return render_template('index.html')
@app.route('/download/<filename>')
def download_file(filename):
    file_path = os.path.join(FILES_DIR, filename)
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return "File not found.", 404


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=4444)
