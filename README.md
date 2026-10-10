# CodeAlpha Task 3 — Data Visualization

## Objective
Transform the Superstore dataset into clear charts that help communicate sales and profit patterns.

## Tools
- Python
- Pandas
- Matplotlib

## Dataset
## Dataset

The project uses `Sample - Superstore.csv`, containing 9,994 records. The dataset is stored in the same folder as `task3_visualization.py`.

The dataset covers orders from January 2014 to December 2017 and includes sales, profit, product category, region, and order date information.

## Visualizations
1. Total sales by product category
2. Total profit by product category
3. Monthly sales trend
4. Total sales by region

## Setup
Open a terminal in this folder and install the libraries:

```bash
python -m pip install pandas matplotlib
```

## Run
```bash
python task3_visualization.py
```

The script creates an `outputs` folder containing four PNG charts and four summary CSV files. It also prints summary figures and tables in the terminal.

## Key findings
## Key Findings

- **Total Sales:** 2,297,200.86 across 9,994 records.
- **Total Profit:** 286,397.02.
- **Top Sales Category:** Technology, with sales of 836,154.03.
- **Top Profit Category:** Technology, with profit of 145,454.95.
- **Regional Performance:** West recorded the highest sales at 725,457.82, while South recorded the lowest at 391,721.91.
- **Profitability Insight:** Furniture generated sales of 741,999.80 but profit of only 18,451.27, suggesting that its profitability deserves further investigation.

## GitHub
Suggested repository name: `CodeAlpha_Task3_Data_Visualization`

Suggested repository contents:
- `task3_visualization.py`
- `README.md`
- `outputs/` (the four chart images and summary CSV files)
- `Sample - Superstore.csv` only if you are allowed to redistribute the dataset
