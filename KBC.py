import random
import pyttsx3
# import pygame
# pygame.mixer.music.load("/Users/anshulnigam/Downloads/sounds/kbc_bg_loop.wav")



# pygame.mixer.init()

# Background music
# def start_background_music():
#     pygame.mixer.music.load("kbc_bg_loop.wav")
#     pygame.mixer.music.set_volume(0.2)
#     pygame.mixer.music.play(-1)

# def stop_background_music():
#     pygame.mixer.music.stop()

# # Sound effects
# def play_sound_effect(filename):
#     sound = pygame.mixer.Sound(filename)
#     sound.set_volume(0.7)
#     sound.play()

engine = pyttsx3.init()

# Questions [question, A, B, C, D, correct_option_index]
questions = [
    ["What is the capital of India", "Mumbai", "New Delhi", "Kolkata", "Chennai", 2],
    ["Who is known as the 'Father of the Nation' in India", "Jawaharlal Nehru", "Bhagat Singh", "Mahatma Gandhi", "Subhas Chandra Bose", 3],
    ["How many players are there in a cricket team (on field)", "10", "11", "12", "9", 2],
    ["What is the chemical symbol for water", "H2O", "CO2", "O2", "H2SO4", 1],
    ["Which planet is known as the Red Planet", "Earth", "Venus", "Mars", "Jupiter", 3],
    ["Who was the first President of India", "Dr. Rajendra Prasad", "Dr. B.R. Ambedkar", "Sardar Patel", "Dr. APJ Abdul Kalam", 1],
    ["What is the currency of Japan", "Won", "Yuan", "Yen", "Baht", 3],
    ["Which organ purifies blood in the human body", "Heart", "Lungs", "Liver", "Kidney", 4],
    ["Who discovered gravity when he saw a falling apple", "Galileo Galilei", "Isaac Newton", "Albert Einstein", "Michael Faraday", 2],
    ["In which year did India gain independence", "1945", "1947", "1950", "1948", 2],
    ["What is the largest desert in the world", "Sahara", "Thar", "Gobi", "Kalahari", 1],
    ["Who wrote the national anthem of India", "Rabindranath Tagore", "Bankim Chandra Chatterjee", "Sarojini Naidu", "Lata Mangeshkar", 1],
    ["Which gas is most abundant in the Earth’s atmosphere", "Oxygen", "Carbon dioxide", "Hydrogen", "Nitrogen", 4],
    ["What is the name of India’s first satellite", "Chandrayaan-1", "Bhaskara", "Aryabhata", "INSAT", 3],
    ["Who was the first woman to win a Nobel Prize", "Marie Curie", "Mother Teresa", "Rosalind Franklin", "Florence Nightingale", 1]
]

question_number = [
    "Pehla", "Dusra", "Tisra", "Chautha", "Paanchva", "Chhatha", "Saatva", "Aathva", "Nauva", "Dasva",
    "Gyarahva", "Barahva", "Terahva", "Chaudahva", "Pandrahva"
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000,
          640000, 1250000, 2500000, 5000000, "1crore"]

lifelines = ["50-50", "doubledip"]
money = 0

def lifeline50_50(question, correct_answer):
    options = [1, 2, 3, 4]
    options.remove(correct_answer)
    wrong_options = random.sample(options, 2)
    display_options = []

    for i in range(1, 5):
        if i not in wrong_options:
            display_options.append(i)

    print("\n50-50 Lifeline Activated! Ye rhe aapke options:\n")
    for i in display_options:
        print(f"{chr(64+i)}. {question[i]}")
    return display_options

def doubledip(correct_answer):
    print("Double Dip Lifeline Activated! Aapko do chance milenge.")
    for attempt in range(2):
        try:
            answer = int(input(f"Attempt {attempt+1} - Enter your answer (1-4): "))
            if answer == correct_answer:
                print("Sahi jawab!")
                engine.say("Sahi jawab!")
                engine.runAndWait()
                return True
            else:
                print("Galat jawab!")
                if attempt == 0:
                    print("Ek aur moka hai aapke paas.")
        except:
            print("Invalid input.")
    return False

# Start game
# start_background_music()

for i in range(0, 15):
    print(f"\n{question_number[i]} sawaal {levels[i]} rupye ke liye:\n")
#     play_sound_effect("kbc_question.wav")
    engine.say(f"Ye raha {question_number[i]} sawaal {levels[i]} rupye ke liye")
    engine.runAndWait()

    question = questions[i]
    correct_answer = question[5]
    print(f"{question[0]}\n")
    print(f"A. {question[1]}\t\t\t B. {question[2]}")
    print(f"C. {question[3]}\t\t\t D. {question[4]}\n")

    used_lifeline = False

    if lifelines:
        need_lifeline = input("Kya aap lifeline lena chahenge? (ha/na): ").lower()
        if need_lifeline == "ha":
            print(f"Available lifelines: {lifelines}")
            choice = input("Kaunsi lifeline chahenge? ").lower()

            if choice == "50-50" and "50-50" in lifelines:
                lifeline50_50(question, correct_answer)
                lifelines.remove("50-50")
                used_lifeline = True

            elif choice == "doubledip" and "doubledip" in lifelines:
                if doubledip(correct_answer):
                    # play_sound_effect("kbc_correct.wav")
                    money = levels[i]
                    print(f"Aap jeet gaye {levels[i]} rupye!")
                    engine.say(f"Aap jeet gaye {levels[i]} rupye")
                    engine.runAndWait()
                    lifelines.remove("doubledip")
                    continue  # skip rest of loop to go to next question
                else:
                    # play_sound_effect("kbc_wrong.wav")
                    engine.say("Dono jawab galat the. Aapka safar yahi khatam.")
                    engine.runAndWait()
                    break
                lifelines.remove("doubledip")

    if not used_lifeline:
        try:
            answer = int(input("Enter your answer (1-4): "))
            if answer == correct_answer:
                print("Sahi jawab!")
               #  play_sound_effect("kbc_correct.wav")
                engine.say("Sahi jawab")
                print(f"Aap jeet gaye {levels[i]} rupye\n")
                engine.say(f"Aap jeet gaye {levels[i]} rupye")
                engine.runAndWait()
            else:
                print("Galat jawab!")
               #  play_sound_effect("kbc_wrong.wav")
                engine.say("Galat jawab")
                print("Aapka safar yahin samapth hota hai.")
                engine.runAndWait()
                break
        except:
            print("Invalid input detected. Exiting game.")
            break

    if levels[i] == 10000:
        money = 10000
    elif levels[i] == 320000:
        money = 320000
    elif i == 14:
        money = "1 crore"

    if i != 14:
        cont = input(f"Kya aap {levels[i+1]} rupye ke liye khelna chahenge? (ha/na): ").lower()
        if cont == "na":
            break

# End of game
# stop_background_music()
print(f"Aap ghar le ja rahe hain {money} rupye.")
engine.say(f"Aap ghar le ja rahe hain {money} rupye")
engine.say("Thanks for coming!")
engine.runAndWait()
