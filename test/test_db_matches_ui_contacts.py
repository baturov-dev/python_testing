
from model.contact import Contact



def test_contact_list(app, db):
    ui_list = sorted(app.contact.get_contact_list(), key = Contact.id_or_max)
    db_list = sorted(db.get_contact_list(), key = Contact.id_or_max)
    for i in range(len(ui_list)):
        assert ui_list[i] == db_list[i]
        assert ui_list[i].all_emails_from_home_page == app.contact.merge_emails_like_on_home_page(db_list[i])
        assert sorted(ui_list[i].all_phones_from_home_page) == sorted(app.contact.merge_phones_like_on_home_page(db_list[i]))
