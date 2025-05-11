from flask import Flask, render_template, request

app = Flask(__name__)  # デフォルト設定でOK

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/osint')
def osint():
    return render_template('OSINT.html')

@app.route('/result', methods=['POST'])
def result():
    user_answer = int(request.form.get('answer'))
    correct_answer = 2  # 電柱が正解
    is_correct = (user_answer == correct_answer)
    
    # 選択された答えの説明を設定
    answer_text = {
        1: "雲の配置",
        2: "電柱",
        3: "洋服"
    }.get(user_answer, "不明")
    
    return render_template('result.html', 
                         is_correct=is_correct,
                         user_answer=answer_text,
                         correct_answer="電柱")


@app.route('/question1')
def question1():
    return render_template('question1.html')

@app.route('/question2')
def question2():
    return render_template('question2.html')

@app.route('/question3')
def question3():
    return render_template('question3.html')

@app.route('/question4')
def question4():
    return render_template('question4.html')

@app.route('/question5')
def question5():
    return render_template('question5.html')

if __name__ == "__main__":
    app.run(debug=True,port= 5015)
