from train.train import Train
from test.test import Test
from log.logger import Logger
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/train", methods=["POST"])
def train_model():
    if request.method == 'POST':
        train = Train()
        train.start()
    return "Training completed! "


@app.route("/test", methods=['POST'])
def test_model():

    if request.method == 'POST':
        text = request.form["text"]
        if text is not None and text is not ' ':
            test = Test()
            text = str(test.predict([text])[0])

    return text


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
