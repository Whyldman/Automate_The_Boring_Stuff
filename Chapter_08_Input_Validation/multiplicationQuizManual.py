import random, time


def multiplicationQuiz(questions=10, min=1, max=10):
    numberOfQuestions = questions
    correctAnswers = 0

    for questionNumber in range(numberOfQuestions):
        x = random.randint(min, max)
        y = random.randint(min, max)
        answer = x * y

        attempts = 1

        while True:
            start_time = time.time()
            response = int(input(f'#{questionNumber + 1}: {x} x {y}\n'))
            response_time = time.time() - start_time

            if response_time > 3:
                print('Out of time!')
                break
            elif response != answer and attempts < 3:
                print(f'Incorrect. Try Again')
                attempts += 1
                continue
            elif response != answer and attempts == 3:
                print(f'Incorrect. The answer is {answer}')
                break
            elif attempts > 3:
                print('Out of tries!')
                break
            else:  # This runs if no exceptions were raised
                print('Correct!')
                correctAnswers += 1
                break

        time.sleep(1)  # Brief pause
    print('Score: %s / %s' % (correctAnswers, numberOfQuestions))


multiplicationQuiz(3)
