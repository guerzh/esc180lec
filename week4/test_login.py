import login

if __name__ == '__main__':
    # Test 1: successful login
    login.initialize()
    if login.login("cluett", "matrix") == "OK":
        print("Test 1 passed")
    else:
        print("Test 1 failed")

    # Test 2: three unsuccessful logins in a row, then correct login
    login.initialize()
    login.login("cluett", "integral")
    login.login("cluett", "integral")
    login.login("cluett", "integral")
    if login.login("cluett", "matrix") == "Refused":
        print("Test 2 passed")
    else:
        print("Test 2 failed")

    # Test 3: three unsuccessful logins, not in a row
    login.initialize()
    login.login("cluett", "integral")
    login.login("thywissen", "newton")
    login.login("cluett", "integral")
    login.login("cluett", "integral")
    if login.login("cluett", "matrix") == "Refused":
        print("Test 3 passed")
    else:
        print("Test 3 failed")


    # Test 4: three unsuccessful logins, not in a row
    login.initialize()
    login.login("cluett", "integral")
    login.login("thywissen", "newton")
    login.login("guerzhoy", "integral")
    login.login("cluett", "integral")
    if login.login("cluett", "matrix") == "Refused":
        print("Test 4 passed")
    else:
        print("Test 4 failed")