# 🏔️ Climb GUI - Legacy Implementation (Reflex)

This is the **Reflex** implementation for **Climb GUI**. Reference the [reflex docs](https://reflex.dev/docs/getting-started/introduction) if you have trouble with this setup.

---

## 📖 Table of Contents

1. [Prerequisites](#prerequisites)
2. [Setup Instructions](#setup-instructions)
   - [Installing Dependencies](#installing-dependencies)
   - [Running the App](#running-the-app)
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
   cd Climb_GUI
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

### **Running the App**
Start the Reflex app:

```bash
reflex run
```

The API will be available at `http://localhost:3000`.