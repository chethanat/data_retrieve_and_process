from flask import Flask, jsonify

app = Flask(__name__)

# In-memory storage for processed data
data_storage = {}


def retrieve_data():
    """
    Mock data for simulation purpose
    :return: mock_data
    """
    mock_data = {
        "text": "sample text",
        "series": [1, 2, 3]
    }
    return mock_data


def process_data(data):
    """
    Function for data processing.
    :param data: the data that needs to process
    :return: processed data
    """
    data["text"] = data["text"].upper()
    data["sum_of_series"] = sum(data["series"])
    return data


@app.route('/fetch_data', methods=['GET'])
def fetch_data():
    """
    Function to retrieve data from external site like Shopify
    :return: Retrieved data
    """
    data = retrieve_data()
    processed_data = process_data(data)
    # store the data in-memory
    data_storage["processed"] = processed_data
    return jsonify({"message": "Data retrieved and processed successfully"})


@app.route('/get-processed-data', methods=['GET'])
def get_processed_data():
    """
    Retrieve processed data from in-memory
    :return:
    processed data on success
    No processed data on failure
    """
    if 'processed' in data_storage:
        return jsonify(data_storage["processed"])
    else:
        return jsonify({"message": "No processed data found!"}), 404


if __name__ == '__main__':
    app.run(debug=True)
