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
    a,b = 0, 1
    mycounter = userInput
    mycounter = mycounter - 1
    mcount = 1
    myresult = []
    myresult.append(a)
    myresult.append(b)
    if userInput < 0:
        print 'Input Error:  Negative Number ',userInput
        return 'Input Error:  Negative Number '

    elif userInput <= 2:
        print 'Input Error:  Number needs to be greater than 2', userInput
        return 'Input Error:  Number needs to be greater than 2'
    else:
        for i in range(1,mycounter):
                temp = a
                a = b
                b = temp + b
                myresult.append(b)
        print "Fibonacci series for first ",userInput, "numbers"
        print template(" {{name}}", name=myresult)
        return template("<p> {{name}}</p>", name=myresult)



if __name__ == '__main__':
    bottle.debug(True) # display traceback
    run(host='192.168.56.139', port=8080)


