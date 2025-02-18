import streamlit as st
import subprocess
from typing import List, Optional

# Import LangChain modules
from langchain.llms import BaseLLM
from langchain import PromptTemplate, LLMChain
from langchain.schema import Generation, LLMResult

#########################################
# 1. Custom LLM Class using DeepSeek
#########################################

class DeepSeekLLM(BaseLLM):
    @property
    def _llm_type(self) -> str:
        return "DeepSeekLLM"
    
    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        """
        Calls the local DeepSeek model via Ollama using a subprocess call.
        Ensure Ollama is installed and the 'deepseek-r1:7b' model is available locally.
        """
        # Ensure prompt is a string (in case it's not)
        prompt_str = str(prompt)
        command = ["ollama", "run", "deepseek-r1:7b", prompt_str]
        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            return f"Error calling DeepSeek model: {e}"
    
    def _generate(self, prompt: str, stop: Optional[List[str]] = None) -> LLMResult:
        """
        Implements the abstract _generate method by calling _call and wrapping
        the result in a LLMResult object.
        """
        text = self._call(prompt, stop=stop)
        generation = Generation(text=text)
        return LLMResult(generations=[[generation]])

#########################################
# 2. Function to Generate Story Continuation
#########################################

def generate_story(user_input: str, story_context: str) -> str:
    """
    Uses a LangChain prompt template to combine the current story context with the user's input,
    then queries the DeepSeek model to generate a continuation.
    """
    # Define the prompt template
    template = (
        "You are an AI co-author for collaborative storytelling.\n\n"
        "Current story context:\n{story_context}\n\n"
        "User's input:\n{user_input}\n\n"
        "Please continue the story with creative plot twists, rich character arcs, and an engaging narrative."
    )
    prompt_template = PromptTemplate(template=template, input_variables=["story_context", "user_input"])
    
    # Create a custom LLM instance and an LLM chain
    llm = DeepSeekLLM()
    chain = LLMChain(llm=llm, prompt=prompt_template)
    
    # Generate the story continuation
    story_continuation = chain.run({"story_context": story_context, "user_input": user_input})
    return story_continuation

#########################################
# 3. Streamlit User Interface
#########################################

def main():
    st.title("Collaborative Storytelling Companion")
    
    # Initialize session state to hold the evolving story context
    if "story_context" not in st.session_state:
        st.session_state.story_context = "Once upon a time, in a mystical land, adventure awaited."
    
    st.subheader("Current Story")
    # Display the current story context
    story_context = st.text_area("Story Context", st.session_state.story_context, height=200)
    
    st.subheader("Your Contribution")
    # Field for the user to add plot twists or ideas
    user_input = st.text_input("Enter your plot twist or idea:")
    
    if st.button("Continue Story"):
        if user_input.strip() == "":
            st.error("Please enter an idea or plot twist to continue the story.")
        else:
            with st.spinner("Generating story continuation..."):
                continuation = generate_story(user_input, story_context)
                # Update the story context with the generated continuation
                updated_story_context = story_context + "\n" + continuation
                st.session_state.story_context = updated_story_context
                st.success("Story updated!")
                st.text_area("Updated Story", updated_story_context, height=300)

if __name__ == "__main__":
    main()