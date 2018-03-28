# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.contacts_page_is_opened()
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Petya", middlename="Viktorovich", lastname="Volkov", nickname="Batya",
                               title="Nope", company="Home", address="Moscow", home_tel="1", mobile_tel="2", work_tel="3",
                               fax="4", email="yep@rambler.ru", email2="yep2@rambler.ru", email3="yep3@rambler.ru",
                               homepage="batya.ru", byear="1989", ayear="2009", address2="Nope", notes="Nope")
    app.contact.create(contact)
    app.contact.contacts_page_is_opened()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

