""" CSC108 Assignment 3: Social Networks - Starter code """
from typing import List, Tuple, Dict, TextIO

def load_profiles(profiles_file: TextIO, person_to_friends: \
                  Dict[str, List[str]], person_to_networks: \
                  Dict[str, List[str]]) -> None:
    """Update the "person to friends" dictionary person_to_friends and the
    "person to networks" dictionary person_to_networks to include data from
    profiles_file.

    Docstring examples not given since result depends on input data.
    """
    line = profiles_file.readline()
    while line != '':
        name = format_name(line)
        line = add_to_dict(name, person_to_friends, person_to_networks, \
                           profiles_file)
    
    sort_values(person_to_friends)
    sort_values(person_to_networks)


def get_average_friend_count(person_to_friends: Dict[str, List[str]]) -> float:
    """Return the average number of friends that people who appear as keys in 
    the given "person to friends" dictionary have.
    
    >>> get_average_friend_count({'Mit Kapadia': ['Alexander Jonckers', \
     'Jacob Brown', 'Jay Kapadia', 'John Ventura'], 'John Ventura': \
     ['Gamila Jonckers', 'Rachel Lawerenz']})
    3.0
    """
    if person_to_friends != {}:
        total_friends = 0
        
        for person in person_to_friends:
            total_friends += len(person_to_friends[person])
        
        return total_friends / len(person_to_friends)
    return 0.0

def get_families(person_to_friends: Dict[str, List[str]]) -> Dict[str, \
                                                                  List[str]]:
    """Return a "last name to first names" dictionary based on the given 
    "person to friends" dictionary.
    
    >>> dict1 = {'Mit Kapadia': ['Alexander Jonckers', 'Jacob Brown', \
    'Jay Kapadia', 'John Ventura'], 'John Ventura': ['Gamila Jonckers', \
    'Rachel Lawerenz']}
    >>> get_families(dict1)
    {'Kapadia': ['Jay', 'Mit'], 'Jonckers': ['Alexander', 'Gamila'], 'Brown': \
['Jacob'], 'Ventura': ['John'], 'Lawerenz': ['Rachel']}
    """
    lastname_to_firstname = {}
    
    for person in person_to_friends:
        firstname = person[:person.rfind(' ')]
        lastname = person[person.rfind(' ') + 1:]
        
        create_key_value_pairs(lastname_to_firstname, lastname, firstname)
        
        for friend in person_to_friends[person]:
            firstname = friend[:friend.rfind(' ')]
            lastname = friend[friend.rfind(' ') + 1:]
            
            create_key_value_pairs(lastname_to_firstname, lastname, firstname)            
    
    sort_values(lastname_to_firstname)
    
    return lastname_to_firstname


def invert_network(person_to_networks: Dict[str, List[str]]) -> Dict[str, \
                                                                     List[str]]:
    """Return a "network to people" dictionary based on the given "person to 
    networks" dictionary. The values in the dictionary are sorted 
    alphabetically.
    
    >>> networks = {'Mit Kapadia': ['Chess Club', 'Finance Club'], 'John Ventura': \
    ['Chess Club', 'Law Association']}
    >>> invert_network(networks)
    {'Chess Club': ['John Ventura', 'Mit Kapadia'], 'Finance Club': \
['Mit Kapadia'], 'Law Association': ['John Ventura']}
    """
    network_to_people = {}
    
    for person in person_to_networks:
        for network in person_to_networks[person]:
            create_key_value_pairs(network_to_people, network, person)
    
    sort_values(network_to_people)
    
    return network_to_people


def get_friends_of_friends(person_to_friends: Dict[str, List[str]], \
    person: str) -> List[str]:
    """Given a "person to friends" dictionary and the name of a person, return 
    the list of names of people who are friends of the named person's friends, 
    sorted alphabetically.
    
    >>> friends = {'Mit Kapadia': ['Alexander Jonckers', \
     'Jacob Brown', 'Jay Kapadia', 'John Ventura'], 'John Ventura': \
     ['Gamila Jonckers', 'Mit Kapadia', 'Rachel Lawerenz'], 'Jay Kapadia': \
     ['Jacob Brown', 'Gamila Jonckers', 'Mike Ross', 'Mit Kapadia']}
    >>> get_friends_of_friends(friends, 'Mit Kapadia')
    ['Gamila Jonckers', 'Gamila Jonckers', 'Jacob Brown', 'Mike Ross', \
'Rachel Lawerenz']
    """
    friends_of_friends = []
    
    if person in person_to_friends:
        friends = person_to_friends[person]
    
        for friend in friends:
            if friend in person_to_friends:
                friends_of_friends.extend(person_to_friends[friend])
                
        while person in friends_of_friends:
            friends_of_friends.remove(person)
        
        friends_of_friends.sort()
    
    return friends_of_friends


