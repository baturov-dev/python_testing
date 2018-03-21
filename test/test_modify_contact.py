from model.contact import Contact


def test_modify_first_contact(app):
    app.contact.modify_first_contact(Contact(firstname="Vasya", middlename="Olegovich", lastname="Watrushkin", nickname="Vasyok",
                               title="Yep", company="Work", address="LA", home_tel="5", mobile_tel="6", work_tel="7",
                               fax="8", email="work@rambler.ru", email2="work2@rambler.ru", email3="work3@rambler.ru",
                               homepage="vasyok.ru", byear="1995", ayear="2015", address2="Nope2", notes="Nope3"))
