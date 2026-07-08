from dotenv import load_dotenv
import os


load_dotenv()


key = os.getenv("GOOGLE_API_KEY")


if key:
    print("API key loaded successfully")
    print(key[:8] + "********")
else:
    print("API key NOT found")