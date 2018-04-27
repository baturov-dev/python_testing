from fixture.db import DbFixture

db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    l = db.get_emails_list()
    for item in l:
        print(item)
    print(len(l))


try:
    e = db.get_emails_list()
    for item in e:
        print(item)
    print(len(e))


finally:
    db.destroy()
