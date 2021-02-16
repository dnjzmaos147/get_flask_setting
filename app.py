from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/testpote')
def test():
    return render_template('post.html')

@app.route('/pote', methods=['POST'])
def po():
    value = request.form['test']
    return {
        "d" : "fff",
        "v" : value
    }

@app.route('/post', methods=['POST'])
def post():
    value = request.form['word']
    test = "테스트문장"
    print("val", value)
    print("test", test)
    return {
        "ajax에서받은값" : value,
        "flaskroute에서주는값" : test
    }

if __name__ == '__main__':
    app.run()