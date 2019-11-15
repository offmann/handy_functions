# !pip install pyspellchecker

from spellchecker import SpellChecker

def spell_check(sent, language):
  
  spell = SpellChecker(language=language)

  sent = sent.split()
  
  # find those words that may be misspelled
  misspelled = spell.unknown(sent)

  most_likely = dict() 
  candidats = dict()

  for word in misspelled:
      # Get the one `most likely` answer
      most_likely[word] = spell.correction(word)

      # Get a list of `likely` options
      candidats[word] = spell.candidates(word)


  return (("The errors in the sentence are : {} ".format(misspelled)),
          ("The most likely answer : {}".format(most_likely)),
          ("The other likely options  : {}".format(candidats)))
