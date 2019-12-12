class Company:

    def __init__(self, name, email, recruiters, cap):
        if "@" not in email:
            raise Exception("{} is not a valid email".format(email))
        self.name = name
        self.email = email
        self.recruiters = recruiters
        self.is_cap = cap
        
    def name():
        return self.name
    
    def email():
        return self.email

    def recruiters():
        return self.recruiters

    def cap():
        return self.is_cap