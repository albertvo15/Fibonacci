import bottle
from bottle import route, run, request,template


@route('/')
def index():
    return '''
    <form action="/getfib" method="post">Enter a number to generate Fibonacci sequence: <input name="userInput" t /></form>

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
stack@ubuntu:~/python$ cp myfib.py genFib.py
stack@ubuntu:~/python$ python genFib.py
Bottle v0.12.8 server starting up (using WSGIRefServer())...
Listening on http://192.168.56.139:8080/
Hit Ctrl-C to quit.

userInput =  15
Fibonacci series for first  15 numbers
 [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
192.168.56.1 - - [10/Sep/2015 13:09:45] "POST /getfib HTTP/1.1" 200 64
stack@ubuntu:~/python$ cat genFib.py
import bottle
from bottle import route, run, request,template


@route('/')
def index():
    return '''
    <form action="/getfib" method="post">Enter a number to generate Fibonacci sequence: <input name="userInput" t /></form>

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
    run(host='localhost', port=8080)
