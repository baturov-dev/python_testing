# -*- coding: utf-8 -*-import unittest
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="Group1", header="Grouplogo", footer="Groupcomment"))
    app.session.logout()


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))


