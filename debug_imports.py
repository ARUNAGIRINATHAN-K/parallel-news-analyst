try:
    import langchain
    print(f"LangChain version: {langchain.__version__}")
    print(f"LangChain path: {langchain.__file__}")
    
    import langchain.memory
    print("langchain.memory found")
except ImportError as e:
    print(f"ImportError: {e}")
    try:
        import langchain_community.memory
        print("langchain_community.memory found")
    except ImportError as e2:
        print(f"langchain_community.memory also failed: {e2}")

try:
    from langchain.memory import ConversationBufferMemory
    print("ConversationBufferMemory import successful")
except ImportError as e:
    print(f"ConversationBufferMemory import failed: {e}")
