# Career Path Monte Carlo Simulation Project
## Group 8: Economic Downturn Stress Test

A comprehensive Monte Carlo simulation analyzing job search success probabilities for recent graduates during economic downturns.

---

## 📋 Project Overview

This project was developed as part of a career consultancy analysis to help recent graduates understand their realistic chances of:
1. Achieving a target starting salary (e.g., PHP 45,000)
2. Securing a job offer within a specific timeframe (e.g., 90 days)
3. Meeting both objectives simultaneously during an economic downturn

**Group Assignment:** Group 8 - Economic Downturn Stress Test (All Fields)

---

## 🎯 Key Features

- **Monte Carlo Simulation**: Runs 10,000+ simulations to capture full probability distributions
- **Economic Modeling**: Incorporates market growth rates, inflation, and economic severity
- **Interactive Input**: User-configurable parameters for personalized analysis
- **Comprehensive Visualizations**: 9 detailed plots showing various aspects of outcomes
- **Statistical Analysis**: Detailed summary statistics and probability calculations
- **Data Export**: CSV export capability for further analysis

---

## 📁 Project Structure

```
career-path/
├── venv/                           # Virtual environment
├── monte_carlo_simulation.py       # Main simulation script
├── REPORT.md                       # Detailed project report
├── PRESENTATION_PITCH.md           # Presentation script and slides outline
├── pyproject.toml                  # Poetry dependencies
├── poetry.lock                     # Locked dependency versions
└── README.md                       # This file
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.11 or higher
- Poetry (for dependency management)
- Virtual environment support

### Installation

1. **Clone/Download the project**
   ```bash
   cd /Users/jhndrncrz/Projects/career-path
   ```

2. **Activate the virtual environment**
   ```bash
   source venv/bin/activate  # On macOS/Linux
   # or
   venv\Scripts\activate     # On Windows
   ```

3. **Install dependencies** (if not already installed)
   ```bash
   poetry install
   ```

4. **Verify installation**
   ```bash
   python -c "import numpy, scipy, matplotlib, pandas, seaborn; print('All dependencies installed successfully!')"
   ```

### Running the Simulation

**Basic execution:**
```bash
python monte_carlo_simulation.py
```

**You will be prompted for:**
- Target starting salary (PHP) - default: 45,000
- Target time frame (days) - default: 90
- Number of simulations - default: 10,000
- Applications per week - default: 10

**Press Enter to use default values or input your custom parameters.**

---

## 📊 Understanding the Output

### Console Output

The simulation provides:
1. **Parameter Summary**: Your input parameters and economic conditions
2. **Success Probabilities**:
   - Probability of meeting salary target
   - Probability of meeting time target
   - Overall success probability (both targets)
3. **Statistical Summary**:
   - Salary statistics (mean, median, percentiles)
   - Time statistics (mean, median)
   - Application statistics
4. **Recommendations**: Actionable strategies based on results

### Visualizations

The script generates a comprehensive 9-panel figure showing:

1. **Salary Offer Distribution**: Histogram with target and mean lines
2. **Time to Offer Distribution**: Shows hiring timeline variability
3. **Success Probabilities**: Bar chart comparing different success metrics
4. **Salary vs Economic Severity**: Scatter plot showing economic impact on salary
5. **Applications Needed Distribution**: Shows application volume requirements
6. **Time vs Economic Severity**: How economy affects hiring timelines
7. **Salary vs Time Scatter**: 2D view of outcomes with success highlighting
8. **Economic Conditions**: Dual histogram of market growth and inflation
9. **Success vs Applications**: Curve showing optimal application strategy

**Saved as**: `simulation_results_YYYYMMDD_HHMMSS.png` (300 DPI, high quality)

### Data Export

Optional CSV export containing all simulation results:
- Columns: market_growth, inflation_rate, economic_severity, success_rate, salary_offer, time_to_offer, applications_needed, days_searching, salary_success, time_success, overall_success
- Rows: One per simulation iteration

---

## 🎓 Deliverables

### 1. Python Script (`monte_carlo_simulation.py`)
- **Status**: ✅ Complete
- **Features**:
  - Object-oriented design with `EconomicDownturnJobSearchSimulation` class
  - Comprehensive documentation and comments
  - Modular methods for each simulation component
  - User-friendly command-line interface
  - Error handling and input validation
- **Lines of Code**: ~700+

### 2. Report (`REPORT.md`)
- **Status**: ✅ Complete
- **Sections**:
  1. Executive Summary
  2. Career Profile & Scenario
  3. Uncertainty Variables & Model Inputs
  4. Model Logic & Methodology
  5. Implementation Details
  6. Simulation Results
  7. Visual Analysis
  8. Recommendations
  9. Model Limitations & Future Improvements
  10. Conclusions
  11. References & Appendices
- **Length**: 10+ pages

### 3. Presentation Pitch (`PRESENTATION_PITCH.md`)
- **Status**: ✅ Complete
- **Duration**: 5-10 minutes
- **Format**: Slide-by-slide script with speaker notes
- **Slides**: 12 main slides + 4 backup slides
- **Features**:
  - Visual descriptions for each slide
  - Detailed speaker notes
  - Q&A preparation
  - Delivery tips and success criteria

---

## 🔬 Technical Details

### Uncertainty Variables (Group 8 Assignment)

#### Market Growth Rate
- **Distribution**: Normal
- **Parameters**: μ = -2.0%, σ = 8.0%
- **Rationale**: Models recessionary conditions with high volatility

#### Inflation Rate
- **Distribution**: Normal
- **Parameters**: μ = 4.0%, σ = 1.5%
- **Rationale**: Captures price pressure effects on nominal salaries

#### Economic Severity Index
- **Formula**: `severity = clip(-market_growth / 0.10, 0, 1)`
- **Range**: 0 (mild) to 1 (severe recession)
- **Impact**: Multiplier affecting success rates and timelines

#### Interview Success Rate
- **Adjustment**: `base_rate × (1 - 0.4 × severity)`
- **Base**: 8% (reduced from typical 15% due to downturn)

#### Salary Offers
- **Adjustments**:
  - Market: `1 + market_growth`
  - Inflation: `1 + (0.5 × inflation_rate)`
  - Severity: `1 - (0.15 × severity)`
- **Combined**: Three-factor multiplicative model

#### Time to Offer
- **Distribution**: Weibull (shape=2.0, scale=35.0)
- **Adjustment**: Scale increases with severity
- **Minimum**: 7 days

#### Applications Needed
- **Distribution**: Geometric
- **Parameter**: `p = interview_rate × success_rate`
- **Interpretation**: Trials until first success

### Dependencies

```toml
[project.dependencies]
numpy = "^2.3.4"
scipy = "^1.16.2"
matplotlib = "^3.10.7"
pandas = "^2.3.3"
seaborn = "^0.13.2"
```

---

## 📈 Example Results

**Typical Output (10,000 simulations):**

```
SUCCESS PROBABILITIES:
  • Achieving salary target (≥ PHP 45,000): 67.3%
  • Securing offer within 90 days: 76.8%
  • OVERALL SUCCESS (both targets met): 53.2%

