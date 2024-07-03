import json
from difflib import get_close_matches
from typing import List
from calculate import calc
from open_apps import start
from ai_speak import speak
from date_time import current_date, current_time
from weather import get_weather
from internet_speed import perform_speedtest
from image_capture import camera, screenshot


# Loading the dictionary in program.
def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
        return data


# Saving unknown responses into the json file
def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)


# Finding the best matches for responses we can get from knowledge dictionary.
def find_best_match(user_question: str, questions: List[str]) -> str or None:
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.8)
    return matches[0] if matches else None


# It searches question keywords in knowledge_base if question keywords match 60% it returns the answer.
def get_answer_for_questions(question: str, knowledge_base: dict) -> str or None:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]


def ALICE(query):
    # Loading the knowledge base and its path in Eliza.
    knowledge_base: dict = load_knowledge_base('knowledge_base.json')

    # User to input the question.
    while True:
        user_input: str = query
        user_input = user_input.lower()

        # user input stored in string is used in find_best_match in questions dictionary.
        best_match: str or None = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])

        # If match succeeds than it will print the answer.
        if best_match:
            answer: str = get_answer_for_questions(best_match, knowledge_base)
            # print(f"ALICE: {answer}")
            # speak(f"{answer}")
            return answer
        else:
            if "quit" in user_input or "bye" in user_input or "exit" in user_input:
                # print("ALICE: bye hope to see you again...")
                bye = "bye hope to see you again..."
                return bye

            elif "date" in user_input:
                date = current_date()
                return date

            elif "time" in user_input:
                time = current_time()
                return time

            elif "open" in user_input:
                start(user_input)
                return "Opened Application"

            elif "calculate" in user_input or "multiply" in user_input or "divide" in user_input or "plus" in user_input or "minus" in user_input:
                calculate = calc(user_input)
                return calculate

            elif "weather" in user_input or "temperature" in user_input or "climate" in user_input:
                weather = get_weather("52e874f99f88a68005c1078f7250ae2d", "Mumbai")
                return weather

            elif "internet speed" in user_input:
                internet_speed = perform_speedtest()
                return internet_speed

            elif "screenshot" in user_input or "screen" in user_input:
                screen = screenshot()
                return screen
            elif "camera" in user_input or "photo" in user_input or "image" in user_input:
                photo = camera()
                return photo

            else:
                error = "404 \nAnswer not found in database"
                return error


if __name__ == '__main__':
    ALICE(query="exit")


# def load():
def append(param):
    return None


def save():
    return None


def load():
    return None
