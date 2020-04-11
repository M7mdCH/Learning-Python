print('AUTHOR = M7mdCH')
import webbrowser, time
time.sleep(1)
print('What website would like to go to ?')
input()
print('These are the supported websites CASE SENSITIVE')
print('Apple - Facebook - GitHub - Google - Instagram  - Microsoft - Office - Xbox - YouTube')
website=input('')
if (website) == 'YouTube':
    print('What would you like to search for in Youtube ?')
    query=input()
    webbrowser.open('https://www.youtube.com/results?search_query='+ (query), new=2)
if (website) == 'Google':
    print('What would you like to search for in Google ?')
    query=input()
    webbrowser.open('https://www.google.com/search?q=' + (query), new=2)
if (website) == 'GitHub':
    print('Would you like to go to my repository on GitHub ? y/n')
    gitrepo=input()
    if (gitrepo) == 'y':
        webbrowser.open('https://github.com/M7mdCH/Learning-Python', new=2)
    if (gitrepo) == 'n':
        webbrowser.open('https://github.com/', new=2)
if (website) == 'Apple':
    webbrowser.open('apple.com', new=2)
if (website) == 'Facebook':
    webbrowser.open('fb.com', new=2)
if (website) == 'Instagram':
    webbrowser.open('instagram.com', new=2)
if (website) == 'Microsoft':
    webbrowser.open('microsoft.com', new=2)
if (website) == 'Office':
    webbrowser.open('office.com', new=2)
if (website) == 'Xbox':
    webbrowser.open('xbox.com', new=2)