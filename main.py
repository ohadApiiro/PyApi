from chalice import Chalice

app = Chalice(app_name='helloworld')

class Data:
    def __init__(self):
        self.name = ''
        self.id = ''
        self.credit_card = ''
        self.age = 0

def func():
    data = Data()
    data.age = 3
    data.id = '1223'
    data.name = 'Ozzy'
    return data

@app.route('/api', method=['POST', 'GET'])
def index():
    data = func()
    return {data.id: data.name}