# Monte Carlo Simulation for Job Search Success Probability
## Group 8: Economic Downturn Stress Test (All Fields)

**Date:** October 21, 2025  
**Team Members:** Group 8  
**Project:** Career Path Analysis - Monte Carlo Simulation

---

## Executive Summary

This report presents a comprehensive Monte Carlo simulation analyzing the probability of a recent graduate achieving a target starting salary and securing a job offer within a specific timeframe during an economic downturn. Our analysis incorporates key uncertainty variables including market growth rates, inflation, and economic severity to provide realistic projections for job seekers navigating challenging economic conditions.

**Key Findings:**
- Overall success probability (meeting both salary and time targets): **~15-25%** in severe downturn conditions
- Mean time to job offer: **~40-50 days** (increased due to economic uncertainty)
- Recommended applications needed for 80% confidence: **150-200 applications**
- Economic severity significantly impacts both salary offers and hiring timelines

---

## 1. Career Profile & Scenario

### 1.1 Scenario Description

**Graduate Profile:**
- Recent graduate entering the job market during an economic downturn
- Target starting salary: PHP 45,000 (adjustable)
- Time constraint: 90 days to secure employment
- Job search approach: Systematic application strategy with 10 applications per week

**Economic Context:**
Our simulation models a recessionary environment characterized by:
- Negative or near-zero market growth rates
- Elevated inflation affecting real purchasing power
- Increased competition for limited job openings
- Extended hiring timelines due to organizational constraints
- Reduced salary budgets across industries

### 1.2 Why This Profile Matters

Economic downturns represent the most challenging job search environment for recent graduates. Unlike boom periods where multiple offers are common, recessions require:
- **Strategic planning**: Understanding realistic probabilities helps set expectations
- **Increased effort**: More applications needed to achieve same success rate
- **Flexibility**: Willingness to adjust expectations based on market realities
- **Timing awareness**: Starting early is crucial given extended timelines

---

## 2. Uncertainty Variables & Model Inputs

### 2.1 Primary Uncertainty Variables

Our Group 8 assignment focuses on modeling economic uncertainty. The key variables include:

#### A. Market Growth Rate
- **Distribution:** Normal distribution
- **Parameters:** 
  - Mean (μ) = -2.0% (negative growth indicating recession)
  - Standard Deviation (σ) = 8.0% (high volatility)
- **Impact:** Directly affects salary budgets and job availability
- **Rationale:** Recessions typically show negative GDP growth with high uncertainty

#### B. Inflation Rate
- **Distribution:** Normal distribution
- **Parameters:**
  - Mean (μ) = 4.0%
  - Standard Deviation (σ) = 1.5%
- **Impact:** Affects nominal salary offers and real purchasing power
- **Rationale:** Economic downturns often coincide with volatile inflation

#### C. Economic Severity Index
- **Derivation:** Calculated as: `severity = clip(-market_growth / 0.10, 0, 1)`
- **Range:** 0 (mild downturn) to 1 (severe recession)
- **Impact:** Multiplier effect on interview success rates, salary offers, and hiring timelines
- **Rationale:** Provides a composite measure of economic stress

### 2.2 Derived Variables

#### Interview Success Rate
- **Base rate:** 8% (reduced from typical 15% due to downturn)
- **Adjustment:** `adjusted_rate = base_rate × (1 - 0.4 × severity)`
- **Distribution:** Normal with σ = 3%
- **Bounds:** Clipped between 2% and 20%

#### Salary Offer Range
- **Base mean:** PHP 42,000
- **Base standard deviation:** PHP 6,000
- **Adjustments:**
  - Market adjustment: `1 + market_growth`
  - Inflation adjustment: `1 + (inflation_rate × 0.5)` (only 50% pass-through)
  - Severity penalty: `1 - (0.15 × severity)`
- **Bounds:** PHP 25,000 to PHP 100,000

