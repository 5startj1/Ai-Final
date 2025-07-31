import  nltk
from nltk.chat.util import Chat, reflections

   # Define = set of pairs -  this is  the list of patterns 
pairs = [
            [
              r"my name is Tyler",
              ["hi it's nice to see you  how can i help you today?"]
            ],
            [
              r"my favorite food is sushi ",
              ["hey thats cool, mine is pizza "]
            ],
            [
              r"what are you going to do today",
              [" hey i think I'll go to the beach it is a nice day today"]
            ],
            [
              r"Come on let's 1v1 !",
              [" hey, Bet lets go to 7 i'm going to win! "]
            ],
            [
              r"Mom can I have another snack ",
              ["hi yea sure what would you like?"]
            ],
            [
              r"Richie get on the game!",
              [" hey I'm already on let me invite you real quick "]
            ],
            [
              r"my name is Tyler",
              ["heyy my names kyle nice to meet you !"]
            ],
            
            [
              r"quit",
              ["goodby havea nice day!"]
            ],
            [
              r"(.*)",
              
              [" I'm not sure how to respond to that"]
            ],
   ]
          
# Create a chatbot using the defined pairs and reflections
chatbot = Chat(pairs, reflections)
# Function to interact with the chatbot
def chat():
    print("Hello, I am your chatbot. How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Goodbye! Have a nice day!")
            break
        else:
            response = chatbot.respond(user_input)
            if response:
                print("Bot:", response)
            else:
                print("Bot: I'm not sure how to respond to that.")
chat()







        
                    
        

        