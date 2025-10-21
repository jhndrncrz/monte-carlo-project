# Quick Start Guide
## Career Path Monte Carlo Simulation - Group 8

### 🚀 Running the Simulation in 3 Steps

#### Step 1: Activate Virtual Environment
```bash
cd /Users/jhndrncrz/Projects/career-path
source venv/bin/activate
```

#### Step 2: Run the Simulation
```bash
python monte_carlo_simulation.py
```

#### Step 3: Respond to Prompts
```
Enter target starting salary (PHP) [default: 45000]: [Press Enter or type amount]
Enter target time frame (days) [default: 90]: [Press Enter or type days]
Enter number of simulations [default: 10000]: [Press Enter or type number]
Enter applications per week [default: 10]: [Press Enter or type number]
```

**Tip:** Just press Enter to use all default values for a quick test run.

---

### 📊 What You'll Get

1. **Console Output:**
   - Success probabilities (salary, time, overall)
   - Statistical summary (mean, median, percentiles)
   - Recommendations for your job search strategy

2. **Visualization:**
   - A comprehensive 9-panel figure saved as PNG
   - File name: `simulation_results_YYYYMMDD_HHMMSS.png`

3. **Data Export (Optional):**
   - CSV file with all simulation results
   - File name: `simulation_results_YYYYMMDD_HHMMSS.csv`

---

### ⚡ Quick Test Run

For a fast test (takes ~10 seconds):
```bash
python monte_carlo_simulation.py
# When prompted, enter:
# Salary: 45000 (or press Enter)
# Days: 90 (or press Enter)
# Simulations: 1000 (instead of default 10000)
# Apps/week: 10 (or press Enter)
```

---

### 📁 Project Files Overview

| File | Purpose | Size |
|------|---------|------|
| `monte_carlo_simulation.py` | Main simulation script | ~700 lines |
| `REPORT.md` | Detailed project report | ~10 pages |
| `PRESENTATION_PITCH.md` | Presentation script | ~12 slides |
| `README.md` | Full documentation | Comprehensive |
| `pyproject.toml` | Dependencies | Auto-generated |

---

### 🎯 Default Simulation Parameters

- **Target Salary:** PHP 45,000
- **Target Time:** 90 days
- **Simulations:** 10,000 iterations
- **Application Rate:** 10 per week
- **Market Growth:** -2% mean, 8% std dev
- **Inflation:** 4% mean, 1.5% std dev

---

### 💡 Tips for Best Results

1. **Use 10,000+ simulations** for stable results (more = better)
2. **Allow 1-2 minutes** for full simulation to complete
3. **Check the plots** - they tell the full story
4. **Export CSV** if you want to do further analysis in Excel
5. **Try different parameters** to see how outcomes change

---

### 🛠️ Troubleshooting

**Problem:** `ModuleNotFoundError`
**Solution:** Make sure virtual environment is activated and run `poetry install`

**Problem:** Plots don't display
**Solution:** Check if matplotlib backend is configured. On some systems, you may need to install additional graphics libraries.

**Problem:** Simulation too slow
**Solution:** Reduce number of simulations to 1000-5000 for faster testing

**Problem:** Want to change economic parameters
**Solution:** Edit the values in the `__init__` method of the class (lines 35-60)

---

### 📞 Need Help?

1. Check `README.md` for comprehensive documentation
2. Read `REPORT.md` Section 3 for methodology details
3. Review code comments - every function is documented
4. Test with smaller simulation counts first

---

### ✅ Checklist Before Presentation

- [ ] Run full simulation with default parameters
- [ ] Verify all 9 plots are generated
- [ ] Review console output for key statistics
- [ ] Practice explaining the ~50% success rate
- [ ] Prepare to discuss 150-200 application recommendation
- [ ] Review PRESENTATION_PITCH.md speaker notes
- [ ] Have backup answers for Q&A ready

---

**You're all set! Good luck with your project! 🎓**
