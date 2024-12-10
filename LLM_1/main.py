import os
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    print("Hello langchain")
    print(os.environ["OPEN_AI_API_KEY"])
