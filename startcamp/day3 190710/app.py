from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('hello.html')
    
@app.route('/hi')
def hi():
    return render_template('py.html')

# variable routing! 경로를 변수로 활용한다.
@app.route('/hi/<string:name>')
def higye(name):
    return render_template('hi2.html',name=name)

# /cube/<숫자>
# 세제곱 결과를 보여주는 페이지!
@app.route('/cube/<int:number>')
def mul_3(number):
    result=pow(number,3)
    return str(result)

# /lunch/사람이름
# 한식 스페셜A 스페셜B
@app.route('/lunch/<string:name>')
def menu(name):
    lunch=['한식','스페셜A','스페셜B']
    return render_template('menu.html',name=name,menu=random.choice(lunch))

# 로또! /Lotto
# 로또 번호 6개를 추천해주는 페이지

@app.route('/Lotto')


def Lotto():
    result = random.sample(range(1,46),6)
    return str(result)

if __name__ == "__main__":
    # python app.py 를 하면 아래의 코드 블록을 실행시킨다.
    app.run(debug=True)