import webbrowser
import utils
import datetime
from datetime import datetime
import wikipedia
from youtube_search import YoutubeSearch
import smtplib


def current_time():
    time = datetime.now()

    hour = int(time.strftime("%I"))
    minutes = int(time.strftime("%M"))
    am_pm = time.strftime("%p")

    utils.speak(f"The current time is {hour} : {minutes} : {am_pm}")


def greet():
    # Get the current time
    time_now = datetime.now()

    # Get the current hour
    hour_now = time_now.hour

    greeting = ""
    if hour_now < 12:
        greeting = "Morning"
    else:
        greeting = "Evening"

    utils.speak(f"Good {greeting} master! How may I assist you today?")


# search wikipedia
def wiki(query):
    # remove 'wiki' from commands
    search_term = query.replace('wiki', '').strip()
    try:
        # get a summary of search results and speak
        result = wikipedia.summary(search_term, sentences=2)
        utils.speak("According to Wikipedia, " + result)
    except wikipedia.exceptions.PageError:
        utils.speak("Sorry, I couldn't find any information on " + search_term)
    except wikipedia.exceptions.DisambiguationError:
        utils.speak("There are multiple matches for " + search_term + ". Please provide more specific information.")


# search google
def google(query):
    if 'open' in query:
        utils.speak('Opening Google')
        webbrowser.open_new_tab('https://www.google.com')
        return

    search_term = query.replace('google', '').strip()
    webbrowser.open_new_tab("https://www.google.com/search?q=" + search_term)
    utils.speak("Here are the search results for " + search_term)


def youtube(query):
    if 'open' in query:
        utils.speak("Opening Youtube")
        webbrowser.open_new_tab('https://www.youtube.com')
        return

    search_term = query.replace('play', '').strip()
    search_term = search_term.replace('in youtube', '').strip()
    print(search_term)
    videos = YoutubeSearch(search_term, max_results=1).to_dict()
    webbrowser.open_new_tab('https://www.youtube.com' + videos[0]['url_suffix'])


def mail():
    try:
        server = smtplib.SMTP("smtp-mail.outlook.com", port=587)
        server.ehlo()
        server.starttls()

        utils.speak('Please enter your email and password')
        print("****MANUALLY ENTER YOUR EMAIL AND PASSWORD****")
        sender = input("Email(Only supports outlook because stupid gmail disabled this service): ")
        utils.speak("The password isn't masked. So, be careful that it is not exposed to other individuals around you")
        password = input("Password: ")
        server.login(sender, password)

        utils.speak("Specify the receiver")
        receiver = input("Receiver: ")

        utils.speak("What would you like to send?")
        # content = utils.listen()
        content = input("Text: ")

        server.sendmail(sender, receiver, content)
        print("Successfully sent")
        server.close()

    except Exception as e:
        print("Some Error Occurred")
