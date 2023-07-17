from Question import Question

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n",
    "What color are bananas?\n(a) Pink\n(b) Teal\n(c) Yellow\n",
    "What color are strawberries?:\n(a) Yellow\n(b) Red\n(c) Blue\n"
]

questionss = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("Your score was " + str(score) + "/" + str(len(questionss)))

run_test(questionss)