CREATE TABLE companies (
    company_id VARCHAR(24) PRIMARY KEY,
    company_name VARCHAR(130)
);

CREATE TABLE charges (
    id VARCHAR(24) PRIMARY KEY,
    company_id VARCHAR(24) NOT NULL,
    amount DECIMAL(16,2) NOT NULL,
    status VARCHAR(30) NOT NULL,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NULL,
    CONSTRAINT fk_company FOREIGN KEY (company_id) REFERENCES companies(company_id)
);