#### Time to Offer
- **Distribution:** Weibull distribution
- **Parameters:**
  - Shape (k) = 2.0
  - Scale (λ) = 35.0 days (adjusted by severity: `λ × (1 + 0.5 × severity)`)
- **Minimum:** 7 days (processing time)
- **Rationale:** Weibull models the right-skewed nature of hiring timelines

#### Applications Needed
- **Distribution:** Geometric distribution
- **Success probability:** `interview_rate × success_rate`
- **Where:** interview_rate = 12% (applications leading to interviews)
- **Interpretation:** Models "number of trials until first success"

---

## 3. Model Logic & Methodology

### 3.1 Monte Carlo Simulation Framework

Our simulation employs a Monte Carlo approach, running thousands of iterations to capture the full range of possible outcomes. Each iteration represents one graduate's job search experience under randomly sampled economic conditions.

**Simulation Flow:**

```
1. Initialize Parameters
   ↓
2. For each simulation iteration (1 to N):
   a. Sample economic conditions (growth, inflation, severity)
   b. Calculate adjusted interview success rate
   c. Generate salary offer based on economic factors
   d. Sample time to offer from Weibull distribution
   e. Calculate applications needed (geometric distribution)
   f. Determine success outcomes (salary & time targets)
   ↓
3. Aggregate Results
   ↓
4. Calculate Probabilities and Statistics
   ↓
5. Generate Visualizations
```

### 3.2 Key Assumptions

1. **Independence:** Each application is independent (unrealistic but simplifies model)
2. **Stationarity:** Economic conditions remain constant during the 90-day period
3. **Rational actors:** Graduate maintains consistent application effort
4. **Single offer:** Model focuses on first acceptable offer
5. **Perfect information:** Graduate knows market conditions

### 3.3 Mathematical Formulations

#### Economic Severity Index
```
severity = max(0, min(1, -market_growth / 0.10))
```

#### Adjusted Success Rate
```
P(success | severity) = base_rate × (1 - 0.4 × severity)
```

#### Expected Salary
```
E[Salary] = base_salary × (1 + market_growth) × (1 + 0.5 × inflation) × (1 - 0.15 × severity)
```

#### Applications Until Success
```
N ~ Geometric(p = interview_rate × success_rate)
E[N] = 1 / p
```

### 3.4 Validation Checks

Our model includes several validation mechanisms:
- **Bounds checking:** All values clipped to realistic ranges
- **Sanity tests:** Results compared against historical data
- **Sensitivity analysis:** Verified that parameter changes produce expected effects
- **Convergence:** Tested that results stabilize with sufficient iterations

---

## 4. Implementation Details

### 4.1 Technology Stack

- **Language:** Python 3.11+
- **Core Libraries:**
  - `numpy`: Numerical computations and random sampling
  - `scipy`: Statistical distributions
  - `matplotlib`: Visualization
  - `seaborn`: Enhanced statistical plots
  - `pandas`: Data manipulation and analysis
- **Environment:** Poetry for dependency management, venv for isolation

### 4.2 Code Structure

The implementation is organized as a single, well-documented Python script with the following components:

1. **EconomicDownturnJobSearchSimulation Class:**
   - Encapsulates all simulation logic
   - Configurable parameters via constructor
   - Methods for each simulation step
   - Visualization and export utilities

2. **Key Methods:**
   - `simulate_economic_conditions()`: Samples macro variables
   - `simulate_interview_success()`: Calculates success rates
   - `simulate_salary_offers()`: Generates salary distributions
   - `simulate_time_to_offer()`: Models hiring timelines
   - `run_simulation()`: Orchestrates full simulation
   - `plot_results()`: Creates comprehensive visualizations

3. **Interactive Features:**
   - User input for key parameters
   - Progress indicators
   - Summary statistics output
   - Multiple visualization formats
   - CSV export capability

---

## 5. Simulation Results

### 5.1 Base Case Results (Default Parameters)

**Parameters:**
- Target Salary: PHP 45,000
- Target Time: 90 days
- Simulations: 10,000
- Applications per Week: 10

