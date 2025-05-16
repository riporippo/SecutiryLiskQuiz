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
    user_answer = request.form.get('answer')
    pattern = r'(?=.*url|URL)(?=.*(異なる|違う|ない|)).*'
    # 正規表現で「url」と「異なる」または「違う」が含まれているかチェック
    is_correct = bool(re.search(pattern, user_answer))
    return render_template('result4.html', 
                         is_correct=is_correct,
                         user_answer=user_answer,
                         correct_answer="urlが異なる")

@app.route('/result5', methods=['POST'])
def result5():
    user_answer = int(request.form.get('answer'))
    correct_answer = 3  # 正解の値
    is_correct = (user_answer == correct_answer)
    
    # 選択された答えの説明を設定
    answer_text = {
        1: "なにもしない",
        2: "スマートフォンやパソコン本体のOSのバージョンだけ最新にする",
        3: "スマートフォンやパソコン本体のOSのバージョンに加え、アプリやソフト、ネットにつながるIT機器も最新の状態にしておく",
        4: "神に願う"
    }.get(user_answer, "不明")
    return render_template('result5.html', 
                         is_correct=is_correct,
                         user_answer=answer_text,
                         correct_answer="スマートフォンやパソコン本体のOSのバージョンに加え、アプリやソフト、ネットにつながるIT機器も最新の状態にしておく")

@app.route('/result6', methods=['POST'])
def result6():
    user_answer = request.form.getlist('answer')
    correct_answer = {"2", "3"}  # 正解の値
    is_correct = correct_answer == set(user_answer)
    answer_text_map = {
        "1": "お父さんの生年月日を使う",
        "2": "パスワードを使いまわさない",
        "3": "パスワードは紙やパスワード管理アプリで安全に保管",
        "4": "パスワードの定期変更"
    }
    selected_answers = [answer_text_map.get(ans, "不明") for ans in user_answer]
    correct_answer_text = [answer_text_map[ans] for ans in correct_answer]
    return render_template('result6.html', 
                         is_correct=is_correct,
                         user_answer=selected_answers,
                         correct_answer=correct_answer_text)

@app.route('/result7', methods=['POST'])
def result7():
    user_answer = int(request.form.get('answer'))
    correct_answer = 4  # 正解の値
    is_correct = (user_answer == correct_answer)
    
    # 選択された答えの説明を設定
    answer_text = {
        1: "フィッシング",
        2: "スキミング",
        3: "ブルートフォースアタック",
        4: "ショルダーハッキング"
    }.get(user_answer, "不明")
    return render_template('result7.html', 
                         is_correct=is_correct,
                         user_answer=answer_text,
                         correct_answer="ショルダーハッキング")

@app.route('/result8', methods=['POST'])
def result8():
    user_answer = int(request.form.get('answer'))
    correct_answer = 3  # 正解の値
    is_correct = (user_answer == correct_answer)
    answer_text = {
        1: "パスワードを2回入力することで安全性を高める方法",
        2: "1つの方法だけで本人確認を行う仕組み",
        3: "複数の異なる認証要素を使って本人確認を行う仕組み",
        4: "アプリの自動ログイン機能のこと"
    }.get(user_answer, "不明")
    return render_template('result8.html', 
                         is_correct=is_correct,
                         user_answer=answer_text,
                         correct_answer="複数の異なる認証要素を使って本人確認を行う仕組み")

@app.route('/result9', methods=['POST'])
def result4():
    user_answer = request.form.get('answer')
    pattern = r'(?=.*url|URL)(?=.*(異なる|違う|ない|)).*'
    # 正規表現で「url」と「異なる」または「違う」が含まれているかチェック
    is_correct = bool(re.search(pattern, user_answer))
    return render_template('result9.html', 
                         is_correct=is_correct,
                         user_answer=user_answer,
                         correct_answer="urlが異なる")

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

@app.route('/question6')
def question6():
    return render_template('question6.html')

@app.route('/question7')
def question7():
    return render_template('question7.html')

@app.route('/question8')
def question8():
    return render_template('question8.html')

@app.route('/question9')
def question9():
    return render_template('question9.html')



if __name__ == "__main__":
    app.run(debug=True,port= 5015)
