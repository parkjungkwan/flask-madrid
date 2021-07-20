"""
name, phone, email, address
"""


class Contacts(object):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def to_string(self):
        print(f'{self.name}, {self.phone}, {self.email}, {self.address}')


def set_contact():
    return None


def get_contacts():
    pass


def del_contact(ls, name):
    pass


def menu(ls):
    # return '\t'.join(ls)
    t = ''
    for i, j in enumerate(ls):
        t += str(i)+'-'+j+'\t'
    return int(input(t))

def main():
    ls = []
    c = Contacts()
    while 1:
        menu = menu(['exit', 'add', 'print', 'delete'])
        if menu == 1:
            t = set_contact()
            ls.append(t)
        elif menu == 2:
            get_contacts()
        elif menu == 3:
            del_contact(ls, input('Del Name'))
        else:
            break




if __name__ == '__main__':
    # ls = ['0-exit', '1-add', '2-print', '3-delete']
    # ls2 = ['exit', 'add', 'print', 'delete']
    # print(menu(ls2))
    main()