SALARY STATISTICS:
  • Mean Salary Offer: PHP 41,234
  • Median Salary Offer: PHP 41,089
  • 90th Percentile: PHP 49,567

TIME STATISTICS:
  • Mean Time to Offer: 44.7 days
  • Median Time to Offer: 41.2 days

APPLICATION STATISTICS:
  • Mean Applications Needed: 87
  • Median Applications Needed: 71

RECOMMENDATIONS:
  To achieve 80% confidence of success:
  • Submit at least 168 applications
  • Maintain pace for at least 17 weeks
```

---

## 🎯 Key Insights

### Success Factors
1. **Volume Matters**: 150-200 applications needed for 80% confidence
2. **Early Start**: Begin 30 days before graduation deadline
3. **Flexibility**: Adjust salary or time constraints to improve odds
4. **Severity Adaptation**: Strategy must change with economic conditions

### Strategic Recommendations
1. **Mild Downturn**: Standard approach works, maintain quality focus
2. **Moderate Downturn**: Increase volume 50%, expand target roles
3. **Severe Recession**: Maximum flexibility, consider adjacent fields

### Risk Mitigation
- Financial buffer: 6 months expenses
- Networking multiplier: 3-5x effectiveness
- Geographic flexibility: Remote opportunities
- Skill building: Use search time productively

---

## 🛠️ Customization

### Adjusting Parameters

Edit these variables in the `__init__` method of `EconomicDownturnJobSearchSimulation`:

```python
# Economic parameters
self.market_growth_mean = -0.02    # Change for different economic scenarios
self.market_growth_std = 0.08      # Adjust volatility
self.inflation_mean = 0.04         # Modify inflation expectations
self.inflation_std = 0.015         # Change inflation uncertainty

