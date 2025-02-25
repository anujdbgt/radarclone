# radarclone

Before coding, define the key functionalities of your app:
✅ User inputs symptoms (e.g., "burning stomach pain at night")
✅ App identifies possible diseases and homeopathic remedies
✅ App provides references from repertories
✅ Users can search using synonyms & natural language
✅ (Optional) Case history storage & user management
**Technology Stack**
Backend -	FastAPI (Python)
Frontend -	React (Web) or Flutter (Mobile)
LLM for reasoning -	Llama 3 / Mistral 7B (Self-Hosted)
Embeddings for search -	BGE (bge-base-en)
Vector Search	- FAISS (Self-Hosted)
Database -	PostgreSQL with pgvector or SQLite
Hosting -	Local server / VPS (DigitalOcean, AWS, etc.)
