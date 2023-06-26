# from flask import Flask, render_template, request

# from text_summary import summarizer

# app=Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/analyze',methods=['GET','POST'])
# def analyze():
#     if request.method=='POST':
#         rowtext=request.form['text']
#         summary, original_txt,len_origi_txt,len_summary=summarizer(rowtext)

#     return render_template('summary.html',summary=summary,original_txt=original_txt,len_origi_txt=len_origi_txt,len_summary=len_summary)

# if __name__== "__main__":
#     app.run(debug=True)



from flask import Flask, render_template, request
from text_summary import summarizer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('test.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    rowtext = request.form['text']
    summary, original_txt, len_origi_txt, len_summary = summarizer(rowtext)
    
    return render_template('summaytest.html', summary=summary, original_txt=original_txt,  len_origi_txt=len_origi_txt, len_summary=len_summary)

if __name__ == "__main__":
    app.run(debug=True)
