# Grammar Checker
# https://bitbucket.org/spirit/language_tool
# https://github.com/myint/language-check
# 
# GAN approach
# sentence -> realizer permutations -> adversarial network (grammar checker)
#
# Use existing sentences as model for proper grammar in adversarial network
# (in addition to grammar check). This handles problematic false negatives
# like "PAL 233 has arrived what terminal." that are not captured by
# grammar checkers. In other words, realized sentences likely pass all
# grammar checkers despite being idiomatically incorrect.
import numpy as np
from sklearn.utils.extmath import cartesian
import urllib3, json

from pez_ai import grammar

http = urllib3.PoolManager()

forms = {
  'tense': np.array(["past","present","future"], 'U9'),
  'perfect': [True,False],
  'passive': [True,False],
  'number': ['singular','passive'],
}

def permute_sentence(text, form):
  nps = grammar.noun_phrases(text)
  vps = grammar.verb_phrases(text)
  pass


# Parse sentence and extract SVO plus other POS
# Get set of permutations
def get_language_forms():
  def jsonize(x):
    sentence = { 'features': { 
      "tense":x[0], "perfect":x[1],
      "passive":x[2], "number":x[3]
    }}
    return sentence

  raw = cartesian(forms.values()).tolist()
  return [ jsonize(x) for x in raw ]

# Return sentences
# Add synonyms for verbs, nouns via NLTK synsets
def permute_synonyms(sentence):
  pass



def send_data(json_str):
  req = http.request('POST', "http://localhost:8099/generate",
    headers={"Content-Type":"application/json"},
    body=json_str)
  return req.read()



def test_permute():
  # http://www.chompchomp.com/terms/prepositionalphrase.htm
  raw = [
    "Which bonds does Justine care about?",
    "During what hours can stocks and bonds be traded?",
    "Why is there a debit or credit in my account?",
    "Why hasn't Vanguard taken money from, or moved money into, my money market account?",
    "How are dividends and interest credited to my account?",
    "What can I do with a security that is considered worthless?",
    "How do I close my brokerage account, and are there any fees for doing so?",
    "The book on the bathroom floor is swollen from shower steam.",
    "The sweet potatoes in the vegetable bin are green with mold.",
    "The note from Beverly confessed that she had eaten the leftover pizza",
    "Freddy is stiff from yesterday's long football practice",
    "Before class, Josh begged his friends for a pencil",
    "Feeling brave, we tried the Dragon Breath Burritos at Tito's Taco Palace",
    "Neither of these cookbooks contains the recipe for Manhattan-style squid eyeball stew",
    "My essay, to be perfectly honest, flew out of the bus window while I was riding to school.",
    "The bathroom tiles, whenever time permits, require a good scrubbing, for the grout is black with mold.",
    "Since Francisco was five years old, swimming has been his passion",
    "Francisco enjoys swimming more than spending time with his girlfriend Diana",
    "Now Francisco practices his sport in safe swimming pools",
    "After drinking the old milk, Vladimir turned green",
    "A ten-item quiz seems impossibly long after a night of no studying",
    "Sylvia tasted the spicy squid eyeball stew",
    "The squid eyeball stew tasted good.",
    "Sherylee smacked her lips as raspberry jelly dripped from the donut onto her white shirt."
  ]
