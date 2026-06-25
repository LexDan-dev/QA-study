import random
import time

# ---- Константы ----
# -- для numbers_with_break --
RANGE_START = 1
RANGE_END = 8
STOP_NUMBER = 5

# -- для print_words --
WORDS_COUNT = 10

# -- для monitor_rostics_load --
MAX_ITERATIONS = 10
LOAD_THRESHOLD = 85
MIN_LOAD = 0
MAX_LOAD = 100
PAUSE_SECONDS = 0.5


# ---- Класс и функции ----
class LoopsPractice:
    def numbers_with_break(self):
        numbers = list(range(RANGE_START, RANGE_END))
        for number in numbers:
            print(number, end=" ")
            if number == STOP_NUMBER:
                break
        print()

    def print_words(self):
        words = [f"str{i}" for i in range(WORDS_COUNT)]
        for word in words:
            print(word, end=" ")
        print()

    def monitor_rostics_load(self):
        iteration = 0
        while iteration < MAX_ITERATIONS:
            load = random.randint(MIN_LOAD, MAX_LOAD)
            if load > LOAD_THRESHOLD:
                print(f"Итерация {iteration + 1}: ВНИМАНИЕ, высокая нагрузка {load}%!")
            else:
                print(f"Итерация {iteration + 1}: нагрузка {load}%")
            time.sleep(PAUSE_SECONDS)
            iteration += 1


if __name__ == "__main__":
    practice = LoopsPractice()
    practice.numbers_with_break()
    practice.print_words()
    practice.monitor_rostics_load()
