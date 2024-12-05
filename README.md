# Payment Verification Script

This script automates the process of verifying payment screenshots by extracting text from the images and comparing it with user-entered IDs (UTR numbers). It supports downloading Google Drive-hosted payment screenshots and performs text recognition using `easyocr`.

## Features
- Downloads payment screenshots from Google Drive or direct URLs.
- Extracts text from images using Optical Character Recognition (OCR).
- Matches extracted text with the entered IDs (UTR numbers).
- Generates a verification report in Excel format.

## Prerequisites
- Python 3.8 or higher
- Install the following Python packages:
  - `pandas`
  - `easyocr`
  - `requests`
  - `pillow`
  - `openpyxl`

You can install these packages using:
```bash
pip install pandas easyocr requests pillow openpyxl
```

## How to Use
1. Prepare an Excel file named `verify.xlsx` with the following columns:
   - `payment_screenshot`: Links to the payment screenshots (Google Drive or other URLs).
   - `entered_id`: User-entered IDs (UTR numbers) to verify against the screenshots.

2. Run the script:
   ```bash
   python verfication.py
   ```

3. Once the script finishes, the verification results will be saved in `verification_results.xlsx`.

## Output
- The generated Excel file (`verification_results.xlsx`) will have the following columns:
  - `Links`: Original screenshot URLs.
  - `Entered UTR No`: User-entered IDs.
  - `Result`: The verification result (`Matched`, `Not Matched`, or error details).

## Notes
- For Google Drive links, ensure the links are in the **view format** (`https://drive.google.com/file/d/<file_id>/view`).
- The script will convert these links to direct download links automatically.

## Troubleshooting
- If the script fails to download a file, ensure the link is accessible and permissions are correct.
- If `easyocr` outputs an error, ensure your system meets its prerequisites (e.g., PyTorch compatibility).