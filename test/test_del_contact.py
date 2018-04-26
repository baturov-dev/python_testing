
from model.contact import Contact
import random

def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Petya", middlename="Viktorovich", lastname="Volkov", nickname="Batya",
                                   title="Nope", company="Home", address="Moscow", home_tel="1", mobile_tel="2",
                                   work_tel="3",fax="4", email="yep@rambler.ru", email2="yep2@rambler.ru",
                                   email3="yep3@rambler.ru",homepage="batya.ru", byear="1989", ayear="2009",
                                   address2="Nope", notes="Nope"))
    app.contact.contacts_page_is_opened()
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact(contact)
    app.contact.contacts_page_is_opened()
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
