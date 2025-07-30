import streamlit as st
import nltk
from nltk.wsd import lesk
from nltk.tokenize import word_tokenize
nltk.download("punkt")
nltk.download('punkt_tab')
nltk.download("wordnet")
nltk.download("averaged_perceptron_tagger")

# Page configuration
st.set_page_config(
    page_title="Word Sense Disambiguation",
    page_icon="🔍",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        text-align: center;
        color: white;
    }
    .stButton > button {
        border-radius: 8px;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="main-header"><h1>🔍 Word Sense Disambiguation</h1><p>Discover the meaning of words in context</p></div>', unsafe_allow_html=True)

# Sidebar for additional info
with st.sidebar:
    st.markdown("### ℹ️ About")
    st.markdown("""
    This tool helps you understand the specific meaning of a word based on its context in a sentence.
    
    **How it works:**
    1. Enter your text in the text area
    2. Specify the word you want to analyze
    3. Click analyze to see the word's meaning in context
    """)
    
    st.markdown("### 📝 Example")
    st.markdown("""
    **Text:** "The bank is near the river."\n
    **Word:** "bank"\n
    **Result:** Financial institution vs. river bank
    """)

# Main content area
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 📝 Enter Your Text")
    text = st.text_area("Text to analyze",height=150,placeholder="Enter the text you want to analyze...")

with col2:
    st.markdown("### 🎯 Target Word")
    word = st.text_input("Word to analyze",placeholder="Enter the word...")
    analyze_button = st.button("🔍 Analyze Word", use_container_width=True)

# Results section
if analyze_button and text and word:
    st.markdown("---")
    st.markdown("### 📊 Analysis Results")
    try:
        sense = lesk(word_tokenize(text), word)        
        if sense:
            st.markdown(f"**✅ Analysis Complete!**")
            st.markdown(f"**Word:** {word}")
            st.markdown(f"**Definition:** {sense.definition()}")
        else:
            st.markdown(f"**⚠️ No specific sense found**")
            st.markdown(f"The word '{word}' was not found in the text or no specific sense could be determined.")
    except Exception as e:
        st.error(f"An error occurred during analysis: {str(e)}")
elif analyze_button:
    st.warning("Please enter both text and a word to analyze.")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 0 1rem;'>
    <p>🔍 Word Sense Disambiguation Tool | Powered by NLP</p>
</div>
""", unsafe_allow_html=True)