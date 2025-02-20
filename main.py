import streamlit as st
import subprocess
from typing import List, Optional
from datetime import datetime

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
# 2. Story Management Functions
#########################################

def save_story_checkpoint():
    """Save the current story state as a checkpoint"""
    if "checkpoints" not in st.session_state:
        st.session_state.checkpoints = []
    
    checkpoint = {
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'content': st.session_state.story_context
    }
    st.session_state.checkpoints.append(checkpoint)

def restore_checkpoint(index):
    """Restore the story to a previous checkpoint"""
    if 0 <= index < len(st.session_state.checkpoints):
        st.session_state.story_context = st.session_state.checkpoints[index]['content']

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
# 3. Enhanced Streamlit User Interface
#########################################

def main():
    # Set page config
    st.set_page_config(
        page_title="Story Weaver AI",
        page_icon="📚",
        layout="wide"
    )

    # Custom CSS
    st.markdown("""
        <style>
        .stButton>button {
            width: 100%;
            margin-bottom: 10px;
        }
        .story-container {
            background-color: #f0f2f6;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Title with emoji
    st.title("📚 Kathamitra")
    
    # Initialize session states
    if "story_context" not in st.session_state:
        st.session_state.story_context = "Once upon a time, in a mystical land, adventure awaited."
    if "chapter_count" not in st.session_state:
        st.session_state.chapter_count = 1

    # Create two columns for the main layout
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("📖 Current Story")
        story_context = st.text_area(
            "Story Content",
            st.session_state.story_context,
            height=400,
            key="story_area"
        )

        # Story statistics
        word_count = len(story_context.split())
        st.info(f"Word count: {word_count} | Chapter: {st.session_state.chapter_count}")

    with col2:
        st.subheader("🎨 Story Controls")
        
        # User input with genre selection
        genre = st.selectbox(
            "Select Genre",
            ["Fantasy", "Science Fiction", "Mystery", "Romance", "Horror"]
        )
        
        writing_style = st.select_slider(
            "Writing Style",
            options=["Concise", "Balanced", "Descriptive"],
            value="Balanced"
        )
        
        user_input = st.text_area(
            "Enter your plot twist or idea:",
            height=100
        )

        # Control buttons
        col_btn1, col_btn2 = st.columns(2)
        
        with col_btn1:
            if st.button("🔄 Continue Story"):
                if user_input.strip() == "":
                    st.error("Please enter an idea or plot twist.")
                else:
                    with st.spinner("Weaving your story..."):
                        continuation = generate_story(user_input, story_context)
                        updated_story = story_context + "\n\n" + continuation
                        st.session_state.story_context = updated_story
                        st.success("Story updated!")
        
        with col_btn2:
            if st.button("📑 New Chapter"):
                st.session_state.chapter_count += 1
                save_story_checkpoint()
                st.success(f"Started Chapter {st.session_state.chapter_count}")

        # Story management tools
        st.subheader("🛠️ Story Management")
        
        if st.button("💾 Save Checkpoint"):
            save_story_checkpoint()
            st.success("Checkpoint saved!")

        if "checkpoints" in st.session_state and st.session_state.checkpoints:
            checkpoint_index = st.selectbox(
                "Restore Checkpoint",
                range(len(st.session_state.checkpoints)),
                format_func=lambda x: f"Checkpoint {x + 1} - {st.session_state.checkpoints[x]['timestamp']}"
            )
            
            if st.button("⏮️ Restore"):
                restore_checkpoint(checkpoint_index)
                st.success("Story restored to checkpoint!")

        # Export options
        st.subheader("📤 Export Options")
        export_format = st.selectbox(
            "Export Format",
            ["TXT", "PDF", "DOCX"]
        )
        
        if st.button("📥 Export Story"):
            st.info(f"Story would be exported as {export_format} (Feature coming soon)")

if __name__ == "__main__":
    main()