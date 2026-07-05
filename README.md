# Lagos Real Estate Market Analysis

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Pandas](https://img.shields.io/badge/Pandas-2.0-green)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

## Overview
An end-to-end data analysis project scraping and analysing over 14,000 
residential property listings from NigeriaPropertyCentre to uncover 
pricing patterns, location trends, and market insights across Lagos, Nigeria.

This project covers the full data science pipeline — web scraping, 
data cleaning, exploratory data analysis, and storytelling through 
visualisation.

---

## Research Questions
1. Does location significantly affect property price?
2. Does property type influence pricing?
3. What does a typical Lagos property look like in terms of bedrooms, 
   bathrooms, and price range?
4. Which locations appear underpriced or overpriced relative to the market?
5. Which property features correlate most strongly with price?

---

## Dataset
- **Source**: [NigeriaPropertyCentre](https://nigeriapropertycentre.com)
- **Collection Method**: Web scraping using BeautifulSoup and Requests
- **Pages Scraped**: 500 of 1,725 available pages (~29% of total listings)
- **Raw Records**: 20,500 listings
- **Clean Records**: 14,995 Lagos residential listings
- **Features**: Title, Price, Location, Property Type, Bedrooms, 
  Bathrooms, Toilets, Parking Space, URL

---

## Project Structure

```
Lagos-Real-Estate-Analysis/
│
├── notebooks/
│   ├── 01_scraping.ipynb
│   ├── 02_analysis.ipynb
│   └── 03_modelling.ipynb  ← future
│
├── data/
│   └── lagosIsland.csv
│   └── lagos_clean.csv
│
└── README.md
```

---

## Key Findings
- **Location is the dominant pricing factor** — Ikoyi commands prices 
  ₦7.19B above the Lagos average while mainland areas like Ikorodu and 
  Surulere sit over ₦1B below average
- **Detached duplexes** are the most expensive property type at an 
  average of ₦2.8B — nearly 3x higher than the next category
- **A typical Lagos property** has 4 bedrooms and a median price of ₦330M
- **Price distribution is heavily right-skewed** — driven by luxury 
  properties in Ikoyi, Banana Island and Victoria Island
- **Room count has near-zero correlation with price** (0.02) — location 
  and property type are far stronger predictors

---

## Tools & Libraries
| Tool | Purpose |
|---|---|
| Python 3.13 | Core programming language |
| BeautifulSoup | Web scraping |
| Requests | HTTP requests |
| Pandas | Data manipulation and cleaning |
| NumPy | Numerical operations |
| Matplotlib | Data visualisation |
| Seaborn | Statistical visualisation |
| VS Code | Development environment |

---

## How to Run
1. Clone the repository
```bash
git clone https://github.com/dtechtitan/Lagos-Real-Estate-Analysis.git
```

2. Install dependencies
```bash
pip install pandas numpy matplotlib seaborn beautifulsoup4 requests
```

3. Open the notebook
```bash
cd Lagos-Real-Estate-Analysis
jupyter notebook notebooks/lagos_real_estate_analysis.ipynb
```

---

## Limitations
- Analysis is based on 29% of total available listings — findings are 
  representative but not exhaustive
- Prices are as listed by agents and may not reflect actual transaction 
  prices
- Missing data in bedroom, bathroom and parking columns due to incomplete 
  agent listings

---

## Author
**Mayowa Daniel** — Data Science Student, University of Lagos  
GitHub: [@dtechtitan](https://github.com/dtechtitan)  
Email: dtomisin07@gmail.com

---

## Next Steps
- [ ] Build a Lagos House Price Prediction Model using regression
