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
]

def generate_challenge(character_level, challenges):
    relevant_challenges = [c for c in challenges if c['level'] <= character_level]
    return random.choice(relevant_challenges)
