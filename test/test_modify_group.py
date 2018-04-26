from model.group import Group
import random

def test_modify_some_group(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name="test1", header="test2", footer="test3"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    new_group = Group(name="mod1", header="mod2", footer="mod3")
    new_group.id = group.id
    app.group.modify_group_by_id(group.id, new_group)
    new_groups = db.get_group_list()
    for i in range(len(old_groups)):
        if old_groups[i].id == new_group.id:
            old_groups[i] = new_group
            break
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


