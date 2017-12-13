# Solution for week5 exercise Spell

class Spell(object):
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation

    def __str__(self):
        return self.name + ' ' + self.incantation + '\n' + self.getDescription()

    def getDescription(self):
        return 'No description'

    def execute(self):
        print(self.incantation)


class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')
    def getDescription(self): # question 5
        return 'This charm summons an object to the caster, potentially over a significant distance.'

class Confundo(Spell):
    def __init__(self):
        Spell.__init__(self, 'Confundo', 'Confundus Charm')

    def getDescription(self):
        return 'Causes the victim to become confused and befuddled.'

def studySpell(spell):
    print(spell)

#spell = Accio()
# Accio is a new instance of class Spell and it is store in variable spell
# with name = Summoning charm , incantation = Accio, It does not print anything
#spell.execute()
# going back to class Spell and run execute on instance spell. This prints out self.incatation of instance spell = Accio
#studySpell(spell)
# prints Summoning Charm Accio / No description
#studySpell(Confundo())
# prints out Confundus Charm Confundo Causes the victim to become confused and befuddled
