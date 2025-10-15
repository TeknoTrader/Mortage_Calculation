# 🏠 Interactive Mortgage Calculator by Nicola Chimenti

A comprehensive **web-based mortgage calculator** built with **Streamlit** and **Python**, designed to provide detailed amortization analysis, payment optimization strategies, and interactive visualizations.  
This tool helps users understand their mortgage costs, explore payment alternatives, and make informed financial decisions.

## 🌐 Live Demo

**Try it now:** [https://mortagecalculation.streamlit.app/](https://mortagecalculation.streamlit.app/)

No installation required — start calculating immediately in your browser!

---

## 🧩 Features

### 💰 Complete Mortgage Analysis
Calculate and visualize your mortgage with precision, including:
- **Monthly payment breakdown** (principal + interest)
- **Total cost** over the entire loan term
- **Amortization schedule** with date-by-date details
- **Interactive charts** showing payment composition over time

**Key Capabilities:**
- Support for multiple currencies (USD, EUR, RUB, etc.)
- Customizable loan parameters (amount, rate, duration)
- Real-time calculations with instant visual feedback
- Mobile-responsive design with alternative rendering modes

---

### 📊 Advanced Visualization
Two display modes to suit any device:
- **Interactive Mode**: Plotly-powered dynamic charts with hover details
- **Image Mode**: Static matplotlib charts optimized for mobile devices

**Visual Components:**
- Payment breakdown over time (cumulative interest vs. principal)
- Pie chart showing total interest vs. principal ratio
- Balance evolution chart
- Detailed amortization timeline

---

### 💡 Payment Optimization Strategies
Discover how to **save money** by adjusting your payment frequency:
- **Weekly payment** calculator with savings comparison
- **Bi-weekly payment** alternative analysis
- Side-by-side comparison with standard monthly payments
- Clear visualization of potential savings

**How it works:**  
By paying more frequently (weekly or bi-weekly), you make more payments per year with the same monthly budget, reducing total interest paid over the loan lifetime.

---

### 🌍 Multilingual Support
Full interface translation in:
- 🇬🇧 **English**
- 🇮🇹 **Italiano**
- 🇷🇺 **Русский**

---

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/mortgage-calculator.git
cd mortgage-calculator
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
streamlit run web_application.py
```

4. **Open your browser**  
The app will automatically open at `http://localhost:8501`

---

## 🚀 Usage

1. **Select your language** from the dropdown menu
2. **Enter loan parameters**:
   - Loan amount
   - Annual interest rate (%)
   - Loan term (years)
   - Starting date
3. **Choose visualization mode** (Interactive or Image)
4. **Click "Calculate"** to see results
5. **Explore additional features**:
   - Toggle "Amortization Chart" for detailed payment evolution
   - Toggle "Amortization Plan" for the complete payment schedule
   - Review payment optimization strategies at the bottom

---

## 📁 Project Structure

```
mortgage-calculator/
├── web_application.py      # Main Streamlit application
├── variable_rates.py       # Additional scenarios module (WIP)
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

---

## 🔧 Technical Details

**Built with:**
- **Streamlit**: Web framework for data apps
- **Plotly**: Interactive visualizations
- **Matplotlib**: Static chart generation
- **Pandas & NumPy**: Data manipulation and calculations
- **dateutil**: Advanced date handling

**Key Calculations:**
- Monthly payment: `M = P × [r(1+r)^n] / [(1+r)^n - 1]`
- Where P = principal, r = monthly rate, n = number of payments
- Amortization follows standard financial formulas with period-by-period interest calculation

**Alternative Payment Frequencies:**
- Weekly payments: 52 payments per year
- Bi-weekly payments: 26 payments per year
- Uses the same monthly budget, distributed more frequently to reduce interest accumulation

---

## 💼 Use Cases

This calculator is perfect for:
- **Homebuyers** planning their mortgage and comparing loan offers
- **Current homeowners** exploring refinancing opportunities
- **Financial advisors** demonstrating payment strategies to clients
- **Students & educators** learning about loan amortization and financial mathematics
- **Anyone** wanting to understand the true cost of borrowing

---

## 🎯 Roadmap

Future enhancements planned:
- [ ] Variable rate mortgage simulation with Monte Carlo scenarios
- [ ] Extra payment calculator showing time and interest saved
- [ ] Refinancing analysis comparing current vs. new loan terms
- [ ] Tax deduction calculator for mortgage interest
- [ ] Side-by-side comparison tool for multiple loan offers
- [ ] Export detailed reports to PDF format
- [ ] Historical interest rate data integration for trend analysis
- [ ] Early payoff calculator with accelerated payment schedules
- [ ] Break-even analysis for points and fees

---

## 📊 Example Calculation

**Scenario:** €200,000 loan at 5% annual rate for 30 years

**Results:**
- Monthly Payment: €1,073.64
- Total Paid: €386,511.57
- Total Interest: €186,511.57
- Interest represents 48.3% of total payments

**Optimization Strategy:**
- By paying €268.41 weekly (same monthly budget split into 4 weeks)
- You save approximately €12,000 in interest
- Loan is paid off several years earlier

*This demonstrates the power of increased payment frequency!*

---

## 💬 Feedback & Contributions

If you find this tool useful or have ideas for improvement, feel free to:
- Open an **[Issue](../../issues)** for bug reports or feature requests
- Submit a **Pull Request** to contribute enhancements
- Share your use cases and suggestions

Community feedback drives development!

---

## 📜 License

Distributed under the **MIT License** — free to use, modify, and share with proper attribution.

---

## 👤 Author

**Nicola Chimenti**  
Financial Tools Developer & Business Analyst

🌐 [MQL5 Profile](https://www.mql5.com/it/users/teknotrader/seller#!category=2)  

📧 [Fiverr Profile](https://www.fiverr.com/sellers/teknonicola/)

⌨ Contact: teknotrader.nc@gmail.com

---

## 🙏 Acknowledgments

This project was developed to help people better understand their mortgage commitments and explore ways to save money through optimized payment strategies.

---

## ❓ FAQ

**Q: Can I use this for commercial purposes?**  
A: Yes, the MIT license allows commercial use with attribution.

**Q: Is my data stored anywhere?**  
A: No, all calculations happen locally in your browser. No data is transmitted or stored.

**Q: Can I add more languages?**  
A: Absolutely! Check the `translations` dictionary in `web_application.py` and submit a PR.

**Q: Why do weekly payments save money?**  
A: By paying weekly, you make 52 payments per year instead of 12 monthly ones. This means you pay down principal faster, reducing the total interest accrued.

**Q: Does this work for any type of loan?**  
A: Yes! While designed for mortgages, you can use it for any amortizing loan (car loans, personal loans, etc.).

**Q: Can I calculate my exact savings with extra payments?**  
A: The current version focuses on payment frequency optimization. Extra payment features are on the roadmap!

---

⭐ **If you find this calculator helpful, please give the repository a star — it helps others discover the tool!**
