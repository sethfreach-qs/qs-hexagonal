CREATE TABLE IF NOT EXISTS tickets (
    id SERIAL PRIMARY KEY,
    description VARCHAR(255),
    priority VARCHAR(255),
    status VARCHAR(255),
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);
