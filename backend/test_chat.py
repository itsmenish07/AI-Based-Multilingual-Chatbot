from chatbot import ask_question

print("AI Welfare Assistant")
print("Type 'exit' to quit\n")

while True:

    question = input("Ask: ")

    if question.lower() == "exit":
        break

    answer = ask_question(question)

    print("\nAnswer:")
    print(answer)
    print()