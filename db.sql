-- Create Industry Table
CREATE TABLE Industry (
    industry_id SERIAL PRIMARY KEY,
    industry_name VARCHAR(255) NOT NULL UNIQUE
);

-- Create Company Table
CREATE TABLE Company (
    company_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    ticker VARCHAR(50),
    industry_id INT REFERENCES Industry(industry_id),
    hq_country VARCHAR(100),
    revenue FLOAT,
    emission_intensity FLOAT
);

-- Create ESG_Metrics Table
CREATE TABLE ESG_Metrics (
    esg_id SERIAL PRIMARY KEY,
    company_id INT REFERENCES Company(company_id),
    metric_type VARCHAR(255) NOT NULL,
    value FLOAT,
    year INT
);

-- Create Financial_Metrics Table
CREATE TABLE Financial_Metrics (
    finance_id SERIAL PRIMARY KEY,
    ticker VARCHAR(50) NOT NULL,
    metric_type VARCHAR(255) NOT NULL,
    value FLOAT,
    year INT
);

