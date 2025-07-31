import datetime

# Simulated OpenAI-like response engine
def generate_response(prompt):
    prompt = prompt.lower()

    # Function 1: Answering Questions
    if "capital of france" in prompt:
        return "The capital of France is Paris."
    elif "ozone layer" in prompt:
        return "The ozone layer absorbs harmful UV rays, protecting life on Earth."
    elif "facts about the sun" in prompt:
        return (
            "1. The Sun is a star.\n"
            "2. It is about 4.6 billion years old.\n"
            "3. It is composed primarily of hydrogen and helium."
        )
    elif "water cycle" in prompt:
        return "The water cycle involves evaporation, condensation, precipitation, and collection."

    # Function 2: Summarizing Text
    elif "summarize" in prompt:
        return "Summary: This passage explains the core ideas using simplified language."
    elif "main points" in prompt:
        return "Main points: The article discusses causes, impacts, and solutions."
    elif "overview" in prompt:
        return "Overview: The document provides a high-level view of the key concepts presented."

    # Function 3: Creative Content
    elif "story about a dragon" in prompt:
        return (
            "Once upon a time, a lonely dragon found a village that welcomed him. "
            "Together, they lived in harmony and peace."
        )
    elif "poem about autumn" in prompt:
        return (
            "Leaves fall gently, golden and bright,\n"
            "Whispers of wind in the crisp twilight."
        )
    elif "science fiction novel" in prompt:
        return (
            "Idea: In a future where memories can be traded, a hacker discovers a buried identity "
            "that could collapse the system."
        )
    else:
        return "This is a simulated AI response based on your prompt."

# Log feedback with timestamp
def log_feedback(prompt, response, feedback):
    with open("feedback_log.txt", "a", encoding="utf-8") as log_file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"[{timestamp}]\n")
        log_file.write(f"Prompt: {prompt}\n")
        log_file.write(f"Response: {response}\n")
        log_file.write(f"Feedback: {feedback}\n")
        log_file.write("=" * 60 + "\n")

# Main assistant program
def run_ai_assistant():
    print("🤖 Welcome to Your Advanced AI Assistant")
    print("-----------------------------------------")

    while True:
        print("\nPlease choose a task:")
        print("1. Answer a Question")
        print("2. Summarize a Text")
        print("3. Generate Creative Content")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print("\n📚 Choose a question to ask:")
            print("a. What is the capital of France?")
            print("b. Explain the importance of the ozone layer.")
            print("c. Give me 3 facts about the Sun.")
            print("d. Describe the water cycle.")
            sub = input("Enter your choice (a-d): ").strip().lower()

            prompts = {
                "a": "What is the capital of France?",
                "b": "Explain the importance of the ozone layer.",
                "c": "Give me 3 facts about the Sun.",
                "d": "Describe the water cycle."
            }
            prompt = prompts.get(sub, "")
            if prompt:
                response = generate_response(prompt)
                print("\n🧠 Response:\n", response)
                feedback = input("\nWas this helpful? (yes/no): ")
                log_feedback(prompt, response, feedback)
            else:
                print("Invalid choice.")

        elif choice == "2":
            print("\n📄 Choose a summarization style:")
            print("a. General Summary")
            print("b. Extract Main Points")
            print("c. Provide an Overview")
            text = input("\nPaste your text to summarize: ")
            style = input("Enter summary style (a/b/c): ").strip().lower()

            if style == "a":
                prompt = f"Summarize the following text: {text}"
            elif style == "b":
                prompt = f"What are the main points of this text: {text}"
            elif style == "c":
                prompt = f"Provide a brief overview of this document: {text}"
            else:
                print("Invalid summary style.")
                continue

            response = generate_response(prompt)
            print("\n📌 Summary:\n", response)
            feedback = input("\nWas this summary helpful? (yes/no): ")
            log_feedback(prompt, response, feedback)

        elif choice == "3":
            print("\n🎨 Choose creative prompt:")
            print("a. Write a story about a dragon and a village.")
            print("b. Create a poem about autumn.")
            print("c. Generate an idea for a science fiction novel.")
            sub = input("Enter your choice (a/b/c): ").strip().lower()

            prompts = {
                "a": "Write a story about a dragon and a village.",
                "b": "Create a poem about autumn.",
                "c": "Generate an idea for a science fiction novel."
            }
            prompt = prompts.get(sub, "")
            if prompt:
                response = generate_response(prompt)
                print("\n📝 Creative Output:\n", response)
                feedback = input("\nDid you like it? (yes/no): ")
                log_feedback(prompt, response, feedback)
            else:
                print("Invalid option.")

        elif choice == "4":
            print("👋 Exiting. Thank you for using the AI Assistant!")
            break

        else:
            print("❌ Invalid input. Please choose a number from 1 to 4.")

# Entry point
if __name__ == "__main__":
    run_ai_assistant()
