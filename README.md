# 🔍 Word Sense Disambiguation Tool

A modern web application built with Streamlit that helps users understand the specific meaning of words based on their context in sentences. This tool uses Natural Language Processing (NLP) techniques to disambiguate word senses.

## Live Demo

[Click here to access the live demo](https://word-sense-disambiguation.streamlit.app/)

## ✨ Features

- **Modern Web Interface**: Beautiful, responsive design with gradient styling
- **Real-time Analysis**: Instant word sense disambiguation
- **User-friendly**: Intuitive interface with clear instructions
- **Context-aware**: Analyzes words based on surrounding text
- **Error Handling**: Robust error handling and validation
- **Examples**: Built-in examples to help users understand the tool

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone or download the project**
   ```bash
   # If you have git installed
   git clone <repository-url>
   cd word-sense-disambiguation
   ```

2. **Install required dependencies**
   ```bash
   pip install streamlit nltk
   ```

3. **Download NLTK data** (required for the first run)
   ```python
   python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab'); nltk.download('wordnet'); nltk.download('averaged_perceptron_tagger')"
   ```

4. **Run the application**
   ```bash
   streamlit run main.py
   ```

5. **Open your browser**
   - The app will automatically open at `http://localhost:8501`
   - If it doesn't open automatically, manually navigate to the URL

## 📖 How to Use

1. **Enter Text**: Type or paste the text you want to analyze in the text area
2. **Specify Word**: Enter the specific word you want to disambiguate
3. **Analyze**: Click the "🔍 Analyze Word" button
4. **View Results**: See the word's definition and meaning in context

### Example Usage

**Input Text:**
```
"The bank is near the river."
```

**Target Word:**
```
bank
```

**Result:**
- The tool will determine whether "bank" refers to a financial institution or the side of a river

## 🛠️ Technical Details

### Technologies Used

- **Streamlit**: Web application framework
- **NLTK**: Natural Language Processing library
- **Lesk Algorithm**: Word sense disambiguation algorithm

### Project Structure

```
word-sense-disambiguation/
├── main.py             # Main application file
├── README.md           # This documentation file
└── requirements.txt    # Python dependencies (optional)
```