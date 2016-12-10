class Musician(object):
  def __init__(self, sounds):
    self.sounds = sounds
    
  def solo(self, length):
    for i in range(length):
      print self.sounds[i % len(self.sounds)],
    print " "
    
class Bassist(Musician): # The Musician class is the parent of the Bassist class
  def __init__(self):
    #first call of the __init__ method of the parent class
    super(Bassist, self).__init__(["Twang", "Thrumb", "Bling"])
    
class Guitarist(Musician):
  def __init__(self):
    #Call the __init__ method of the parent class
    super(Guitarist, self).__init__(["Boink", "Bow", "Boom"])
    
  def tune(self):
    print "Be with you in a moment"
    print "Twoning, sproing, splang"
    
class Drummer(Musician):
  def __init__(self):
    #Call the __init__ method of the parent class
    super(Drummer, self).__init__(["Ratta", "Tat", "Tap"])
    
  def count_to_four(self):
    print "One, two, three, four!"
    
  def spontaneously_combust(self):
    print "Boom! ......"
    
class Band(object):
  def __init__(self):
    self.members = {}
    
  def hire(self, role, musician):
    self.members[role] = musician
    
  def fire(self, role):
    if role in self.members:
      del self.members[role]
    
  def play_music(self, length):
    self.members['drummer'].count_to_four()
    for role, musician in self.members.iteritems():
      musician.solo(length)
      
if __name__ == '__main__':
  derek = Drummer()
  nigel = Guitarist()
  david = Bassist()
  the_the = Band()
  the_the.hire('drummer', derek)
  the_the.play_music(5)
  the_the.hire('guitarist', nigel)
  the_the.hire('bassist', david)
  the_the.play_music(3)
  the_the.fire('guitarist')
  the_the.play_music(1)      
