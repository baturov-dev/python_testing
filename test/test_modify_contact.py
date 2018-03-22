from model.contact import Contact


def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Petya", middlename="Viktorovich", lastname="Volkov", nickname="Batya",
                                   title="Nope", company="Home", address="Moscow", home_tel="1", mobile_tel="2",
                                   work_tel="3",fax="4", email="yep@rambler.ru", email2="yep2@rambler.ru",
                                   email3="yep3@rambler.ru",homepage="batya.ru", byear="1989", ayear="2009",
                                   address2="Nope", notes="Nope"))

    app.contact.modify_first_contact(Contact(firstname="Vasya", middlename="Olegovich", lastname="Watrushkin", nickname="Vasyok",
                               title="Yep", company="Work", address="LA", home_tel="5", mobile_tel="6", work_tel="7",
                               fax="8", email="work@rambler.ru", email2="work2@rambler.ru", email3="work3@rambler.ru",
                               homepage="vasyok.ru", byear="1995", ayear="2015", address2="Nope2", notes="Nope3"))
