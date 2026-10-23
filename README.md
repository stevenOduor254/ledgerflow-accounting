# 💼 LedgerFlow Pro

> **Practice Accounting, Audit Review & Financial Reporting Platform**

LedgerFlow Pro is a modern, interactive financial workspace built with **Python** and **Streamlit**. Designed specifically for accounting practices, auditors, and financial managers, it enables seamless review of transaction ledgers, bank reconciliation, Profit & Loss statement generation, and automated audit checks—all within a sleek, executive-grade interface.

---

## ✨ Features

- **📊 Financial Analytics Dashboard:** Real-time visual tracking of monthly cash flows (income vs. expenses) and expense breakdown by category powered by Plotly.
- **📄 Profit & Loss Statement (P&L):** Categorized operating income and expense summaries with profit margins and estimated VAT/Tax calculation options. Export formal P&L reports directly to CSV.
- **🏦 Bank Reconciliation Status:** Instantly filter and audit unreconciled transactions and view variance metrics.
- **📑 Ledger Register & Automated Audit Flags:** Searchable register with automated rule checks detecting duplicate reference numbers and incomplete data entries.
- **✏️ Manual Adjusting Journals:** Post session-level manual journal entries to instantly adjust reporting figures without modifying raw datasets.
- **🎨 Modern Dark UI:** Built with a high-contrast **Midnight Slate** theme (`Plus Jakarta Sans` font & custom CSS) designed for long work sessions without eye strain.

---

## 🛠️ Project Structure

```text
.
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── data/
│   └── sample_transactions.csv # Optional sample transaction ledger
└── README.md                   # Project documentation
```

---

## 🚀 Quick Start

### 1. Prerequisites

Ensure you have **Python 3.9+** installed on your system.

### 2. Clone the Repository

```bash
git clone https://github.com/your-username/ledgerflow-accounting.git
cd ledgerflow-accounting
```

### 3. Set Up a Virtual Environment (Recommended)

```bash
# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 4. Install Dependencies

Create a `requirements.txt` file (or install directly) with the following packages:

```bash
pip install streamlit pandas numpy plotly
```

### 5. Run the Application

```bash
streamlit run app.py
```

The app will automatically launch in your browser at `http://localhost:8501`.

---

## 📋 CSV Data Format Schema

If uploading your own client ledger CSV file, ensure your file includes the following header fields:

| Column Name   | Type    | Description                                             | Example                    |
| :------------ | :------ | :------------------------------------------------------ | :------------------------- |
| `date`        | Date    | Date of transaction (`YYYY-MM-DD` or standard formats)  | `2026-01-15`               |
| `reference`   | String  | Invoice ID, receipt reference, or journal entry number  | `INV-2026-1002`            |
| `description` | String  | Details or narrative for the entry                      | `Client Retainer Payment`  |
| `category`    | String  | Chart of Accounts category                              | `Consulting Services`      |
| `type`        | String  | Must be either `income` or `expense`                    | `income`                   |
| `amount`      | Float   | Non-negative monetary amount                            | `4500.00`                  |
| `reconciled`  | Boolean | *(Optional)* Reconciliation flag (`TRUE` or `FALSE`)   | `TRUE`                     |

*Note: If `reconciled` is omitted, records default to `TRUE`.*

---

## 📊 Usage Guide

1. **Client & Data Setup (Sidebar):**
   - Choose an active client workspace and currency symbol (`KES`, `USD`, `EUR`, `GBP`).
   - Select between the built-in sample data generator or upload a custom CSV file.
   - Adjust reporting date filters or tax rates as needed.

2. **Analyzing Financial Statements:**
   - Navigate across the workspace tabs to inspect cash flow trends, audit reconciliation variances, and review automated integrity checks.
   - Use the **Manual Journal Entry** tab to temporarily adjust numbers during working review.
   - Click **Download Formal P&L Report** or **Export Filtered Ledger** to export formatted CSVs for client presentation.

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to enhance features or add chart customizability.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.
