from model.contact import Contact
import random


def test_modify_some_contact(app, db, check_ui):
    old_contacts = db.get_contact_list()
    contact = Contact(firstname="Vasya", middlename="Olegovich", lastname="Watrushkin", nickname="Vasyok",
                               title="Yep", company="Work", address="LA", home_tel="5", mobile_tel="6", work_tel="7",
                               fax="8", email="work@rambler.ru", email2="work2@rambler.ru", email3="work3@rambler.ru",
                               homepage="vasyok.ru", byear="1995", ayear="2015", address2="Nope2", notes="Nope3")
    if app.contact.count() == 0:
        app.contact.create(contact)
    app.contact.contacts_page_is_opened()
    random_contact = random.choice(old_contacts)
    random_contact.id = contact.id
    app.contact.modify_contact(random_contact, contact)
    app.contact.contacts_page_is_opened()
    new_contacts = db.get_contact_list()
    assert len(old_contacts)  == len(new_contacts)
    for n in range(len(old_contacts)):
        if old_contacts[n].id == contact.id:
            old_contacts[n] = contact
            break
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


