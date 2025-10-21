# Sample Output Example
## Monte Carlo Simulation Results

This document shows what you can expect when running the simulation with default parameters.

---

## Console Output Example

```
======================================================================
MONTE CARLO SIMULATION - ECONOMIC DOWNTURN STRESS TEST
======================================================================

Simulation Parameters:
  Target Salary: PHP 45,000.00
  Target Time Frame: 90 days
  Number of Simulations: 10,000
  Applications per Week: 10

Economic Conditions:
  Market Growth Mean: -2.0%
  Inflation Mean: 4.0%

Running simulation...

======================================================================
SIMULATION COMPLETE
======================================================================

======================================================================
SIMULATION RESULTS SUMMARY
======================================================================

📊 SUCCESS PROBABILITIES:
  • Achieving salary target (≥ PHP 45,000.00):
    67.34%

  • Securing offer within 90 days:
    76.89%

  • OVERALL SUCCESS (both targets met):
    53.21%

💰 SALARY STATISTICS:
  • Mean Salary Offer: PHP 41,234.56
  • Median Salary Offer: PHP 41,089.23
  • Std Deviation: PHP 6,234.78
  • 25th Percentile: PHP 36,890.45
  • 75th Percentile: PHP 45,678.90
  • 90th Percentile: PHP 49,567.12

⏱️  TIME STATISTICS:
  • Mean Time to Offer: 44.7 days
  • Median Time to Offer: 41.2 days

📝 APPLICATION STATISTICS:
  • Mean Applications Needed: 87
  • Median Applications Needed: 71

📉 ECONOMIC CONDITIONS:
  • Mean Economic Severity Index: 0.38
    (0 = mild downturn, 1 = severe recession)

======================================================================
💡 RECOMMENDATIONS
======================================================================

To achieve 80% confidence of success:
  • Submit at least 168 applications
  • Maintain pace for at least 17 weeks
  • Start job search early (market conditions are challenging)

During economic downturn, consider:
  • Expanding job search to adjacent fields
  • Increasing networking efforts (referrals matter more)
  • Being flexible on salary expectations initially
  • Building recession-proof skills
  • Considering temporary/contract work to bridge gaps

======================================================================

📊 Generating visualizations...
📊 Plots saved to: simulation_results_20251021_220530.png

💾 Export results to CSV? (y/n) [default: y]: y
💾 Results exported to: simulation_results_20251021_220530.csv

======================================================================
✅ SIMULATION COMPLETE
======================================================================

Thank you for using the Career Path Simulation tool!
Group 8 - Economic Downturn Stress Test
```

---

## Interpretation Guide

### Success Probabilities

**67.34% - Salary Target**
- About 2 in 3 graduates will achieve PHP 45,000 or higher
- Not guaranteed, but reasonably achievable
- Economic downturn reduces from typical 80-85%

**76.89% - Time Target**
- About 3 in 4 will get an offer within 90 days
- Most hiring processes complete in 30-60 days
- Some extend to 80-100 days due to economic delays

**53.21% - Overall Success**
- Only about 1 in 2 achieve BOTH targets
- This is the critical metric for planning
- Requires either flexibility or backup plan

### Salary Distribution

**Mean vs. Target Gap:**
- Mean offer (PHP 41,234) is below target (PHP 45,000)
- This is expected in recessionary conditions
- Gap of about 8.4% reflects market pressure

**Percentiles:**
- 25th percentile (PHP 36,890): Lower quartile—tough conditions
- 75th percentile (PHP 45,678): Upper quartile—meets target
- 90th percentile (PHP 49,567): Best case scenarios

**Interpretation:**
If you're in the top 25% of candidates or get lucky with timing, you'll exceed the target. Otherwise, expect slightly below.

### Time Statistics

**44.7 days mean:**
- Average hiring process takes about 6.5 weeks
- Faster than worst-case, slower than best-case
- Allows buffer within 90-day window

**41.2 days median:**
- Half of offers come in 6 weeks or less
- Median < Mean indicates right-skewed distribution
- Some very long processes pull the mean up

### Applications Required

**87 mean, 71 median:**
- Typical job seeker needs 71-87 applications
- Some get lucky with 20-30 applications
- Others need 150-200 applications
- High variance due to geometric distribution

