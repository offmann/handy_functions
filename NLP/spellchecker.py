# !pip install pyspellchecker

from spellchecker import SpellChecker

def check_spell(phrase, language):
  spell = SpellChecker(language=language)

  phrase = phrase.split()
  # find those words that may be misspelled
  misspelled = spell.unknown(phrase)

  most_likely = dict() 
  candidats = dict()

  for word in misspelled:
      # Get the one `most likely` answer
      most_likely[word] = spell.correction(word)

      # Get a list of `likely` options
      candidats[word] = spell.candidates(word)


  return (("les erreurs dans la phrase sont : {} ".format(misspelled)),
          ("les corrections les plus proches sont : {}".format(most_likely)),
          ("les candidats les plus proches sont : {}".format(candidats)))
