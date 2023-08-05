"""
This package includes some type conversation.
E.g.
list -> set
set -> list
dict -> key_list
dict -> value_list
dict -> list
so on.
"""

def list_to_set(value:list):
    """
    This function is converts data, list type to set-type. The variable must be a list.
    If you set in the function non-list variable, you will get error. You can use
    other functions for different value type.
    """

    if type(value) is list:
        temp = set()
        for item in value:
            temp.add(item)
        return temp
    else:
        raise Exception(f"You can not convert {type(value)} to set. Please check your value type!")


def set_to_list(value:set):
    """
    This function is converts data, set-type to list-type. The variable must be a set-type value.
    If you set in the function non-set type variable, you will get error. You can use
    other functions for different value type.
    """

    if type(value) is set:
        temp = list()
        for item in value:
            temp.append(item)
        return temp
    else:
        raise Exception(f"You can not convert {type(value)} to list. Please check your value type!")

def list_to_tuple(value:list):
    """
    This function is converts data, list type to tuple-type. The variable must be a list.
    If you set in the function non-list variable, you will get error. You can use
    other functions for different value type.
    """

    if type(value) is list:
        return tuple(value)
    else:
        raise Exception(f"You can not convert {type(value)} to tuple. Please check your value type!")

def tuple_to_list(value:tuple):
    """
    This function is converts data, tuple-type to list-type. The variable must be a tuple.
    If you set in the function non-tuple variable, you will get error. You can use
    other functions for different value type.
    """

    if type(value) is tuple:
        return list(value)
    else:
        raise Exception(f"You can not convert {type(value)} to list. Please check your value type!")

def set_to_tuple(value:set):
    """
    This function is converts data, set-type to tuple-type. The variable must be a set.
    If you set in the function non-set variable, you will get error. You can use
    other functions for different value type.
    """

    if type(value) is set:
        return tuple(value)
    else:
        raise Exception(f"You can not convert {type(value)} to tuple. Please check your value type!")


def tuple_to_set(value:tuple):
    """
    This function is converts data, set-type to tuple-type. The variable must be a tuple.
    If you set in the function non-tuple variable, you will get error. You can use
    other functions for different value type.
    """

    if type(value) is tuple:
        return set(value)
    else:
        raise Exception(f"You can not convert {type(value)} to set. Please check your value type!")


def list_to_dict(value:list):
    """
    This function is converts data, list-type to dict-type. The variable must be a list.
    If you set in the function non-dict variable, you will get error. You can use
    other functions for different value type.
    Given a list, write a Python program to convert the given list to dictionary such that 
    all the odd elements have the key, and even number elements have the value. 
    Since python dictionary is unordered, the output can be in any order.

    e.g:
    list = ["a", 1, "b", 2, "c", 3] -> {"a":1, "b":2, "c":3}
    """
    if type(value) is list:
        return {value[i]: value[i+1] for i in range(0, len(value), 2)}
    else:
        raise Exception(f"You can not convert {type(value)} to dict. Please check your value type!")

def dict_to_list(value:dict):
    """
    This function is converts data, list-type to dict-type. The variable must be a list.
    If you set in the function non-dict variable, you will get error. You can use
    other functions for different value type.
    Given a dict, write a Python program to convert the given dict to list such that 
    all the odd keys and even values will be list element. 

    e.g:
    dict = {"a":1, "b":2, "c":3} -> ["a", 1, "b", 2, "c", 3]
    """

    if type(value) is dict:
        temp = list()
        for item in value:
            temp.append(item)
            temp.append(value[item])
        return temp
    else:
        raise Exception(f"You can not convert {type(value)} to list. Please check your value type!")


def dict_keys_to_list(value:dict):
    """
    This function is converts data, dict-type to list-type. The variable must be a dict.
    If you set in the function non-dict variable, you will get error. You can use
    other functions for different value type.
     This function returns to list of dict keys

    e.g:
    dict = {"a":1, "b":2, "c":3} -> output: ["a", "b", "c"]
    """

    if type(value) is dict:
        temp = list()
        for item in value:
            temp.append(item)
        return temp
    else:
        raise Exception(f"You can not convert {type(value)} to list. Please check your value type!")
        

def dict_values_to_list(value:dict):
    """
    This function is converts data, dict-type to list-type. The variable must be a dict.
    If you set in the function non-dict variable, you will get error. You can use
    other functions for different value type.
    This function returns to list of dict values

    e.g:
    dict = {"a":1, "b":2, "c":3} -> output: [1, 2, 3]
    """
    
    if type(value) is dict:
        temp = list()
        for item in value:
            temp.append(value[item])
        return temp
    else:
        raise Exception(f"You can not convert {type(value)} to list. Please check your value type!")

