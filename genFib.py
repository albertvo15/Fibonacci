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
#    print userInput
    current,previous = 0, 1
    mycounter = userInput
    mycounter = mycounter
    mcount = 1
    myresult = []
    myresult.append(0)
    if userInput < 0:
        return 'Input Error:  Negative Number'

    else:
        while mcount < mycounter:
                current = previous
                myresult.append(previous)
                previous = current + previous
#                print template("<p>Fibonacci {{name}}</p>", name=myresult)
                mcount = mcount + 1
        return template("<p> {{name}}</p>", name=myresult)



if __name__ == '__main__':
    bottle.debug(True) # display traceback
    run(host='192.168.56.139', port=8080)
