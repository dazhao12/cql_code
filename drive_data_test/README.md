# Google Drive data test

This is a minimal test for the workflow:

- keep code in Git/GitHub
- keep working data in Google Drive
- download or export the Drive data as CSV at runtime
- run the analysis script against the downloaded CSV

Example:

```bash
python3 analyze_drive_csv.py from_google_drive.csv
```

`from_google_drive.csv` is ignored by Git because it is runtime data.
