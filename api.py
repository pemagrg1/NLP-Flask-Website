from flask import Flask, request, render_template,jsonify

app = Flask(__name__)

def do_something(text1,text2):
   text1 = text1.upper()
   text2 = text2.upper()
   combine = text1 + text2
   return combine

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/keyExt', methods=["GET"])
def keyword_extraction():
    return render_template('keyExt.html')


@app.route('/preproc', methods=["GET"])
def pre_process():
    return render_template('preproc.html')


@app.route('/others', methods=["GET"])
def others():
    return render_template('others.html')

@app.route('/join', methods=['GET','POST'])
def my_form_post():
    text1 = request.form['text1']
    word = request.args.get('text1')
    text2 = request.form['text2']
    combine = do_something(text1,text2)
    result = {
        "output": combine
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)

@app.route('/lower', methods=["POST"])
def lower_case():
    text1 = request.form['text1']
    print(text1)
    word = text1.lower()
    result = {
        "lower_word": word
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)

