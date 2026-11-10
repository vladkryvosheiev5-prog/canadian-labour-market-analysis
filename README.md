Canadian Labour Market Analysis: January 2026
ECON 351 – Assignment 2 · University of Waterloo
The unemployment rate fell from 6.8% to 6.5% in January 2026, yet employment fell too. This project looks at why, using Statistics Canada Labour Force Survey figures for September 2025 – January 2026.
Key finding
A falling unemployment rate is not automatically good news. It can fall for two very different reasons:
More people become employed, or
Fewer people participate in the labour force (they stop searching and are no longer counted as unemployed).
January was the second case.
Indicator (thousands)	Dec 2025	Jan 2026	Change
Employment	21,146.0	21,121.2	−24.8
Labour force	22,697.7	22,578.7	−119.0
Unemployment	1,551.7	1,457.5	−94.2
Unemployment rate	6.8%	6.5%	−0.4 pp
Participation rate	65.4%	65.0%	−0.4 pp
Since unemployment = labour force − employment, the −94.2k change in unemployment is the −119.0k fall in the labour force minus the −24.8k fall in employment. Almost all of the drop in measured unemployment came from people leaving the labour force, not from people finding jobs.
Unemployment rate = Unemployed / Labour force
Charts
Monthly changes: employment vs. labour force
Month-over-month change in employment and labour force
Employment grew in each of the three months to December (Oct, Nov, Dec). January is the first decline, and the labour force fell nearly five times as much as employment.
Participation rate
Labour force participation rate
Participation sat at 65.2% for three months, ticked up to 65.4% in December, and dropped to 65.0% in January. Unlike December, when employment and participation both expanded, January saw both decline.
Unemployment rate
Unemployment rate
The rate fell from 6.84% in December to 6.45% in January (reported as 6.8% and 6.5%). In October and November it also fell, but with employment rising. January is the only month where the rate fell while employment fell too.
Conclusion
January's decline in the unemployment rate is largely a statistical by-product of a shrinking labour force. A genuine recovery needs rising employment and stable or rising participation, and January delivered neither. The cause of the exit (for example discouragement or short-term volatility) cannot be determined from these five months of seasonally adjusted data alone.
Repository contents
.
├── README.md
├── make_charts.py                  # regenerates the charts from the CSV
├── assets/                         # chart images used in this README
├── data/
│   ├── labour_force_data.csv       # Sep 2025 – Jan 2026 series
│   └── ECON_351_Assignment_2.xlsx  # original workbook (pivot tables + charts)
└── docs/
    └── ECON_351_Assignment_2_corrected.pdf   # full written analysis
Reproduce
bash
pip install matplotlib
python make_charts.py
Data
Employment, labour force, unemployment (thousands of persons) and participation rate (%), monthly, September 2025 – January 2026, from Statistics Canada's Labour Force Survey / Jobs Report.
