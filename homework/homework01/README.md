# Hourly Bike-Sharing Demand Forecast

**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement

A city bike-sharing operations team needs to decide how to reposition bicycles before periods of high demand. When too few bicycles are available at busy times, customers cannot start trips; when too many are placed in low-demand areas, bicycles and staff time are used inefficiently. This project will use historical hourly rental, calendar, and weather data to estimate the number of rentals expected during each hour of the following day.

The initial scope is a system-wide hourly forecast rather than a station-level forecast. Its purpose is to help the operations manager plan daily staffing and bicycle rebalancing. Success will be measured using mean absolute error (MAE) on a held-out time period and by comparing the forecast with a simple baseline that uses demand from the same hour on the previous day. The project will be considered useful if it consistently improves on that baseline and produces a clear daily forecast table that operations staff can review.

## Stakeholder & User

- **Primary stakeholder and decision-maker:** Bike-sharing operations manager, who approves the next day's staffing and rebalancing plan.
- **Primary users:** Dispatch coordinators, who use the hourly forecast to schedule vehicles and staff.
- **Timing and workflow:** The forecast should be available each evening before the next day's operations plan is finalized.

## Useful Answer & Decision

- **Type of answer:** Predictive.
- **Question answered:** How many system-wide bike rentals are expected in each hour of the next day?
- **Decision supported:** When should the operations team schedule additional staff and bicycle-rebalancing capacity?
- **Primary metric:** Mean absolute error (MAE) on a chronological holdout set.
- **Baseline:** Demand observed during the same hour of the previous day.
- **Artifact:** A CSV table and simple line chart containing the next day's 24 hourly demand estimates, plus a short summary of expected peak periods.
- **Decision trigger:** Hours forecast to exceed the 75th percentile of historical hourly demand will be flagged for operational review. The operations manager will make the final staffing decision.

## Assumptions & Constraints

- Historical hourly rental counts, timestamps, calendar variables, and weather observations are available and sufficiently complete.
- Future weather forecasts can be represented by variables compatible with the historical weather data.
- Recent historical patterns are informative about near-term demand.
- The first version predicts total system demand and does not recommend station-level bicycle movements.
- The model supports human decisions; it does not automatically dispatch staff or vehicles.
- Evaluation must respect time order to prevent future information from leaking into training data.
- The initial project uses existing computing resources and open or course-provided data; it does not require real-time infrastructure.

## Known Unknowns / Risks

- **Unusual events:** Holidays, transit disruptions, or large public events may cause demand patterns not represented in the data. Event dates will be reviewed, and large forecast errors will be documented.
- **Weather uncertainty:** The model may be trained on observed weather but used with forecast weather. Performance should later be checked using realistic forecast inputs.
- **Demand drift:** Seasonal changes or changes in rider behavior may reduce accuracy. MAE will be monitored over rolling time windows.
- **Data quality:** Missing or duplicated hourly records could bias the model. Timestamp continuity, duplicates, and missing values will be checked before modeling.
- **Operational threshold:** The 75th-percentile review threshold is an initial assumption and should be validated with the operations manager.
- **Scope limitation:** A reliable system-wide forecast may still be insufficient for station-level rebalancing; station-level modeling is a possible later phase.

## Lifecycle Mapping

Goal -> Stage -> Deliverable

- Define a decision-linked demand problem -> Problem Framing & Scoping (Stage 01) -> Approved scoping statement and stakeholder memo
- Establish a trustworthy dataset -> Data Collection & Preparation -> Validated hourly modeling table and data dictionary
- Understand demand patterns -> Exploratory Data Analysis -> Summary of temporal and weather-related patterns
- Predict next-day hourly rentals -> Modeling & Evaluation -> Baseline comparison, MAE results, and selected forecasting model
- Support daily operational planning -> Communication & Delivery -> 24-hour forecast CSV, peak-period chart, and plain-language summary
- Maintain usefulness over time -> Monitoring -> Rolling error report and drift-review procedure

## Repo Plan

- `data/raw/`: Original source data; files are not modified in place.
- `data/processed/`: Cleaned, analysis-ready hourly data.
- `src/`: Reusable data preparation, feature engineering, and forecasting code.
- `notebooks/`: Exploratory analysis and model-development notebooks.
- `docs/`: Stakeholder-facing documents, including the Stage 01 memo.
- `reports/`: Final charts, evaluation results, and forecast outputs.
- `model/`: Saved model artifacts and associated metadata.

During active development, notebooks and documentation will be updated at least weekly. Data-processing and modeling changes will be committed when a meaningful, reproducible step is completed.

## Stage 01 Deliverables

- [Project scoping README](README.md)
- [Stakeholder brief](docs/stakeholder_brief.md)

