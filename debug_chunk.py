# Debug: Let's see what chunks we actually have
from src.core.document_processor import DocumentProcessor

print("🔍 Debugging Document Chunks")
print("=" * 50)

processor = DocumentProcessor(chunk_size=600, chunk_overlap=100)
docs = processor.process_documents("data/sample_docs")

print(f"Total chunks created: {len(docs)}")
print()

# Show first 5 chunks to see what we're working with
for i, doc in enumerate(docs[:5]):
    print(f"Chunk {i}:")
    print(f"Source: {doc['source']}")
    print(f"Type: {doc['doc_type']}")
    print(f"Length: {len(doc['content'])} characters")
    print(f"Content preview:")
    print(f"'{doc['content'][:200]}...'")
    print("-" * 50)

# Check if chunks contain meaningful content
print("\n🔍 Looking for key DataPower terms:")
search_terms = ['datapower', 'ssl', 'certificate', 'configuration', 'administration', 'endpoint']

for term in search_terms:
    found_in = 0
    for doc in docs:
        if term.lower() in doc['content'].lower():
            found_in += 1
    print(f"'{term}' found in {found_in} chunks")