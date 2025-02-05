```mermaid
graph TD;

    %% Homepage with three choices
    A[🏠 Homepage] -->|Choose School| B[🏫 School Login]
    A -->|Choose Student| C[🎓 Student Login]
    A -->|Choose Staff| D[👨‍🏫 Staff Login]

    %% Login Process
    B -->|Enter Credentials| E[🔑 Login Authentication]
    C -->|Enter Credentials| E
    D -->|Enter Credentials| E

    %% Authentication Outcomes
    E -->|✅ Login Success| F[📊 Dashboard]
    E -->|❌ Login Failed or First Time?| G[📝 Registration Page]

    %% Registration Process
    G -->|Complete Registration| H[🎟️ Redirect to Login]
    H -->|Re-enter Credentials| E

    %% Post Login Navigation
    F -->|Access Features| I[📂 View & Manage Data]
    F -->|Logout| A
