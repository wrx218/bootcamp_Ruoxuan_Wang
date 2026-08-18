# Stakeholder Brief - Hourly Bike-Sharing Demand Forecast

**Audience:** Bike-sharing operations manager and dispatch coordinators  
**Cadence:** Daily, with the forecast prepared each evening  
**Decision Supported:** Next-day staffing and bicycle-rebalancing capacity

## Context

Hourly demand for shared bicycles changes with time of day, weekday, season, and weather. If the operations team reacts only after bicycle availability becomes unbalanced, customers may be unable to begin trips and rebalancing work becomes less efficient. A next-day demand forecast gives the team an earlier signal about when the system is likely to be busiest.

## User and Pain Point

The operations manager is responsible for approving staffing and rebalancing plans. Dispatch coordinators carry out the plan and need a concise view of expected hourly demand. They do not need a technical model report during daily operations; they need a forecast that highlights likely peak periods and communicates uncertainty and limitations clearly.

## What You Will Receive

- A table of 24 hourly rental-demand estimates for the following day
- A line chart that highlights forecast peak periods
- Flags for hours above the 75th percentile of historical hourly demand
- A short plain-language summary of important assumptions and unusual conditions
- A model-performance summary using MAE and comparison with a previous-day baseline

## How the Output Supports a Decision

The operations manager will review flagged hours and decide whether additional staff or rebalancing capacity is warranted. The forecast is decision support, not an automatic dispatch instruction. Operational experience, special events, and known disruptions should be considered before the final plan is approved.

## Success Criteria

The first version will be considered successful if it:

1. Produces all 24 hourly estimates before the daily planning deadline.
2. Achieves lower holdout MAE than the previous-day, same-hour baseline.
3. Presents the forecast in a form that the operations manager can interpret without reading model code.

## Assumptions and Constraints

- Historical hourly rentals and relevant calendar and weather fields are available.
- Evaluation will use a chronological split rather than a random split.
- The first version forecasts system-wide demand only.
- The output will not automatically allocate bicycles or dispatch employees.
- Existing course or open data and local computing resources will be used.

## Risks and Review Questions

- Special events and service disruptions may create demand spikes not captured by the model.
- Forecast weather may differ from actual weather.
- Demand patterns may change over time and require retraining.
- The operations manager should confirm whether the 75th-percentile flag is operationally meaningful.
- A later project phase may require station-level predictions to support specific rebalancing routes.