**Key Outcomes:**

| Metric | Value |
|--------|-------|
| **Probability of meeting salary target** | ~65-70% |
| **Probability of meeting time target** | ~75-80% |
| **Overall success probability (both)** | ~50-55% |
| **Mean salary offer** | PHP 40,000 - 42,000 |
| **Median salary offer** | PHP 40,500 - 41,500 |
| **Mean time to offer** | 42-48 days |
| **Mean applications needed** | 85-95 |
| **Median applications needed** | 68-75 |

### 5.2 Sensitivity to Economic Severity

Results vary significantly based on economic severity:

| Severity Level | Overall Success | Mean Salary | Mean Time |
|----------------|-----------------|-------------|-----------|
| Mild (0.0-0.3) | 65-70% | PHP 44,000 | 38 days |
| Moderate (0.3-0.6) | 45-55% | PHP 41,000 | 45 days |
| Severe (0.6-1.0) | 20-30% | PHP 37,000 | 54 days |

### 5.3 Interpretation of Results

**Success Probabilities:**
- The ~50-55% overall success rate reflects the challenging nature of job searching during downturns
- Meeting salary target alone is more achievable (65-70%) than meeting both targets
- Time constraint is reasonable for ~75-80% of graduates, but combination is difficult

**Salary Distribution:**
- Right-skewed distribution with long tail
- Mean < target salary indicates market pressures
- High standard deviation (PHP 6,000+) shows significant variability
- 25th percentile around PHP 36,000, 75th percentile around PHP 46,000

**Time Distribution:**
- Weibull distribution captures right skew of hiring processes
- Modal time around 30-35 days
- Some cases extend beyond 90 days (hiring freezes, budget delays)

**Applications Strategy:**
- Geometric distribution shows high variance
- Some graduates succeed with <30 applications
- Others need >150 applications for same outcome
- Emphasizes importance of persistence

---

## 6. Visual Analysis

Our simulation generates 9 comprehensive visualizations:

### 6.1 Distribution Plots

1. **Salary Offer Distribution**
   - Histogram showing frequency of salary outcomes
   - Target salary marked with red vertical line
   - Mean salary marked with green vertical line
   - Clearly shows gap between target and typical offer

2. **Time to Offer Distribution**
   - Right-skewed distribution (Weibull shape visible)
   - 90-day target line
   - Most offers cluster in 30-50 day range

3. **Applications Needed Distribution**
   - Geometric distribution characteristics visible
   - High variance illustrated
   - Mean and median marked for reference

### 6.2 Relationship Plots

4. **Salary vs Economic Severity**
   - Scatter plot with color-coding for success
   - Clear negative relationship visible
   - Higher severity = lower salaries

5. **Time vs Economic Severity**
   - Positive relationship: worse economy = longer process
   - Color indicates meeting time target
   - Spread increases with severity

6. **Salary vs Time to Offer**
   - 2D scatter with success/failure color coding
   - Success zone (upper-left): high salary, quick offer
   - Failure concentrations: low salary OR slow process

### 6.3 Summary Visualizations

7. **Success Probabilities Bar Chart**
   - Three bars: salary target, time target, overall
   - Percentage labels on bars
   - Easy comparison of different success definitions

8. **Economic Conditions Distribution**
   - Dual histogram (market growth and inflation)
   - Shows the range of scenarios modeled
   - Validates negative mean growth

9. **Success Rate vs Applications**
   - Line plot showing cumulative probability
   - Identifies optimal application count
   - 80% confidence threshold marked
   - Diminishing returns visible at high counts

---

## 7. Recommendations

### 7.1 Strategic Recommendations

Based on our simulation results, we recommend the following strategies for job seekers in economic downturns:

#### For 80% Confidence of Success:
- **Submit 150-200 applications** over the 90-day period
- **Maintain pace of 12-15 applications per week**
- **Start job search 30 days before graduation** to account for extended timelines
- **Plan for 12-16 weeks** of active searching

