from flask import Flask, request, render_template
from Methods import *

app = Flask('__main__')
provinces = ["Alberta"]
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def dowload():
    keyword=request.form.get('keyword')
    print(keyword)
    if keyword in provinces:
        bills=extalberta()
        csvfile(keyword, bills)
        print(f"{keyword} Data Downloaded!")

    else:
        print("Province Not Valid")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)