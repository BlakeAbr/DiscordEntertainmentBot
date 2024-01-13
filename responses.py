from random import choice


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    #Lists all of the commands the user can use.
    if 'help' in lowered:
        return 'Thank you for using Entertainment bot. Try ?Tell me a joke, ?Rock,Paper,Scissors, ?Flip a coin, ?Would You Rather, ?Quote'
    
    #Flips a coin
    elif 'flip a coin' in lowered:
        return choice(['Heads!',
                       'Tails!',])
    
    #Tells a joke from a random list of jokes https://www.countryliving.com/life/entertainment/a36178514/hilariously-funny-jokes/
    elif 'tell me a joke' in lowered:
        return choice(['Why did the egg hide? It was a little chicken.',
                       "What is a ninja's favorite type of shoes? Sneakers.",
                       "What's the best smelling insect? A deodor-ant.",
                       'What do you call a bear without any teeth? A gummy bear.',
                       'Why couldnt the sunflower ride its bike? It lost its petals.',
                       'What kind of candy do astronauts like? Mars bars.',
                       'I was going to tell a time traveling joke, but you guys didnt like it.',
                       'What does a pig put on dry skin? Oinkment.',
                       'What do you call it when a snowman throws a tantrum? A meltdown.',
                       'My uncle named his dogs Timex and Rolex. They are his watch dogs.',
                       'How do you open a banana? With a mon-key.',
                       'What do you call a pig that does karate? A pork chop.',
                       'What do you call a pony with a sore throat? A little horse.',
                       'What did the mama tomato say to the baby tomato? Catch up!',
                       'How did the pig get to the hogspital? In a hambulance.',
                       'How do celebrities stay cool? They have many fans.',
                       'How much money does a pirate pay for corn? A buccaneer.',
                       'Where do young trees go to learn? Elementree school.',
                       'Why do bees have sticky hair? Because they use a honeycomb.',
                       'How did the student feel when he learned about electricity? Totally shocked.',
                       'I tried to catch fog yesterday. Mist.']) 
    
    #Implementing Rock, Paper, Scissors
    elif 'rock' in lowered:
        return choice(['Rock!',
                       'Scissors!',
                       'Paper!'])
    elif 'scissors' in lowered:
        return choice(['Rock!',
                       'Scissors!',
                       'Paper!'])
    elif 'paper' in lowered:
        return choice(['Rock!',
                       'Scissors!',
                       'Paper!'])
    
    #Generates a random would you rather statement https://www.teenvogue.com/story/how-you-answer-these-171-would-you-rather-questions-says-a-lot-about-you
    elif 'would you rather' in lowered:
        return choice(['Would you rather have smelly feet or bad breath?',
                       "Would you rather communicate telepathically or know every single language on the planet?",
                       "Would you rather run into an alien or Big Foot?",
                       'Would you rather uncontrollably break into song or unexpectedly lose your voice?',
                       'Would you rather bounce off of every surface you touch or never be able to jump again?',
                       'Would you rather have a one-minute conversation with your past self or your future self?',
                       'Would you rather be constantly sticky or constantly itchy?',
                       'Would you rather know what your pets think of you or never hear them speak?',
                       'Would you rather shout all of the time or only be able to whisper?',
                       'Would you rather be a member of the Kardashian family or a member of the Obama family?',
                       'Would you rather look like a fish or smell like a fish?',
                       'Would you rather be Youtube famous or TikTok famous?',
                       'Would you rather be hopelessly lost in an old town or lost in the forest?',
                       'Would you rather be chased through a forest by a zombie or by a lion?',
                       'Would you rather have only seven fingers or only seven toes?',
                       'Would you rather have everything you eat be too sweet or not sweet enough forever?',
                       'Would you rather switch your body with your ex or switch your body with your grandma?',
                       'Would you rather only watch one single movie for the rest of your life or only eat the same food for the rest of your life?',
                       'Would you rather have tons of mediocre friends or one really loyal dog?',
                       'Would you rather eat only burgers for a week or only ice cream for a week?',
                       'Would you rather be able to control fire or control water?']) 
    

    #Generates a random inspirational quote https://www.oberlo.com/blog/motivational-quotes
    elif 'quote' in lowered:
        return choice(['"All our dreams can come true, if we have the courage to pursue them.” —Walt Disney',
                       '“The secret of getting ahead is getting started.” —Mark Twain',
                       '“The best time to plant a tree was 20 years ago. The second best time is now.” ―Chinese Proverb',
                       '“It is hard to beat a person who never gives up.” —Babe Ruth',
                       '“The same boiling water that softens the potato hardens the egg. Its what youre made of. Not the circumstances.” —Unknown',
                       '“Dont be afraid to give up the good to go for the great.” —John D. Rockefeller',
                       '“Everything comes to him who hustles while he waits.” ―Thomas Edison',
                       '“We are what we repeatedly do. Excellence, then, is not an act, but a habit.” ―Aristotle',
                       '“Great things are done by a series of small things brought together.” ―Vincent Van Gogh',
                       '“The hard days are what make you stronger.” ―Aly Raisman',
                       '“Never give up on a dream just because of the time it will take to accomplish it. The time will pass anyway.” ―Earl Nightingale',
                       '“At any given moment you have the power to say: This is not how the story is going to end.” ―Unknown',
                       '“Dreams dont work unless you do.” ―John C. Maxwell',
                       '“I never lose. Either I win or learn.” ―Nelson Mandela',
                       '“Focus on being productive instead of busy.” ―Tim Ferriss',
                       '“Do what you can, with what you have, where you are.” ―Theodore Roosevelt',
                       '“You never know what you can do until you try.” ―William Cobbett',]) 
    
    # if message does not match any responses
    else:
        return "I am sorry, I do not understand your message. Try ?help."
    

