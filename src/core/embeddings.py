"""
Embeddings Generator for Knowledge Transfer Assistant
Converts text chunks to vector embeddings for similarity search
"""

import chromadb
from sentence_transformers import SentenceTransformer
from typing import List, Dict
import os


class EmbeddingsManager:
    """Manages text embeddings and vector database operations"""
    
    def __init__(self, model_name: str = "all-MiniLM-L6-v2", db_path: str = "data/processed/vector_db"):
        """
        Initialize embeddings manager
        
        Args:
            model_name: Sentence transformer model for embeddings
            db_path: Path to store vector database
        """
        self.model_name = model_name
        self.db_path = db_path
        
        # Initialize embedding model
        print(f"Loading embedding model: {model_name}")
        self.embedding_model = SentenceTransformer(model_name)
        
        # Initialize vector database
        os.makedirs(db_path, exist_ok=True)
        self.chroma_client = chromadb.PersistentClient(path=db_path)
        self.collection = self._get_or_create_collection()
        
    def _get_or_create_collection(self):
        """Get or create ChromaDB collection"""
        try:
            return self.chroma_client.get_collection("knowledge_base")
        except:
            return self.chroma_client.create_collection("knowledge_base")
    
    def add_documents(self, documents: List[Dict]) -> None:
        """Add processed documents to vector database"""
        if not documents:
            print("No documents to add")
            return
            
        print(f"Adding {len(documents)} chunks to vector database...")
        
        # Prepare data for ChromaDB
        texts = [doc['content'] for doc in documents]
        metadatas = [{
            'source': doc['source'],
            'chunk_id': doc['chunk_id'],
            'doc_type': doc['doc_type']
        } for doc in documents]
        ids = [f"{doc['source']}_{doc['chunk_id']}" for doc in documents]
        
        # Generate embeddings
        embeddings = self.embedding_model.encode(texts).tolist()
        
        # Add to vector database
        self.collection.add(
            embeddings=embeddings,
            documents=texts,
            metadatas=metadatas,
            ids=ids
        )
        
        print(f"✅ Successfully added {len(documents)} chunks to database")
    
    def search_similar(self, query: str, n_results: int = 5) -> List[Dict]:
        """Search for similar documents based on query"""
        # Generate query embedding
        query_embedding = self.embedding_model.encode([query]).tolist()
        
        # Search in vector database
        results = self.collection.query(
            query_embeddings=query_embedding,
            n_results=n_results
        )
        
        # Format results
        formatted_results = []
        for i in range(len(results['documents'][0])):
            formatted_results.append({
                'content': results['documents'][0][i],
                'metadata': results['metadatas'][0][i],
                'similarity_score': 1 - results['distances'][0][i]  # Convert distance to similarity
            })
        
        return formatted_results