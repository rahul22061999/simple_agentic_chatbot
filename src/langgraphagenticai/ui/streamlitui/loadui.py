import streamlit as st 
import os 
from src.langgraphagenticai.ui.uiconfigfile import Config 


class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    
    def load_streamlit_ui(self):
        st.set_page_config(
            page_title=f"Bot - {self.config.get_page_title()}", 
            layout="wide",
            initial_sidebar_state="expanded" 
        )
        st.header(f"🤖 Bot - {self.config.get_page_title()}")



        with st.sidebar:

            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options)


            if self.user_controls["selected_llm"] == "Groq":

                model_options = self.config.get_groq_model_options()
                self.user_controls["selected_groq_model"] = st.selectbox("Select Model", model_options)
                self.user_controls["GROQ_API_KEY"] = st.text_input("API KEY", type="password")

                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("please enter your groq api key to continue")
            
            ## use case selection 
            self.user_controls["selected_usecase"] = st.selectbox("Select usecases", usecase_options)

            if self.user_controls["selected_usecase"] == "Chatbot with Web":
                tavily_key = st.text_input("TAVILY API KEY", type="password")

                self.user_controls["TAVILY_API_KEY"] = tavily_key

                if tavily_key:
                    os.environ["TAVILY_API_KEY"] = tavily_key
                    st.session_state["TAVILY_API_KEY"] = tavily_key
                else:
                    st.warning("please enter your tavily api key to continue")

               

        
        return self.user_controls
        

