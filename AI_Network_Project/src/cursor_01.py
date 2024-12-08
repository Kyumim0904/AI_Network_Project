
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/response", methods=["POST"])
def response():
    user_input = request.form.get("message")
    if "안녕" in user_input or "반가워" in user_input:
        return "안녕하세요. 반갑습니다!"
    return "무슨 말씀이신지 잘 모르겠어요."

if __name__ == "__main__":
    app.run(debug=True)
