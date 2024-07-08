from flask import Flask, request, render_template
from Methods import *

app = Flask(__name__)
provinces = ["Alberta"]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    keyword=request.form.get('keyword')
    print(keyword)
    if keyword in provinces:
        bills=get_bills()
        print("Bill data loaded")
        csvfile(keyword, bills)
        votes=get_votes()
        print("Votes data loaded")
        csvfile_vote(keyword, votes)
        print(f"{keyword} Data Downloaded!")
    else:
        print("Province Not Valid")

    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)