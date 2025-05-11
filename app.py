from flask import Flask, render_template, request
import re

app = Flask(__name__)  # デフォルト設定でOK

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/osint')
def osint():
    return render_template('OSINT.html')

@app.route('/result1', methods=['POST'])
def result1():
    user_answer = int(request.form.get('answer'))
    correct_answer = 2  # 富士急ハイランドが正解
    is_correct = (user_answer == correct_answer)
    
    # 選択された答えの説明を設定
    answer_text = {
        1: "よみうりランド",
        2: "富士急ハイランド",
        3: "サンリオピューロランド"
    }.get(user_answer, "不明")
    
    return render_template('result1.html', 
                         is_correct=is_correct,
                         user_answer=answer_text,
                         correct_answer="富士急ハイランド")

@app.route('/result2', methods=['POST'])
def result2():
    user_answer = request.form.get('answer')
    # 正規表現で「群馬県」と「利根郡片品村」が含まれているかチェック
    pattern = r'群馬県.*利根郡片品村|利根郡片品村.*群馬県'
    is_correct = bool(re.search(pattern, user_answer))
    return render_template('result2.html',
                         is_correct=is_correct,
                         user_answer=user_answer,
                         correct_answer="群馬県利根郡片品村")

@app.route('/result3', methods=['POST'])
def result3():
    user_answer = int(request.form.get('answer'))
    correct_answer = 2  # 正解の値
    is_correct = (user_answer == correct_answer)
    
    # 選択された答えの説明を設定
    answer_text = {
        1: "選択肢1",
        2: "選択肢2",
        3: "選択肢3"
    }.get(user_answer, "不明")
    
    return render_template('result3.html', 
                         is_correct=is_correct,
                         user_answer=answer_text,
                         correct_answer="正解の選択肢")

@app.route('/result4', methods=['POST'])
def result4():
    user_answer = int(request.form.get('answer'))
    correct_answer = 2  # 正解の値
    is_correct = (user_answer == correct_answer)
    
    # 選択された答えの説明を設定
    answer_text = {
        1: "選択肢1",
        2: "選択肢2",
        3: "選択肢3"
    }.get(user_answer, "不明")
    
    return render_template('result4.html', 
                         is_correct=is_correct,
                         user_answer=answer_text,
                         correct_answer="正解の選択肢")

@app.route('/result5', methods=['POST'])
def result5():
    user_answer = int(request.form.get('answer'))
    correct_answer = 2  # 正解の値
    is_correct = (user_answer == correct_answer)
    
    # 選択された答えの説明を設定
    answer_text = {
        1: "選択肢1",
        2: "選択肢2",
        3: "選択肢3"
    }.get(user_answer, "不明")
    
    return render_template('result5.html', 
                         is_correct=is_correct,
                         user_answer=answer_text,
                         correct_answer="正解の選択肢")

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
