import streamlit as st
import sys
import os

# Add src to path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from core.document_processor import DocumentProcessor
from core.embeddings import EmbeddingsManager
import requests
import json

st.set_page_config(
    page_title="Knowledge Transfer Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Knowledge Transfer Assistant")
st.markdown("*AI-powered knowledge transfer for DataPower, API Connect, and Environment Management*")

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'system_ready' not in st.session_state:
    st.session_state.system_ready = False

# Sidebar for system status
with st.sidebar:
    st.header("📊 System Status")
    
    if st.button("🔄 Initialize Knowledge Base"):
        with st.spinner("Processing documents..."):
            try:
                # Process documents
                processor = DocumentProcessor(chunk_size=600, chunk_overlap=100)
                docs = processor.process_documents("data/sample_docs")
                
                # Setup embeddings
                embeddings_manager = EmbeddingsManager()
                embeddings_manager.add_documents(docs)
                
                st.session_state.embeddings_manager = embeddings_manager
                st.session_state.system_ready = True
                st.session_state.total_chunks = len(docs)
                
                st.success(f"✅ Processed {len(docs)} document chunks")
                
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
    
    if st.session_state.system_ready:
        st.success("🟢 System Ready")
        st.info(f"📄 {st.session_state.total_chunks} chunks loaded")
    else:
        st.warning("🟡 Click 'Initialize Knowledge Base' to start")

# Main chat interface
if st.session_state.system_ready:
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask about DataPower, API Connect, or environments..."):
        # Add user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Generate response (FIXED INDENTATION)
        with st.chat_message("assistant"):
            with st.spinner("Searching knowledge base and generating response..."):
                try:
                    # Search for relevant documents
                    results = st.session_state.embeddings_manager.search_similar(prompt, n_results=3)
                    
                    # Prepare context
                    context_chunks = []
                    sources = []
                    
                    for i, result in enumerate(results, 1):
                        context_chunks.append(result['content'])
                        sources.append({
                            'source': result['metadata']['source'],
                            'score': result['similarity_score'],
                            'chunk_id': result['metadata'].get('chunk_id', i)
                        })
                    
                    # Create context for Llama
                    context_text = "\n\n---\n\n".join(context_chunks)
                    
                    # Create prompt for Llama
                    llama_prompt = f"""You are a helpful technical assistant specializing in DataPower, API Connect, and IT environment management. 

Based on the following documentation excerpts, provide a clear, structured answer to the user's question.

DOCUMENTATION:
{context_text}

USER QUESTION: {prompt}

Please provide:
1. A direct answer to the question
2. Step-by-step instructions if applicable
3. Key points organized clearly
4. Mention which aspects come from the documentation

Format your response to be helpful for someone learning these technologies."""

                    # Send to Ollama
                    ollama_response = requests.post(
                        'http://localhost:11434/api/generate',
                        json={
                            'model': 'llama3.1',
                            'prompt': llama_prompt,
                            'stream': False
                        }
                    )
                    
                    if ollama_response.status_code == 200:
                        llama_answer = ollama_response.json()['response']
                        
                        # Format the complete response
                        final_response = f"""{llama_answer}

---
**📚 Sources:**"""
                        
                        for i, source in enumerate(sources, 1):
                            final_response += f"""
- **{source['source']}** (Relevance: {source['score']:.2f})"""
                        
                        st.markdown(final_response)
                        st.session_state.messages.append({"role": "assistant", "content": final_response})
                        
                    else:
                        # Fallback to simple response if Llama fails
                        fallback_response = "**Based on the documentation:**\n\n"
                        for i, chunk in enumerate(context_chunks, 1):
                            fallback_response += f"**Point {i}:** {chunk[:200]}...\n\n"
                        
                        fallback_response += "**📚 Sources:**\n"
                        for source in sources:
                            fallback_response += f"- {source['source']}\n"
                        
                        st.markdown(fallback_response)
                        st.session_state.messages.append({"role": "assistant", "content": fallback_response})
                        
                except Exception as e:
                    error_msg = f"❌ Error: {str(e)}"
                    st.error(error_msg)
                    st.session_state.messages.append({"role": "assistant", "content": error_msg})

else:
    st.info("👆 Please initialize the knowledge base using the sidebar to get started.")

# Footer
st.markdown("---")
st.markdown("*Built with Streamlit, ChromaDB, and Local LLMs*")