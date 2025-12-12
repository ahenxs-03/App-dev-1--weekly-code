#pytest
from main import weather
from main import is_prime
from main import divider
from main import UserManager
import pytest
def test_weather():
    assert weather(30)=="hot"

#true---
def test_another():
    assert weather(3)=="cold"
    #assert weather(9)=="hot"
    assert weather(8)=="cold"

#test multiple case
assert weather(1)=="cold"
assert weather(2)=="cold"
#assert weather(57)=="cold"
assert weather(27)=="hot"

#no of case--inside fun 2 inside fun 1, out 4
#expected 2 fails 5 pass
# conclusion
# assert work inside fun aswell as outer,
#seperate funn does not impact 
# where assert there trigger 

#but it doesnot work as we expected!
# so commented out wrong part
#-->working
'''if assert is out side of function and any of them false
pytest cannot collect test case, if all true pytest start getting cases, 
each function itself is case, if all check is true test is passed'''
#---------#
#example 2: error handle 
#check error handle feature

def err_check_approach():
    with pytest.raises(ValueError, match="cannot divide by zero"):
        divider(10,0)

''' topic2'''
'''@pytest.fixture: This is a core feature in pytest used to provide a defined,
 reliable, and consistent context (environment, data, etc.) for tests. 
The decorated function returns or yields the data/context needed by the test,
 which then accesses it by including the fixture's name as an argument in its signature.'''

@pytest.fixture
def freshdata():
    '''create fresh data for each test! 
    as to check functionality of class we need object so that fresh data each time 
    create object'''
    return UserManager()
def test_method_add(freshdata):
    assert freshdata.add_user("Ram","rama123@gmail.com") == True
    assert freshdata.get_user("Ram") == "rama123@gmail.com"

    
def test_method_add(freshdata):
    freshdata.add_user("Ram","rama123@gmail.com")
    with pytest.raises(ValueError, match="User already exists"):
        freshdata.add_user("Ram","rama123@gmail.com")
''''total fixture take as a test case collection'''
#####

''''teardown in fixture'''

'''import pytest
# as currently has no db so this portion is commented out
#summary is simple
# yeild clear your parmanent db like sqlite3,mongodb,postgress,etc
#why new method?
1.to assign data you need db() instance
+ 2. each time clear db as it is fully on test purpose
so yeaid clear db
fixture 


@pytest.fixture
def database_connection():
    # Setup code: establish a database connection
    print("\nSetting up database connection...")
    connection = "mock_db_connection" 
    yield connection # The value "connection" is provided to the test

    # Teardown code: this runs after the test finishes
    print("\nClosing database connection...")
    # In a real scenario, you'd close the connection here
    # connection.close()
    
def test_db_interaction(database_connection):
    # The 'database_connection' fixture is injected here
    print(f"Testing with {database_connection}")
    assert database_connection is not None
'''

######topic-3####
''' parameterized testing'''
'''decorator'''
'''use case:= stop using assert everytime
instead define decorator and use
set limiting cases '''
@pytest.mark.parametrize("num, expected",[(1,False),(2,True),(3,True),(7,False)])
def test_is_prime(num,expected):
    assert is_prime(num) == expected
#here number of element in list = number of test cases
#mocks
'''there is  a part of code not active in test environment'''
'''there is  a part of code not active in test environment'''
'''solution :-mock or create a fake version of that dependency'''
#application routing case--
...

###########end
#tldr
''' to try this build a user friendly coding den like leetcode
set a bunch of problem and try to resolve
idea:-1.frontend html
2.terminal undo redo:- best if api else pdsa promlem like code
3. test cases:- pytest mock
4. evaluation :- postgre or sqlite 3 db
''''
