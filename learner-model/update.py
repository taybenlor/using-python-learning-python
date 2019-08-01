import library

concept = input('Which concept are you updating? ')
score = int(input('What score did you get (0-100)? '))

model = library.load_model()
model[concept].append(score)
library.save_model(model)
