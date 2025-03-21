from flask import Flask, render_template, request
app = Flask(__name__, static_folder='./templates/images')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    user_select_answer = int(request.form.get('answer'))
    correct_answer = 1

    is_correct = (user_select_answer == correct_answer)

    return render_template('result.html', is_correct=is_correct)

@app.route('/mondai-1')
def question_1():
    return render_template('question/1.html')

@app.route('/mondai-2')
def question_2():
    return render_template('question/2.html')

@app.route('/mondai-3')
def question_3():
    return render_template('question/3.html')

@app.route('/mondai-4')
def question_4():
    return render_template('question/4.html')

@app.route('/mondai-5')
def question_5():
    return render_template('question/5.html')

if __name__ == "__main__":
    app.run()