**For 80% confidence: 168 applications**
- This accounts for unlucky scenarios
- Ensures success in 8 out of 10 parallel universes
- Aggressive but achievable: 10/week for 17 weeks

### Economic Severity

**0.38 index (moderate downturn):**
- Not mild (0-0.3) but not severe (0.6-1.0)
- Moderate challenges expected
- Strategy should be enhanced, not desperate

---

## Visualization Descriptions

### 1. Salary Offer Distribution
**What it shows:**
- Histogram of 10,000 salary outcomes
- Bell curve centered around PHP 41,000
- Target line at PHP 45,000 on the right side
- Mean line at PHP 41,234

**Key insight:**
Most of the distribution is below target—flexibility may be needed.

### 2. Time to Offer Distribution
**What it shows:**
- Right-skewed (Weibull) distribution
- Peak around 30-35 days
- Long tail extending to 80+ days
- 90-day target line

**Key insight:**
Most offers come in 30-50 days, but outliers exist.

### 3. Success Probabilities
**What it shows:**
- Three bars: Salary (67%), Time (77%), Overall (53%)
- Percentages labeled on top
- Color-coded for clarity

**Key insight:**
Meeting individual targets is easier than meeting both.

### 4. Salary vs Economic Severity
**What it shows:**
- Scatter plot with 10,000 points
- X-axis: Economic severity (0-1)
- Y-axis: Salary offer
- Color: Green = success, Red = failure

**Key insight:**
Higher severity → lower salaries. Clear negative correlation.

### 5. Applications Needed Distribution
**What it shows:**
- Right-skewed histogram
- Most people need 50-100 applications
- Some need 200+ (geometric distribution tail)

**Key insight:**
High variance—your experience may differ significantly.

### 6. Time vs Economic Severity
**What it shows:**
- Scatter plot showing positive correlation
- Worse economy → longer hiring processes
- Color indicates meeting time target

**Key insight:**
In severe recessions, expect 50-70 day processes.

### 7. Salary vs Time Scatter
**What it shows:**
- 2D scatter with success zones
- Upper-left quadrant: Success (high salary, quick)
- Lower-right quadrant: Failure (low salary, slow)

**Key insight:**
Success requires both dimensions aligning.

### 8. Economic Conditions
**What it shows:**
- Dual histogram of market growth and inflation
- Market growth centered at -2% (negative)
- Inflation centered at 4%

**Key insight:**
Validates recession conditions being modeled.

### 9. Success Rate vs Applications
**What it shows:**
- Curve showing probability increases with applications
- Steep rise from 0-100 applications
- Flattens after 150-200 applications
- 80% target line

**Key insight:**
150-200 applications hits sweet spot for effort vs. returns.

---

## How to Use These Results

### If Overall Success is < 40%
**Action:** Severe conditions. Consider:
- Extending timeline to 120 days
- Lowering salary target to PHP 40,000
- Expanding to adjacent fields
- Geographic flexibility

### If Overall Success is 40-60%
**Action:** Moderate conditions. Recommended:
- Standard strategy: 150-200 applications
- Start early (30 days before deadline)
- Build strong network
- Maintain quality applications

### If Overall Success is > 60%
**Action:** Favorable conditions. Optimize:
- Can be more selective
- Fewer applications needed (100-120)
- Focus on top-choice roles
- Less compromise required

---

## Comparing Your Results

**Run the simulation multiple times:**
- Results will vary slightly (Monte Carlo randomness)
- Look for consistent patterns, not exact numbers
- If variance is high, increase simulations to 20,000+

**Expected ranges with 10,000 simulations:**
- Overall success: 50-55%
- Mean salary: PHP 40,000-42,000
- Mean time: 42-48 days
- Recommended apps: 150-180

**If your results fall outside these ranges:**
- Check parameters (did you change defaults?)
- Review economic conditions (severity might be different)
- Consider re-running with more simulations

---

## CSV Output Format

The exported CSV contains these columns:

