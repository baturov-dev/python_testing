# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Petya", middlename="Viktorovich", lastname="Volkov", nickname="Batya",
                               title="Nope", company="Home", address="Moscow", home_tel="1", mobile_tel="2", work_tel="3",
                               fax="4", email="yep@rambler.ru", email2="yep2@rambler.ru", email3="yep3@rambler.ru",
                               homepage="batya.ru", byear="1989", ayear="2009", address2="Nope", notes="Nope"))
    app.session.logout()


