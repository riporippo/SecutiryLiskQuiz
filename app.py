from flask import Flask, render_template, request

app = Flask(__name__)  # デフォルト設定でOK

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
    user_select_answer = int(request.form.get('answer'))
    correct_answer = 1
    is_correct = (user_select_answer == correct_answer)
    return render_template('result.html', is_correct=is_correct)


@app.route('/question')
def question():
    question_data = {
        'image_legit': 'images/legit_site.png',
        'image_phishing': 'images/phishing_site.png',
        'differences': [
            {'x': 120, 'y': 80, 'radius': 20},
            {'x': 300, 'y': 150, 'radius': 20},
        ]
    }
    return render_template('question.html', data=question_data)


# 個別の問題ページ
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
    app.run(debug=True)
