
from model.contact import Contact
from random import randrange

def test_delete_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Petya", middlename="Viktorovich", lastname="Volkov", nickname="Batya",
                                   title="Nope", company="Home", address="Moscow", home_tel="1", mobile_tel="2",
                                   work_tel="3",fax="4", email="yep@rambler.ru", email2="yep2@rambler.ru",
                                   email3="yep3@rambler.ru",homepage="batya.ru", byear="1989", ayear="2009",
                                   address2="Nope", notes="Nope"))
    app.contact.contacts_page_is_opened()
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    app.contact.contacts_page_is_opened()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts
