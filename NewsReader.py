import requests as rq, json
def speak(string_to_speak):
    from win32com.client import Dispatch
    speak= Dispatch("SAPI.spvoice")
    speak.Speak(string_to_speak)

def get_category():
    print("Pease select category of news\n1- Business\n2- Entertainment\n3- Health\n4- Science\n5- Sport\n6- Technology")
    category=int(input("Your Input"))
    if category < 1 or category > 6:
        speak("Please select a valid Category from List")
        get_category()
    return category

def get_news(category):
    if category == 1:
        category = "business"
    elif category == 2:
        category = "entertainment"
    elif category == 3:
        category = "health"
    elif category == 4:
        category = "science"
    elif category == 5:
        category = "sport"
    else:
        category = "Technology"
    API_KEY="2141b2ccd45543bb891ea29b95d40ca1"
    api_url= f"https://newsapi.org/v2/top-headlines?country=in&category={category}&apiKey={API_KEY}"
    speak(f"Please wait while I load the {category} headlines for you")
    top_news= rq.get(api_url).text
    news_json= json.loads(top_news)
    for x in news_json["articles"]:
        speak(f"{x['title']}")
        userinp= input("Press Y/N")
        if userinp == "y" or userinp == "Y":
            speak(x["description"])
        else:
            speak("Thank you for listening")
            break


print("Hello! Welcome to the news speaker")
speak("Hello! Welcome to news speaker. Please Select a category from the list")
category=get_category()
get_news(category)
