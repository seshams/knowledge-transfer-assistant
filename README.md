# 🤖 Knowledge Transfer Assistant

**AI-powered knowledge transfer automation using local LLMs and custom RAG architecture**

Eliminates repetitive knowledge transfer sessions by allowing new team members to instantly access enterprise documentation through natural language queries.

![Knowledge Transfer Assistant Demo](https://img.shields.io/badge/Demo-Live-green) ![Python](https://img.shields.io/badge/Python-3.10-blue) ![AI](https://img.shields.io/badge/AI-Local%20LLM-orange)

## 🎯 Problem Solved

**Before:** Senior engineers spend 4-6 hours per new hire explaining the same Integration technologies, system Architecture, POCs, and environment setup procedures.

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

# Add your PDF documents to the data folder
cp your-documents.pdf data/sample_docs/

# Restart the app and click "🔄 Initialize Knowledge Base"

💡 Usage Examples
For DataPower Administration:

"How do I configure SSL certificates in DataPower?"
"What are the steps to set up a new DataPower service?"
"Show me DataPower troubleshooting procedures"

For API Connect:

"How do I deploy APIs to API Connect?"
"What's the API Connect installation process?"
"API Connect security configuration steps"

For Environment Management:

"What environments do we have and how do I access them?"
"Environment setup and configuration procedures"
"How do I deploy to different environments?"

🏗️ Architecture
PDF Documents → Text Extraction → Intelligent Chunking → Vector Embeddings
                                                              ↓
User Query → Semantic Search → Context Retrieval → Local LLM → Structured Response

Tech Stack

Frontend: Streamlit (Python web framework)
Vector Database: ChromaDB for semantic search
Embeddings: SentenceTransformers (all-MiniLM-L6-v2)
LLM: Llama 3.1 (local via Ollama)
Document Processing: PyPDF2 + LangChain text splitters
Deployment: Local/Cloud agnostic

📊 Business Impact
Quantified Benefits

⏰ Time Savings: 4-6 hours per new hire onboarding
💰 Cost Reduction: Zero ongoing API costs (local LLM)
📈 Consistency: Standardized knowledge transfer every time
🕒 Availability: 24/7 access to institutional knowledge
📈 Scalability: Easy addition of new teams and documentation

Senior Engineer Time Saved: 6 hours/hire × $75/hour = $450/hire
API Costs Avoided: $0 (local LLM vs $20-50/month external APIs)
Consistency Value: Reduced errors and faster time-to-productivity

🛠️ Development
Project Structure
knowledge-transfer-assistant/
├── src/core/
│   ├── document_processor.py    # PDF processing and chunking
│   ├── embeddings.py           # Vector database management
│   └── chat_bot.py            # Response generation
├── data/
│   ├── sample_docs/           # Your PDF documents
│   └── processed/             # Generated embeddings
├── streamlit_app.py          # Web interface
└── requirements.txt          # Dependencies

Adding New Document Types
The system automatically handles new PDFs. To add support for new formats:
# Extend DocumentProcessor for new file types
def load_word_doc(self, file_path: str) -> str:
    # Add Word document processing
    pass

Customizing Response Style
# Modify the prompt in streamlit_app.py
llama_prompt = f"""Your custom instructions for the AI assistant..."""

🚀 Deployment Options
Local Development
streamlit run streamlit_app.py
# Access at http://localhost:8501

📈 Future Enhancements

 Multi-modal support - Images and diagrams processing
 Advanced analytics - Usage tracking and popular questions
 Team integration - Slack/Teams bot deployment
 Cloud deployment - AWS Bedrock integration
 Fine-tuning - Domain-specific model optimization

🤝 Contributing

Fork the repository
Create a feature branch (git checkout -b feature/amazing-feature)
Commit your changes (git commit -m 'Add amazing feature')
Push to the branch (git push origin feature/amazing-feature)
Open a Pull Request


## 🌐 Live Demo

**Try the cloud demo:** [https://huggingface.co/spaces/seshams/knowledge-transfer-assistant](https://huggingface.co/spaces/seshams/knowledge-transfer-assistant)

*Note: The cloud demo shows the core RAG architecture and document processing capabilities. The full local version includes Llama 3.1 for AI-generated responses.*

### Demo Instructions:
1. Click "🔄 Initialize Knowledge Base" 
2. Wait for document processing to complete
3. Try example questions:
   - "How do I configure SSL certificates in DataPower?"
   - "What are the API Connect installation steps?"
4. Notice source attribution and relevance scoring

## 📱 Screenshots
### 1. System Initialization
![sysInterface](https://github.com/user-attachments/assets/fd62bf08-99a1-4842-908f-337f105ee84a)

### 2. Question & Answer Interface
![QnA](https://github.com/user-attachments/assets/6186868b-1218-44fb-a1d9-1b016242052e)

### 3. Response Quality Example
![Quality](https://github.com/user-attachments/assets/9bb46149-c492-426b-8740-61ce18182754)

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

-----------------------------------------------------------------------------------
Built with ❤️ using Python, Streamlit, and Local AI
