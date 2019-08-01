from math import ceil

import library


def calculate_knowledge(scores):
  if len(scores) == 1:
    return scores[0] / 2
  
  knowledge = scores[0]/2
  for score in scores[1:]:
    knowledge = knowledge/2 + score/2
  return knowledge


def print_score(concept, scores):
  knowledge = calculate_knowledge(scores)

  print(concept)
  print(f'|{"=" * ceil(knowledge/10)}{" " * (10 - ceil(knowledge/10))}|', end=' ')

  if knowledge > 90:
    print('Awesome!')
  elif knowledge > 75:
    print('Doing great! Keep practicing.')
  elif knowledge > 50:
    print('Doing well! Keep practicing.')
  else:
    print('The more you practice the more you learn!')
  print()

model = library.load_model()

for concept, scores in model.items():
  print_score(concept, scores)
