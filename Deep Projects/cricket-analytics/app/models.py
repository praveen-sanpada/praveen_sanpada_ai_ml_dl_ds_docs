from langchain.chat_models import ChatOpenAI

class LangChainModel:
    def __init__(self):
        # Initialize the LangChain model with desired configurations
        self.model = ChatOpenAI(model="gpt-3.5-turbo")  # Replace with your model choice
    
    def get_response(self, query):
        response = self.model.generate([query])  # Use the LangChain model to generate responses
        return response['choices'][0]['message']['content']
