# Test with questions that match your actual content
from src.core.document_processor import DocumentProcessor
from src.core.embeddings import EmbeddingsManager

# Set up system
processor = DocumentProcessor(chunk_size=600, chunk_overlap=100)
docs = processor.process_documents("data/sample_docs")
embeddings_manager = EmbeddingsManager()
embeddings_manager.add_documents(docs)

# Questions that should match your content better
test_questions = [
    "Knowledge transfer process",
    "Environment configuration steps", 
    "API Connect setup procedures",
    "Digital Singature configuration",
    "SSL setup",
    "DataPower security"
]

print("🔍 Testing with Content-Matched Questions")
print("=" * 60)

for question in test_questions:
    print(f"\n❓ Question: '{question}'")
    results = embeddings_manager.search_similar(question, n_results=2)
    
    for i, result in enumerate(results, 1):
        score = result['similarity_score']
        content = result['content'][:150].replace('\n', ' ')
        
        # Check if the content actually contains our search terms
        contains_ssl = 'ssl' in content.lower()
        contains_datapower = 'datapower' in content.lower()
        contains_cert = 'certificate' in content.lower()
        
        print(f"  Result {i}: Score {score:.3f}")
        print(f"  Contains: SSL={contains_ssl}, DataPower={contains_datapower}, Cert={contains_cert}")
        print(f"  Content: {content}...")
        
        if score > 0.4:
            print(f"  ✅ This looks relevant!")
        else:
            print(f"  ❌ Low relevance")
        print()