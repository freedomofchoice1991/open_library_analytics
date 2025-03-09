# **Open Library Analytics 📚📊**
A Python project that fetches, processes, and analyzes book data from the **Open Library API**, generating a report as a CSV file. The project is automated using **GitHub Actions** with CI/CD workflows.

---

## **🚀 Features**
✅ Fetches book data from the **Open Library API**  
✅ Processes and cleans book data (author, title, year, ISBN)  
✅ Generates a **CSV report** of book data  
✅ **CI/CD automation** using GitHub Actions  
✅ **Linting & Testing** using `flake8` and `pytest`  
✅ Stores CSV reports as **GitHub Actions artifacts**  

---

## **📂 Project Structure**
```
/open_library_analytics
├── data_pipeline/
│   ├── fetch_data.py          # Fetches book data from Open Library API
│   ├── process_data.py        # Processes the raw API data
│   ├── generate_report.py     # Saves processed data to CSV
│
├── tests/
│   ├── test_generate_report.py # Unit tests for report generation
│   ├── test_process_data.py    # Unit tests for data processing
│
├── .github/
│   ├── workflows/
│   │   ├── ci.yml              # CI pipeline for linting & testing
│   │   ├── deploy.yml          # Deploy pipeline for CSV report generation
│
├── requirements.txt            # Project dependencies
├── README.md                   # Project documentation
└── main.py                     # Main script to run everything
```

---

## **📡 API Integration**
This project uses the **Open Library API** to fetch book data. Example API request:

```
https://openlibrary.org/search.json?author=George%20Orwell&limit=5
```

---

## **⚙️ Installation & Setup**
### **1️⃣ Clone the Repository**
```bash
   git clone https://github.com/your-username/open_library_analytics.git
cd open_library_analytics
```

### **2️⃣ Create a Virtual Environment**
```bash
   python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### **3️⃣ Install Dependencies**
```bash
   pip install -r requirements.txt
```

---

## **📜 Usage**
### **Run the Full Pipeline Locally**
```bash
   python main.py
```

### **Run Individual Modules**
Fetch book data:
```bash
   python data_pipeline/fetch_data.py
```
Process book data:
```bash
   python data_pipeline/process_data.py
```
Generate CSV report:
```bash
   python data_pipeline/generate_report.py
```

---

## **🤖 GitHub Actions CI/CD**
The project has two **automated workflows**:

1️⃣ **CI Pipeline (`ci.yml`)**  
✔ Runs on every `push` and `pull request`.  
✔ Installs dependencies, lints code, and runs tests.  

2️⃣ **Deploy Report (`deploy.yml`)**  
✔ Runs on every push to `main`.  
✔ Generates the CSV report and uploads it as an **artifact**.  

📍 **View artifacts** in **GitHub → Actions → Deploy Report → Artifacts**.

---

## **✅ Running Tests**
Run all tests:
```bash
   pytest tests/
```
Run a specific test:
```bash
   pytest tests/test_process_data.py
```

---

## **📜 Example Output (CSV)**
| Title       | Author        | Year | ISBN       |
|-------------|---------------|------|------------|
| 1984        | George Orwell | 1949 | 1234567890 |
| Animal Farm | George Orwell | 1945 | 0987654321 |


---

## **📄 License**
This project is licensed under the **MIT License**.
