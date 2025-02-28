import pyinputplus as pyip
import random, time

def multiplicationQuiz(questions = 10, min = 1, max = 10):
    numberOfQuestions = questions
    correctAnswers = 0

    for questionNumber in range(numberOfQuestions):
        x = random.randint(min,max)
        y = random.randint(min, max)
        answer = x * y

        prompt = '#%s: %s x %s = ' % (questionNumber, x, y)

        try:
            # Right answers are handled by allowRegexes.
            # Wrong answers are handled by blockRegexes, with a custom message.
            pyip.inputStr(prompt,
                          allowRegexes = ['^%s$' % answer],
                          blockRegexes=[('.*',  f'Incorrect. The answer is {answer}')],
                          timeout=8, limit=3)
        except pyip.TimeoutException:
            print('Out of time!')
        except pyip.RetryLimitException:
            print('Out of tries!')
        else: #This runs if no exceptions were raised

            correctAnswers += 1

        time.sleep(1) # Brief pause
    print('Score: %s / %s' % (correctAnswers, numberOfQuestions))

multiplicationQuiz(5,20,30)
