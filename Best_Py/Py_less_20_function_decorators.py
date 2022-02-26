import webbrowser

def validator(func):
    def wrapper(url):
        if "." in url:
            func(url)
        else:
            print("Invalid URL")
    return wrapper


@validator
def open_url(url):
    webbrowser.open(url)

open_url("https://question-it.com/questions/2116350/organizatsija-lokalnogo-koda-v-paketah-s-ispolzovaniem-modulej-go")

