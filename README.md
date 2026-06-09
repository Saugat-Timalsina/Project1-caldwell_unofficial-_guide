# The Unofficial Guide to Caldwell CS

## Domain

This project is a Retrieval-Augmented Generation system for the unofficial guide to Computer Science professors and Computer Science courses at Caldwell University.

The domain focuses on student-centered knowledge such as professor feedback, course difficulty, lecture style, workload, grading style, and official CS pathways. This knowledge is valuable because official university pages explain programs and requirements, but they do not always explain what students actually experience in classes. Student review information is scattered across professor review pages and informal sources, so this project makes that information searchable through a grounded question-answering system.

## Document Sources

The system uses 10 source documents stored in `data/raw/`.

1. `rmp_arnold_toffler.txt` — Rate My Professors page for Arnold Toffler at Caldwell University.
2. `rmp_vladislav_veksler.txt` — Rate My Professors page for Vladislav Veksler at Caldwell University.
3. `rmp_isaac_damoah.txt` — Rate My Professors page for Isaac Damoah at Caldwell University.
4. `rmp_adriana_wise.txt` — Rate My Professors page for Adriana Wise at Caldwell University.
5. `rmp_lowell_qually.txt` — Rate My Professors page for Lowell Qually at Caldwell University.
6. `rmp_caldwell_cs_department.txt` — Rate My Professors Computer Science department page for Caldwell University.
7. `caldwell_cs_program.txt` — Caldwell University Computer Science program page.
8. `caldwell_cs_department.txt` — Caldwell University Computer Science and Information Systems department page.
9. `caldwell_cs_faculty.txt` — Caldwell University faculty/staff page for the School of Business and Computer Science.
10. `caldwell_cs_four_year_plan.txt` — Caldwell University Computer Science suggested four-year major plan/course planning document.

## Document Pipeline

The pipeline loads plain `.txt` files from `data/raw/`. Each document includes a source name, source type, URL or description, and content. The ingestion script reads each file, removes extra whitespace and repeated blank lines, and returns structured documents with source metadata.

The document pipeline is implemented in:

* `populate_raw_docs.py`
* `ingest.py`
* `chunk.py`
* `embed.py`
* `retrieve.py`
* `generate.py`
* `query.py`
* `app.py`

## Chunking Strategy

The system uses chunks of approximately 700 characters with 100 characters of overlap.

I chose this strategy because the documents are mostly short student review summaries, professor notes, and official course descriptions. A 700-character chunk is large enough to keep a complete professor/course idea together, such as teaching style, feedback quality, difficulty, or course list. The 100-character overlap helps prevent important information from being split across chunk boundaries.

If the chunks were too small, retrieval might return fragments that do not make sense alone. If the chunks were too large, one chunk might contain too many unrelated facts, which could make retrieval less precise.

## Sample Chunks

### Sample Chunk 1

Source: `rmp_vladislav_veksler.txt`

Vladislav Veksler is listed as a Computer Science professor at Caldwell University. The Rate My Professors Computer Science department page lists Vladislav Veksler with a quality rating of 5.0 based on 4 ratings, 100% would take again, and a 1.3 level of difficulty. Student review notes are very positive. Review themes include amazing lectures, being accessible outside class, giving good feedback, being inspirational, and using group projects.

### Sample Chunk 2

Source: `rmp_arnold_toffler.txt`

Arnold Toffler is listed as a Computer Science professor at Caldwell University. The Rate My Professors Computer Science department page lists Arnold Toffler with a quality rating of 3.5 based on 30 ratings, 60% would take again, and a 2.7 level of difficulty. Student review notes suggest mixed experiences. Some students describe his classes as lecture-heavy, test-heavy, or based heavily on slides.

### Sample Chunk 3

Source: `rmp_adriana_wise.txt`

Adriana Wise is listed on Rate My Professors for Caldwell University. The visible review notes are negative. A student describes the class as difficult and says the professor read from a document for much of the semester. The review says homework due dates were unclear and exams were very difficult.

### Sample Chunk 4

Source: `caldwell_cs_program.txt`

