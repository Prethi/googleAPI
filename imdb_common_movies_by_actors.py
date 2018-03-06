# PYTHON3
from imdb import IMDb
import timeit

ia = IMDb()

def get_movie_set_by_id(person_id):
    """ Input: personID,
        Output: find the person_detail by
        passing the personID and info as filmography
        and check if actor/actress and fetch the
        movie ids enacted by the person. The details fetched is of the format:

        person_id is of the format: 0362766

        person_detail = <Person id:0362766[http] name:_Hardy, Tom (I)_>

        person_detail.keys() = ['name', 'imdbIndex', 'birth date', 'headshot', 'akas',
        'actor', 'producer', 'writer', 'soundtrack', 'thanks', 'self', 'archive footage',
        'in development', 'birth notes', 'canonical name', 'long imdb name',
        'long imdb canonicalname', 'full-size headshot']

        if actor or actress present in the obtained keys, then fetch all the movies in a set format.

        movie_set = {movie ids}

        if no actor/actress just return None
     """

    person_detail = ia.get_person(person_id[0].personID, info=["filmography"])
    if 'actor' in person_detail.keys():
        movie_set = {l.movieID for l in person_detail['actor']}
    elif 'actress' in person_detail.keys():
        movie_set = {l.movieID for l in person_detail['actress']}
    else:
        print ('%s is not an actor/actress' % person_detail)
        return
    #print(movie_set)
    return movie_set

def get_movie_list_by_name(person_id):
    """ Input: personID,
        Output: find the person_detail by
        passing the personID and info as filmography
        and check if actor/actress and fetch the
        movie names enacted by the person. The details fetched is of the format:

        person_id is of the format: 0362766

        person_detail = <Person id:0362766[http] name:_Hardy, Tom (I)_>

        movie_list = [movie names]

        if no actor/actress just return None
    """
    person_detail = ia.get_person(person_id[0].personID, info=["filmography"])
    if 'actor' in person_detail.keys():
        movie_list = [l['title'] for l in person_detail['actor']]
    elif 'actress' in person_detail.keys():
        movie_list = [l['title'] for l in person_detail['actress']]
    else:
        print ('%s is not an actor/actress' % person_detail)
        return
    #print(movie_list)
    return movie_list

def find_movies_in_common(movielist):
    """ Input: movielist - is a list of sets containing movie ids of different actors.
        format = [{101,1234,456}, {1234,345,789}, {1234,675,989}]
        Using intersection property of set we find the common ids in the entire list (*movielist),
        and then retrieve the movie name for the common ids using get_movie lib func in imdbpy
        Output: list of common movie names"""
    common_movie_ids = set.intersection(*movielist)
    common_movie_names = [ia.get_movie(movie_id)['title'] for movie_id in common_movie_ids]
    return common_movie_names

def list_comp(list1, list2):
    """ Find common movie names using for and in """
    listcomp_common_movies = [elem for elem in list1 if elem in list2]
    return listcomp_common_movies

def common_movies(movie_lists):
    print (movie_lists)
    """ Compare length of lists and iterate over the list that is small """
    if len(movie_lists[0]) >= len(movie_lists[1]):
        listcomp = list_comp(movie_lists[0], movie_lists[1])
    else:
        listcomp = list_comp(movie_lists[1], movie_lists[0])
    #print('listcomp = ', listcomp)
    return listcomp

def main():
    """ If the entered number of actors is 2, list comprehension of for and in movie names lists
        is used to find common movies.
        If more than 2, set intersection is used to find the common movie ids and movie names
        are retrieved from movieids.
        If the entered person do not exist in IMDB, the user is prompted to continue to
        enter the remaining people.
    """
    try:
        total = int(input('Enter the total number of actors: '))
    except ValueError:
        print ('Not a valid number...')
        return

    movieid_list = []
    moviename_list = []
    for i in range(1, total+1):
        name = input('Enter full name of person: ')

        # Fetch the personID by passing the user entered name: output: 0362766
        person_id = ia.search_person(name)

        if person_id and total>2:
            # Creating list of sets containing movie ids [{movies by actor1},{movies by actor2},..]
            movies = get_movie_set_by_id(person_id)
            if movies != None:
                movieid_list.append(movies)
        elif person_id:
            movies = get_movie_list_by_name(person_id)
            if movies != None:
                 # list of lists
                 moviename_list.append(movies)
        else:
            print ('Entered name does not exist in IMDB, continuing.. ')

    if total>2:
       # set intersection
       res = find_movies_in_common(movieid_list)
    else:
       # list comp
       if len(moviename_list)>1:
           res = common_movies(moviename_list)
       else:
           print ('No actors to compare, there is only one actor')
           return
    print ('Common movies acted by the provided actors are - ',res)


if __name__ == '__main__':
    main()


    # FEW EXAMPLES

    """ $ python3 imdb_movies_list.py
        Enter the total number of actors: 3
        Enter full name of person: prabhas
        Enter full name of person: anushka shetty
        Enter full name of person: sathyaraj
        Common movies acted by the provided actors are -  ['Baahubali: The Beginning', 'Mirchi', 'Baahubali 2: The Conclusion']

        $ python3 imdb_movies_list.py
        Enter the total number of actors: 2
        Enter full name of person: aiso
        Aison Scott is not an actor/actress
        Enter full name of person: ranganathan madhavan
        No actors to compare, there is only one actor

        """
