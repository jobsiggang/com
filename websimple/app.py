from flask import Flask, render_template
from views import simple_views  # views폴더의 파이썬 파일이름으로 추가

app = Flask(__name__)
app.register_blueprint(simple_views.bp)  # bp는 추가된 파이썬 파일에 정의됨


@app.route('/')
def index():
    return render_template('myworks.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="80", debug="true")
