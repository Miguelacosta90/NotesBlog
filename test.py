class human(object):
    def __init__(self, clan=None):
        self.clan = clan
        self.health = 100
        self.strangth = 10
        self.intelligence = 5
        self.stealth = 5

    def taunt(self):
        print "this message is for Humans"

miguel = human("Coding DOJO")
miguel.taunt()

class test(object):
    def __init__(self, phrase='nothing was passed'):
        print "this string will print from phrase" + phrase
        self.phrase = phrase
test1 = test("Hello, World")
test2 = test()
print "Test 1 has phrase: '" + test1.phrase + "'"
print "Test 2 has phrase, '" + test2.phrase + "'"
