import requests

def update_data():
    top_tags=["travel","videogames","box"]
    tags_count=["5","8","3"]
    # initialize and send the data through REST API
    url = 'http://0.0.0.0:8080/updateData'
    request_data = {'label': str(top_tags), 'data': str(tags_count)}
    response = requests.post(url, data=request_data)

if __name__ == "__main__":
    update_data()