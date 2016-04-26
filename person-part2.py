'''
>>> pe.say('the sky is blue')
Prof. eric says: I believe that eric says: the sky is blue

>>> ae.say('the sky is blue')
Prof. eric says: It is obvious that I believe that eric says: the sky is blue
'''

class Person(object):
    def __init__(self, name):
        self.name = name
    def say(self, stuff):
        return self.name + ' says: ' + stuff
    def __str__(self):
        return self.name

class Lecturer(Person):
    def lecture(self, stuff):
        return 'I believe that ' + Person.say(self, stuff)

class Professor(Lecturer):
    def say(self, stuff, prefix=''):
        return prefix + self.name + ' says: ' + self.lecture(stuff)

e = Person('eric')
le = Lecturer('eric')
pe = Professor('eric')

class ArrogantProfessor(Professor):
    def lecture(self, stuff):
        return 'It is obvious that ' + Lecturer.lecture(self, stuff)

    def say(self, stuff):
        return Professor.say(self, '') + stuff

ae = ArrogantProfessor('eric')

print ae.say('the sky is blue') == 'eric says: It is obvious that I believe that eric says: the sky is blue'
print ae.lecture('the sky is blue') == 'It is obvious that I believe that eric says: the sky is blue'

class Professor(Lecturer):
    def say(self, stuff, prefix='Prof. '):
        return prefix + self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor):
    def lecture(self, stuff):
        return 'It is obvious that ' + Lecturer.lecture(self, stuff)
    def say(self, stuff):
        return Professor.say(self, '') + stuff

pe = Professor('eric')
ae = ArrogantProfessor('eric')

print pe.say('the sky is blue')
print pe.say('the sky is blue') == 'Prof. eric says: I believe that eric says: the sky is blue'

print ae.say('the sky is blue')
print ae.say('the sky is blue') == 'Prof. eric says: It is obvious that I believe that eric says: the sky is blue'
