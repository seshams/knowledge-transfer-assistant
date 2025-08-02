# Test with a model better suited for technical content
from src.core.document_processor import DocumentProcessor
from src.core.embeddings import EmbeddingsManager

print("🧪 Testing Different Embedding Model")
print("=" * 50)

# Process documents
processor = DocumentProcessor(chunk_size=400, chunk_overlap=50)  # Smaller chunks
docs = processor.process_documents("data/sample_docs")

# Try a different model that's better for technical content
try:
    embeddings_manager = EmbeddingsManager(model_name="all-mpnet-base-v2")
    print("✅ Using all-mpnet-base-v2 (better for technical content)")
except:
    embeddings_manager = EmbeddingsManager()  # fallback
    print("⚠️ Using default model")

embeddings_manager.add_documents(docs)

# Test simple exact matches first
exact_tests = [
    "SSL",
    "DataPower", 
    "certificate"
]

print("\n🎯 Testing Exact Term Matches:")
for term in exact_tests:
    print(f"\n Searching for: '{term}'")
    results = embeddings_manager.search_similar(term, n_results=2)
    
    for i, result in enumerate(results, 1):
        score = result['similarity_score']
        content = result['content'].lower()
        
        # Check if the exact term appears in the result
        term_found = term.lower() in content
        
        print(f"   Result {i}: Score {score:.3f}, Contains '{term}': {term_found}")
        
        if term_found and score > 0.3:
            print(f"   ✅ SUCCESS: Found '{term}' with decent score")
            # Show some context
            snippet = result['content'][:100].replace('\n', ' ')
            print(f"   Content: {snippet}...")
        elif term_found:
            print(f"   ⚠️ Found '{term}' but low score")
        else:
            print(f"   ❌ '{term}' not in result")