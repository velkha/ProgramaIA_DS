from main.utils.ui_worker import UIWorker

def test_print_colors():
    colors = ['red', 'green', 'blue', 'yellow', 'cyan', 'magenta']
    messages = ['Hello World!'] * len(colors)
    
    for color, message in zip(colors, messages):
        UIWorker.print([message], color)

def test_print_colors():
    colors = ['red', 'green', 'blue', 'yellow', 'cyan', 'magenta']
    messages = ['Hello World!'] * len(colors)
    
    for color, message in zip(colors, messages):
        UIWorker.print([message], color)

def test_print_all_colors():
    colors = ['red', 'green', 'blue', 'yellow', 'cyan', 'magenta']
    message = 'Hello World!'
    
    for color in colors:
        UIWorker.print([message], color)

test_print_colors()
test_print_all_colors()