class ContactList(list):
    def search (self, name):
        '''Return all the contacts that contain search value in their name'''
        matching_contacts = []
        for contact in self:
            print(contact.email)
            if name in contact.email:
                matching_contacts.append(contact)
        return matching_contacts


class Contact:
    all_contacts = ContactList()

    def __init__(self, name, email):
        self.email = email
        self.name = name
        Contact.all_contacts.append(self)


class Supplier(Contact):
    def order(self, order):
        print("If this were a real system we would send"
                "'{}' order to '{}'".format(order, self.name))



class MailSender:
    def send_mail(self, message):
        print("sending emails to " + self.email )

class EmailableContact (Contact, MailSender):
    pass