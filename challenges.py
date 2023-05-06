import random

challenges = [
    {
        'level': 1,
        'title': 'Walk for 10 minutes',
        'description': 'Go for a 10-minute walk outside or on a treadmill.',
        'xp': 10
    },
    {
        'level': 1,
        'title': 'Drink a glass of water',
        'description': 'Drink a full glass of water to stay hydrated.',
        'xp': 5
    },
    {
        'level': 1,
        'title': 'Stretch for 5 minutes',
        'description': 'Perform gentle stretches for 5 minutes.',
        'xp': 10
    },
    {
        'level': 1,
        'title': 'Write down 3 things you are grateful for',
        'description': 'Take a moment to think about and write down 3 things you are grateful for today.',
        'xp': 10
    },
    {
        'level': 1,
        'title': 'Declutter your workspace',
        'description': 'Clean and organize your workspace for improved focus and productivity.',
        'xp': 15
    },
    {
        'level': 2,
        'title': 'Meditate for 5 minutes',
        'description': 'Find a quiet space and meditate for 5 minutes.',
        'xp': 20
    },
    {
        'level': 2,
        'title': 'Do 10 push-ups',
        'description': 'Perform 10 push-ups to build upper body strength.',
        'xp': 20
    },
    {
        'level': 2,
        'title': 'Eat a healthy meal',
        'description': 'Choose a nutritious meal that includes fruits, vegetables, whole grains, and lean protein.',
        'xp': 20
    },
    {
        'level': 2,
        'title': 'Read for 20 minutes',
        'description': 'Read a book, article, or any other text for 20 minutes.',
        'xp': 20
    },
    {
        'level': 2,
        'title': 'Set a goal for the week',
        'description': 'Think about a personal or professional goal you want to achieve this week and write it down.',
        'xp': 25
    },
        {
        'level': 1,
        'title': 'Take the stairs',
        'description': 'Instead of using the elevator or escalator, take the stairs for some physical activity.',
        'xp': 10
    },
    {
        'level': 1,
        'title': 'Listen to a motivational podcast',
        'description': 'Find a motivational podcast and listen to an episode for inspiration.',
        'xp': 10
    },
    {
        'level': 1,
        'title': 'Smile at a stranger',
        'description': 'Brighten someones day by offering them a warm and genuine smile.',
        'xp': 5
    },
    {
        'level': 1,
        'title': 'Call a loved one',
        'description': 'Take some time to call a family member or friend to catch up and stay connected.',
        'xp': 10
    },
    {
        'level': 1,
        'title': 'Try a new fruit or vegetable',
        'description': 'Choose a fruit or vegetable you have never tried before and give it a taste.',
        'xp': 10
    },
    {
        'level': 2,
        'title': 'Create a budget',
        'description': 'Create a budget to help manage your finances and track your spending.',
        'xp': 20
    },
    {
        'level': 2,
        'title': 'Perform a random act of kindness',
        'description': 'Do something nice for someone without expecting anything in return.',
        'xp': 20
    },
    {
        'level': 2,
        'title': 'Write a thank you note',
        'description': 'Express your gratitude by writing a thank you note to someone who has made a positive impact on your life.',
        'xp': 20
    },
    {
        'level': 2,
        'title': 'Try a new workout',
        'description': 'Experiment with a new workout routine or fitness class to challenge your body.',
        'xp': 20
    },
    {
        'level': 2,
        'title': 'Cook a healthy meal at home',
        'description': 'Prepare a nutritious meal at home, using fresh ingredients and whole foods.',
        'xp': 25
    },
    {
        'level': 3,
        'title': 'Volunteer for a local cause',
        'description': 'Donate your time and energy to a local cause or charity that youre passionate about.',
        'xp': 30
    },
    {
        'level': 3,
        'title': 'Learn a new skill',
        'description': 'Challenge yourself by learning a new skill or hobby, such as playing an instrument, cooking, or programming.',
        'xp': 30
    },
    {
        'level': 3,
        'title': 'Practice deep breathing exercises',
        'description': 'Spend 5 minutes focusing on your breath and practicing deep breathing techniques.',
        'xp': 30
    },
    {
        'level': 3,
        'title': 'Set a monthly goal',
        'description': 'Establish a personal or professional goal that you would like to accomplish in the next month.',
        'xp': 30
    },
    {
        'level': 3,
        'title': 'Start a journal',
        'description': 'Begin keeping a journal to document your thoughts, feelings, and experiences.',
        'xp': 35
    },
        {
        'level': 4,
        'title': 'Learn a new language',
        'description': 'Begin learning a new language using books, apps, or online courses.',
        'xp': 40
    },
    {
        'level': 4,
        'title': 'Take a social media break',
        'description': 'Avoid using social media for 24 hours to give yourself a mental break.',
        'xp': 40
    },
    {
        'level': 4,
        'title': 'Declutter a room',
        'description': 'Choose a room in your home and declutter it, removing any unnecessary items.',
        'xp': 40
    },
    {
        'level': 4,
        'title': 'Visit a local landmark',
        'description': 'Take a trip to a local landmark or tourist attraction to explore your area.',
        'xp': 40
    },
    {
        'level': 4,
        'title': 'Write a short story',
        'description': 'Exercise your creativity by writing a short story on any topic you choose.',
        'xp': 45
    },
    {
        'level': 5,
        'title': 'Travel to a new city',
        'description': 'Visit a city you have never been to before and explore the local culture.',
        'xp': 50
    },
    {
        'level': 5,
        'title': 'Build a personal website',
        'description': 'Create a personal website to showcase your skills, experience, and portfolio.',
        'xp': 50
    },
    {
        'level': 5,
        'title': 'Complete a home improvement project',
        'description': 'Tackle a home improvement project to enhance your living space.',
        'xp': 50
    },
    {
        'level': 5,
        'title': 'Run a 5k race',
        'description': 'Train for and participate in a 5k race to challenge your physical fitness.',
        'xp': 50
    },
    {
        'level': 5,
        'title': 'Create a vision board',
        'description': 'Make a visual representation of your goals and dreams to stay motivated.',
        'xp': 55
    },
    {
        'level': 6,
        'title': 'Learn a musical instrument',
        'description': 'Pick up a musical instrument and start learning how to play.',
        'xp': 60
    },
    {
        'level': 6,
        'title': 'Grow your own vegetables',
        'description': 'Start a small vegetable garden at home to grow your own produce.',
        'xp': 60
    },
    {
        'level': 6,
        'title': 'Attend a networking event',
        'description': 'Expand your professional network by attending a local networking event.',
        'xp': 60
    },
    {
        'level': 6,
        'title': 'Plan a surprise for someone',
        'description': 'Organize a surprise for a friend or family member to show your appreciation.',
        'xp': 60
    },
    {
        'level': 6,
        'title': 'Practice public speaking',
        'description': 'Improve your public speaking skills by practicing a speech or presentation.',
        'xp': 65
    },
     {
        'level': 6,
        'title': 'Practice public speaking',
        'description': 'Improve your public speaking skills by practicing a speech or presentation.',
        'xp': 65
    },
    {
        'level': 7,
        'title': 'Join a local club or organization',
        'description': 'Become a member of a local club or organization to meet new people and pursue your interests.',
        'xp': 70
    },
    {
        'level': 7,
        'title': 'Start a side hustle',
        'description': 'Launch a side business or project to generate additional income and develop new skills.',
        'xp': 70
    },
    {
        'level': 7,
        'title': 'Participate in a charity event',
        'description': 'Join a charity event or fundraiser to give back to your community and support a good cause.',
        'xp': 70
    },
    {
        'level': 7,
        'title': 'Take a class or workshop',
        'description': 'Enroll in a class or workshop to learn something new and expand your skillset.',
        'xp': 70
    },
    {
        'level': 7,
        'title': 'Write a letter to your future self',
        'description': 'Compose a letter to your future self, reflecting on your current thoughts, goals, and aspirations.',
        'xp': 75
    },
    {
        'level': 8,
        'title': 'Create a piece of art',
        'description': 'Express yourself creatively by producing a piece of art in any medium you choose.',
        'xp': 80
    },
    {
        'level': 8,
        'title': 'Attend a cultural event',
        'description': 'Experience a cultural event, such as a concert, play, or festival, to broaden your horizons.',
        'xp': 80
    },
    {
        'level': 8,
        'title': 'Develop a morning routine',
        'description': 'Establish a consistent morning routine to start your day off right.',
        'xp': 80
    },
    {
        'level': 8,
        'title': 'Host a dinner party',
        'description': 'Invite friends or family over and host a dinner party to enjoy good food and company.',
        'xp': 80
    },
    {
        'level': 8,
        'title': 'Complete a puzzle',
        'description': 'Challenge your mind by completing a jigsaw puzzle, crossword, or sudoku.',
        'xp': 85
    },
    {
        'level': 9,
        'title': 'Mentor someone',
        'description': 'Share your knowledge and experience by mentoring someone in your field or community.',
        'xp': 90
    },
    {
        'level': 9,
        'title': 'Start a blog',
        'description': 'Launch a blog to share your thoughts, experiences, or expertise with others.',
        'xp': 90
    },
    {
        'level': 9,
        'title': 'Plan and execute a personal project',
        'description': 'Create a plan for a personal project and see it through to completion.',
        'xp': 90
    },
    {
        'level': 9,
        'title': 'Connect with an old friend',
        'description': 'Reach out to an old friend you have not spoken to in a while to reconnect and catch up.',
        'xp': 90
    },
]

def generate_challenge(character_level, challenges):
    relevant_challenges = [c for c in challenges if c['level'] <= character_level]
    return random.choice(relevant_challenges)
