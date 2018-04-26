from model.contact import Contact
import random
import string
import os.path
import jsonpickle
from random import randint
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 1
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone():
    return "+" + str(randint(1,10)) + "-" + "".join([random.choice(string.digits) for i in range(3)]) + "-" + \
           "".join([random.choice(string.digits) for i in range(3)]) + "-" + "".join([random.choice(string.digits) for i in range(2)]) + \
            "-" + "".join([random.choice(string.digits) for i in range(2)])

def random_email():
    symbols = string.ascii_letters + string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(1,10))]) + "@" + "".join([random.choice(symbols) for i in range(random.randrange(1,10))]) + ".ru"


testdata = [Contact(firstname=random_string("name", 10), middlename=random_string("middlename", 10), lastname=random_string("lastname", 10),
                    nickname=random_string("nickname", 10), title="", company=random_string("name", 10), address=random_string("address", 30), home_tel=random_phone(),  email=random_email(),
                    mobile_tel=random_phone(), work_tel=random_phone(), fax="", email2=random_email(), email3=random_email(), homepage="", byear="", ayear="",
                    address2=random_string("address", 30), notes=random_string("name", 10))
    for i in range(n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))