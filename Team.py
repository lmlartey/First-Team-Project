class Team:

    def __init__(self):
        """ Asks for the user input for a noun and stores the noun in
        the instance variable self.word.  Remember a noun is a person,
        place, or thing. """
        # TODO by person 3
	self.word = raw_input('enter a noun:  ')
        pass

    def reverse_input(self):
        """ Changes self.word to its reverse.  For example if
        self.word is 'apples', then it becomes 'selppa'."""
        # TODO by person 1
 	k=self.word
	print k[::-1]
	
		
        pass
    
    def print_in_sentence(self):
        """ Insert self.word in the sentence 'Today I dreamt of
        <self.word> while walking on the beach.' replacing <self.word>
        for the noun that was chosen during class construction. """
        print "Today I dreamt of %s while walking on the beach."%(self.word)	 
        # TODO by person 2
      

t = Team()
t.reverse_input()
t.print_in_sentence()

#thanks be to God
#i dont know why this no dey push go the site. i dey fork am
