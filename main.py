from core.brain import generate_response
from core.emotion import detect_emotion
from core.memory import load_memory, update_memory
from core.planner import plan_task, get_upcoming_tasks
from core.journal import get_prompt, save_entry

def main():
    print("🧠 SageMind Initialized.")
    print("Commands: plan: <task>, show tasks, journal, exit\n")

    memory = load_memory()

    while True:
        user_input = input("🧑 You: ").strip()

        if user_input.lower() == "exit":
            print("👋 Goodbye.")
            break

        elif user_input.lower().startswith("plan:"):
            task = user_input[5:].strip()
            steps = plan_task(task)
            print("📋 SageMind planned:")
            for s in steps:
                print(f"➤ {s['step']} | ⏳ {s['deadline']} | 🔺 {s['priority']}")

        elif user_input.lower() == "show tasks":
            tasks = get_upcoming_tasks()
            if not tasks:
                print("📭 No tasks.")
            else:
                print("🗓️ Upcoming Tasks:")
                for t in tasks:
                    print(f"➤ {t['step']} | ⏳ {t['deadline']} | 🔺 {t['priority']}")

        elif user_input.lower() == "journal":
            prompt = get_prompt()
            print(f"📝 Journal Prompt: {prompt}")
            response = input("Your entry: ").strip()
            save_entry(response)
            print("✅ Entry saved.")

        else:
            emotion = detect_emotion(user_input)
            print(f"[🧠 Emotion: {emotion['emotion']} ({emotion['confidence']:.2f})]")
            response = generate_response(user_input, memory)
            print(f"🤖 SageMind: {response}")
            memory = update_memory(user_input, response)

if __name__ == "__main__":
    main()