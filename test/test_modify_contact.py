from model.contact import Contact
from random import randrange


def test_modify_first_contact(app):
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Vasya", middlename="Olegovich", lastname="Watrushkin", nickname="Vasyok",
                               title="Yep", company="Work", address="LA", home_tel="5", mobile_tel="6", work_tel="7",
                               fax="8", email="work@rambler.ru", email2="work2@rambler.ru", email3="work3@rambler.ru",
                               homepage="vasyok.ru", byear="1995", ayear="2015", address2="Nope2", notes="Nope3")
    app.contact.contacts_page_is_opened()
    if app.contact.count() == 0:
        app.contact.create(contact)
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    app.contact.contacts_page_is_opened()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts)  == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

