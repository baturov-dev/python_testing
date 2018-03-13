# -*- coding: utf-8 -*-import unittest
from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="Group1", header="Grouplogo", footer="Groupcomment"))
    app.session.logout()


