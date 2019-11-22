import requests
import json
import csv

actors = [[] for _ in range(2000)]
actpk = 1
for page in range(1, 7):
    print(f'-----------------{page}---------------')
    response = requests.get(f'https://api.themoviedb.org/3/movie/now_playing?api_key=6b356c5ae179a5d932c01687a436b72e&language=ko-KR&page={page}&region=KR').text
    res = json.loads(response)

    tmp = []
    for idx, part in enumerate(res['results']):
        response2 = requests.get(f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key=20ea3580299a37f479eee8e01bc91ded&movieNm={part["title"]}').text
        movies = json.loads(response2)

        if len(movies.get("movieListResult").get("movieList")):
            print(movies.get('movieListResult').get('movieList')[0].get('movieCd'))
            response3 = requests.get(f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key=20ea3580299a37f479eee8e01bc91ded&movieCd={movies.get("movieListResult").get("movieList")[0].get("movieCd")}').text
            movie = json.loads(response3)

            with open('actors.csv', 'a', newline='', encoding='utf-8') as actorfile:
                movie_actors = movie.get('movieInfoResult').get('movieInfo').get('actors')
                if idx == 0:
                    fieldnames = ['pk', 'name', 'name_en']
                    writer = csv.DictWriter(actorfile, fieldnames=fieldnames)
                    for actor in movie_actors:
                        if actor not in tmp:
                            ko = actor.get('peopleNm')
                            en = actor.get('peopleNmEn')
                            actors[idx].append(actpk)
                            writer.writerow({
                                'pk': actpk,
                                'name': ko,
                                'name_en': en
                                })
                            actpk += 1
                        else:
                            index = tmp.index(actor)
                            actors[idx].append(index)
                else:
                    writer = csv.writer(actorfile)
                    for actor in movie_actors:
                        if actor not in tmp:
                            ko = actor.get('peopleNm')
                            en = actor.get('peopleNmEn')
                            writer.writerow([actpk, ko, en])
                            actors[idx].append(actpk)
                            actpk += 1
                        else:
                            index = tmp.index(actor)
                            actors[idx].append(index)

    with open('movie.csv', 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['id', 'title', 'original_title', 'score', 'poster_url', 'genres', 'description', 'open_date', 'actors']
        writer = csv.writer(csvfile)
        for i, part in enumerate(res['results']):
            writer.writerow([
                part['id'], 
                part['title'], 
                part['original_title'],
                part['vote_average'], 
                part['poster_path'],
                list(part['genre_ids']), 
                part['overview'], 
                part['release_date'],
                actors[i]
            ])