| Column | Description | Range |
|--------|-------------|-------|
| market_growth | Sampled market growth rate | -0.20 to 0.10 |
| inflation_rate | Sampled inflation rate | 0.01 to 0.08 |
| economic_severity | Calculated severity index | 0 to 1 |
| success_rate | Interview success rate | 0.02 to 0.20 |
| salary_offer | Generated salary offer | 25,000 to 100,000 |
| time_to_offer | Time to receive offer (days) | 7 to 100+ |
| applications_needed | Applications until success | 1 to 500+ |
| days_searching | Days of active search | 7 to 350+ |
| salary_success | Met salary target? | True/False |
| time_success | Met time target? | True/False |
| overall_success | Met both targets? | True/False |

**Use cases for CSV:**
- Excel pivot tables for custom analysis
- Additional visualization in Tableau/Power BI
- Statistical testing in R or SPSS
- Sharing with advisors for deeper review

---

## Quick Interpretation Flowchart

```
Start: Look at Overall Success %
    │
    ├─ > 70%: Great odds! Standard job search strategy
    │
    ├─ 50-70%: Moderate odds. Follow 150-200 app recommendation
    │
    ├─ 30-50%: Challenging. Need flexibility on salary OR time
    │
    └─ < 30%: Very difficult. Major adjustments needed
                - Lower salary target by 15-20%, OR
                - Extend timeline to 120 days, OR
                - Expand to multiple fields/locations

Then: Check Economic Severity
    │
    ├─ < 0.3 (Mild): Economy recovering, conditions improving
    │
    ├─ 0.3-0.6 (Moderate): Typical recession, plan accordingly
    │
    └─ > 0.6 (Severe): Deep recession, survival strategies needed

Finally: Review Application Recommendation
    │
    └─ Aim for 80% confidence number
        Set weekly goals (divide by 12-16 weeks)
        Track progress religiously
        Adjust if hit rates differ from model
```

---

## Example Real-World Application

**Scenario:** You just ran the simulation and got:
- Overall success: 48%
- Recommended apps: 175
- Mean salary: PHP 40,500

**Your response:**

1. **Set realistic expectations:**
   - "I have about a 50-50 chance with current targets"
   - "This is not a guarantee—I need contingencies"

2. **Develop your strategy:**
   - "175 applications over 16 weeks = 11 per week"
   - "I'll start now, not wait for graduation"
   - "Every Monday: 5 apps, Every Thursday: 6 apps"

3. **Build flexibility:**
   - "If I get PHP 42,000 offer at day 60, I'll seriously consider it"
   - "I'll expand to data analyst roles, not just developer"
   - "Remote positions give me 3x more options"

4. **Monitor and adapt:**
   - "After 50 applications, check my interview rate"
   - "If < 10%, my resume needs work"
   - "If > 15%, I can be slightly more selective"

5. **Prepare backup plan:**
   - "If day 75 arrives with no offers, I'll lower salary target to PHP 40k"
   - "I'll consider 3-month contract roles as entry points"
   - "I'll network intensively—referrals are 3-5x more effective"

**Result:**
By treating the simulation as a planning tool, not a prediction, you maximize your actual chances of success.

---

## Common Questions About Output

**Q: Why is overall success so much lower than individual targets?**
A: Probability multiplication. 70% × 80% ≈ 56%. Both need to happen, which is harder than just one.

**Q: Can I improve my odds beyond what the model shows?**
A: Yes! The model assumes average candidate. Top performers (exceptional portfolio, strong network, great interviewing) can multiply success rates by 1.5-2x.

**Q: What if my actual results differ from the simulation?**
A: Simulation shows expected value across many parallel universes. YOUR universe is just one sample. You might get lucky (succeed faster) or unlucky (struggle more). That's the nature of probability.

**Q: Should I stop after 87 applications (the mean)?**
A: No! That's the average, but it has high variance. The 168 recommendation accounts for unlucky scenarios. Don't stop until you have an acceptable offer.

**Q: How often should I re-run the simulation?**
A: Initially, once to set your baseline strategy. Then, re-run every month if economic conditions change significantly (e.g., recession deepens or improves).

---

**This output represents 10,000 simulated job searches. Your actual experience will be one path through this probability space. Use these insights to optimize your strategy, not as a crystal ball.**

---

*Document created: October 21, 2025*  
*Group 8 - Career Path Monte Carlo Simulation*
