J.A.R.V.I.S.

JARVIS is an intelligent, privacy-isolated "Second Brain" platform designed for students. It can seamlessly ingest, organize, and resolve user query about their academic or professional universe. By combining a decoupled microservices architecture with an advanced RAG pipeline, JARVIS can synthesize unstructured contextual data, like dense PDFs, lecture slides, screenshots, and synchronized emails into a unified, low-latency semantic search and conversational interface.


1) Key Features & Architectural Highlights


 a) Multi-Modal Ingestion Pipeline: Extracted text normalization across documents and syllabus PDFs.
  
 b) Decoupled Async Processing: Heavy computation tasks (PDF parsing, text chunking, and embedding generation) are completely offloaded to background workers, preventing API gateway blocking.
  
 c) Asymmetric Sliding-Window Chunking: Document processing utilizes a sliding text window with an explicit overlap factor to guarantee context preservation at text boundaries.
  
 d) Strict Multi-Tenant Isolation: Vector database queries enforce rigid relational metadata filtering to guarantee absolute user data privacy and prevent cross-tenant data leaks.
  
 e) Cost-Optimized RAG Orchestration: Drastically minimizes LLM context window overhead by querying top-K mathematically similar semantic vector fragments instead of feeding raw unorganized files to the API.

2) Tech Stack & System Design

The platform is explicitly designed with a true separation of concerns, separating user states, object assets, and hyper-dimensional geometric vector space.

System Architecture Overview

       [ Next.js Frontend UI ]
                 │
           (HTTP / JSON)
                 ▼
       [ FastAPI App Gateway ] ──(Pushes Ingestion Jobs)──► [ Redis Task Queue ]
                 │                                                   │
     (Auth & Metadata Queries)                            (Executes Embeddings)
                 ▼                                                   ▼
       [ PostgreSQL Database ]                            [ Pinecone Vector DB ]


3) Frontend: Next.js (App Router), TypeScript, Tailwind CSS, Shadcn/UI


4) Backend Gateway: FastAPI (Asynchronous Python Framework)

5) Task Management & Broker: Redis Cache & Task Runner Engine

6) Structured Storage: PostgreSQL (Relational metadata storage, user management, and thread histories)

7) Vector Engine: Pinecone Serverless (Hyper-dimensional embedding vectors)
