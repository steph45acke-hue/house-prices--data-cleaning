# House Prices Dataset: Automated Data Preprocessing & Cleaning Pipeline

A robust, production-ready Python data preprocessing pipeline designed to handle structural anomalies, address extreme missingness, and execute type-casting for the Ames Housing dataset. This project showcases structured data cleaning practices essential for preparing tabular datasets for high-performance machine learning models.

---

## 📌 Project Overview
In real-world data science, raw data is rarely ready for modeling. This project implements a programmatic, reproducible approach to data cleaning using **Python** and **Pandas**. By explicitly handling systemic missing data (differentiating between structural missingness and random data omissions), this script transforms messy structural features into mathematically sound variables.

### Key Highlights:
* **No Hardcoding:** Built entirely using vectorized Pandas operations for optimal performance.
* **Domain-Specific Logic:** Imputation strategies are governed by data-dictionary definitions (e.g., distinguishing when `NaN` means "None/No Feature").
* **Zero-Leakage Workflow:** Designed to inspect and process data features systemically without introducing target leakage.

---

## 🛠️ Data Cleaning Architecture & Tasks

The pipeline executes through a structured, multi-stage layout:

### 🔹 Task 1: Structural Exploration & Target Isolation
* Evaluates data dimensions using shape attributes (`.shape`).
* Automatically isolates the target distribution variable (`SalePrice`) by programmatically comparing the feature alignments between the training and testing matrices.

### 🔹 Task 2: Advanced Missing Value Profiling
* Generates a structural missingness report to audit columns carrying null values.
* **Feature-Specific Imputation:**
  * Imputes numeric structural elements (like `LotFrontage`) using descriptive statistics (Median/Mean).
  * Cleans complex categorical text columns (such as `Alley`, `Electrical`, and `MasVnrType`) by mapping explicit structural absences using high-frequency occurrences or domain-logical string labels (e.g., replacing `NaN` with `'None'`).

### 🔹 Task 3: Exploratory Visual Auditing
* Integrates a visual validation step using **Matplotlib**.
* Generates analytical plots detailing the exact distribution and frequency of missing records across independent variables before and after pipeline execution.

### 🔹 Task 4: Complete Pipeline Verification
* Runs a final programmatic evaluation using `.isnull().sum()` across the entire data matrix to verify that exactly **0 missing values** remain.

---

## 💻 Tech Stack & Dependencies
* **Language:** Python 3.x
* **Libraries:** * `pandas` (Data manipulation, alignment, and vector operations)
  * `numpy` (Low-level array tracking)
  * `matplotlib` (Statistical visualization)
* **IDE:** JetBrains PyCharm

---

## 🚀 How to Run the Pipeline

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/house-prices-data-cleaning.git](https://github.com/YOUR_USERNAME/house-prices-data-cleaning.git)
cd house-prices-data-cleaning
