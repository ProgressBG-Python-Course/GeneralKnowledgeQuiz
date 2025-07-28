class Question:
    def __init__(self, text, answer, categories=None, type=None):
        self.text = text
        self.answer = answer
        self.categories = categories if categories is not None else []
        self.type = type

    def check_answer(self, user_answer):
        """ Check if the user's answer is correct.

        Args:
            user_answer (str): The answer provided by the user.

        Returns:
            bool: True if the answer is correct, False otherwise.
        """
        return user_answer.lower() == self.answer.lower()

    def __str__(self):
        return  "Question: " + self.text + "\n" \
                "Answer: " + self.answer + "\n" \
                "Categories: " + ", ".join(self.categories) + "\n" \
                "Type: " + (self.type if self.type else "N/A")


if __name__ == "__main__":
    question = Question(
        text="What is the capital of France?",
        answer="Paris",
        categories=["Geography", "Europe"],
        type="multiple_choice"
    )

    print(question.text)
    user_answer = input("Your answer: ")
    if question.check_answer(user_answer):
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", question.answer)