def make_recommendations(person: str, person_to_friends: Dict[str, List[str]], \
    person_to_networks: Dict[str, List[str]]) -> List[Tuple[str, int]]:
    """For the person specified, this makes recommendations about potential 
    friends based on mutual friends, common networks, and last names. It returns
    a list of tuples containing the potential friend and their score.
    
    >>> p2f = {'Jay Pritchett': ['Claire Dunphy', 'Gloria Pritchett', \
    'Manny Delgado'], 'Claire Dunphy': ['Jay Pritchett', 'Mitchell Pritchett', \
    'Phil Dunphy'], 'Manny Delgado': ['Gloria Pritchett', 'Jay Pritchett', \
    'Luke Dunphy'], 'Mitchell Pritchett': ['Cameron Tucker', 'Claire Dunphy', \
    'Luke Dunphy'], 'Alex Dunphy': ['Luke Dunphy'], 'Cameron Tucker': \
    ['Gloria Pritchett', 'Mitchell Pritchett'], 'Haley Gwendolyn Dunphy': \
    ['Dylan D-Money', 'Gilbert D-Cat'], 'Phil Dunphy': ['Claire Dunphy', \
    'Luke Dunphy'], 'Dylan D-Money': ['Chairman D-Cat', \
    'Haley Gwendolyn Dunphy'], 'Gloria Pritchett': ['Cameron Tucker', \
    'Jay Pritchett', 'Manny Delgado'], 'Luke Dunphy': ['Alex Dunphy', \
    'Manny Delgado', 'Mitchell Pritchett', 'Phil Dunphy']}
    >>> p2n = {'Claire Dunphy': ['Parent Teacher Association'], \
    'Manny Delgado': ['Chess Club'], 'Mitchell Pritchett': ['Law Association'],\
    'Alex Dunphy': ['Chess Club', 'Orchestra'], 'Cameron Tucker': \
    ['Clown School', 'Wizard of Oz Fan Club'], 'Phil Dunphy': \
    ['Real Estate Association'], 'Gloria Pritchett': \
    ['Parent Teacher Association']}
    >>> make_recommendations('Jay Pritchett', p2f, p2n)
    [('Mitchell Pritchett', 2), ('Cameron Tucker', 1), ('Luke Dunphy', 1), \
('Phil Dunphy', 1)]
    >>> make_recommendations('Claire Dunphy', p2f, p2n)
    [('Luke Dunphy', 3), ('Gloria Pritchett', 2), ('Cameron Tucker', 1), \
('Manny Delgado', 1)]
    """
    potential_friends = []
    possible_friends = get_possible_friends(person_to_friends, person)
    friends_of_friends = []
    network_to_people = invert_network(person_to_networks)
    is_person_in_networks = person in person_to_networks
    person_lastname = person[person.rfind(' ') + 1:]
    
    if person in person_to_friends:    
        friends_of_friends = get_friends_of_friends(person_to_friends, person)
    
    for friend in possible_friends:
        score = 0
        score += friends_of_friends.count(friend)
        score += common_networks(person, is_person_in_networks, friend, \
                                 person_to_networks, network_to_people)
        check_lastnames(score, person_lastname, friend, potential_friends)
    sort_tuples_list(potential_friends)
    return potential_friends


def common_networks(person: str, is_person_in_networks: bool, friend: str, \
                    person_to_networks: Dict[str, List[str]], \
                    network_to_people: Dict[str, List[str]]) -> int:
    """Return the number of networks that person and friend have in common using
    person_to_networks and network_to_people dictionaries.
    
    >>> networks = {'Mit Kapadia': ['Chess Club', 'Finance Club'], \
    'John Ventura': ['Chess Club', 'Law Association']}
    >>> invert_networks = {'Chess Club': ['John Ventura', 'Mit Kapadia'], \
    'Finance Club': ['Mit Kapadia'], 'Law Association': ['John Ventura']}
    >>> common_networks('Mit Kapadia', True, 'John Ventura', networks, \
invert_networks)
    1
    """
    score = 0
    if (is_person_in_networks) and (friend in person_to_networks):
        for network in network_to_people:
            if person in network_to_people[network] and friend in \
               network_to_people[network]:
                score += 1
    return score


def check_lastnames(score: int, person_lastname: str, friend: str, \
                    potential_friends: List[Tuple[str, int]]) -> None:
    """Add 1 to score if person_lastname and friend's lastname are the same and 
    then add a tuple of form (friend, score) to potential_friends.
    
    >>> potential_friends = []
    >>> check_lastnames(2, 'Kapadia', 'Jay Kapadia', potential_friends)
    >>> potential_friends
    [('Jay Kapadia', 3)]
    """
    if score > 0:
        if person_lastname == friend[friend.rfind(' ') + 1:]:
            score += 1
        potential_friends.append((friend, score))    


