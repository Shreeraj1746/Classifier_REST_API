from logging import DEBUG

from flask import Flask, render_template, request, jsonify

from classify import classify_named_entities


app = Flask(__name__)
app.logger.setLevel(DEBUG)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/classify')
def classify():
    if 'text' in request.args:
        predictions = classify_named_entities(request.args['text'])
        data = dict()
        for tup in predictions:
            data[tup[0]] = tup[1]

        resp = jsonify(data)
        resp.status_code = 200
        return resp

    return jsonify(dict())


if __name__ == '__main__':
    app.run(debug=True)
