class Contact(object):
    ContactList = [];

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.ContactList.append(self)


class Contact2(object):
    ContactList = [];

    def __init__(self, name, email):
        # self.ContactList = [];
        self.name = name
        self.email = email
        self.ContactList.append(self)


if __name__ == "__main__":
    ca = Contact("Amy", "amy@example.net")
    cb = Contact("Ben", "ben@example.net")
    print(ca.ContactList)
    ca.ContactList.append("aaa")
    print(cb.ContactList)

    ca2 = Contact2("Ann", "ann@example.net")
    cb2 = Contact2("Bruce", "bruce@example.net")
    print(ca2.ContactList)
    ca2.ContactList.append("bbb")
    print(cb2.ContactList)
    # print(Contact2.ContactList)
