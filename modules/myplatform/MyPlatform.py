import platform

class MyPlatform:
    def __init__(self):
        system = platform.system().lower()
        dist = platform.dist()
        if system == 'windows': # Windows
            self.path = 'D:/Projects'
        elif system == 'darwin': # Mac OSX
            self.path = '/Users/Nelson/Projects'
        elif system == 'linux':
            if dist[1] == '14.04': # PythonAnywhere Linux
                self.path = '/home/nelson137/Projects'
            elif dist[1] == '16.04': # Ubuntu-Desktop Linux
                self.path = '/home/limbo/Projects'
            else:
                sel.path = 'Unknown System'
        else:
            self.path = 'Unknown System'
