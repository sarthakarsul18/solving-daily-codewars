class Sleigh(object):
    def authenticate(self, name, password):
        self.name = name
        self.password = password
        
        if name=='Santa Claus' and password=='Ho Ho Ho!':
            return True
        else:
            return False
        