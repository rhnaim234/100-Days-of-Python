class QuizeBrain:


    def __init__(self, q_list):
        self.question_number=0
        self.score=0
        self.question_list=q_list

    def next_question(self):
        current_question=self.question_list[self.question_number]
        self.question_number=self.question_number+1
        user_ans=input(f"Q.{self.question_number}: {current_question.text} (True/False):")
        self.check_ans(user_ans, current_question.answer)

    score = 0
    def check_ans(self, user_ans, correct_answer):

        if user_ans.lower()==correct_answer.lower():
            self.score=self.score+1
            print("You got it right!")
        else:
            print("Sorry, that's wrong.")
        print(f"The correct answer is {correct_answer}")
        print(f"Your score is {self.score}/{self.question_number}")

    def still_has_question(self):
        return  self.question_number<len(self.question_list)

