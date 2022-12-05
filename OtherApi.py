class Rest:
    @ufa(route='/api/strange')
    def strange_api(self, param1, param2):
        pass


class UserAdmin:
    def __init__(self):
        self.phone = ''
        self.name = ''
        self.address = ''
        self.cvv = ''
        self.product_name = ''
