import random
import asyncio

class Games:
    """Collection of fun games and interactive commands"""
    
    @staticmethod
    def magic_8ball():
        """Get a random magic 8 ball response"""
        responses = [
            "It is certain 🎱",
            "It is decidedly so 🎱",
            "Without a doubt 🎱",
            "Yes definitely 🎱",
            "You may rely on it 🎱",
            "As I see it, yes 🎱",
            "Most likely 🎱",
            "Outlook good 🎱",
            "Signs point to yes 🎱",
            "Reply hazy, try again 🎱",
            "Ask again later 🎱",
            "Better not tell you now 🎱",
            "Cannot predict now 🎱",
            "Concentrate and ask again 🎱",
            "Don't count on it ❌",
            "My reply is no ❌",
            "My sources say no ❌",
            "Outlook not so good ❌",
            "Very doubtful ❌"
        ]
        return random.choice(responses)
    
    @staticmethod
    def rps():
        """Rock, Paper, Scissors"""
        choices = ["🪨 Rock", "📄 Paper", "✂️ Scissors"]
        return random.choice(choices)
    
    @staticmethod
    def spin_wheel():
        """Spin the wheel of fortune"""
        prizes = [
            "💰 1000 points!",
            "🎁 Mystery box!",
            "🚀 Rocket fuel!",
            "💎 Diamond!",
            "🌟 Golden star!",
            "🎪 Circus ticket!",
            "🍕 Free pizza!",
            "🎮 Gaming session!",
            "💪 Super power!",
            "🦸 Superhero mode!"
        ]
        return random.choice(prizes)
    
    @staticmethod
    def horse_race():
        """Simulate a horse race"""
        horses = ["🐴 Lightning", "🐎 Thunder", "🐴 Storm", "🐎 Wind", "🐴 Phoenix"]
        random.shuffle(horses)
        return horses[0]
    
    @staticmethod
    def slot_machine():
        """Play a slot machine"""
        symbols = ["🍎", "🍊", "🍋", "🍌", "🍉", "🍇", "🍓", "🎰"]
        reel1 = random.choice(symbols)
        reel2 = random.choice(symbols)
        reel3 = random.choice(symbols)
        
        result = f"{reel1} {reel2} {reel3}"
        if reel1 == reel2 == reel3:
            return f"{result} - JACKPOT! 💰💰💰"
        elif reel1 == reel2 or reel2 == reel3:
            return f"{result} - You won! 🎉"
        else:
            return f"{result} - Better luck next time!"
    
    @staticmethod
    def trivia_question():
        """Get a random trivia question"""
        questions = [
            {
                "q": "What is the largest planet in our solar system?",
                "a": "Jupiter"
            },
            {
                "q": "What year did the Titanic sink?",
                "a": "1912"
            },
            {
                "q": "Who painted the Mona Lisa?",
                "a": "Leonardo da Vinci"
            },
            {
                "q": "What is the smallest country in the world?",
                "a": "Vatican City"
            },
            {
                "q": "How many continents are there?",
                "a": "7"
            },
            {
                "q": "What is the capital of France?",
                "a": "Paris"
            },
            {
                "q": "What gas do plants absorb from the atmosphere?",
                "a": "Carbon Dioxide"
            },
            {
                "q": "Who wrote Romeo and Juliet?",
                "a": "William Shakespeare"
            },
            {
                "q": "What is the hottest planet in our solar system?",
                "a": "Venus"
            },
            {
                "q": "How many sides does a hexagon have?",
                "a": "6"
            }
        ]
        return random.choice(questions)
    
    @staticmethod
    def random_insult():
        """Generate a silly insult"""
        adjectives = ["silly", "goofy", "wacky", "zany", "quirky", "bonkers", "loopy", "nutty"]
        nouns = ["noodle", "potato", "spaghetti", "cabbage", "flamingo", "cheese", "pickle", "donut"]
        return f"You absolute {random.choice(adjectives)} {random.choice(nouns)}!"
    
    @staticmethod
    def pick_random(*options):
        """Pick a random option from a list"""
        if not options:
            return "No options provided!"
        return random.choice(options)
