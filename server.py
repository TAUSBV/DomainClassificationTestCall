from flask import Flask
from flask import request
import pickle
app = Flask(__name__)


@app.route('/classify_embeddings', methods=['POST'])
def classify_embeddings():
    # on server side read the data using get_data and unpickle
    data = pickle.loads(request.get_data())
    print(data['email'])
    print(data['tu'].keys())
    # calculation for generating classification
    return "0"


if __name__ == "__main__":
    app.run()
