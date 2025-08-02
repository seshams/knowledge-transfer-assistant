# Test hybrid approach: keyword + semantic search
from src.core.document_processor import DocumentProcessor
from src.core.embeddings import EmbeddingsManager
import re

print("🔍 Testing Hybrid Search (Keyword + Semantic)")
print("=" * 60)

# Set up system
processor = DocumentProcessor(chunk_size=400, chunk_overlap=50)  # Smaller chunks
docs = processor.process_documents("data/sample_docs")

# Create a simple keyword filter function
def keyword_filter(docs, keywords):
    """Filter documents that contain any of the keywords"""
    filtered = []
    for doc in docs:
        content_lower = doc['content'].lower()
        if any(keyword.lower() in content_lower for keyword in keywords):
            filtered.append(doc)
    return filtered

# Test questions with keyword pre-filtering
test_cases = [
    {
        "question": "SSL certificate setup",
        "keywords": ["ssl", "certificate"]
    },
    {
        "question": "DataPower configuration", 
        "keywords": ["datapower", "configuration", "config"]
    },
    {
        "question": "DataPower administration",
        "keywords": ["datapower", "admin"]
    }
]

for i, test in enumerate(test_cases, 1):
    print(f"\n{'='*50}")
    print(f"TEST {i}: {test['question']}")
    print(f"Keywords: {test['keywords']}")
    print("-" * 50)
    
    # Step 1: Filter by keywords first
    keyword_filtered = keyword_filter(docs, test['keywords'])
    print(f"📝 Keyword filter found: {len(keyword_filtered)} relevant chunks")
    
    if keyword_filtered:
        # Step 2: Use embeddings on the filtered set
        embeddings_manager = EmbeddingsManager()
        embeddings_manager.add_documents(keyword_filtered)
        
        results = embeddings_manager.search_similar(test['question'], n_results=min(3, len(keyword_filtered)))
        
        for j, result in enumerate(results, 1):
            score = result['similarity_score']
            content = result['content'][:200].replace('\n', ' ')
            
            print(f"\n  Result {j}: Score {score:.3f}")
            print(f"  Content: {content}...")
            
            if score > 0.3:
                print(f"  ✅ Reasonable match!")
            else:
                print(f"  ⚠️ Low semantic score but contains keywords")
    else:
        print("❌ No chunks found with those keywords")

print(f"\n{'='*60}")
print("💡 Hybrid approach: Filter by keywords first, then semantic search")
print("This should give better results for technical content!")