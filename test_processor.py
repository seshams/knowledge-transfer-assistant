# Test the complete pipeline: DocumentProcessor + EmbeddingsManager
from src.core.document_processor import DocumentProcessor
from src.core.embeddings import EmbeddingsManager

print("🚀 Testing complete RAG pipeline...")

# Step 1: Process documents
print("\n1. Processing documents...")
processor = DocumentProcessor(chunk_size=800, chunk_overlap=100)
docs = processor.process_documents("data/sample_docs")
print(f"✅ Processed {len(docs)} chunks")

# Step 2: Initialize embeddings manager
print("\n2. Initializing embeddings system...")
embeddings_manager = EmbeddingsManager()

# Step 3: Add documents to vector database
print("\n3. Adding documents to vector database...")
embeddings_manager.add_documents(docs)

# Step 4: Test search functionality
print("\n4. Testing search functionality...")

# Test queries related to your DataPower document
test_queries = [ 
    "How do I configure SSL certificates?",
    "What is DataPower administration?",
    "How to set up endpoints?",
    "DataPower configuration steps"
]

for query in test_queries:
    print(f"\n🔍 Query: '{query}'")
    results = embeddings_manager.search_similar(query, n_results=2)
    
    for i, result in enumerate(results, 1):
        print(f"  Result {i}:")
        print(f"    Source: {result['metadata']['source']}")
        print(f"    Type: {result['metadata']['doc_type']}")
        print(f"    Score: {result['similarity_score']:.3f}")
        print(f"    Content: {result['content'][:100]}...")
        print()

print("🎉 RAG pipeline test completed!")