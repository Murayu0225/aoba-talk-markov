import markovify

text = open("./../data/mecab.txt", "r").read()

text_model = markovify.NewlineText(text, state_size=3, well_formed=False)

with open('./../data/learned_data.json', 'w') as f:
    f.write(text_model.to_json())
