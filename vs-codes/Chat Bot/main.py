import re  #For regex
import long_responses as long

#A function that calculates the proability that the message is the corresponding message.
def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    #Recognizing text.
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    #Calculate the accuracy percentage
    percentage = float(message_certainty) / float(len(recognised_words))

    #Check required words are included as well.
    for word in required_words:
        if word not in user_message:
            has_required_words = False #prevents us from wrongly matching a different sentense.
            break

    #Create the return statement of the function which returns the accuracy of each sentense, 
    #so they can later be compared & return the best response possible.
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0 #Means nothing really matched, so it's going to be the lowest value possible.

def check_all_messages(message):
    #create a dictionary
    highest_prob_list = {}

    #create a function which is going to simplify the response creation & adding items to the dictionary.
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list  #Set probability list to a non-local variable so we can use them inside here.
        #Refer to the highest prob list & create a key at the index of bot_response, for inserting values.
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

#Responses.........................................................
#The key will be the response that you want the bot to answer to your recognized words.
    response('Hello!', ['hello', 'hi', 'sup', 'hey', 'heyo'], single_response=True) 
    response('Bye!', ['bye', 'bye bye', 'see', 'yah', 'see', 'you', 'goodbye'], single_response=True) 
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('Thank you!', ['i', 'love', 'code'], required_words=['love', 'code'])

    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])
    response(long.R_HOBBIES, ['what', 'like', 'doing'], required_words=['like', 'doing'])
    response(long.R_FEELINGS, ['do', 'you', 'feelings'], required_words=['you', 'feelings'])
    response(long.R_OUTFIT, ['what', 'you', 'wearing'], required_words=['you', 'wearing'])
    response(long.R_TRAVEL, ['do', 'you', 'like', 'travelling'], required_words=['you', 'travel'])
    response(long.R_WEATHER, ['what', 'weather'], required_words=['what', 'weather'])
    response(long.R_BOOKS, ['do', 'you', 'read', 'books'], required_words=['you', 'read'])
    response(long.R_MUSIC, ['what', 'music', 'you', 'listen'], required_words=['you', 'listen'])
    response(long.R_EXERCISE, ['do', 'you', 'exercise'], required_words=['you', 'exercise'])
    response(long.R_RELATIONSHIPS, ['do', 'you', 'relationships'], required_words=['you', 'relationships'])
    response(long.R_HISTORY, ['history'], required_words=['history'])
    response(long.R_FUTURE, ['future'], required_words=['future',])
    response(long.R_LANGUAGES, ['languages',], required_words=['languages',])
    response(long.R_UNIVERSE, ['universe'], required_words=['universe'])


    best_match = max(highest_prob_list, key=highest_prob_list.get)
    #print(highest_prob_list)

#We want to return the unknown response if the highest probability at the index of the best match is less than 1.
    #It means it has a very low score, which is probably 0, thus not a match for anything.
    #If all the matches are less than 1, we'll return the unknown response.
    #Else, we'll return whatever the best match is.
    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


def get_response(user_input):
    #Split the message into an array, so each word can be analyzed separately from the user message.
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower()) 
    #r''-removes all the symbols from the messages, & allows us just to have the clean words separately.
    #\s+ checks for spaces.
    response = check_all_messages(split_message)
    return response


#Testing the response system.
while True:     #Create an infinite while True loop so that we can always get new responses.
    print ('Bot: ' + get_response(input('You: ')))