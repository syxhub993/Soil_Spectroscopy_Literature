# Zotero Setup

This folder contains the script used to create the Zotero collection structure for the soil hyperspectral deep learning literature project.

## Required Environment Variables

Create a local `.env` file in the repository root:

```env
ZOTERO_API_KEY=your_zotero_api_key_here
ZOTERO_USER_ID=your_zotero_user_id_here
ZOTERO_LIBRARY_TYPE=user
```

The API key must have Zotero library write permission.

## Run

From the repository root:

```bash
python zotero_setup/setup_zotero_collections.py
```

The script creates missing collections and README notes. Existing collections and notes are skipped.
