J.A.R.V.I.S.

J.A.R.V.I.S. is an intelligent, privacy-isolated "Second Brain" platform designed for students to seamlessly ingest, organize, and query their academic universe. By combining a decoupled microservices architecture with an advanced Retrieval-Augmented Generation (RAG) pipeline, J.A.R.V.I.S. synthesizes unstructured contextual data—including dense PDFs, lecture slides, screenshots, and synchronized emails—into a unified, low-latency semantic search and conversational interface.

🚀 Key Features & Architectural Highlights
Multi-Modal Ingestion Pipeline: Extracted text normalization across academic documents and syllabus PDFs.

Decoupled Async Processing: Heavy computation tasks (PDF parsing, text chunking, and embedding generation) are completely offloaded to background workers, preventing API gateway blocking.

Asymmetric Sliding-Window Chunking: Document processing utilizes a sliding text window with an explicit overlap factor to guarantee context preservation at text boundaries.

Strict Multi-Tenant Isolation: Vector database queries enforce rigid relational metadata filtering to guarantee absolute user data privacy and prevent cross-tenant data leaks.

Cost-Optimized RAG Orchestration: Drastically minimizes LLM context window overhead by querying top-K mathematically similar semantic vector fragments instead of feeding raw unorganized files to the API.

🛠️ Tech Stack & System Design
The platform is explicitly designed with a true separation of concerns, separating user states, object assets, and hyper-dimensional geometric vector space.

System Architecture Overview
Plaintext
       [ Next.js Frontend UI ]
                 │
           (HTTP / JSON)
                 ▼
       [ FastAPI App Gateway ] ──(Pushes Ingestion Jobs)──► [ Redis Task Queue ]
                 │                                                   │
     (Auth & Metadata Queries)                            (Executes Embeddings)
                 ▼                                                   ▼
       [ PostgreSQL Database ]                            [ Pinecone Vector DB ]
Frontend: Next.js (App Router), TypeScript, Tailwind CSS, Shadcn/UI

Backend Gateway: FastAPI (Asynchronous Python Framework)

Task Management & Broker: Redis Cache & Task Runner Engine

Structured Storage: PostgreSQL (Relational metadata storage, user management, and thread histories)

Vector Engine: Pinecone Serverless (Hyper-dimensional embedding vectors)
