from flask import Flask, request

app = Flask(__name__)

# test this route with localhost:5000/grandpa/hi grandpa
@app.route('/sample/<sample>')
def sample_route(grandpa):
    if sample.isupper():
        return sample
    else:
        return "What? I can't hear you!"   


# test this route with localhost:5000/sample/?text=hi
# @app.route('/sample/')
# def sample_route():
#     text = request.args.get('text') 
#     if text.isupper():
#         return text
#     else:
#         return "What? I can't hear you!"   


if __name__ == "__main__":
    app.run(debug=True)
