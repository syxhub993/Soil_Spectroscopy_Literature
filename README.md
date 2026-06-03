# Soil Spectroscopy Literature Workspace

This repository is a research workspace for literature review on:

- Soil Spectroscopy
- Hyperspectral Remote Sensing
- Deep Learning
- Soil Property Prediction

The goal is to keep Zotero as the formal reference manager and use this repository as the research-output workspace for reading plans, paper summaries, research maps, and reproducibility notes.

## Repository Structure

```text
literature/
  papers/
  notes/
  summaries/
  reading_plan/
  research_map/
zotero_setup/
  setup_zotero_collections.py
  .env.example
README.md
requirements.txt
.gitignore
.gitattributes
```

## Main Folders

- `literature/`: Local research workspace for notes, reading plans, paper summaries, and research maps.
- `literature/summaries/`: Structured paper-reading templates and future paper summaries.
- `literature/reading_plan/`: Weekly and staged reading plans.
- `literature/research_map/`: Research trees, topic maps, and gap analysis.
- `zotero_setup/`: Script for creating the Zotero collection hierarchy.

## Zotero Workflow

Zotero is used to manage paper records, PDFs, metadata, citations, and tags.

This repository is used to manage research thinking and outputs:

1. Add candidate papers to Zotero collection `99_To_Read`.
2. Classify and tag papers in Zotero after screening.
3. Write structured summaries in `literature/summaries/`.
4. Record research ideas and questions in `literature/notes/`.
5. Put reproducible papers in Zotero collection `12_Reproducible_Papers`.
6. Put gap-related papers in Zotero collection `13_Possible_Research_Gaps`.

## Zotero Setup Script

The Zotero setup script is located at:

```bash
zotero_setup/setup_zotero_collections.py
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a local `.env` file from `zotero_setup/.env.example`:

```env
ZOTERO_API_KEY=your_zotero_api_key_here
ZOTERO_USER_ID=your_zotero_user_id_here
ZOTERO_LIBRARY_TYPE=user
```

Run the script from the repository root:

```bash
python zotero_setup/setup_zotero_collections.py
```

The script checks existing collections first. Existing collections and README notes are skipped.

## Security

- Do not commit `.env`.
- Do not store Zotero API keys in code or Markdown files.
- Use a Zotero API key with only the permissions required for this task.
- The `.gitignore` file excludes `.env`, Python cache files, and editor metadata.

## License

No license has been selected yet.
