"""
Monte Carlo Simulation for Job Search Success Probability
Group 8: Economic Downturn Stress Test (All Fields)

This script simulates the probability of achieving a target starting salary
and securing a job offer within a specific time frame during economic uncertainty.

Author: Group 8
- Cruz, John Adrian B.
- Dumable, Racy Anne M.
- Ferrer, Jamie Noreen C.
- Gatche, John Mark M.
- Urcia, John Lawrence H.
Date: October 21, 2025
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import pandas as pd
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Set style for better-looking plots
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)


class EconomicDownturnJobSearchSimulation:
    """
    Monte Carlo simulation for job search outcomes during economic downturn.
    
    Models the impact of:
    - Market growth rate (with negative/zero mean during downturn)
    - Inflation effects on salary offers
    - Economic uncertainty on interview success rates
    - Time to offer variability
    """
    
    def __init__(self, 
                 target_salary=45000,
                 target_days=90,
                 num_simulations=10000,
                 applications_per_week=10):
        """
        Initialize simulation parameters.
        
        Parameters:
        -----------
        target_salary : float
            Target starting salary in PHP
        target_days : int
            Target number of days to secure a job offer
        num_simulations : int
            Number of Monte Carlo simulations to run
        applications_per_week : int
            Number of job applications submitted per week
        """
        self.target_salary = target_salary
        self.target_days = target_days
        self.num_simulations = num_simulations
        self.applications_per_week = applications_per_week
        
        # Economic downturn parameters
        self.market_growth_mean = -0.02  # -2% mean growth (recession)
        self.market_growth_std = 0.08    # High volatility
        self.inflation_mean = 0.04       # 4% inflation mean
        self.inflation_std = 0.015       # 1.5% inflation std
        
        # Base job search parameters (adjusted for downturn)
        self.base_interview_rate = 0.12  # 12% of applications lead to interview
        self.base_success_rate = 0.08    # 8% interview success (lower in downturn)
        self.base_salary_mean = 42000    # Lower base salary in downturn
        self.base_salary_std = 6000      # Salary variability
        
        # Time parameters (Weibull distribution)
        self.time_shape = 2.0            # Shape parameter (controls distribution shape)
        self.time_scale = 35.0           # Scale parameter (average ~30 days)
        
        # Results storage
        self.results = None
        self.summary_stats = None
        
    def simulate_economic_conditions(self):
        """Simulate economic conditions for each iteration."""
        # Market growth rate (negative or near-zero during downturn)
        market_growth = np.random.normal(
            self.market_growth_mean, 
            self.market_growth_std, 
            self.num_simulations
        )
        
        # Inflation rate
        inflation_rate = np.random.normal(
            self.inflation_mean,
            self.inflation_std,
            self.num_simulations
        )
        
        # Economic severity index (0 = mild, 1 = severe downturn)
        # Based on how negative the growth is
        economic_severity = np.clip(-market_growth / 0.10, 0, 1)
        
        return market_growth, inflation_rate, economic_severity
    
    def simulate_interview_success(self, economic_severity):
        """
        Simulate interview success rate adjusted for economic conditions.
        
        During downturns:
        - More competition for fewer jobs
        - Companies are more selective
        - Success rates decrease with severity
        """
        # Adjust success rate based on economic severity
        adjusted_success_rate = self.base_success_rate * (1 - 0.4 * economic_severity)
        
        # Add individual variability
        success_rates = np.random.normal(
            adjusted_success_rate,
            0.03,  # 3% standard deviation
            self.num_simulations
        )
        
        # Clip to realistic bounds
        success_rates = np.clip(success_rates, 0.02, 0.20)
        
        return success_rates
    
    def simulate_salary_offers(self, market_growth, inflation_rate, economic_severity):
        """
        Simulate salary offers adjusted for economic conditions.
        
        Salary is affected by:
        - Market growth (negative = lower salaries)
        - Inflation (increases nominal salary needs)
        - Economic severity (reduces employer budgets)
        """
        # Base salary adjusted for market conditions
        market_adjustment = 1 + market_growth
        
        # Inflation adjustment (employers may not fully adjust for inflation in downturn)
        inflation_adjustment = 1 + (inflation_rate * 0.5)  # Only 50% adjustment
        
        # Severity penalty (companies cut budgets in severe downturns)
        severity_penalty = 1 - (0.15 * economic_severity)
        
        # Combined adjustment
        adjusted_salary_mean = (self.base_salary_mean * 
                               market_adjustment * 
                               inflation_adjustment * 
                               severity_penalty)
        
        # Generate salary offers with high variability
        salaries = np.random.normal(
            adjusted_salary_mean,
            self.base_salary_std * (1 + 0.3 * economic_severity),  # More variability
            self.num_simulations
        )
        
        # Ensure realistic minimums
        salaries = np.clip(salaries, 25000, 100000)
        
        return salaries
    
    def simulate_time_to_offer(self, economic_severity):
        """
        Simulate time to receive job offer using Weibull distribution.
        
        During downturns:
        - Hiring processes take longer (budget approvals, layoffs, etc.)
        - Time scale increases with severity
        """
        # Adjust time scale based on economic severity
        adjusted_scale = self.time_scale * (1 + 0.5 * economic_severity)
        
        # Generate times using Weibull distribution
        times = np.random.weibull(self.time_shape, self.num_simulations) * adjusted_scale
        
        # Add some minimum processing time
        times = times + 7  # At least 7 days
        
        return times
    
    def calculate_applications_needed(self, success_rate):
        """
        Calculate number of applications needed based on success rate.
        
        Uses geometric distribution to model "trials until success"
        """
        # Interview rate (percentage that lead to interviews)
        interview_rate = self.base_interview_rate
        
        # Combined probability (application -> interview -> offer)
        combined_success_rate = interview_rate * success_rate
        
        # Simulate number of applications until success (geometric distribution)
        applications_needed = np.random.geometric(
            combined_success_rate,
            self.num_simulations
        )
        
        return applications_needed
    
    def run_simulation(self):
        """Run the complete Monte Carlo simulation."""
        print("=" * 70)
        print("MONTE CARLO SIMULATION - ECONOMIC DOWNTURN STRESS TEST")
        print("=" * 70)
        print(f"\nSimulation Parameters:")
        print(f"  Target Salary: PHP {self.target_salary:,.2f}")
        print(f"  Target Time Frame: {self.target_days} days")
        print(f"  Number of Simulations: {self.num_simulations:,}")
        print(f"  Applications per Week: {self.applications_per_week}")
        print(f"\nEconomic Conditions:")
        print(f"  Market Growth Mean: {self.market_growth_mean:.1%}")
        print(f"  Inflation Mean: {self.inflation_mean:.1%}")
        print(f"\nRunning simulation...")
        
        # Step 1: Simulate economic conditions
        market_growth, inflation_rate, economic_severity = self.simulate_economic_conditions()
        
        # Step 2: Simulate interview success rates
        success_rates = self.simulate_interview_success(economic_severity)
        
        # Step 3: Simulate salary offers
        salary_offers = self.simulate_salary_offers(
            market_growth, 
            inflation_rate, 
            economic_severity
        )
        
        # Step 4: Simulate time to offer
        time_to_offer = self.simulate_time_to_offer(economic_severity)
        
        # Step 5: Calculate applications needed
        applications_needed = self.calculate_applications_needed(success_rates)
        
        # Step 6: Calculate weeks of job searching
        weeks_needed = np.ceil(applications_needed / self.applications_per_week)
        days_searching = weeks_needed * 7
        
        # Step 7: Determine success outcomes
        salary_success = salary_offers >= self.target_salary
        time_success = time_to_offer <= self.target_days
        overall_success = salary_success & time_success
        
        # Store results in DataFrame
        self.results = pd.DataFrame({
            'market_growth': market_growth,
            'inflation_rate': inflation_rate,
            'economic_severity': economic_severity,
            'success_rate': success_rates,
            'salary_offer': salary_offers,
            'time_to_offer': time_to_offer,
            'applications_needed': applications_needed,
            'days_searching': days_searching,
            'salary_success': salary_success,
            'time_success': time_success,
            'overall_success': overall_success
        })
        
        # Calculate summary statistics
        self._calculate_summary_stats()
        
        print("\n" + "=" * 70)
        print("SIMULATION COMPLETE")
        print("=" * 70)
        
        return self.results
    
    def _calculate_summary_stats(self):
        """Calculate summary statistics from simulation results."""
        self.summary_stats = {
            'probability_salary_target': self.results['salary_success'].mean(),
            'probability_time_target': self.results['time_success'].mean(),
            'probability_overall_success': self.results['overall_success'].mean(),
            'mean_salary': self.results['salary_offer'].mean(),
            'median_salary': self.results['salary_offer'].median(),
            'std_salary': self.results['salary_offer'].std(),
            'mean_time': self.results['time_to_offer'].mean(),
            'median_time': self.results['time_to_offer'].median(),
            'mean_applications': self.results['applications_needed'].mean(),
            'median_applications': self.results['applications_needed'].median(),
            'percentile_25_salary': self.results['salary_offer'].quantile(0.25),
            'percentile_75_salary': self.results['salary_offer'].quantile(0.75),
            'percentile_90_salary': self.results['salary_offer'].quantile(0.90),
            'mean_economic_severity': self.results['economic_severity'].mean(),
        }
    
    def print_summary(self):
        """Print summary statistics."""
        if self.summary_stats is None:
            print("Error: No simulation results available. Run simulation first.")
            return
        
        print("\n" + "=" * 70)
        print("SIMULATION RESULTS SUMMARY")
        print("=" * 70)
        
        print(f"\n📊 SUCCESS PROBABILITIES:")
        print(f"  • Achieving salary target (≥ PHP {self.target_salary:,.2f}):")
        print(f"    {self.summary_stats['probability_salary_target']:.2%}")
        
        print(f"\n  • Securing offer within {self.target_days} days:")
        print(f"    {self.summary_stats['probability_time_target']:.2%}")
        
        print(f"\n  • OVERALL SUCCESS (both targets met):")
        print(f"    {self.summary_stats['probability_overall_success']:.2%}")
        
        print(f"\n💰 SALARY STATISTICS:")
        print(f"  • Mean Salary Offer: PHP {self.summary_stats['mean_salary']:,.2f}")
        print(f"  • Median Salary Offer: PHP {self.summary_stats['median_salary']:,.2f}")
        print(f"  • Std Deviation: PHP {self.summary_stats['std_salary']:,.2f}")
        print(f"  • 25th Percentile: PHP {self.summary_stats['percentile_25_salary']:,.2f}")
        print(f"  • 75th Percentile: PHP {self.summary_stats['percentile_75_salary']:,.2f}")
        print(f"  • 90th Percentile: PHP {self.summary_stats['percentile_90_salary']:,.2f}")
        
        print(f"\n⏱️  TIME STATISTICS:")
        print(f"  • Mean Time to Offer: {self.summary_stats['mean_time']:.1f} days")
        print(f"  • Median Time to Offer: {self.summary_stats['median_time']:.1f} days")
        
        print(f"\n📝 APPLICATION STATISTICS:")
        print(f"  • Mean Applications Needed: {self.summary_stats['mean_applications']:.0f}")
        print(f"  • Median Applications Needed: {self.summary_stats['median_applications']:.0f}")
        
        print(f"\n📉 ECONOMIC CONDITIONS:")
        print(f"  • Mean Economic Severity Index: {self.summary_stats['mean_economic_severity']:.2f}")
        print(f"    (0 = mild downturn, 1 = severe recession)")
        
        # Recommendations
        print(f"\n" + "=" * 70)
        print("💡 RECOMMENDATIONS")
        print("=" * 70)
        
        # Calculate recommended applications for 80% success rate
        success_80_mask = self.results['overall_success'] == True
        if success_80_mask.sum() > 0:
            apps_80 = self.results.loc[success_80_mask, 'applications_needed'].quantile(0.80)
            weeks_80 = np.ceil(apps_80 / self.applications_per_week)
            print(f"\nTo achieve 80% confidence of success:")
            print(f"  • Submit at least {apps_80:.0f} applications")
            print(f"  • Maintain pace for at least {weeks_80:.0f} weeks")
            print(f"  • Start job search early (market conditions are challenging)")
        
        print(f"\nDuring economic downturn, consider:")
        print(f"  • Expanding job search to adjacent fields")
        print(f"  • Increasing networking efforts (referrals matter more)")
        print(f"  • Being flexible on salary expectations initially")
        print(f"  • Building recession-proof skills")
        print(f"  • Considering temporary/contract work to bridge gaps")
        
        print("\n" + "=" * 70)
    
    def plot_results(self):
        """Generate comprehensive visualization of simulation results."""
        if self.results is None:
            print("Error: No simulation results available. Run simulation first.")
            return
        
        # Create figure with subplots
        fig = plt.figure(figsize=(20, 12))
        
        # 1. Salary Distribution
        ax1 = plt.subplot(3, 3, 1)
        self._plot_salary_distribution(ax1)
        
        # 2. Time to Offer Distribution
        ax2 = plt.subplot(3, 3, 2)
        self._plot_time_distribution(ax2)
        
        # 3. Success Rate Comparison
        ax3 = plt.subplot(3, 3, 3)
        self._plot_success_rates(ax3)
        
        # 4. Salary vs Economic Severity
        ax4 = plt.subplot(3, 3, 4)
        self._plot_salary_vs_severity(ax4)
        
        # 5. Applications Needed Distribution
        ax5 = plt.subplot(3, 3, 5)
        self._plot_applications_distribution(ax5)
        
        # 6. Time vs Economic Severity
        ax6 = plt.subplot(3, 3, 6)
        self._plot_time_vs_severity(ax6)
        
        # 7. Salary vs Time Scatter
        ax7 = plt.subplot(3, 3, 7)
        self._plot_salary_vs_time(ax7)
        
        # 8. Economic Conditions Distribution
        ax8 = plt.subplot(3, 3, 8)
        self._plot_economic_conditions(ax8)
        
        # 9. Success Probability by Applications
        ax9 = plt.subplot(3, 3, 9)
        self._plot_success_vs_applications(ax9)
        
        plt.tight_layout()
        
        # Save figure in multiple formats
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Save as PNG
        png_filename = f"simulation_results_{timestamp}.png"
        plt.savefig(png_filename, dpi=300, bbox_inches='tight')
        print(f"\n📊 Plots saved to: {png_filename}")
        
        # Save as SVG
        svg_filename = f"simulation_results_{timestamp}.svg"
        plt.savefig(svg_filename, format='svg', bbox_inches='tight')
        print(f"📊 Plots saved to: {svg_filename}")
        
        plt.show()
    
    def _plot_salary_distribution(self, ax):
        """Plot salary distribution with target line."""
        ax.hist(self.results['salary_offer'], bins=50, alpha=0.7, 
                color='skyblue', edgecolor='black')
        ax.axvline(self.target_salary, color='red', linestyle='--', 
                   linewidth=2, label=f'Target: PHP {self.target_salary:,.0f}')
        ax.axvline(self.results['salary_offer'].mean(), color='green', 
                   linestyle='--', linewidth=2, label=f'Mean: PHP {self.results["salary_offer"].mean():,.0f}')
        ax.set_xlabel('Salary Offer (PHP)', fontsize=10, fontweight='bold')
        ax.set_ylabel('Frequency', fontsize=10, fontweight='bold')
        ax.set_title('Salary Offer Distribution', fontsize=12, fontweight='bold')
        ax.legend()
        ax.grid(True, alpha=0.3)
    
    def _plot_time_distribution(self, ax):
        """Plot time to offer distribution."""
        ax.hist(self.results['time_to_offer'], bins=50, alpha=0.7, 
                color='lightcoral', edgecolor='black')
        ax.axvline(self.target_days, color='red', linestyle='--', 
                   linewidth=2, label=f'Target: {self.target_days} days')
        ax.axvline(self.results['time_to_offer'].mean(), color='green', 
                   linestyle='--', linewidth=2, label=f'Mean: {self.results["time_to_offer"].mean():.1f} days')
        ax.set_xlabel('Time to Offer (days)', fontsize=10, fontweight='bold')
        ax.set_ylabel('Frequency', fontsize=10, fontweight='bold')
        ax.set_title('Time to Offer Distribution', fontsize=12, fontweight='bold')
        ax.legend()
        ax.grid(True, alpha=0.3)
    
    def _plot_success_rates(self, ax):
        """Plot success rate comparison."""
        success_data = {
            'Salary Target': self.summary_stats['probability_salary_target'] * 100,
            'Time Target': self.summary_stats['probability_time_target'] * 100,
            'Overall Success': self.summary_stats['probability_overall_success'] * 100
        }
        
        bars = ax.bar(success_data.keys(), success_data.values(), 
                      color=['skyblue', 'lightcoral', 'lightgreen'],
                      edgecolor='black', linewidth=1.5)
        
        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{height:.1f}%',
                   ha='center', va='bottom', fontweight='bold')
        
        ax.set_ylabel('Probability (%)', fontsize=10, fontweight='bold')
        ax.set_title('Success Probabilities', fontsize=12, fontweight='bold')
        ax.set_ylim(0, 100)
        ax.grid(True, alpha=0.3, axis='y')
    
    def _plot_salary_vs_severity(self, ax):
        """Plot salary vs economic severity."""
        scatter = ax.scatter(self.results['economic_severity'], 
                           self.results['salary_offer'],
                           c=self.results['overall_success'],
                           cmap='RdYlGn', alpha=0.5, s=10)
        ax.axhline(self.target_salary, color='red', linestyle='--', 
                   linewidth=2, alpha=0.7)
        ax.set_xlabel('Economic Severity Index', fontsize=10, fontweight='bold')
        ax.set_ylabel('Salary Offer (PHP)', fontsize=10, fontweight='bold')
        ax.set_title('Salary vs Economic Severity', fontsize=12, fontweight='bold')
        plt.colorbar(scatter, ax=ax, label='Success')
        ax.grid(True, alpha=0.3)
    
    def _plot_applications_distribution(self, ax):
        """Plot distribution of applications needed."""
        ax.hist(self.results['applications_needed'], bins=50, alpha=0.7,
                color='plum', edgecolor='black')
        ax.axvline(self.results['applications_needed'].mean(), color='green',
                   linestyle='--', linewidth=2, 
                   label=f'Mean: {self.results["applications_needed"].mean():.0f}')
        ax.axvline(self.results['applications_needed'].median(), color='orange',
                   linestyle='--', linewidth=2,
                   label=f'Median: {self.results["applications_needed"].median():.0f}')
        ax.set_xlabel('Applications Needed', fontsize=10, fontweight='bold')
        ax.set_ylabel('Frequency', fontsize=10, fontweight='bold')
        ax.set_title('Applications Needed Distribution', fontsize=12, fontweight='bold')
        ax.legend()
        ax.grid(True, alpha=0.3)
    
    def _plot_time_vs_severity(self, ax):
        """Plot time to offer vs economic severity."""
        scatter = ax.scatter(self.results['economic_severity'],
                           self.results['time_to_offer'],
                           c=self.results['time_success'],
                           cmap='RdYlGn', alpha=0.5, s=10)
        ax.axhline(self.target_days, color='red', linestyle='--',
                   linewidth=2, alpha=0.7)
        ax.set_xlabel('Economic Severity Index', fontsize=10, fontweight='bold')
        ax.set_ylabel('Time to Offer (days)', fontsize=10, fontweight='bold')
        ax.set_title('Time to Offer vs Economic Severity', fontsize=12, fontweight='bold')
        plt.colorbar(scatter, ax=ax, label='Within Target Time')
        ax.grid(True, alpha=0.3)
    
    def _plot_salary_vs_time(self, ax):
        """Plot salary vs time to offer scatter."""
        success = self.results['overall_success']
        
        ax.scatter(self.results.loc[~success, 'time_to_offer'],
                  self.results.loc[~success, 'salary_offer'],
                  c='red', alpha=0.3, s=20, label='Failed')
        ax.scatter(self.results.loc[success, 'time_to_offer'],
                  self.results.loc[success, 'salary_offer'],
                  c='green', alpha=0.5, s=20, label='Success')
        
        ax.axhline(self.target_salary, color='blue', linestyle='--',
                   linewidth=2, alpha=0.5)
        ax.axvline(self.target_days, color='blue', linestyle='--',
                   linewidth=2, alpha=0.5)
        
        ax.set_xlabel('Time to Offer (days)', fontsize=10, fontweight='bold')
        ax.set_ylabel('Salary Offer (PHP)', fontsize=10, fontweight='bold')
        ax.set_title('Salary vs Time to Offer', fontsize=12, fontweight='bold')
        ax.legend()
        ax.grid(True, alpha=0.3)
    
    def _plot_economic_conditions(self, ax):
        """Plot economic conditions distributions."""
        ax2 = ax.twinx()
        
        # Market growth distribution
        ax.hist(self.results['market_growth'] * 100, bins=40, alpha=0.5,
               color='red', edgecolor='black', label='Market Growth (%)')
        
        # Inflation distribution
        ax2.hist(self.results['inflation_rate'] * 100, bins=40, alpha=0.5,
                color='blue', edgecolor='black', label='Inflation (%)')
        
        ax.set_xlabel('Percentage (%)', fontsize=10, fontweight='bold')
        ax.set_ylabel('Frequency (Market Growth)', fontsize=10, fontweight='bold', color='red')
        ax2.set_ylabel('Frequency (Inflation)', fontsize=10, fontweight='bold', color='blue')
        ax.set_title('Economic Conditions Distribution', fontsize=12, fontweight='bold')
        
        ax.tick_params(axis='y', labelcolor='red')
        ax2.tick_params(axis='y', labelcolor='blue')
        
        lines1, labels1 = ax.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
        ax.grid(True, alpha=0.3)
    
    def _plot_success_vs_applications(self, ax):
        """Plot success probability vs number of applications."""
        # Bin applications and calculate success rate
        bins = np.arange(0, self.results['applications_needed'].max() + 20, 20)
        bin_centers = (bins[:-1] + bins[1:]) / 2
        
        success_by_apps = []
        for i in range(len(bins) - 1):
            mask = (self.results['applications_needed'] >= bins[i]) & \
                   (self.results['applications_needed'] < bins[i+1])
            if mask.sum() > 0:
                success_rate = self.results.loc[mask, 'overall_success'].mean()
                success_by_apps.append(success_rate * 100)
            else:
                success_by_apps.append(0)
        
        ax.plot(bin_centers, success_by_apps, marker='o', linewidth=2,
               markersize=8, color='darkgreen')
        ax.axhline(80, color='red', linestyle='--', linewidth=2,
                  label='80% Target', alpha=0.7)
        ax.fill_between(bin_centers, 0, success_by_apps, alpha=0.3, color='lightgreen')
        
        ax.set_xlabel('Number of Applications', fontsize=10, fontweight='bold')
        ax.set_ylabel('Success Probability (%)', fontsize=10, fontweight='bold')
        ax.set_title('Success Rate vs Applications Submitted', fontsize=12, fontweight='bold')
        ax.legend()
        ax.grid(True, alpha=0.3)
        ax.set_ylim(0, 100)
    
    def export_results(self, filename='simulation_results.csv'):
        """Export simulation results to CSV file."""
        if self.results is None:
            print("Error: No simulation results available. Run simulation first.")
            return
        
        self.results.to_csv(filename, index=False)
        print(f"\n💾 Results exported to: {filename}")


def main():
    """Main execution function."""
    print("\n" + "=" * 70)
    print("CAREER PATH SIMULATION - GROUP 8")
    print("Economic Downturn Stress Test")
    print("=" * 70)
    
    # Get user inputs
    print("\n📝 Please enter simulation parameters:")
    print("-" * 70)
    
    try:
        target_salary = float(input("Enter target starting salary (PHP) [default: 45000]: ") or "45000")
        target_days = int(input("Enter target time frame (days) [default: 90]: ") or "90")
        num_simulations = int(input("Enter number of simulations [default: 10000]: ") or "10000")
        applications_per_week = int(input("Enter applications per week [default: 10]: ") or "10")
    except ValueError:
        print("\n⚠️  Invalid input. Using default values.")
        target_salary = 45000
        target_days = 90
        num_simulations = 10000
        applications_per_week = 10
    
    # Create and run simulation
    simulation = EconomicDownturnJobSearchSimulation(
        target_salary=target_salary,
        target_days=target_days,
        num_simulations=num_simulations,
        applications_per_week=applications_per_week
    )
    
    # Run simulation
    results = simulation.run_simulation()
    
    # Print summary
    simulation.print_summary()
    
    # Generate plots
    print("\n📊 Generating visualizations...")
    simulation.plot_results()
    
    # Export results
    export = input("\n💾 Export results to CSV? (y/n) [default: y]: ").lower() or "y"
    if export == 'y':
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        simulation.export_results(f'simulation_results_{timestamp}.csv')
    
    print("\n" + "=" * 70)
    print("✅ SIMULATION COMPLETE")
    print("=" * 70)
    print("\nThank you for using the Career Path Simulation tool!")
    print("Group 8 - Economic Downturn Stress Test\n")


if __name__ == "__main__":
    main()
