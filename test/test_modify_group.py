from model.group import Group


def test_modify_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Group(name="Group2", header="Grouplogo2", footer="Groupcomment2"))
    app.session.logout()