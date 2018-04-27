from model.contact import Contact


def test_contact_list(app, db):
    ui_list = app.contact.get_contact_list()
    db_list = db.get_contact_list()
    assert sorted(ui_list, key = Contact.id_or_max) == sorted(db_list, key = Contact.id_or_max)
    assert sorted(app.contact.get_emails_ui()) == sorted(db.get_emails_list())
    assert sorted(app.contact.get_phones_ui()) == sorted(db.get_phones_list())