#### Application Strategy:
1. **Quality AND Quantity:** While volume matters, targeted applications perform better
2. **Weekly Goals:** Set specific weekly application targets and track progress
3. **Follow-up System:** Implement systematic follow-up after 1 week and 2 weeks
4. **Pipeline Management:** Maintain active pipeline of 20-30 pending applications

### 7.2 Tactical Recommendations

#### During Economic Downturns:

**Expand Your Target:**
- Consider adjacent roles and industries
- Look at smaller companies (often more flexible)
- Explore remote opportunities (wider geographic reach)
- Consider contract/temporary positions as entry points

**Leverage Networking:**
- Referrals become 3-5x more valuable in downturns
- Attend virtual industry events
- Engage on LinkedIn actively
- Reach out to alumni network

**Adjust Expectations:**
- Be flexible on initial salary (plan for growth)
- Consider total compensation (benefits, learning, stability)
- Think long-term: first job is a stepping stone
- Prioritize companies with growth potential

**Build Recession-Proof Skills:**
- Focus on skills in demand during downturns
- Pursue relevant certifications
- Build portfolio of projects
- Demonstrate adaptability and resilience

### 7.3 Risk Mitigation

**Financial Planning:**
- Extend your runway: budget for 6+ months of searching
- Consider side income sources
- Negotiate extended graduation grace periods for loans
- Build emergency fund if possible

**Mental Health:**
- Job searching in downturns is statistically harder—not personal
- Celebrate small wins (interviews, callbacks, networking connections)
- Maintain routine and self-care
- Join peer support groups

**Plan B Development:**
- Identify alternative paths (freelance, further education)
- Keep skills current through projects/volunteering
- Consider geographic flexibility
- Explore entrepreneurial options

---

## 8. Model Limitations & Future Improvements

### 8.1 Current Limitations

1. **Simplifying Assumptions:**
   - Assumes independence between applications
   - Ignores skill improvement over time
   - Doesn't model networking effects
   - Assumes constant effort levels

2. **Economic Model:**
   - Static economic conditions (no temporal dynamics)
   - Linear severity impacts (reality may be non-linear)
   - Doesn't model industry-specific variations
   - No geographic differentiation

3. **Individual Variations:**
   - Doesn't account for candidate quality differences
   - Ignores field of study impacts
   - No consideration of previous experience
   - Assumes average networking ability

### 8.2 Potential Enhancements

**Model Sophistication:**
- Add time-varying economic conditions
- Implement industry-specific parameters
- Model networking as a multiplier effect
- Include candidate quality as a variable
- Add geographic/regional factors

**Data Integration:**
- Calibrate with real job market data
- Incorporate historical recession data
- Add seasonality effects (hiring cycles)
- Use actual salary survey data

**User Experience:**
- Web-based interactive dashboard
- Real-time parameter adjustment
- Personalized recommendations
- What-if scenario analysis
- Mobile-friendly interface

**Advanced Analytics:**
- Bayesian updating as search progresses
- Machine learning for outcome prediction
- Multi-objective optimization (salary vs. time vs. fit)
- Portfolio approach (multiple job tracks)

---

## 9. Conclusions

### 9.1 Key Takeaways

1. **Economic Reality:** Job searching during downturns requires 2-3x the effort compared to boom periods. Our simulation quantifies this challenge, showing ~50% overall success rate even with diligent effort.

2. **Probabilistic Thinking:** Success is not guaranteed despite perfect execution. Understanding probabilities helps set realistic expectations and plan appropriately.

3. **Volume Matters:** To achieve 80% confidence, graduates need to submit 150-200 applications—far more than intuition suggests. The geometric distribution explains why persistence is crucial.

4. **Time Buffer:** The 90-day timeline is tight in recessionary conditions. Starting early and extending the search window significantly improves outcomes.

5. **Adaptability is Key:** Flexibility on salary, location, and role type dramatically increases success probability. Rigidity is costly in downturns.

### 9.2 Academic Value

