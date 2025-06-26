## Info-Retrieval-chatbot

AI-based Help Bot for Information Retrieval from a Knowledge Graph Based on Static/Dynamic Web Portal Content <br>
The [MOSDAC](www.mosdac.gov.in) portal hosts satellite data and services accessible to the public. It includes <br> 
extensive FAQs, documentation, product specifications, and support material. However, users often struggle to <br>
locate precise information due to layered navigation, mixed content formats, and time constraints. An AI-based <br>
help bot is envisioned to intelligently parse all hosted content and return instant, contextual responses to <br>
user queries, enhancing usability and knowledge accessibility across the platform.

## Objective:

- Develop an intelligent virtual assistant leveraging NLP/ML for query understanding and precise information retrieval.
- Extract and model structured/unstructured content into a dynamic knowledge graph.
- Support geospatial data intelligence for spatially-aware question answering.
- Ensure contextual, relationship-based information discovery.
- Ensure modularity for deployment across other web portals with similar architectures.

## Expected Outcomes:

- An AI-powered conversational help bot capable of resolving user queries accurately from the MOSDAC portal. <br>
- Knowledge graph architecture for entity/relationship mapping across the portal. <br>

## Dataset Required:

- Static and dynamic web content including:
- Product catalogues, FAQ sections, documentation (PDF, DOCX, XLSX, etc.)
- Meta tags, tables, web pages, and accessibility tags (ARIA-labels)
- Satellite mission details, product types, and scientific articles

## Suggested Tools/Technologies:

- Python, NVIDIA RAG, LLMs, spaCy, NLTK
- Dialogflow, Rasa, LangChain, Node.js

## Expected Solution / Steps to be followed to achieve the objectives:

- Data Ingestion: Crawl and extract structured/unstructured content from MOSDAC.
- Knowledge Graph Creation: Entity and relationship extraction using NLP techniques.
- Model Selection: Choose or fine-tune a model for semantic understanding and conversational context.
- Training: Train the model using FAQs, documents, and user intent classification.
- UI/UX Layer: Build a front-end chatbot interface using frameworks like React or Streamlit.
- Integration: Deploy backend services and integrate LLM or retrieval-augmented generation module for real-time querying.
- Modularization: Package with scalable architecture for deployment on alternate domains.

## Evaluation Parameters:

- Intent Recognition Accuracy: How accurately user queries are interpreted.
- Entity Recognition Accuracy: Precision of keyword/topic extraction.
- Response Completeness: Coverage of answer relative to query context.
- Response Consistency: Logical consistency across multi-turn conversations.
