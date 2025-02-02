# 🏔️ Climb GUI - Frontend (React)

This is the **React frontend** for **Climb GUI**.

---

## 📖 Table of Contents

1. [Prerequisites](#prerequisites)
2. [Setup Instructions](#setup-instructions)
   - [Installing Dependencies](#installing-dependencies)
   - [Running the Frontend](#running-the-frontend)
   - [Environment Variables](#environment-variables)
---

## **Prerequisites**
- **Node.js**: `>= 16.0.0`
  - Check if Node.js is installed:
    ```bash
    node -v
    ```
  - Download & install from [Node.js official site](https://nodejs.org/).
- **npm**: Comes with Node.js, but you can upgrade it:
  ```bash
  npm install -g npm
  ```
To verify the installations:
```bash
node -v   # Check Node.js version
npm -v    # Check npm version
```

## Setup Instructions

### **Installing Dependencies**
Ensure you have **Node.js (>=16.0.0)** installed.

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install required dependencies:
   ```bash
   npm install
   ```

---

### **Running the Frontend**
Start the React development server:

```bash
npm run dev
```

By default, the frontend runs at **`http://localhost:5173`**.

---

### **Environment Variables**
Create a `.env` file in the `frontend` directory for API configuration.

Example:
```
VITE_BACKEND_URL=http://localhost:8080
VITE_API_KEY=YOUR-API-KEY
```