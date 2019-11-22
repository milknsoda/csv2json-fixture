import requests
import csv
import json

response = requests.get('https://api.themoviedb.org/3/genre/movie/list?api_key=6b356c5ae179a5d932c01687a436b72e&language=ko').text
print(type(response))
res = json.loads(response)
print(res)
with open('genre.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['id', 'name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for part in res['genres']:
        writer.writerow(part)