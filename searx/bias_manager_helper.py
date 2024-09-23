import requests

# Define the server URL (assuming the server is running on localhost)
URL = 'http://biasmanager:5000/predict'


def make_prediction(model, task, sentence):
    """Send a POST request to the server with given parameters and return the response."""
    data = {
        'model': model,
        'task': task,
        'sentence': sentence,
        'explain': True
    }
    # Send POST request to the server
    try:
        response = requests.post(URL, data=data)
        response.raise_for_status()  # Raise an error if the request failed
        return response.json()  # Convert response to JSON
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


def predict_and_explain(text, model='convbert', task='cognitive-bias'):
    """Main function to make a prediction and return the prediction and explanation."""
    result = make_prediction(model, task, text)
    prediction = result.get('prediction', 0)
    explained_text = result.get('explained_text', 'No explanation available')
    return (prediction, explained_text)
