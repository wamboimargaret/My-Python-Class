# A function named concatenate_args that takes any number of string arguments in positional arguments format and concatenates them into a single string
def concatenate_args(*args):
    result = ""
    for arg in args:
        result += arg
    return result

# A function named concatenate_kwargs that takes any number of string arguments in keyword arguments  format and concatenates them into a single string
def concatenate_kwargs(**kwargs):
    result = ""
    for key, value in kwargs.items():
        result += value
    return result