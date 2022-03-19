import eel 
from eel import init, start

if __name__ == '__main__':

    
    init('web')
    @eel.expose                         # Expose this function to Javascript
    def say_hello_py(x):
        print('Hello from %s' % x)

    say_hello_py('Python World!')
    eel.say_hello_js('Python World!')   # Call a Javascript function

    # options = {
    #     'mode': 'custom',
    #     'args': ['node_modules/electron/dist/electron', '.']
    # }



    # start('splash.html', options=options)
    start('splash.html', mode='custom', cmdline_args=['node_modules/electron/dist/electron', '.'], port=8002)

    # start ('splash.html',geometry={'size': (1200,600) , 'position': (50, 50)}, port=8012)
