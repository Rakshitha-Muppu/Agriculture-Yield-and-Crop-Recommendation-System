# Agriculture Yield Prediction and Crop Recommendation System

## Project Overview

This project is a Data + AI + Cloud-based system designed to help predict crop yield and recommend suitable crops based on agricultural conditions.

It uses machine learning techniques along with a data processing pipeline to analyze agricultural data and generate meaningful predictions.

Users can either manually enter agricultural details or upload CSV files for analysis. The system processes the data, applies machine learning models, and returns predictions.

---

## Problem Statement

Farmers often lack data-driven insights regarding:

- Expected crop production
- Suitable crops for specific environmental conditions
- Efficient use of agricultural resources

This leads to reduced productivity and poor crop planning decisions.

---

## Proposed Solution

The system provides a complete data-driven solution:

- Collects agricultural data (manual or CSV upload)
- Cleans and processes data using a data pipeline
- Applies machine learning models for prediction
- Stores results in cloud database (Azure SQL)
- Displays results through a simple dashboard

---

## User Inputs

Users can provide data in two ways:

### Manual Input
- Soil Type
- Temperature
- Rainfall
- Land Area
- Crop Information

### CSV File Upload
- Users can upload datasets containing agricultural records

---

## System Outputs

- Predicted Crop Yield
- Recommended Crop
- Data Insights Dashboard
- Stored Prediction History

---

## Technologies Used

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python
- Flask

### Machine Learning
- Pandas
- NumPy
- Scikit-learn

### Database (Cloud)
- Azure SQL Database

### Version Control
- GitHub

---

## Data Pipeline Flow

Raw Data → Data Cleaning → Feature Processing → ML Model → Prediction → Cloud Storage

---

## Expected Benefits

- Supports data-driven farming decisions
- Improves crop planning and management
- Helps estimate agricultural production
- Demonstrates real-world use of Data, AI, and Cloud integration

---

## Future Enhancements

- Weather Impact Analysis
- Real-Time Weather API Integration
- Fertilizer Recommendation System
- Mobile Application Support
- Advanced Agricultural Analytics Dashboard