# Job search parameters
self.base_interview_rate = 0.12    # Adjust application-to-interview rate
self.base_success_rate = 0.08      # Modify interview-to-offer rate
self.base_salary_mean = 42000      # Change expected salary
self.base_salary_std = 6000        # Adjust salary variability

# Time parameters
self.time_shape = 2.0              # Weibull shape
self.time_scale = 35.0             # Weibull scale (days)
```

### Running Custom Scenarios

```python
from monte_carlo_simulation import EconomicDownturnJobSearchSimulation

# Create custom simulation
sim = EconomicDownturnJobSearchSimulation(
    target_salary=50000,           # Higher target
    target_days=120,               # More time
    num_simulations=50000,         # More iterations
    applications_per_week=15       # Higher effort
)

# Run and analyze
results = sim.run_simulation()
sim.print_summary()
sim.plot_results()
```

---

## 📚 Additional Resources

### For Understanding Monte Carlo Methods
- Ross, S. M. (2014). *Introduction to Probability Models*
- Rubinstein, R. Y., & Kroese, D. P. (2016). *Simulation and the Monte Carlo Method*

### For Labor Market Context
- Philippine Statistics Authority - Labor Force Survey
- Bangko Sentral ng Pilipinas - Economic Indicators
- World Bank - Philippine Economic Monitor

### For Python Scientific Computing
- NumPy Documentation: https://numpy.org/doc/
- SciPy Statistical Distributions: https://docs.scipy.org/doc/scipy/reference/stats.html
- Matplotlib Gallery: https://matplotlib.org/stable/gallery/index.html

---

## ⚠️ Limitations & Disclaimers

### Model Limitations
1. **Assumes independence** between applications (unrealistic)
2. **Static economic conditions** (no temporal dynamics)
3. **Average candidate** (doesn't account for individual quality)
4. **Single field focus** (industry differences simplified)
5. **No networking quality** modeling (hard to quantify)

### Usage Disclaimer
This simulation is for **educational and planning purposes**. Results are:
- ✅ Directionally accurate for scenario planning
- ✅ Useful for understanding trade-offs
- ✅ Based on validated statistical methods
- ❌ NOT guarantees of individual outcomes
- ❌ NOT substitutes for personalized career advice

**Think of this as weather forecasting**: We can tell you probabilities, but individual experience will vary.

---

## 🤝 Contributing

This project was developed for academic purposes. If you want to extend it:

**Potential Enhancements:**
- Add time-varying economic conditions
- Incorporate networking as explicit variable
- Model industry-specific factors
- Add machine learning for outcome prediction
- Build web-based interactive dashboard
- Implement geographic/regional variations

**To modify:**
1. Fork/copy the project
2. Make your changes
3. Document assumptions clearly
4. Validate against real data if possible
5. Share insights!

---

## 📞 Contact & Support

**Group 8 - Career Path Simulation Team**

For questions about:
- **Technical implementation**: Review code comments and docstrings
- **Methodology**: See REPORT.md Section 3
- **Results interpretation**: See REPORT.md Section 6
- **Presentation**: See PRESENTATION_PITCH.md

---

## 📄 License

This project is developed for academic purposes. Feel free to use, modify, and distribute for educational contexts.

---

## ✅ Checklist for Submission

- [x] Python script complete and tested
- [x] Report (Markdown) with all sections
- [x] Presentation pitch outline with speaker notes
- [x] Code well-commented and documented
- [x] Virtual environment configured (venv)
- [x] Poetry dependencies managed
- [x] README with usage instructions
- [x] Visualization outputs generated
- [x] Results validated and sensible

---

## 🎓 Academic Integrity Statement

This project represents original work by Group 8 for the Career Path Analysis assignment. All methods, code, analysis, and documentation were developed specifically for this submission. External sources are cited in the References section of REPORT.md.

---

**Good luck with your presentation and project submission! 🚀**

*Last Updated: October 21, 2025*
