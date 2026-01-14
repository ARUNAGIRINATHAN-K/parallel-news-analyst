try:
    from langchain.chains import ConversationalRetrievalChain
    print("ConversationalRetrievalChain found in langchain.chains")
except ImportError:
    print("ConversationalRetrievalChain NOT found in langchain.chains")
    try:
        from langchain.chains import ConversationalRetrievalChain
    except ImportError:
        pass