Caldwell University's Bachelor of Science in Computer Science prepares students for a technology career with a strong foundation in computer programming and focused electives. Important courses listed include CS 195 Computer Programming I, CS 196 Computer Programming II, CS 225 Introduction to Operating Systems, CS 340 Introduction to Data Science, and CS 420 Artificial Intelligence.

### Sample Chunk 5

Source: `caldwell_cs_department.txt`

The Computer Science and Information Systems Department at Caldwell University equips students with skills, competencies, and mindsets needed to succeed in technology. The department lists majors and minors including Computer Science, Computer Information Systems, Business Analytics, Management Information Systems, and Human-Computer Interaction.

## Embedding Model

The system uses `all-MiniLM-L6-v2` from the `sentence-transformers` library.

I chose this model because it runs locally, is free, does not require API credits, and is fast enough for a small course project. For a production deployment, I would consider tradeoffs such as embedding accuracy, cost, latency, context length, multilingual support, privacy, and whether a local or API-based embedding model would be better for informal student language.

## Vector Store

The system uses ChromaDB as the vector store. Each chunk is stored with:

* chunk text
* source document name
* chunk index
* embedding vector

## Retrieval Test Results

### Retrieval Test 1

Query: Which professor gives good feedback?

Top returned chunks included:

* `rmp_arnold_toffler.txt`
* `rmp_vladislav_veksler.txt`
* `rmp_isaac_damoah.txt`
* `rmp_lowell_qually.txt`

These chunks are relevant because they contain review themes about professors giving good feedback, being accessible, helping students, or helping students understand the material.

### Retrieval Test 2

Query: Which professor seems difficult?

Top returned chunks included:

* `rmp_adriana_wise.txt`
* `rmp_arnold_toffler.txt`

These chunks are relevant because they mention difficult exams, unclear homework due dates, lecture-heavy style, test-heavy classes, and mixed student experiences.

### Retrieval Test 3

Query: What CS courses does Caldwell offer?

Top returned chunks included:

* `caldwell_cs_program.txt`
* `caldwell_cs_department.txt`
* `caldwell_cs_four_year_plan.txt`

These chunks are relevant because they list official CS courses, CS pathways, and major planning information.

## Grounded Generation

Grounded generation is enforced through the system prompt in `generate.py`.

The prompt instructs the model to answer only using the retrieved context and not use outside knowledge. If the retrieved context does not contain enough information, the model must say:

> I don't have enough information in the collected documents to answer that.

The system also returns source document names and chunk numbers so the answer can be traced back to retrieved evidence.

## Example Responses

### Example Response 1

Question: Which professor gives good feedback?

System response:

According to the retrieved context from `rmp_arnold_toffler.txt` and `rmp_vladislav_veksler.txt`, two professors are mentioned as giving good feedback: Arnold Toffler and Vladislav Veksler.

Sources:

* `rmp_arnold_toffler.txt chunk 1`
* `rmp_vladislav_veksler.txt chunk 0`

### Example Response 2

Question: What CS courses does Caldwell offer?

System response:

The retrieved Caldwell documents list several CS courses, including CS 195 Computer Programming I, CS 196 Computer Programming II, CS 225 Introduction to Operating Systems, CS 230 Front-End Web Development, CS 340 Introduction to Data Science, CS 420 Artificial Intelligence, CS 487 Field Internship I, and CS 491 Undergraduate Research I.

Sources:

* `caldwell_cs_program.txt chunk 0`
* `caldwell_cs_four_year_plan.txt chunk 0`

### Out-of-Scope Example

Question: What is the tuition cost at Caldwell University?

System response:

I don't have enough information in the collected documents to answer that.

Sources retrieved:

* `caldwell_cs_program.txt chunk 0`
* `caldwell_cs_faculty.txt chunk 0`
* `caldwell_cs_department.txt chunk 0`
* `caldwell_cs_four_year_plan.txt chunk 0`

## Query Interface

The project uses a Gradio web interface in `app.py`.

Input field:

* User question

Output fields:

* Answer
* Retrieved sources

