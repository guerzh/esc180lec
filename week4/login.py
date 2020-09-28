
def login(username, password):
    # users: guerzhoy, cluett, thywissen
    # password: SJAFJKdfjsdf@#$adks, matrix, newton
    global n_attempts
    if n_attempts >= 3:
        n_attempts += 1
        return "Refused"
    if username == "guerzhoy" and password == "SJAFJKdfjsdf@#$adks":
        n_attempts = 0
        return "OK"
    elif username == "cluett" and password == "matrix":
        n_attempts = 0
        return "OK"
    elif username == "thywissen" and password == "newton":
        return "OK"
    else:
        n_attempts += 1
        return "Retry"

def initialize():
    global n_attempts
    n_attempts = 0

initialize()
if __name__ == "__main__":
    initialize()
    login("cluett", "matrix")
    login("cluett", "matrix0")
    login("cluett", "matrix")
    login("cluett", "matrix1")
    login("collins", "elegance")
    login("collins", "elegance")