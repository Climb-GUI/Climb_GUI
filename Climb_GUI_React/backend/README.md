# 🏔️ Climb GUI - Backend (Flask)

This is the **Flask backend** for **Climb GUI**.

---

## 📖 Table of Contents

1. [Prerequisites](#prerequisites)
2. [Setup Instructions](#setup-instructions)
   - [Installing Dependencies](#installing-dependencies)
   - [Running the Backend](#running-the-backend)
   - [Environment Variables](#environment-variables)
3. [Testing](#testing)

---

## **Prerequisites**
- **Python**: `>= 3.8`
- **pip**: Comes with Python, but you can upgrade it:
  ```bash
  python -m pip install --upgrade pip
  ```

## Setup Instructions

### **Installing Dependencies**

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. (Optional) Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

### **Running the Backend**
Start the Flask server:

```bash
python server.py
```

The API will be available at `http://localhost:8080`.

---

### **Environment Variables**
Create a `.env` file in the `backend` directory to store the API key.

Example:
```
API_KEY=YOUR-API-KEY
```

---

## Testing

If you have done the steps above, you can test by visiting `http://localhost:8080/api/test` or running

```bash
curl -X GET "http://localhost:8080/api/test" -H "Authorization: Bearer YOUR-API-KEY"
```