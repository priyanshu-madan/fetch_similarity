from flask import Flask, render_template, request, g
from doc_similarity import get_similarity
app = Flask(__name__)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/", methods=['GET', 'POST'])
def home_post():
    text_1 = request.form['message']
    text_2 = request.form['message_2']
    similarity = get_similarity(text_1,text_2)
    g.simi = similarity
    g.text1 = text_1
    g.text2 = text_2
    return render_template('index.html')

if __name__ == '__main__':
    app.run()