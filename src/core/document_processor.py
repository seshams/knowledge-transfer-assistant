"""
Document Processor for Knowledge Transfer Assistant
Handles multiple document types: DataPower, Architecture, Web Standards
"""

import os
from typing import List, Dict
from pathlib import Path
try:
    import PyPDF2
except ImportError:
    import pypdf as PyPDF2
from langchain.text_splitter import RecursiveCharacterTextSplitter


class DocumentProcessor:
    """Processes various document types for RAG system"""
    
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 200):
        """
        Initialize the document processor
        
        Args:
            chunk_size: Size of text chunks for processing
            chunk_overlap: Overlap between chunks to maintain context
        """
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )
        
    def load_pdf(self, file_path: str) -> str:
        """Extract text from PDF file"""
        try:
            with open(file_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                text = ""
                
                # Read each page
                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    text += page.extract_text() + "\n"
                
                return text.strip()
                
        except Exception as e:
            print(f"Error reading PDF {file_path}: {str(e)}")
            return ""
    
    def process_documents(self, docs_folder: str) -> List[Dict]:
        """Process all documents in a folder and split into chunks"""
        processed_docs = []
        
        # Get all PDF files in the folder
        docs_path = Path(docs_folder)
        pdf_files = list(docs_path.glob("*.pdf"))
        
        print(f"Found {len(pdf_files)} PDF files to process...")
        
        for pdf_file in pdf_files:
            print(f"Processing: {pdf_file.name}")
            
            # Extract text from PDF
            text = self.load_pdf(str(pdf_file))
            
            if text:
                # Split text into chunks
                chunks = self.text_splitter.split_text(text)
                
                # Create metadata for each chunk
                for i, chunk in enumerate(chunks):
                    doc_info = {
                        'content': chunk,
                        'source': pdf_file.name,
                        'chunk_id': i,
                        'doc_type': self._classify_document(pdf_file.name)
                    }
                    processed_docs.append(doc_info)
        
        print(f"Created {len(processed_docs)} chunks from all documents")
        return processed_docs

    def _classify_document(self, filename: str) -> str:
        """Classify document type based on filename"""
        filename_lower = filename.lower()
        
        if 'datapower' in filename_lower:
            return 'datapower'
        elif 'architecture' in filename_lower or 'design' in filename_lower:
            return 'architecture'
        elif 'standard' in filename_lower or 'spec' in filename_lower:
            return 'standards'
        else:
            return 'general'