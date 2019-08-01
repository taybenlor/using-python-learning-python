import csv
from collections import defaultdict

def load_model():
  scores = defaultdict([])
  with open('model/scores.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
      concept = row[0]
      score_list = row[1:]
      scores[concept] = score_list
  return scores

def save_model(scores):
  with open('model/scores.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    for concept, score_list in scores.items():
      writer.writerow([concept] + score_list)
