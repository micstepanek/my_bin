#!/usr/bin/env python3
a = 3
def log():
    print(locals())
log()
exit()
import time
from selenium import webdriver

driver = webdriver.Chrome('/home/h/ajj/chromedriver')  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()





exit()

import sqlalchemy.ext.declarative
import sqlalchemy.orm

print(sqlalchemy.__version__)
engine = sqlalchemy.create_engine('postgresql://a:a@localhost/mydb', echo=True)
Base = sqlalchemy.ext.declarative.declarative_base()
class User(Base):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    fullname = sqlalchemy.Column(sqlalchemy.String)
    nickname = sqlalchemy.Column(sqlalchemy.String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
                             self.name, self.fullname, self.nickname)
# Base.metadata.create_all(engine)
ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()
session.add(ed_user)
our_user = session.query(User).filter_by(name='ed').first()
print(our_user)
ed_user.nickname = 'eddie'
if False:
    session.add_all([
     User(name='wendy', fullname='Wendy Williams', nickname='windy'),
     User(name='mary', fullname='Mary Contrary', nickname='mary'),
     User(name='fred', fullname='Fred Flintstone', nickname='freddy')])
print(User.__table__, ed_user.fullname)
print(session.new)
session.commit()
ed_user.name = 'Edwardo'
session.rollback()
print(session.new)
for instance in session.query(User).order_by(User.id):
    print(instance.name, instance.fullname)
exit()

#x = sp.check_output(['./test_cpp'])
#print(1,x)
#import time
#x = sp.check_output(['read1'])
#print(1,x)
#sp.run(['i3-msg', 'move', 'scratchpad'])
#import threading #
#def compute1():
#    print(1)
#    for i in range(5000000):
#        i = i + i
#    print(1)
#
#def compute2():
#    print(2)
#    for i in range(50000000):
#        i = i + i
#    print(2)
#
#x = threading.Thread(target=compute2)
#x.start()
#
#compute1()
#import readline
#x = 'abc'
import i3ipc
#import time

i3 = i3ipc.Connection()
tree = i3.get_tree()

def print_and_go_deep(thing, indent):
    if thing:
        try:
            print(indent * ' ', thing.type, thing.name)
        except:
            pass
        indent += 4 
        nodes = thing.nodes
        [print_and_go_deep(node, indent) for node in nodes]
    else:
        print('___')

print_and_go_deep(tree, 0)


#print(tree.find_named('DP1')[0].find_named('content')[0].name)
