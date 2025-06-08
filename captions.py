import random

def generate_captions(topic, count):
    quotes = {
        "love": [
            "Love is not what you say, love is what you do.",
            "Where there is love, there is life.",
            "Love is the heartbeat of the soul.",
            "To love and be loved is to feel the sun from both sides.",
            "True love begins when nothing is looked for in return.",
            "Love isn't something you find, it's something that finds you.",
            "Love cures people—both the ones who give it and the ones who receive it.",
            "In your smile, I see something more beautiful than stars.",
            "Love is composed of a single soul inhabiting two bodies.",
            "Let us always meet each other with a smile—for the smile is the beginning of love."
        ],
        "friendship": [
            "True friends are never apart, maybe in distance but never in heart.",
            "Friendship doubles your joy and divides your sorrow.",
            "A real friend is one who walks in when the rest of the world walks out.",
            "Friends are the family you choose.",
            "The greatest gift of life is friendship.",
            "Friendship is a sheltering tree.",
            "A friend is someone who knows all about you and still loves you.",
            "Life is better with true friends.",
            "Hard times reveal true friends.",
            "Friendship is born at that moment when one says to another: 'What! You too?'"
        ],
        "life": [
            "Life is what happens when you're busy making other plans.",
            "Life is really simple, but we insist on making it complicated.",
            "The purpose of life is a life of purpose.",
            "Live life to the fullest, and focus on the positive.",
            "Difficult roads often lead to beautiful destinations.",
            "Life is short, and it’s up to you to make it sweet.",
            "Life is not about waiting for the storm to pass but learning to dance in the rain.",
            "Life doesn’t require that we be the best, only that we try our best.",
            "You get in life what you have the courage to ask for.",
            "Your life does not get better by chance, it gets better by change."
        ],
        "attitude": [
            "Your attitude determines your direction.",
            "A bad attitude is like a flat tire, you can't go anywhere until you change it.",
            "Attitude is a little thing that makes a big difference.",
            "A positive attitude can really make dreams come true.",
            "Stay strong, make them wonder how you're still smiling.",
            "Don’t stop until you’re proud.",
            "Success is 99% attitude and 1% talent.",
            "Be yourself; everyone else is already taken.",
            "You become what you believe.",
            "Turn your wounds into wisdom."
        ],
        "success": [
            "Success is not the key to happiness. Happiness is the key to success.",
            "Success doesn’t come to you, you go to it.",
            "Success is walking from failure to failure with no loss of enthusiasm.",
            "Work hard in silence, let success make the noise.",
            "Don’t watch the clock; do what it does. Keep going.",
            "Success usually comes to those who are too busy to be looking for it.",
            "Opportunities don’t happen, you create them.",
            "Success is not final; failure is not fatal: It is the courage to continue that counts.",
            "Don’t be afraid to give up the good to go for the great.",
            "Success is the sum of small efforts repeated day in and day out."
        ],
        "love failure": [
            "Sometimes goodbye is a second chance.",
            "The heart was made to be broken.",
            "Love hurts, but it also teaches you strength.",
            "Moving on doesn’t mean you forget, it means you choose happiness.",
            "Tears are words the heart can’t say.",
            "Love failure doesn’t mean life failure.",
            "Sometimes the one who loves you is not the one meant for you.",
            "The pain of love failure is the start of self-love.",
            "Love taught me to care, but failure taught me to grow.",
            "Behind every broken heart is a stronger version of yourself."
        ],
        "life failure": [
            "Failure is not the opposite of success, it’s part of success.",
            "Every failure is a step closer to success.",
            "In the middle of difficulty lies opportunity.",
            "You only fail when you stop trying.",
            "Success is stumbling from failure to failure with no loss of enthusiasm.",
            "Don’t fear failure. Fear being in the same place next year.",
            "Failure is the opportunity to begin again, more intelligently.",
            "Failures are the stairs to success.",
            "Failure is proof that you tried.",
            "Behind every successful person is a list of failures."
        ],
        "motivation": [
            "Push yourself, because no one else is going to do it for you.",
            "Great things never come from comfort zones.",
            "Don’t limit your challenges; challenge your limits.",
            "Wake up with determination. Go to bed with satisfaction.",
            "The harder you work for something, the greater you'll feel when you achieve it.",
            "Believe in yourself and all that you are.",
            "Dream it. Wish it. Do it.",
            "Do something today that your future self will thank you for.",
            "Success starts with self-discipline.",
            "Your only limit is your mind."
        ],
        "car love": [
            "Fuel your passion, not just your car.",
            "A car is not just a vehicle, it's a love story.",
            "Shift gears, chase dreams.",
            "Four wheels move the body, but a car you love moves the soul.",
            "Drive it like you stole it.",
            "Life is too short to drive boring cars.",
            "Car lovers see beauty in speed.",
            "Every car has a story. What's yours?",
            "More than metal, it's emotion.",
            "A good car takes you places; a great car becomes your place."
        ],
        "bike love": [
            "Ride fast, live free.",
            "Two wheels, endless love.",
            "Life is better on two wheels.",
            "My bike, my rules, my freedom.",
            "Feel the wind, live the ride.",
            "It’s not just a bike, it’s a lifestyle.",
            "The road is calling, and I must ride.",
            "Throttle therapy is real.",
            "Your vibe attracts your tribe — bikers know this.",
            "Born to ride, forced to work."
        ],
        "travel": [
            "Travel is the only thing you buy that makes you richer.",
            "Collect memories, not things.",
            "Life is short and the world is wide.",
            "Let’s wander where the Wi-Fi is weak.",
            "To travel is to live.",
            "Jobs fill your pocket, adventures fill your soul.",
            "Escape and breathe the air of new places.",
            "Travel far enough to meet yourself.",
            "The world is waiting. Are you ready?",
            "Travel is a journey to the soul."
        ],
        "happy": [
            "Happiness is not by chance, but by choice.",
            "Do more of what makes you happy.",
            "Smile, it confuses people.",
            "Happiness is homemade.",
            "Be happy not because everything is good, but because you see the good in everything.",
            "Happiness blooms from within.",
            "Your happiness depends on your attitude.",
            "Enjoy the little things.",
            "Happiness is a warm hug.",
            "Choose joy every day."
        ],
        "sad": [
            "Tears are words the heart can’t say.",
            "It’s okay to feel sad sometimes.",
            "Behind every smile is a little pain.",
            "Sadness flies away on the wings of time.",
            "You cannot protect yourself from sadness without protecting yourself from happiness.",
            "Even the darkest night will end and the sun will rise.",
            "Crying is how the heart speaks when your lips can’t explain the pain.",
            "Sometimes we need sadness to know happiness.",
            "It’s okay not to be okay.",
            "Pain is real, but so is hope."
        ]
    }

    return random.sample(quotes.get(topic.lower(), ["No quotes found for this topic."]), min(count, 10))
