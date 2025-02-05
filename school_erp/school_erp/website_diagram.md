```mermaid
graph TD;
    
    subgraph "Frontend (Client-Side)"
        A[HTML Templates] -->|Requests| B[Django Backend]
    end

    subgraph "Backend (Server-Side)"
        B[Django Backend] -->|Authenticates| C[Django Auth System]
        B -->|Queries| D[MySQL Database]
    end

    subgraph "Database Layer"
        D[MySQL Database] -->|Stores Data| E[Student, Teacher, Admin Records]
    end
