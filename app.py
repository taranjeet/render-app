import os

from flask import Flask, jsonify, request
from embedchain import Pipeline as App

app = Flask(__name__)

ec_app = App()
ec_app.add("data/b1.pdf")
ec_app.add("data/b2.pdf")
ec_app.add("data/b3.pdf")
ec_app.add("data/b4.pdf")
ec_app.add("data/b5.pdf")


def get_answer(question):
    print(f"Received question {question}")
    return ec_app.query(question)


@app.route('/ask', methods=['GET'])
def ask():
    # Retrieve the 'query' parameter from the URL
    user_query = request.args.get('query', '')
    output = {
        "query": user_query
    }
    if user_query:
        answer = get_answer(user_query)
        output["answer"] = answer

    # Return the 'query' parameter in a JSON response
    return jsonify(output)

if __name__ == '__main__':
    app.run()
