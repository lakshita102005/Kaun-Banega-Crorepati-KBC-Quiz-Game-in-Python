import time
from colorama import Fore, Style, init  
from playsound import playsound
# ANSI colors
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"
BOLD="\033[1m"
BLUE="\033[34m"
MAGENTA="\033[35m"
CYAN="\033[36m"
questions = [
    # 1-5: Easy
    "What is the capital of India?",
    "Which planet is known as the Red Planet?",
    "Who is known as the Father of the Nation (India)?",
    "Which festival is known as the 'Festival of Lights'?",
    "What is the national currency of India?",

    # 6-10: Medium
    "Which organ in the human body purifies blood?",
    "Who wrote the Indian National Anthem?",
    "In which sport is the term 'LBW' used?",
    "Which is the largest continent in the world?",
    "What does 'HTTP' stand for in website addresses?",

    # 11-15: Hard
    "Who was the first woman Prime Minister of India?",
    "Which gas is most abundant in Earth's atmosphere?",
    "Where is the headquarters of the United Nations?",
    "Who invented the telephone?",
    "Which is the longest river in the world?"
]
options = [
    ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
    ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
    ["A. Mahatma Gandhi", "B. Subhash Chandra Bose", "C. Bhagat Singh", "D. Jawaharlal Nehru"],
    ["A. Diwali", "B. Holi", "C. Eid", "D. Christmas"],
    ["A. Dollar", "B. Rupee", "C. Pound", "D. Yen"],

    ["A. Heart", "B. Kidney", "C. Liver", "D. Lungs"],
    ["A. Bankim Chandra Chatterjee", "B. Rabindranath Tagore", "C. Mahatma Gandhi", "D. Subhash Chandra Bose"],
    ["A. Cricket", "B. Hockey", "C. Football", "D. Tennis"],
    ["A. Asia", "B. Africa", "C. Europe", "D. Australia"],
    ["A. Hyper Text Transfer Protocol", "B. High Transfer Text Protocol", "C. Hyper Text Translate Program", "D. High Tech Transfer Protocol"],

    ["A. Sarojini Naidu", "B. Pratibha Patil", "C. Indira Gandhi", "D. Sonia Gandhi"],
    ["A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"],
    ["A. Paris", "B. New York", "C. Geneva", "D. London"],
    ["A. Alexander Graham Bell", "B. Thomas Edison", "C. Nikola Tesla", "D. James Watt"],
    ["A. Nile", "B. Amazon", "C. Yangtze", "D. Mississippi"]
]
answers = [
    "B",  # New Delhi
    "B",  # Mars
    "A",  # Mahatma Gandhi
    "A",  # Diwali
    "B",  # Rupee

    "B",  # Kidney
    "B",  # Rabindranath Tagore
    "A",  # Cricket
    "A",  # Asia
    "A",  # Hyper Text Transfer Protocol

    "C",  # Indira Gandhi
    "B",  # Nitrogen
    "B",  # New York
    "A",  # Alexander Graham Bell
    "A"   # Nile
]
prize_money = [
    1000, 2000, 3000, 5000, 10000,
    20000, 40000, 80000, 160000, 320000,
    640000, 1250000, 2500000, 5000000, 10000000
]
total=0
playsound("backgound_tune.mp3")
print(BLUE, BOLD,"🤩🎯WELCOME TO KAUN BANEGA CROREPATI AKA KBC🤩🎯",RESET)
playsound("welcome.mp3")
playsound("begin.mp3")
for i in range(len(questions)):
    print("-" * 50)
    print(f"{MAGENTA} DEVIYO AUR SAJJANNO  {i+1} QUESTION AAPKI SCREEN PE YE RHA:{RESET} \n \n {questions[i]}")
    print("-" * 50)
    for opt in options[i]:
        print(opt)
    user_ans=input("\n enter your answer(A/B/C/D): ").strip().upper()
    print(YELLOW, "Computer ji option " ,user_ans," pe... lock kiya jaaye! " , RESET)
    playsound("lock.mp3")
    time.sleep(2)
    if user_ans==answers[i]:
        total+=prize_money[i]
        print(f"{GREEN} ✅🥳 Aapka jawaab bilkul sahi hai ! Bahut khoob! Aap jeet chuke hai Rs. {prize_money[i]}\n {RESET}")
    else:
        print(f"{RED} ❌😢Afsoos ye jawab galat hai ! Sahi jawab tha : {answers[i]}\n {RESET}")
        break
print(f"{CYAN}🏆🎉Aap aaj ghar leke jaa rhe hai Rs.{GREEN} {total}{RESET}")
playsound("khush.mp3")
        