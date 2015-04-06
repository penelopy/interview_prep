""" https://www.interviewcake.com/question/inflight-entertainment """
 


def inflight_movie(flight_length, array_of_movies):
    d = {}
    for movie in array_of_movies: 
        matching_movie = flight_length - movie
        
        if matching_movie in d: 
            return True
        d[movie] = True

    return False

print inflight_movie(240, [40, 200, 50, 150, 90, 90])