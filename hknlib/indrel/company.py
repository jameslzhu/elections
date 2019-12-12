class Company:

    def __init__(self, name, email, cap, recruiters=None):
        if "@" not in email:
            raise Exception("{} is not a valid email".format(email))
        self.name = name
        self.email = email
        self.is_cap = cap
        self.recruiters = recruiters
        
    def name():
        return self.name
    
    def email():
        return self.
    
    def cap():
        return self.is_cap

    def recruiters():
        return self.recruiters
        