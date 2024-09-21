from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def bmi():
    html_str = """

    <!DOCTYPE html>
 <html lang="kr">
 <head>
 <meta charset="UTF-8">
 <title>BMI 계산기</title>
 </head>
 <body>
 <form method="GET" action="/bmi">
 <h2> BMI 계산기</h2>
 <label>키(cm) :
 <input type="text" name="height"> 
 몸무게(kg) :
 <input type="text" name="weight">
 </label>
 <button type="submit">출력</button>
 </form>
 </body>
 </html>
 """
    return html_str

@app.route("/bmi/")
def bmi_html():
    height = float(request.args.get("height"))
    weight = float(request.args.get("weight"))
    bmi = weight / ((height / 100) ** 2)
    html_str = f"당신의 BMI는 {bmi:.2f}입니다.</strong><br>"
    return html_str

app.run(debug=True)