Sample interaction:

User question:

Which professor gives good feedback?

System answer:

According to the retrieved context, Arnold Toffler and Vladislav Veksler are mentioned as giving good feedback.

Retrieved sources:

* `rmp_arnold_toffler.txt chunk 1`
* `rmp_vladislav_veksler.txt chunk 0`

## Evaluation Report

| # | Question                                         | Expected Answer                                                                                                                                          | System Response                                                                                     | Accuracy |
| - | ------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | -------- |
| 1 | Which professor gives good feedback?             | The system should mention professors whose documents say they give good feedback, such as Vladislav Veksler, Arnold Toffler, or Isaac Damoah.            | The system mentioned Arnold Toffler and Vladislav Veksler as professors connected to good feedback. | Accurate |
| 2 | Which professor seems difficult?                 | The system should mention Adriana Wise or Arnold Toffler because those documents mention difficult exams, test-heavy classes, or lecture-heavy teaching. | The system identified professor difficulty based on retrieved student review chunks.                | Accurate |
| 3 | What CS courses does Caldwell offer?             | The system should list courses such as CS 195, CS 196, CS 225, CS 230, CS 340, CS 420, internship, and research.                                         | The system returned Caldwell CS course information from official Caldwell documents.                | Accurate |
| 4 | What do students say about Adriana Wise?         | The system should mention difficult exams, unclear homework due dates, lecture-heavy style, lots of homework, and attendance.                            | The system summarized negative review themes about Adriana Wise from the document.                  | Accurate |
| 5 | What is the tuition cost at Caldwell University? | The system should refuse because tuition information is outside the collected CS professor/course documents.                                             | I don't have enough information in the collected documents to answer that.                          | Accurate |

## Failure Case

One important failure/out-of-scope case was the query:

What is the tuition cost at Caldwell University?

The expected behavior was a refusal because the project documents only contain information about Caldwell CS professors, CS courses, department pathways, and student review notes. The system correctly refused to answer, but the retrieved sources still included official Caldwell CS program and department chunks because those were the closest semantic matches to the word “Caldwell.”

Cause:

The retrieval system always returns the top 4 chunks, even when none of them truly answer the question. The generation prompt prevented hallucination by refusing to answer, but the retrieval stage still returned weakly related Caldwell documents.

Future fix:

I would add a distance threshold so the system refuses earlier when retrieved chunks are not relevant enough.

## Spec Reflection

One way the spec helped was by forcing me to plan the domain, documents, chunking strategy, retrieval approach, and evaluation questions before building the system. This made the pipeline easier to implement because I knew what each stage needed to produce.

One way my implementation diverged from the original plan was that I used clean manually prepared text files instead of live web scraping. I made this choice because professor review pages and university pages can be inconsistent to scrape, and using controlled `.txt` documents made the project more reliable and easier to evaluate.

## AI Usage Transparency

I used AI tools as a coding and debugging assistant, but I reviewed and tested the output myself.

First, I used ChatGPT to help create the ingestion and chunking scripts. I directed it to load `.txt` documents from `data/raw/`, clean whitespace, and create chunks using my planned chunk size and overlap. I reviewed the code and tested it using `python ingest.py` and `python chunk.py`.

Second, I used ChatGPT to help implement the retrieval and generation pipeline. I directed it to use `all-MiniLM-L6-v2`, ChromaDB, Groq, and a grounded prompt that refuses out-of-scope questions. I tested retrieval separately before generation and confirmed that the system returned source documents and chunk numbers.

Third, I used ChatGPT to debug errors such as missing Python packages, missing `ask()` function in `query.py`, and Gradio import issues. I did not simply accept the code blindly; I ran each stage and corrected errors based on the actual terminal output.

## How to Run

Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Populate documents:

```bash
python populate_raw_docs.py
```

Build vector store:

```bash
python embed.py
```

Run retrieval test:

```bash
python retrieve.py
```

Run generation test:

```bash
python generate.py
```

Run app:

```bash
python app.py
```

Then open:

```text
http://127.0.0.1:7860
```