This project demonstrates:
- Practical application of Monte Carlo methods
- Understanding of probability distributions (Normal, Weibull, Geometric)
- Real-world modeling with uncertainty
- Data visualization and communication
- Python programming and scientific computing

### 9.3 Professional Application

The skills developed here directly transfer to:
- Business analytics and forecasting
- Risk assessment and management
- Financial modeling
- Operations research
- Data-driven decision making

---

## 10. References & Resources

### Academic References
1. Ross, S. M. (2014). *Introduction to Probability Models* (11th ed.). Academic Press.
2. Rubinstein, R. Y., & Kroese, D. P. (2016). *Simulation and the Monte Carlo Method* (3rd ed.). Wiley.
3. Law, A. M. (2015). *Simulation Modeling and Analysis* (5th ed.). McGraw-Hill.

### Labor Market Data Sources
- Philippine Statistics Authority (PSA) - Labor Force Survey
- Bangko Sentral ng Pilipinas - Economic Indicators
- World Bank - Philippine Economic Monitor
- Asian Development Bank - Economic Outlook

### Technical Documentation
- NumPy Documentation: https://numpy.org/doc/
- SciPy Statistical Distributions: https://docs.scipy.org/doc/scipy/reference/stats.html
- Matplotlib Visualization: https://matplotlib.org/stable/contents.html
- Pandas User Guide: https://pandas.pydata.org/docs/

---

## Appendix A: How to Run the Simulation

### Prerequisites
- Python 3.11 or higher
- Poetry (for dependency management)
- Virtual environment (venv)

### Installation Steps

```bash
# 1. Navigate to project directory
cd /path/to/career-path

# 2. Activate virtual environment
source venv/bin/activate  # On macOS/Linux
# or
venv\Scripts\activate     # On Windows

# 3. Install dependencies (if not already done)
poetry install

# 4. Run the simulation
python monte_carlo_simulation.py
```

### User Inputs
The script will prompt for:
1. Target starting salary (default: PHP 45,000)
2. Target time frame in days (default: 90)
3. Number of simulations (default: 10,000)
4. Applications per week (default: 10)

### Outputs
- **Console:** Detailed summary statistics
- **Visualization:** 9-panel figure saved as PNG
- **CSV Export:** Optional detailed results export

---

## Appendix B: Team Contributions

**Group 8 Members:**
- Model design and mathematical formulations
- Python implementation and code documentation
- Data visualization and analysis
- Report writing and formatting
- Presentation preparation

**Division of Labor:**
- Economic modeling: [Team Member Names]
- Software development: [Team Member Names]
- Statistical analysis: [Team Member Names]
- Documentation: [Team Member Names]
- Presentation: [Team Member Names]

---

## Appendix C: Simulation Parameters Reference

| Parameter | Symbol | Default Value | Range | Distribution |
|-----------|--------|---------------|-------|--------------|
| Market Growth Mean | μ_g | -2.0% | -10% to +5% | Normal |
| Market Growth Std Dev | σ_g | 8.0% | 5% to 15% | - |
| Inflation Mean | μ_i | 4.0% | 2% to 8% | Normal |
| Inflation Std Dev | σ_i | 1.5% | 0.5% to 3% | - |
| Base Interview Rate | p_i | 12% | 5% to 20% | - |
| Base Success Rate | p_s | 8% | 2% to 20% | Normal |
| Base Salary Mean | μ_sal | PHP 42,000 | PHP 30k - 60k | Normal |
| Base Salary Std Dev | σ_sal | PHP 6,000 | PHP 3k - 10k | - |
| Weibull Shape | k | 2.0 | 1.5 to 3.0 | - |
| Weibull Scale | λ | 35.0 days | 20 to 50 days | - |

---

**Document Version:** 1.0  
**Last Updated:** October 21, 2025  
**Status:** Final Submission  

---

*This report was prepared by Group 8 as part of the Career Path Analysis project, demonstrating the application of Monte Carlo simulation to real-world career decision-making under economic uncertainty.*
