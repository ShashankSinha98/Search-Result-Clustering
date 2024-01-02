import pandas as pd
from NltkPreprocessingSteps import NltkPreprocessingSteps

documents = ["the young french men crowned world champions",
             "Google Translate app is getting more intelligent everyday",
             "Facebook face recognition is driving me crazy",
             "who is going to win the Golden Ball title this year",
             "these camera apps are funny",
             "Croacian team made a brilliant world cup campaign reaching the final match",
             "Google Chrome extensions are useful.",
             "Social Media apps leveraging AI incredibly",
             "Qatar 2022 FIFA world cup is played in winter",
             "I hadn't thought you aren't the person",
             "<h1>Course ML Specialization</h1>",
             "Mr. Bean is in London",
             "#FIFA2023 is viral on twitter",
             "Fußball ist in Deutschland sehr beliebt.",
              "Er gehört zu Europa.",
              "I can't understnd the ruls of Socccer."]

df = pd.DataFrame(documents, columns=["docs"])
txt_preproc = NltkPreprocessingSteps(df['docs'])

processed_text = \
    txt_preproc \
    .remove_html_tags()\
    .replace_diacritics()\
    .expand_contractions()\
    .remove_numbers()\
    .fix_typos()\
    .remove_punctuations_except_periods()\
    .lemmatize()\
    .remove_double_spaces()\
    .remove_all_punctuations()\
    .remove_stopwords()\
    .get_processed_text()

print(processed_text)
