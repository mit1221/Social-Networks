""" CSC108 Assignment 3: Social Networks - Starter code """
from typing import List, Tuple, Dict, TextIO
profiles = open('profiles.txt')
p = {}
n = {}
ex1 = {'Jay Pritchett': ['Claire Dunphy', 'Gloria Pritchett', 'Manny Delgado'], 'Claire Dunphy': ['Jay Pritchett', 'Mitchell Pritchett', 'Phil Dunphy'], 'Manny Delgado': ['Gloria Pritchett', 'Jay Pritchett', 'Luke Dunphy'], 'Mitchell Pritchett': ['Cameron Tucker', 'Claire Dunphy', 'Luke Dunphy'], 'Alex Dunphy': ['Luke Dunphy'], 'Cameron Tucker': ['Gloria Pritchett', 'Mitchell Pritchett'], 'Haley Gwendolyn Dunphy': ['Dylan D-Money', 'Gilbert D-Cat'], 'Phil Dunphy': ['Claire Dunphy', 'Luke Dunphy'], 'Dylan D-Money': ['Chairman D-Cat', 'Haley Gwendolyn Dunphy'], 'Gloria Pritchett': ['Cameron Tucker', 'Jay Pritchett', 'Manny Delgado'], 'Luke Dunphy': ['Alex Dunphy', 'Manny Delgado', 'Mitchell Pritchett', 'Phil Dunphy']}
ex2 = {'Claire Dunphy': ['Parent Teacher Association'], 'Manny Delgado': ['Chess Club'], 'Mitchell Pritchett': ['Law Association'], 'Alex Dunphy': ['Chess Club', 'Orchestra'], 'Cameron Tucker': ['Clown School', 'Wizard of Oz Fan Club'], 'Phil Dunphy': ['Real Estate Association'], 'Gloria Pritchett': ['Parent Teacher Association']}

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
        if name not in person_to_friends:
            person_to_friends[name] = []
        if name not in person_to_networks:
            person_to_networks[name] = [] 
    
        line = profiles_file.readline()
        while line != '\n' and line != '':
            if ',' in line:
                friend = format_name(line)            
                if friend not in person_to_friends[name]:
                    person_to_friends[name].append(friend)
            else:
                network = line.rstrip('\n')
                if network not in person_to_networks[name]:
                    person_to_networks[name].append(network)
            line = profiles_file.readline()
        line = profiles_file.readline()
    
    for person in list(person_to_friends.keys()):
        if person_to_friends[person] == []:
            person_to_friends.pop(person)
    
    for person in list(person_to_networks.keys()):
        if person_to_networks[person] == []:
            person_to_networks.pop(person)
    
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
    
    >>> get_families({'Mit Kapadia': ['Alexander Jonckers', \
     'Jacob Brown', 'Jay Kapadia', 'John Ventura'], 'John Ventura': \
     ['Gamila Jonckers', 'Rachel Lawerenz']})
    {'Kapadia': ['Jay', 'Mit'], 'Jonckers': ['Alexander', 'Gamila'], 'Brown': \
['Jacob'], 'Ventura': ['John'], 'Lawerenz': ['Rachel']}
    >>>
    
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


def invert_network(person_to_networks: Dict[str, List[str]]) -> Dict[str, List[str]]:
    """Return a "network to people" dictionary based on the given "person to 
    networks" dictionary. The values in the dictionary are sorted 
    alphabetically.
    
    >>> invert_network({'Mit Kapadia': ['Chess Club', 'Finance Club'], \
     'John Ventura': ['Chess Club', 'Law Association']})
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
    
    >>> get_friends_of_friends({'Mit Kapadia': ['Alexander Jonckers', \
     'Jacob Brown', 'Jay Kapadia', 'John Ventura'], 'John Ventura': \
     ['Gamila Jonckers', 'Mit Kapadia', 'Rachel Lawerenz'], 'Jay Kapadia': \
     ['Jacob Brown', 'Gamila Jonckers', 'Mike Ross', 'Mit Kapadia']}, \
     'Mit Kapadia')
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
    """
    """
    potential_friends = []
    
    if person in person_to_friends:
        possible_friends = get_potential_friends(person_to_friends, person)
        person_friends = person_to_friends[person]

        for friend in possible_friends:
            score = 0
            if friend in person_to_friends:
                friend_friends = person_to_friends[friend]
                
                for person_ in person_friends:
                    if person_ in friend_friends:
                        score += 1
            
            if friend in person_to_networks:
                network_to_people = invert_network(person_to_networks)
                for network in network_to_people:
                    if person in network_to_people[network] and friend in \
                       network_to_people[network]:
                        score += 1
            if score > 0:
                if person[person.rfind(' ') + 1:] == \
                   friend[friend.rfind(' ') + 1:]:
                    score += 1
                potential_friends.append((friend, score))  
    sort_tuples_list(potential_friends)
    return potential_friends


def sort_tuples_list(list1: List[Tuple[str, int]]) -> None:
    '''Sort list1, which is a list of tuples from highest to lowest score. If 
    the same score occurs in more than one tuple, then sort those 
    elements alphabetically.
    '''
    end = len(list1) - 1
    
    while end != 0:
        for i in range(end):
            if list1[i][1] < list1[i + 1][1]:
                list1[i], list1[i + 1] = list1[i + 1], list1[i]
            if (list1[i][1] == list1[i + 1][1]) and (list1[i][0] > \
                                                     list1[i + 1][0]):
                list1[i], list1[i + 1] = list1[i + 1], list1[i]  
        end = end - 1    

def format_name(person: str) -> str:
    """Return a new string in the format "FirstName(s) LastName" given the 
    format "LastName, FirstName(s)\n"
    
    >>> format_name('D-Money, Dylan\\n')
    'Dylan D-Money'
    >>> format_name('Dunphy, Haley Gwendolyn\\n')
    'Haley Gwendolyn Dunphy'
    """
    person = person.rstrip('\n')
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
    >>> d = {'Chess Club': ['Mit Kapadia']}
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


def get_potential_friends(person_to_friends: Dict[str, List[str]], \
                          person: str) -> List[str]:
    """Return a list of all the people that person is not friends with.
    
    >>> get_potential_friends({'Mit Kapadia': ['Alexander Jonckers', \
     'Jacob Brown', 'Jay Kapadia', 'John Ventura'], 'John Ventura': \
     ['Gamila Jonckers', 'Mit Kapadia', 'Rachel Lawerenz'], 'Jay Kapadia': \
     ['Jacob Brown', 'Gamila Jonckers', 'Mike Ross', 'Mit Kapadia']}, \
     'Mit Kapadia')
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
    
    return potential_friends


if __name__ == '__main__':
    import doctest
    doctest.testmod()
