#!/usr/bin/jython

# Make sure we add simplenlg to the path
import sys
from time import clock

print "%.3f:\t Adding simplenlg to path" % clock()
sys.path.append("./simplenlg.jar")

print "%.3f:\t Importing simplenlg" % clock()
# Import the parts of the library we'll be handling directly
from simplenlg.framework import NLGFactory, CoordinatedPhraseElement, ListElement
from simplenlg.lexicon import Lexicon
from simplenlg.realiser.english import Realiser
from simplenlg.features import Feature, Tense, NumberAgreement

print "%.3f:\t Initialising the Lexicon, NLGFactory, and Realiser" % clock()
# Initalise the lexicon, factory and realiser. This only needs to be done once
lexicon = Lexicon.getDefaultLexicon()
nlgFactory = NLGFactory(lexicon)
realiser = Realiser(lexicon)

print "%.3f:\t Creating tree for first sentence" % clock()
# Now we start work on the first sentence
s1 = nlgFactory.createClause() # Create a placeholder
s1.setSubject("john") # Add John as the subject
s1.setVerb("baking") # Add baking as the verb. N.B. The verb is inflected

cake = nlgFactory.createNounPhrase("cake") # Create a noun phrase around the word 'cake'
cake.setDeterminer("a") # But we don't know it's 'the' cake, so indefinite article required
s1.setObject(cake) # Set it as the object of the sentence

ingObj = nlgFactory.createNounPhrase("ingredients") # We need to be able to describe ingredients
ingObj.setDeterminer("a") # But they aren't definite yet, so 'a' is the appropriate determiner
ingObj.setFeature(Feature.NUMBER, NumberAgreement.PLURAL) # It's a collection, so they're plural

fromPrep = nlgFactory.createPrepositionPhrase() # This is part of a prepositional phrase
fromPrep.addComplement(ingObj) # The preposited thing is the ingredients
fromPrep.setPreposition("from") # It's derived from, so 'from' should be the right preposition?
s1.addComplement(fromPrep) # Add the preposition phrase as a complement to the sentence

s1.setFeature(Feature.TENSE, Tense.PAST) # PROV is in the past tense.

print "%.3f:\t Creating tree for second sentence" % clock()
# Second sentence
s2 = nlgFactory.createClause() # Create placeholder

ingNameNP = nlgFactory.createNounPhrase("ingredients") # This time the ingredients are the subject
ingNameNP.setDeterminer("the") # But they are now definite, so the determiner is "the"
ingNameNP.setFeature(Feature.NUMBER, NumberAgreement.PLURAL) # And they're still plural

s2.setSubject(ingNameNP) # The ingredients are the subject
s2.setVerb("be") # The verb is 'to be' 

ings = [nlgFactory.createNounPhrase("eggs"), # Create a list of nouns
        nlgFactory.createNounPhrase("butter"),
        nlgFactory.createNounPhrase("flour"),
        nlgFactory.createNounPhrase("sugar")]

ings[0].setFeature(Feature.NUMBER, NumberAgreement.PLURAL) # The eggs are actually plural!

ingsNP = nlgFactory.createCoordinatedPhrase() # Now we want to build the list into a syntactic structure.

for ing in ings:
    ingsNP.addCoordinate(ing) # So we add them one at a time.

s2.setObject(ingsNP) # And set this structure as the object of the sentence
s2.setFeature(Feature.TENSE, Tense.PAST) # Still PROV, still past tense

print "%.3f:\t Putting the sentences into a paragraph" % clock()
par = nlgFactory.createParagraph() # Create a paragraph placeholder
par.addComponent(s1) # Add the first sentence
par.addComponent(s2) # Add the second

print "%.3f:\t Realising paragraph" % clock()
realisedPar = realiser.realise(par)
realisedParString = realisedPar.getRealisation() # Realise and print the paragraph.
print realisedParString
print "%.3f:\t Execution complete." % clock()
