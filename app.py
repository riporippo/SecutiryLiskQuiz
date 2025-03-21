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
    return render_template('question1.html')

if __name__ == "__main__":
    app.run()