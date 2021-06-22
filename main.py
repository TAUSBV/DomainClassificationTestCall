import requests
import pickle


if __name__ == '__main__':
    # We already have embeddings generated and saved in pickled objects
    # but we have to load it to normal dictionary to post over http
    with open("ExampleSegments/0.pkl", "rb") as f:
        segment = pickle.load(f)
    # data to post
    data = {
        'tu': segment,
        'email': 'name@example.com',
        'outputtype': 0
    }
    # rather than using json to dump we created a pickle dump
    requests.post('http://127.0.0.1:5000/classify_embeddings', data=pickle.dumps(data))
