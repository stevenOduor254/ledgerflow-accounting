from datetime import datetime, date
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------
st.set_page_config(
    page_title="LedgerFlow Pro | Practice Accounting Platform",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded",
)

DATA_DIR = Path(__file__).parent / "data"

# ---------------------------------------------------------
# DESIGN SYSTEM & STYLING (PROFESSIONAL MIDNIGHT SLATE)
# ---------------------------------------------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@500;600&display=swap');

    :root {
        --primary: #6366f1;
        --primary-dark: #4f46e5;
        --primary-light: #1e2235;
        --primary-subtle: #161b2e;
        --page: #0b0f17;
        --surface: #141c2e;
        --surface-hover: #1a243d;
        --ink: #f8fafc;
        --muted: #94a3b8;
        --line: #1e293b;
        --accent-blue: #3b82f6;
        --accent-emerald: #10b981;
        --accent-amber: #f59e0b;
        --accent-rose: #f43f5e;
    }

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    .stApp {
        background: var(--page);
        color: var(--ink);
    }

    [data-testid="stHeader"] {
        background: rgba(11, 15, 23, 0.85);
        backdrop-filter: blur(12px);
    }

    [data-testid="stSidebar"] {
        background: var(--surface);
        border-right: 1px solid var(--line);
    }

    [data-testid="stSidebar"] > div:first-child {
        padding-top: 1.2rem;
    }

    /* Brand Header */
    .brand {
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 0 0 1.2rem 0;
        border-bottom: 1px solid var(--line);
        margin-bottom: 1.2rem;
    }

    .brand-mark {
        width: 42px;
        height: 42px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 10px;
        color: white;
        background: linear-gradient(135deg, #6366f1 0%, #312e81 100%);
        font-size: 19px;
        font-weight: 700;
        box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
    }

    .brand-name {
        font-size: 18px;
        font-weight: 700;
        letter-spacing: -0.5px;
        color: var(--ink);
        line-height: 1.2;
    }

    .brand-caption {
        color: var(--muted);
        font-size: 11px;
        font-weight: 500;
    }

    /* Top Page Header */
    .page-heading {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin: 0.2rem 0 1.4rem 0;
        padding-bottom: 1rem;
        border-bottom: 1px solid var(--line);
    }

    .eyebrow {
        color: #818cf8;
        text-transform: uppercase;
        letter-spacing: 1.4px;
        font-size: 11px;
        font-weight: 700;
        margin-bottom: 4px;
    }

    .page-title {
        font-size: 28px;
        font-weight: 700;
        letter-spacing: -1px;
        color: var(--ink);
        margin: 0;
    }

    .page-subtitle {
        color: var(--muted);
        font-size: 13px;
        margin-top: 4px;
    }

    .client-badge {
        background: var(--primary-subtle);
        color: #a5b4fc;
        padding: 6px 14px;
        border-radius: 20px;
        font-weight: 600;
        font-size: 12px;
        border: 1px solid rgba(99, 102, 241, 0.3);
    }

    /* Metric Cards */
    [data-testid="stMetric"] {
        background: var(--surface);
        border: 1px solid var(--line);
        border-radius: 12px;
        padding: 16px 18px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2), 0 2px 4px -1px rgba(0, 0, 0, 0.1);
        transition: transform 150ms ease, border-color 150ms ease, box-shadow 150ms ease;
    }

    [data-testid="stMetric"]:hover {
        border-color: var(--primary);
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(99, 102, 241, 0.15);
    }

    [data-testid="stMetricLabel"] p {
        font-size: 11px !important;
        color: var(--muted) !important;
        font-weight: 600 !important;
        text-transform: uppercase;
        letter-spacing: 0.6px;
    }

    [data-testid="stMetricValue"] {
        font-family: 'JetBrains Mono', monospace;
        font-size: 21px !important;
        font-weight: 700;
        color: var(--ink);
    }

    /* Custom Sections */
    .section-heading {
        font-size: 16px;
        font-weight: 700;
        letter-spacing: -0.3px;
        color: var(--ink);
        margin: 0 0 2px 0;
    }

    .section-caption {
        font-size: 12px;
        color: var(--muted);
        margin-bottom: 0.8rem;
    }

    /* Buttons */
    .stButton > button, .stDownloadButton > button {
        background: var(--primary);
        color: white;
        border: none;
        border-radius: 8px;
        font-weight: 600;
        font-size: 13px;
        padding: 0.5rem 1rem;
        transition: all 150ms ease;
    }

    .stButton > button:hover, .stDownloadButton > button:hover {
        background: var(--primary-dark);
        color: white;
        box-shadow: 0 4px 12px rgba(99, 102, 241, 0.35);
    }

    /* Tabs Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        border-bottom: 1px solid var(--line);
        padding-bottom: 4px;
    }

    .stTabs [data-baseweb="tab"] {
        height: 38px;
        border-radius: 6px;
        padding: 0 16px;
        font-weight: 600;
        font-size: 13px;
        color: var(--muted);
        background-color: transparent;
    }

    .stTabs [aria-selected="true"] {
        background-color: var(--primary-subtle) !important;
        color: #a5b4fc !important;
        border: 1px solid rgba(99, 102, 241, 0.2);
    }

    .footer {
        border-top: 1px solid var(--line);
        margin-top: 3rem;
        padding: 1.2rem 0;
        color: var(--muted);
        font-size: 12px;
        display: flex;
        justify-content: space-between;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# HELPER FUNCTIONS & MOCK DATA GENERATOR
# ---------------------------------------------------------
def generate_sample_data():
    """Generates fallback audit-ready financial transactions if file is missing."""
    dates = pd.date_range(start="2026-01-01", periods=65, freq="D")
    categories_income = ["Client Retainers", "Consulting Services", "Audit Fees", "Tax Advisory"]
    categories_expense = ["Office Rent", "Software Subscriptions", "Staff Payroll", "Utilities", "Travel & Meals", "Legal Fees"]
    
    records = []
    np.random.seed(42)
    
    for i, d in enumerate(dates):
        if np.random.rand() > 0.4:
            records.append({
                "date": d.strftime("%Y-%m-%d"),
                "reference": f"INV-2026-{1000 + i}",
                "description": f"Client Service Payment - #{1000 + i}",
                "category": np.random.choice(categories_income),
                "type": "income",
                "amount": round(float(np.random.uniform(1500, 12000)), 2),
                "reconciled": np.random.choice([True, False], p=[0.85, 0.15])
            })
        if np.random.rand() > 0.3:
            records.append({
                "date": d.strftime("%Y-%m-%d"),
                "reference": f"EXP-2026-{2000 + i}",
                "description": f"Operational Vendor Expense - #{2000 + i}",
                "category": np.random.choice(categories_expense),
                "type": "expense",
                "amount": round(float(np.random.uniform(150, 4500)), 2),
                "reconciled": np.random.choice([True, False], p=[0.9, 0.1])
            })
            
    return pd.DataFrame(records)

def normalise_columns(df):
    """Clean and standardize DataFrame columns."""
    df = df.copy()
    df.columns = [str(column).strip().lower().replace(" ", "_") for column in df.columns]
    return df

def prepare_transactions(df):
    """Validate, clean, and cast data types for accounting precision."""
    required = {"date", "reference", "description", "category", "type", "amount"}
    missing = required - set(df.columns)
    
    if missing:
        raise ValueError(f"Missing required columns: {', '.join(sorted(missing))}")

    df = df.copy()
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    df["type"] = df["type"].astype(str).str.strip().str.lower()
    
    for col in ["reference", "description", "category"]:
        df[col] = df[col].fillna("").astype(str).str.strip()

    if "reconciled" not in df.columns:
        df["reconciled"] = True
    else:
        df["reconciled"] = df["reconciled"].astype(bool)

    valid = (
        df["date"].notna()
        & df["amount"].notna()
        & (df["amount"] >= 0)
        & df["type"].isin(["income", "expense"])
    )

    excluded_count = int((~valid).sum())
    df = df.loc[valid].copy()

    return df, excluded_count

# Initialize Session State for Manual Adjustments
if "manual_journals" not in st.session_state:
    st.session_state.manual_journals = []

# ---------------------------------------------------------
# SIDEBAR: PRACTICE & CLIENT MANAGEMENT
# ---------------------------------------------------------
with st.sidebar:
    st.markdown(
        """
        <div class="brand">
            <div class="brand-mark">LF</div>
            <div>
                <div class="brand-name">LedgerFlow Pro</div>
                <div class="brand-caption">Practice Automation & Review</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("#### Practice Client")
    client_name = st.selectbox(
        "Active Client Engagement",
        ["Apex Logistics Ltd", "Alpha Retailers Kenya", "Horizon Tech Solutions", "Kibo Ventures Inc"],
        index=0
    )

    currency_symbol = st.selectbox(
        "Currency Profile",
        ["KES (KSh)", "USD ($)", "EUR (€)", "GBP (£)"],
        index=0
    ).split(" ")[1].replace("(", "").replace(")", "")

    st.divider()
    st.markdown("#### Data Source")
    source = st.radio(
        "Select transaction source",
        ["Example Ledgers", "Upload CSV"],
        label_visibility="collapsed",
        key="data_source",
    )

    raw_df = None

    if source == "Upload CSV":
        upload = st.file_uploader(
            "Import Client Ledger (CSV)",
            type=["csv"],
            help="CSV must include: date, reference, description, category, type, amount",
        )
        if upload is not None:
            try:
                raw_df = pd.read_csv(upload)
            except Exception as exc:
                st.error(f"Could not read uploaded CSV: {exc}")
                st.stop()
        else:
            st.info("Upload a client CSV file to populate workspace.")
            st.stop()
    else:
        sample_path = DATA_DIR / "sample_transactions.csv"
        if sample_path.exists():
            try:
                raw_df = pd.read_csv(sample_path)
            except Exception:
                raw_df = generate_sample_data()
        else:
            raw_df = generate_sample_data()

# Process Data safely
try:
    raw_df = normalise_columns(raw_df)
    transactions, excluded_rows = prepare_transactions(raw_df)
    
    if st.session_state.manual_journals:
        manual_df = pd.DataFrame(st.session_state.manual_journals)
        manual_df["date"] = pd.to_datetime(manual_df["date"])
        transactions = pd.concat([transactions, manual_df], ignore_index=True)
        
except ValueError as exc:
    st.error(str(exc))
    st.info("Required column schema: `date, reference, description, category, type, amount`")
    st.stop()

if transactions.empty:
    st.error("No valid transactions found in selected dataset.")
    st.stop()

# ---------------------------------------------------------
# SIDEBAR: DATE RANGE & TAX CONTROLS
# ---------------------------------------------------------
with st.sidebar:
    st.divider()
    st.markdown("#### Reporting Period")
    
    min_date = transactions["date"].min().date()
    max_date = transactions["date"].max().date()

    date_range = st.date_input(
        "Filter Period",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date,
    )

    if isinstance(date_range, (tuple, list)) and len(date_range) == 2:
        begin = pd.Timestamp(date_range[0])
        finish = pd.Timestamp(date_range[1]) + pd.Timedelta(days=1) - pd.Timedelta(microseconds=1)
        transactions = transactions[transactions["date"].between(begin, finish)].copy()
    elif isinstance(date_range, (tuple, list)) and len(date_range) == 1:
        transactions = transactions[transactions["date"].dt.date == date_range[0]].copy()

    st.divider()
    st.markdown("#### Tax & Compliance")
    vat_rate = st.slider("Standard VAT / Sales Tax (%)", min_value=0, max_value=30, value=16, step=1)

# ---------------------------------------------------------
# HEADER DISPLAY
# ---------------------------------------------------------
st.markdown(
    f"""
    <div class="page-heading">
        <div>
            <div class="eyebrow">Practice Client Automation Workspace</div>
            <h1 class="page-title">Financial Review & Reporting</h1>
            <div class="page-subtitle">Standardized accounting audit, bank reconciliation, and P&L summaries.</div>
        </div>
        <div>
            <span class="client-badge">Client: {client_name}</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

if excluded_rows > 0:
    st.warning(f"⚠️ **Audit Note:** Excluded {excluded_rows:,} record(s) with invalid timestamps, null amounts, or invalid transaction types.")

# ---------------------------------------------------------
# CORE METRICS COMPUTATION
# ---------------------------------------------------------
total_income = transactions.loc[transactions["type"] == "income", "amount"].sum()
total_expenses = transactions.loc[transactions["type"] == "expense", "amount"].sum()
net_income = total_income - total_expenses
profit_margin = (net_income / total_income * 100) if total_income > 0 else 0.0

vat_output = total_income * (vat_rate / (100 + vat_rate))
vat_input = total_expenses * (vat_rate / (100 + vat_rate))
net_vat_payable = vat_output - vat_input

m1, m2, m3, m4, m5 = st.columns(5)
m1.metric("Gross Revenue", f"{currency_symbol} {total_income:,.2f}")
m2.metric("Total Expenses", f"{currency_symbol} {total_expenses:,.2f}")
m3.metric("Net Income", f"{currency_symbol} {net_income:,.2f}", delta=f"{profit_margin:.1f}% Margin")
m4.metric(f"Net Tax ({vat_rate}%)", f"{currency_symbol} {net_vat_payable:,.2f}")
m5.metric("Total Ledger Entries", f"{len(transactions):,}")

st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# WORKSPACE TABS
# ---------------------------------------------------------
tab_analytics, tab_pl, tab_recon, tab_register, tab_journal = st.tabs([
    "📊 Financial Dashboard", 
    "📄 Profit & Loss Statement", 
    "🏦 Bank Reconciliation", 
    "📑 Transaction Register", 
    "✏️ Manual Journal Entry"
])

# ---------------------------------------------------------
# TAB 1: FINANCIAL DASHBOARD
# ---------------------------------------------------------
with tab_analytics:
    col_left, col_right = st.columns([1.3, 1], gap="medium")

    with col_left:
        st.markdown('<div class="section-heading">Monthly Cash Flow Trend</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-caption">Track monthly operational revenues vs outgoing expenses over time.</div>', unsafe_allow_html=True)

        df_trend = transactions.copy()
        df_trend["period"] = df_trend["date"].dt.to_period("M").dt.to_timestamp()
        trend_summary = df_trend.groupby(["period", "type"])["amount"].sum().reset_index()

        if not trend_summary.empty:
            fig_trend = px.bar(
                trend_summary,
                x="period",
                y="amount",
                color="type",
                barmode="group",
                color_discrete_map={"income": "#6366f1", "expense": "#f43f5e"},
                labels={"amount": f"Amount ({currency_symbol})", "period": "Month", "type": "Type"},
            )
            fig_trend.update_layout(
                template="plotly_dark",
                margin=dict(l=10, r=10, t=10, b=10),
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                height=320,
            )
            st.plotly_chart(fig_trend, use_container_width=True)
        else:
            st.info("Insufficient timeline data to map monthly trends.")

    with col_right:
        st.markdown('<div class="section-heading">Expense Breakdown by Category</div>', unsafe_allow_html=True)
        st.markdown('<div class="section-caption">Highest spending centers requiring budget review.</div>', unsafe_allow_html=True)

        expense_df = transactions[transactions["type"] == "expense"]
        if not expense_df.empty:
            cat_summary = expense_df.groupby("category")["amount"].sum().reset_index()
            fig_pie = px.pie(
                cat_summary,
                values="amount",
                names="category",
                hole=0.45,
                color_discrete_sequence=px.colors.qualitative.Prism,
            )
            fig_pie.update_layout(
                template="plotly_dark",
                margin=dict(l=10, r=10, t=10, b=10),
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                height=320,
            )
            st.plotly_chart(fig_pie, use_container_width=True)
        else:
            st.info("No expense categories recorded in this timeframe.")

# ---------------------------------------------------------
# TAB 2: PROFIT & LOSS STATEMENT (P&L)
# ---------------------------------------------------------
with tab_pl:
    st.markdown('<div class="section-heading">Statement of Profit or Loss</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="section-caption">Summary financial report for period ending {max_date}.</div>', unsafe_allow_html=True)

    pl_col1, pl_col2 = st.columns([2, 1], gap="large")

    with pl_col1:
        st.subheader("Revenue / Income")
        inc_df = transactions[transactions["type"] == "income"].groupby("category")["amount"].sum().reset_index()
        inc_df.columns = ["Category", f"Amount ({currency_symbol})"]
        st.dataframe(inc_df, use_container_width=True, hide_index=True)
        st.markdown(f"**Total Operating Revenue:** `{currency_symbol} {total_income:,.2f}`")

        st.divider()

        st.subheader("Operating Expenses")
        exp_df = transactions[transactions["type"] == "expense"].groupby("category")["amount"].sum().reset_index()
        exp_df.columns = ["Category", f"Amount ({currency_symbol})"]
        st.dataframe(exp_df, use_container_width=True, hide_index=True)
        st.markdown(f"**Total Operating Expenses:** `{currency_symbol} {total_expenses:,.2f}`")

        st.divider()

        st.markdown(f"### Net Operating Profit: `{currency_symbol} {net_income:,.2f}`")

    with pl_col2:
        st.markdown("#### Tax & Profitability Ratios")
        st.write(f"• **Net Profit Margin:** `{profit_margin:.2f}%`")
        st.write(f"• **Estimated Output VAT:** `{currency_symbol} {vat_output:,.2f}`")
        st.write(f"• **Claimable Input VAT:** `{currency_symbol} {vat_input:,.2f}`")
        st.write(f"• **Estimated Net Tax Obligation:** `{currency_symbol} {net_vat_payable:,.2f}`")

        pl_export = pd.concat([
            pd.DataFrame([{"Category": "--- REVENUE ---", "Amount": ""}]),
            inc_df,
            pd.DataFrame([{"Category": "TOTAL REVENUE", f"Amount ({currency_symbol})": total_income}]),
            pd.DataFrame([{"Category": "--- EXPENSES ---", "Amount": ""}]),
            exp_df,
            pd.DataFrame([{"Category": "TOTAL EXPENSES", f"Amount ({currency_symbol})": total_expenses}]),
            pd.DataFrame([{"Category": "NET PROFIT", f"Amount ({currency_symbol})": net_income}])
        ])
        
        csv_pl = pl_export.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="📥 Download Formal P&L Report (CSV)",
            data=csv_pl,
            file_name=f"Profit_And_Loss_{client_name.replace(' ', '_')}.csv",
            mime="text/csv",
        )

# ---------------------------------------------------------
# TAB 3: BANK RECONCILIATION
# ---------------------------------------------------------
with tab_recon:
    st.markdown('<div class="section-heading">Bank Reconciliation & Audit Status</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-caption">Identify un-reconciled items and ledger variances.</div>', unsafe_allow_html=True)

    unreconciled_df = transactions[~transactions["reconciled"]]
    reconciled_count = transactions["reconciled"].sum()
    unreconciled_count = len(unreconciled_df)

    rec_m1, rec_m2, rec_m3 = st.columns(3)
    rec_m1.metric("Reconciled Transactions", f"{reconciled_count:,}")
    rec_m2.metric("Un-reconciled Items", f"{unreconciled_count:,}")
    rec_m3.metric("Un-reconciled Variance", f"{currency_symbol} {unreconciled_df['amount'].sum():,.2f}")

    st.markdown("#### Items Pending Bank Verification")
    if unreconciled_count > 0:
        st.dataframe(
            unreconciled_df[["date", "reference", "description", "category", "type", "amount"]],
            use_container_width=True,
            hide_index=True,
            column_config={
                "amount": st.column_config.NumberColumn(f"Amount ({currency_symbol})", format=f"{currency_symbol} %.2f")
            }
        )
    else:
        st.success("🎉 All ledger transactions are fully reconciled with bank statements!")

# ---------------------------------------------------------
# TAB 4: TRANSACTION REGISTER & AUDIT CHECKS
# ---------------------------------------------------------
with tab_register:
    st.markdown('<div class="section-heading">Ledger Search & Audit Flags</div>', unsafe_allow_html=True)
    
    search_query = st.text_input(
        "Filter transactions",
        placeholder="Type to search reference, description, or category...",
        label_visibility="collapsed"
    )

    reg_df = transactions.copy()

    if search_query.strip():
        q = search_query.strip()
        reg_df = reg_df[
            reg_df["reference"].str.contains(q, case=False, na=False) |
            reg_df["description"].str.contains(q, case=False, na=False) |
            reg_df["category"].str.contains(q, case=False, na=False)
        ]

    display_df = reg_df.sort_values("date", ascending=False).copy()
    display_df["date"] = display_df["date"].dt.strftime("%d %b %Y")

    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True,
        height=320,
        column_config={
            "date": "Date",
            "reference": "Reference",
            "description": "Description",
            "category": "Category",
            "type": "Type",
            "reconciled": st.column_config.CheckboxColumn("Reconciled"),
            "amount": st.column_config.NumberColumn(f"Amount ({currency_symbol})", format=f"{currency_symbol} %.2f"),
        }
    )

    st.markdown("#### Automated Audit Checks")
    audit_flags = []

    if transactions["reference"].ne("").any():
        dups = transactions[transactions["reference"].ne("") & transactions["reference"].duplicated(keep=False)]
        if not dups.empty:
            audit_flags.append(f"⚠️ **Duplicate References Detected:** {len(dups)} transactions share identical reference IDs.")

    blank_desc = transactions[transactions["description"].str.strip() == ""]
    if not blank_desc.empty:
        audit_flags.append(f"⚠️ **Incomplete Records:** {len(blank_desc)} transaction(s) have missing descriptions.")

    if audit_flags:
        for flag in audit_flags:
            st.warning(flag)
    else:
        st.success("✅ No integrity issues detected in this dataset.")

    csv_reg = display_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Export Filtered Ledger (CSV)",
        data=csv_reg,
        file_name=f"Ledger_Export_{client_name.replace(' ', '_')}.csv",
        mime="text/css",
    )

# ---------------------------------------------------------
# TAB 5: MANUAL JOURNAL ENTRY
# ---------------------------------------------------------
with tab_journal:
    st.markdown('<div class="section-heading">Record Adjusting Journal Entry</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-caption">Manually inject adjusting debits/credits directly into the session ledger.</div>', unsafe_allow_html=True)

    with st.form("manual_journal_form", clear_on_submit=True):
        j_col1, j_col2, j_col3 = st.columns(3)
        with j_col1:
            j_date = st.date_input("Journal Date", value=date.today())
            j_ref = st.text_input("Reference ID", value=f"JNL-{datetime.now().strftime('%H%M%S')}")
        with j_col2:
            j_type = st.selectbox("Type", ["income", "expense"])
            j_cat = st.text_input("Category", value="Adjusting Entries")
        with j_col3:
            j_amount = st.number_input("Amount", min_value=0.01, step=10.0, value=100.0)
            j_desc = st.text_input("Description", value="Manual ledger adjustment")

        submitted = st.form_submit_button("Post Journal Entry")

        if submitted:
            new_entry = {
                "date": pd.Timestamp(j_date),
                "reference": j_ref,
                "description": j_desc,
                "category": j_cat,
                "type": j_type,
                "amount": float(j_amount),
                "reconciled": True
            }
            st.session_state.manual_journals.append(new_entry)
            st.success(f"Journal entry **{j_ref}** posted successfully! Switch tabs to see updated financial totals.")
            st.rerun()

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------
st.markdown(
    f"""
    <div class="footer">
        <div>LedgerFlow Pro · Automated Accounting Workspace</div>
        <div>Active Client: <b>{client_name}</b> | Currency: <b>{currency_symbol}</b></div>
    </div>
    """,
    unsafe_allow_html=True,
)