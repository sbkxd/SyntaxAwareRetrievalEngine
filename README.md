# Syntax-Aware Semantic Retrieval Engine for Cross-Domain Sports Rulebooks

> A syntax-aware semantic retrieval and Retrieval-Augmented Generation (RAG) framework for contextual gameplay rule interpretation across traditional sports and esports domains.

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge\&logo=python)
![spaCy](https://img.shields.io/badge/spaCy-en__core__web__sm-green?style=for-the-badge\&logo=spacy)
![FAISS](https://img.shields.io/badge/FAISS-Vector_Search-orange?style=for-the-badge)
![Gemini](https://img.shields.io/badge/Gemini-2.5_Flash-purple?style=for-the-badge\&logo=google)
![Google Colab](https://img.shields.io/badge/Google_Colab-Notebook-yellow?style=for-the-badge\&logo=googlecolab)

---

# Abstract

This project presents a syntax-aware semantic retrieval and Retrieval-Augmented Generation (RAG) framework for gameplay rule interpretation across multiple sports and esports domains. The system combines linguistic query analysis, sparse lexical retrieval, dense semantic retrieval, vector similarity search, hybrid retrieval fusion, explainable retrieval reasoning, and Gemini-based answer generation into a unified semantic retrieval architecture.

The primary challenge addressed by the project is cross-domain gameplay ambiguity, where procedural terms such as *spike*, *timeout*, *zone*, *block*, and *round* possess entirely different semantic meanings across sports and esports rulebooks. The proposed framework improves contextual retrieval robustness through domain-aware routing, syntax-aware query decomposition, semantic vector retrieval, and explainable RAG grounding.

---

# Project Motivation

Cross-domain sports and esports rulebooks contain highly ambiguous gameplay terminology. Traditional keyword-based retrieval systems frequently fail because identical procedural terms may represent completely unrelated gameplay concepts across domains.

The project addresses this ambiguity problem by combining syntax-aware linguistic analysis, semantic embeddings, domain-aware routing, and hybrid retrieval fusion.

## Cross-Domain Ambiguity Examples

| Ambiguous Term | Football               | Cricket              | Pickleball      | Valorant            | BGMI              |
| -------------- | ---------------------- | -------------------- | --------------- | ------------------- | ----------------- |
| Spike          | Shoe studs             | Fast delivery impact | Ball strike     | Bomb device         | Damage spike      |
| Zone           | Defensive region       | Field placement      | Non-volley zone | Smoke/control zone  | Safe/play zone    |
| Timeout        | Match pause            | Strategic break      | Match pause     | Tactical timeout    | Technical timeout |
| Round          | Tournament round       | Over sequence        | Rally cycle     | Match round         | Survival round    |
| Block          | Defensive interception | Shot prevention      | Net block       | Utility obstruction | Map obstruction   |

---

# System Architecture

```text
Rulebook PDFs
      │
      ▼
PDF Extraction (PyMuPDF)
      │
      ▼
Metadata Construction
(domain, source_file, page_number)
      │
      ▼
Exploratory Dataset Analysis
      │
      ▼
Text Preprocessing Pipeline
 ├── Basic Cleaning
 ├── Symbol Normalisation
 ├── Tokenisation
 ├── Stopword Removal
 └── Lemmatisation
      │
      ▼
Syntax-Aware Linguistic Analysis
 ├── Noun Extraction
 ├── Verb Extraction
 ├── Modal Verb Detection
 └── Query Refinement
      │
      ▼
Retrieval Preparation
 ├── TF-IDF Text
 └── Embedding Text
      │
      ▼
Chunking Pipeline
(150-word Sliding Window)
      │
      ▼
Domain-Aware Retrieval Routing
      │
      ▼
Sparse TF-IDF Retrieval
      │
      ▼
Dense Semantic Retrieval (GloVe)
      │
      ▼
FAISS Vector Search
      │
      ▼
Hybrid Retrieval Fusion
      │
      ▼
Explainable Retrieval Layer
      │
      ▼
RAG Context Construction
      │
      ▼
Gemini 2.5 Flash
      │
      ▼
Grounded Gameplay Answer Generation
      │
      ▼
Evaluation & Comparative Analysis
```

---

# Tech Stack

| Tool / Library | Version / Model         | Purpose                                    |
| -------------- | ----------------------- | ------------------------------------------ |
| Python         | 3.10                    | Core programming language                  |
| PyMuPDF (fitz) | Latest                  | PDF text extraction                        |
| NLTK           | Latest                  | Tokenisation, stopwords, lemmatisation     |
| spaCy          | en_core_web_sm          | Linguistic analysis and POS tagging        |
| gensim         | glove-wiki-gigaword-100 | Dense semantic embeddings                  |
| scikit-learn   | Latest                  | TF-IDF vectorisation and cosine similarity |
| FAISS          | IndexFlatL2             | Vector similarity search                   |
| Gemini         | gemini-2.5-flash        | Retrieval-Augmented Generation             |
| pandas         | Latest                  | Data handling                              |
| matplotlib     | Latest                  | Dataset visualisation                      |
| openpyxl       | Latest                  | Excel result export                        |
| Google Colab   | Cloud Environment       | Notebook execution                         |

---

# Repository Structure

```text
SyntaxAwareRetrievalEngine/
│
├── app/
│   ├── data/
│   │   └── raw_rulebooks/
│   │
│   └── outputs/
│       └── exported_reports/
│
├── notebooks/
│   └── BhanuKarthik_NLP_CourseProject.ipynb
│
├── src/
│   ├── preprocessing/
│   ├── chunking/
│   ├── retrieval/
│   ├── embeddings/
│   ├── explainability/
│   ├── rag/
│   ├── evaluation/
│   └── utils/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# Local Project Paths

| Component                   | Local Path                                                            |
| --------------------------- | --------------------------------------------------------------------- |
| Notebook Directory          | `E:\Projects\SyntaxAwareRetrievalEngine\notebooks`                    |
| Rulebook Dataset Directory  | `E:\Projects\SyntaxAwareRetrievalEngine\app\data\raw_rulebooks`       |
| Exported Evaluation Reports | `E:\Projects\SyntaxAwareRetrievalEngine\app\outputs\exported_reports` |

---

# Prerequisites

## Python Version

```text
Python 3.10
```

---

## Install Required Packages

```bash
pip install -r requirements.txt
```

---

## NLTK Downloads

```python
import nltk

nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("averaged_perceptron_tagger")
```

---

## spaCy Model Download

```bash
python -m spacy download en_core_web_sm
```

---

## GloVe Embedding Download

The notebook automatically downloads:

```text
glove-wiki-gigaword-100
```

through:

```python
gensim.downloader.load()
```

---

## Gemini API Key Requirement

A valid Gemini API key is required for the RAG pipeline.

```python
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")
```

---

# Setup and Running Instructions

## 1. Clone Repository

```bash
git clone https://github.com/your-username/SyntaxAwareRetrievalEngine.git

cd SyntaxAwareRetrievalEngine
```

---

## 2. Open Google Colab

Upload:

```text
BhanuKarthik_NLP_CourseProject.ipynb
```

from:

```text
E:\Projects\SyntaxAwareRetrievalEngine\notebooks
```

---

## 3. Upload Rulebook PDFs

Upload all rulebook PDFs from:

```text
E:\Projects\SyntaxAwareRetrievalEngine\app\data\raw_rulebooks
```

into the Colab runtime environment.

---

## 4. Configure DATASET_PATH

```python
DATASET_PATH = "/content/Dataset"
```

---

## 5. Install Dependencies

```python
!pip install pymupdf
!pip install gensim
!pip install faiss-cpu
!pip install spacy
!pip install openpyxl
```

---

## 6. Download spaCy Model

```python
!python -m spacy download en_core_web_sm
```

---

## 7. Configure Gemini API Key

```python
genai.configure(api_key="YOUR_API_KEY")
```

---

## 8. Run Notebook Sequentially

Execute all notebook cells sequentially from:

```text
Section 1 → Section 16
```

---

# Domain Hint Configuration

The retrieval system uses keyword-based domain routing through a DOMAIN_HINTS dictionary.

```python
DOMAIN_HINTS = {

    "Valorant": [
        "spike",
        "agent",
        "round",
        "tactical",
        "timeout"
    ],

    "Cricket": [
        "bowler",
        "innings",
        "wicket",
        "over",
        "delivery"
    ]
}
```

## Extending to New Domains

To add a new domain:

1. Add the domain PDF rulebooks
2. Create a new domain entry in `DOMAIN_HINTS`
3. Add gameplay-specific procedural keywords
4. Rebuild embeddings and retrieval indexes

---

# Retrieval Systems Explained

## TF-IDF Retrieval

TF-IDF retrieval uses sparse lexical matching through `TfidfVectorizer` with unigram and bigram representations. It performs strongly for explicit procedural terminology and exact keyword overlap but struggles with semantic paraphrasing and contextual ambiguity.

---

## Dense Semantic Retrieval (GloVe)

Dense retrieval converts gameplay chunks and queries into averaged GloVe word embeddings. Cosine similarity search enables contextual semantic matching and paraphrase handling, improving retrieval robustness for ambiguity-heavy gameplay queries.

---

## FAISS Vector Search

FAISS performs efficient vector similarity search using `IndexFlatL2`. Chunk embeddings are indexed as float32 vectors, enabling scalable nearest-neighbour semantic retrieval across gameplay rulebook chunks.

---

## Hybrid Retrieval

Hybrid retrieval combines sparse TF-IDF scores and dense semantic similarity scores through weighted score fusion. This approach balances lexical precision with semantic contextual understanding and serves as the primary retrieval architecture used by the downstream RAG pipeline.

---

# Evaluation Results

| Retrieval System | Domain Accuracy | Top-1 Accuracy | Top-K Accuracy | MRR  |
| ---------------- | --------------- | -------------- | -------------- | ---- |
| TF-IDF Retrieval | 50.0%           | 50.0%          | 50.0%          | 0.50 |
| Dense Retrieval  | 50.0%           | 50.0%          | 50.0%          | 0.50 |
| FAISS Retrieval  | 70.0%           | 60.0%          | 60.0%          | 0.60 |
| Hybrid Retrieval | 50.0%           | 50.0%          | 50.0%          | 0.50 |

> Detailed evaluation outputs are available inside the exported Excel workbooks located in:

```text
E:\Projects\SyntaxAwareRetrievalEngine\app\outputs\exported_reports
```

---

# Output Files

## 1. explainable_retrieval_results.xlsx

Contains:

* query
* predicted_domain
* sparse_score
* dense_score
* hybrid_score
* retrieved_chunk
* source_file
* page_number

---

## 2. rag_evaluation_results.xlsx

Contains:

* query
* predicted_domain
* retrieved_context
* generated_answer
* source metadata
* retrieval scores

---

## 3. complete_evaluation_results.xlsx

Multi-sheet workbook containing:

* TF-IDF evaluation results
* Dense retrieval results
* FAISS retrieval results
* Hybrid retrieval results
* Comparative metric tables

---

# Ambiguity Test Queries

| Query                                                                                     | Expected Domain |
| ----------------------------------------------------------------------------------------- | --------------- |
| What happens if coach communication is interrupted during a tactical timeout in Valorant? | Valorant        |
| What is the maximum number of overs a bowler may bowl in an innings?                      | Cricket         |
| What are the penalties for entering the field without referee permission?                 | Football        |
| Can players block or attempt to block an opponent's serve?                                | Pickleball      |
| Under what conditions can a BGMI match be replayed after technical failure?               | BGMI            |

---

# Known Limitations

* Sparse retrieval remains sensitive to procedural wording variation.
* Dense semantic retrieval occasionally retrieves broader contextual chunks.
* Hybrid retrieval performance depends on score balancing quality.
* Fragmented gameplay rules across multiple chunks reduce retrieval completeness.
* RAG output quality remains dependent on retrieval grounding quality.
* Single-term ambiguous queries occasionally affect domain routing accuracy.

---

# Future Improvements

* Sentence-BERT embeddings
* Cross-encoder reranking
* Pinecone / Weaviate vector databases
* Transformer-based rerankers
* Multilingual gameplay rule support
* Real-time rulebook updates
* Multi-hop retrieval reasoning
* Agentic retrieval workflows
* Streamlit deployment interface

---

# Author

**S Bhanu Karthik**
