def error_name(error):
    name_start = str(type(error)).rfind('.') + 1
    name = str(type(error))[name_start:-2]
    return name


