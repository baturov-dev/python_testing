from model.contact import Contact


def test_delete_first_contact(app):
    app.contact.contacts_page_is_opened()
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Petya", middlename="Viktorovich", lastname="Volkov", nickname="Batya",
                                   title="Nope", company="Home", address="Moscow", home_tel="1", mobile_tel="2",
                                   work_tel="3",fax="4", email="yep@rambler.ru", email2="yep2@rambler.ru",
                                   email3="yep3@rambler.ru",homepage="batya.ru", byear="1989", ayear="2009",
                                   address2="Nope", notes="Nope"))
    app.contact.delete_first_contact()
