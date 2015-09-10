import bottle
from bottle import route, run, request,template


@route('/')
def index():
    return '''
    <form action="/getfib" method="post">Enter a number to generate Fibonacci sequence: <input name="userInput" type="number" /><input type="submit" /></form>

    '''

@route('/getfib',method='POST')
def getfib():
    userInput = int(request.forms.get('userInput'))
    print "userInput = ",userInput
    current,previous = 0, 1
    mycounter = userInput
    mycounter = mycounter - 1
    mcount = 1
    myresult = []
    myresult.append(current)
    myresult.append(previous)
    if userInput < 0:
        return 'Input Error:  Negative Number '

    elif userInput <= 2:
        return 'Input Error:  Number needs to be greater than 2'
    else:
        while mcount < mycounter:
                current, previous = previous,current + previous
                myresult.append(previous)
#                print template("<p> {{name}}</p>", name=myresult)
                mcount = mcount + 1
#        print template("<p> {{name}}</p>", name=myresult)
        return template("<p> {{name}}</p>", name=myresult)



if __name__ == '__main__':
    bottle.debug(True) # display traceback
    run(host='192.168.56.139', port=8080)

