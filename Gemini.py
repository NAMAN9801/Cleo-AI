from config import API_KEY
import google.generativeai as genai
genai.configure(api_key=API_KEY)


class Gemini:
    """A function where i can put in the input and then i can get or return the output as this.
  A class in a function where all this shit is happening"""
    def __init__(self):

        # Set up the model
        self.generation_config = {
            "temperature": 0.9,
            "top_p": 1,
            "top_k": 1,
            "max_output_tokens": 256,
        }

        self.safety_settings = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
        ]

        self.model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                           generation_config=self.generation_config,
                                           safety_settings=self.safety_settings)

        self.convo = self.model.start_chat(history=[
        ])

    def question(self, prompt_input):
        self.convo.send_message(f"{prompt_input}.")
        return self.convo.last.text
