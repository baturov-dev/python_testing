from model.group import Group


def test_modify_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test1", header="test2", footer="test3"))
    app.group.modify_first_group(Group(name="Group2", header="Grouplogo2", footer="Groupcomment2"))
