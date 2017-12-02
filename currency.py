from urllib.request import urlopen

def changeA(jstr):
    numA=""
    for i in range (len(jstr)):
        letter=jstr[i]
        if letter in "1234567890.":
            letter=letter
        else:
            letter=" "
        numA=numA+letter            #to get the number we need
    num=numA.split()
    numB = num[1]                   #to get the result
    numB = float(numB)              #to change the type
    return numB
def exchange(b, c, d):             
    """
    Returns: amount of currency received in the given exchange.

    In this exchange, the user is changing amount_from money in 
    currency currency_from to the currency currency_to. The value 
    returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string for a valid currency code

    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string for a valid currency code

    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float
    """
    a='http://cs1110.cs.cornell.edu/2016fa/a1server.php?'
    url = a+"from="+b+"&to="+c+"&amt="+d
    doc = urlopen(url)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    numC=changeA(jstr)
    return numC
def test_exchange():
    assert(2.0952375 == exchange("USD", "EUR", "2.5"))
def test_changeA():
    assert(2.24075 == changeA('{ "from" : "2.5 United States Dollars", "to" : "2.24075 Euros", "success" : true, "error" : "" }'))                            
def test_All():
    """test all cases"""
    test_changeA()
    test_exchange()
    print("All tests passed")
test_All()    
