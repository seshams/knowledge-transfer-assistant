# 🤖 Knowledge Transfer Assistant

**AI-powered knowledge transfer automation using local LLMs and custom RAG architecture**

Eliminates repetitive knowledge transfer sessions by allowing new team members to instantly access enterprise documentation through natural language queries.

![Knowledge Transfer Assistant Demo](https://img.shields.io/badge/Demo-Live-green) ![Python](https://img.shields.io/badge/Python-3.10-blue) ![AI](https://img.shields.io/badge/AI-Local%20LLM-orange)

## 🎯 Problem Solved

**Before:** Senior engineers spend 4-6 hours per new hire explaining the same Integration technologies, system rchitecture, POCs, and environment setup procedures.

**After:** New hires get instant, 24/7 access to expert knowledge through an AI assistant that provides step-by-step guidance with source citations.

## ✨ Key Features

- 🔍 **Semantic Search** - Natural language queries across multiple technical documents
- 🤖 **Local LLM Integration** - Llama 3.1 for human-like responses with zero API costs
- 📚 **Source Attribution** - Every answer includes document references and relevance scores
- 💬 **Professional Chat Interface** - Streamlit-powered web application
- 🔒 **Secure & Private** - All data processing happens locally, no external APIs
- ⚡ **Easy Document Management** - Drag-and-drop PDF addition and automatic processing

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- 16GB RAM recommended
- macOS/Linux (Windows supported)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/[your-username]/knowledge-transfer-assistant.git
cd knowledge-transfer-assistant

# 2. Install dependencies
pip install -r requirements.txt

# 3. Install and setup Ollama
brew install ollama  # macOS
# or: curl -fsSL https://ollama.ai/install.sh | sh  # Linux

# 4. Download the LLM model
ollama pull llama3.1

# 5. Start the application
streamlit run streamlit_app.py
