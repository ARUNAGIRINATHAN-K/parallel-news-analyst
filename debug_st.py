import sys
print(f"Python Executable: {sys.executable}")
print(f"Python Path: {sys.path}")

try:
    import sentence_transformers
    print(f"Successfully imported sentence_transformers. Version: {sentence_transformers.__version__}")
    print(f"File location: {sentence_transformers.__file__}")
except ImportError as e:
    print(f"Failed to import sentence_transformers: {e}")
except Exception as e:
    print(f"An error occurred during import: {e}")

try:
    from langchain_community.embeddings import HuggingFaceEmbeddings
    print("Successfully imported HuggingFaceEmbeddings")
except ImportError as e:
    print(f"Failed to import HuggingFaceEmbeddings: {e}")
