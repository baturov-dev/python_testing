# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app, json_contacts):
    contact = json_contacts
    app.contact.contacts_page_is_opened()
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    app.contact.contacts_page_is_opened()
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