def sort_tuples_list(list1: List[Tuple[str, int]]) -> None:
    '''Sort list1, which is a list of tuples from highest to lowest score. If 
    the same score occurs in more than one tuple, then sort those 
    elements alphabetically.
    
    >>> list1 = [('Mit Kapadia', 4), ('Jay Pritchett', 3), ('Claire Dunphy', 5), \
    ('Cameron Tucker', 3)]
    >>> sort_tuples_list(list1)
    >>> list1
    [('Claire Dunphy', 5), ('Mit Kapadia', 4), ('Cameron Tucker', 3), \
('Jay Pritchett', 3)]
    '''
    end = len(list1) - 1
    
    while end > 0:
        for i in range(end):
            if list1[i][1] < list1[i + 1][1]:
                list1[i], list1[i + 1] = list1[i + 1], list1[i]
            elif (list1[i][1] == list1[i + 1][1]) and (list1[i][0] > \
                                                     list1[i + 1][0]):
                list1[i], list1[i + 1] = list1[i + 1], list1[i]  
        end = end - 1    


def add_to_dict(name: str, person_to_friends: Dict[str, List[str]], \
                person_to_networks: Dict[str, List[str]], profiles_file: \
                TextIO) -> str:
    """Reads a line from profiles_file and adds it to the 
    person_to_friends or person_to_networks dictionary depending on the 
    contents of it. Returns the next line.
    
    Docstring examples not given since result depends on input data.
    """
    line = profiles_file.readline()
    while line != '\n' and line != '':
        if ',' in line:
            friend = format_name(line)
            create_key_value_pairs(person_to_friends, name, friend)
        else:
            network = line.rstrip('\n')
            create_key_value_pairs(person_to_networks, name, network)
        line = profiles_file.readline()
    return profiles_file.readline()


def format_name(person: str) -> str:
    """Return a new string in the format "FirstName(s) LastName" given the 
    format "LastName, FirstName(s)\n"
    
    >>> format_name('D-Money, Dylan  \\n')
    'Dylan D-Money'
    >>> format_name('Dunphy, Haley Gwendolyn\\n')
    'Haley Gwendolyn Dunphy'
    """
    person = person.rstrip(' \n')
    lastname = person[:person.find(',')]
    firstname = person[person.find(',') + 2:]
    return firstname + ' ' + lastname


def create_key_value_pairs(dictionary: Dict[str, List[str]], key: str, \
                           value: str) -> None:
    """Make a new key-value pair in dictionary with key and value, where all 
    the values in dictionary are of type list.
    
    >>> d = {}
    >>> create_key_value_pairs(d, 'Chess Club', 'Mit Kapadia')
    >>> d
    {'Chess Club': ['Mit Kapadia']}
    >>> create_key_value_pairs(d, 'Chess Club', 'John Ventura')
    >>> d
    {'Chess Club': ['Mit Kapadia', 'John Ventura']}
    """
    if key not in dictionary:
        dictionary[key] = []
    if value not in dictionary[key]:
        dictionary[key].append(value)


def sort_values(dictionary_to_sort: Dict[str, List[str]]) -> None:
    """Sort the values in dictionary_to_sort alphabetically.
    
    >>> d = {'Parent Association': ['Gloria Pritchett', \
    'Claire Dunphy'], 'Chess Club': ['Manny Delgado', 'Alex Dunphy']}
    >>> sort_values(d)
    >>> d
    {'Parent Association': ['Claire Dunphy', 'Gloria Pritchett'], \
'Chess Club': ['Alex Dunphy', 'Manny Delgado']}
    """
    for key in dictionary_to_sort:
        dictionary_to_sort[key].sort()


def get_possible_friends(person_to_friends: Dict[str, List[str]], \
                          person: str) -> List[str]:
    """Return a list of all the people that person is not friends with.
    
    >>> friends = {'Mit Kapadia': ['Alexander Jonckers', 'Jacob Brown', \
    'Jay Kapadia', 'John Ventura'], 'John Ventura': ['Gamila Jonckers', \
    'Mit Kapadia', 'Rachel Lawerenz'], 'Jay Kapadia': ['Jacob Brown', \
    'Gamila Jonckers', 'Mike Ross', 'Mit Kapadia']}
    >>> get_possible_friends(friends, 'Mit Kapadia')
    ['Gamila Jonckers', 'Rachel Lawerenz', 'Mike Ross']
    """
    potential_friends = []
    
    if person in person_to_friends:    
        current_friends = person_to_friends[person]
        
        for person_ in person_to_friends:
            if person_ not in current_friends and person_ not in \
               potential_friends:
                potential_friends.append(person_)
            
            for friend in person_to_friends[person_]:
                if friend not in current_friends and friend not in \
                   potential_friends:
                    potential_friends.append(friend)
                    
        while person in potential_friends:
            potential_friends.remove(person)
    else:
        for key in person_to_friends:
            if key not in potential_friends:
                potential_friends.append(key)
            for friend in person_to_friends[key]:
                if friend not in potential_friends:
                    potential_friends.append(friend)
    
    return potential_friends


if __name__ == '__main__':
    import doctest
    doctest.testmod()
