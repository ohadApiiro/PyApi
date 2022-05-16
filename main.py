from chalice import Chalice

app = Chalice(app_name='helloworld')


@app.route('/api', method=['POST', 'GET'])
def index():
    return {'hello': 'world'}