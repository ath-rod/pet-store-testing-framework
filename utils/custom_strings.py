def error_name(error) -> str:
    """
        Returns the name of the caught error for logging purposes:
        i.e. ConnectionError is returned from "HTTPConnectionPool [...] [Errno 11001] getaddrinfo failed"

            Parameters:
                error: caught exception
    """
    name_start = str(type(error)).rfind('.') + 1
    name = str(type(error))[name_start:-2]
    return name
