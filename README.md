# GeminiScienceBot

**Title:** Curious Cosmos: Your AI Guide to the Universe's Equations

**Description:**

Curious Cosmos is an interactive web application built with Streamlit that leverages Google's GenerativeAI framework (specifically the Gemini-Pro model) to create a conversational AI assistant for exploring scientific concepts. Users can ask questions related to physics, math, and chemistry, and receive informative and engaging responses.

**Key Features:**

- **AI-Powered Conversation:** Utilize the power of generative AI to have natural and insightful interactions about scientific topics.
- **Streamlit Integration:** Employ Streamlit for a user-friendly and web-based interface.
- **Topic-Specific Responses:** Tailor responses to physics, math, and chemistry queries, leveraging topic keywords for focused assistance.
- **Informative Assistant:** Provide helpful guidance even for non-scientific prompts or non-recognized topics.

**Installation:**

1. **Clone the repository:** Use `git clone https://github.com/<your-username>/curious-cosmos.git` to clone this repository.
2. **Create a virtual environment (recommended):** Create and activate a virtual environment using tools like `venv` or `conda` to isolate project dependencies.
3. **Install dependencies:** Run `pip install -r requirements.txt` to install the required Python libraries (Streamlit, dotenv, google-generativeai, pyttsx3).
4. **Set up Google API Key:**
   - Create a project in the Google Cloud Console.
   - Enable the Google GenerativeAI API for your project.
   - Create an API key and store it securely as an environment variable. You can use the `dotenv` library for this purpose.
   - Add the following line to your `.env` file, replacing `<YOUR_API_KEY>` with your actual key: `GOOGLE_API_KEY=<YOUR_API_KEY>`

**Usage:**

1. **Start the application:** Run `streamlit run app.py` (assuming your main script is called `app.py`).
2. **Interact with Mrs. Fox:** Ask questions related to physics, math, and chemistry in the provided chat interface.
3. **Greeting and Non-Specific Topics:** Use greetings like "hello" or "hi" for a friendly response. For non-scientific prompts, you'll receive an informative message explaining Mrs. Fox's capabilities and offering to greet you.

**Additional Notes:**

- This project is still under development, and Mrs. Fox's knowledge and capabilities will continue to improve.
- The `pyttsx3` library is included for potential text-to-speech functionality, but it's not currently implemented in this version. You can explore adding this feature in the future.
- Feel free to customize the project to fit your specific needs, such as expanding the range of supported scientific topics or tailoring the greetings and responses.


<img width="1429" alt="Screenshot 2024-07-10 at 7 50 38 PM" src="https://github.com/johnny-john7/GeminiScienceBot/assets/116308028/c40b3339-98b5-440e-8e4a-19eeeea151e9">
