# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string
from random import randint

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone():
    return "+" + str(randint(1,10)) + "-" + "".join([random.choice(string.digits) for i in range(3)]) + "-" + \
           "".join([random.choice(string.digits) for i in range(3)]) + "-" + "".join([random.choice(string.digits) for i in range(2)]) + \
            "-" + "".join([random.choice(string.digits) for i in range(2)])

def random_email():
    symbols = string.ascii_letters + string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(1,10))]) + "@" + "".join([random.choice(symbols) for i in range(random.randrange(1,10))]) + ".ru"


testdata = [Contact(firstname=random_string("name", 10), middlename=random_string("middlename", 10), lastname=random_string("lastname", 10),
                    nickname=random_string("nickname", 10), title="", company=random_string("name", 10), address=random_string("address", 30), home_tel=random_phone(),  email=random_email(),
                    mobile_tel=random_phone(), work_tel=random_phone(), fax="", email2=random_email(), email3=random_email(), homepage="", byear="", ayear="",
                    address2=random_string("address", 30), notes=random_string("name", 10))
    for i in range(3)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    app.contact.contacts_page_is_opened()
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    app.contact.contacts_page_is_opened()
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

