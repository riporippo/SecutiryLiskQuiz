from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    letter = "フィッシングサイトに気を付けよう"
    return letter

if __name__ == "__main__":
    app.run()