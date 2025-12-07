# BobaFit 🧋  
A nutrition tracking web app that displays nutrition facts for foods using the **CalorieNinjas API**, with a **Next.js frontend** and **AWS Lambda backend**.

---

## 📌 Project Overview & Purpose  
BobaFit allows users to quickly search for any food and instantly view nutrition facts such as **calories, protein, carbohydrates, fats, and fiber**.  
The app includes **autocomplete search**, enabling users to find items faster and explore healthier eating habits without needing to manually inspect food labels.

This project was built to learn the fundamentals of **full-stack development**, API integration, and cloud backend architecture using AWS services.

---

## 🎥 Video Demo  
👉 https://youtu.be/WRKjoRxcGOI

---

## 🛠 Installation & Setup Instructions  

### 1. **Install Node.js (v18 or newer)**  
Download at: https://nodejs.org/

### 2. **Clone the Repository**  
```bash
git clone <your-repo-url>
cd bobafit
```

### 3. **Install Dependencies**  
```bash
npm install
```

---

## ▶️ How to Run & Reproduce Results  

### **Run the Development Server**
```bash
npm run dev
```

Then open your browser and go to:

👉 **http://localhost:3000**

You can now search for any food (e.g., "apple", "chicken breast") and view nutrition facts.

### **Backend Reproduction (Optional – Only Needed if Testing Lambda)**
If you want to run the Lambda function locally:

1. Install Python 3.10+
2. Install dependencies inside the Lambda folder:
   ```bash
   pip install -r requirements.txt -t .
   ```
3. Deploy using AWS Console or AWS SAM (optional for assignment).

The frontend will still run even without the live Lambda backend by using mock data.

---

## 🧰 Technologies & Libraries Used  

### **Frontend**
- Next.js  
- React  
- TypeScript  
- Tailwind CSS  

### **Backend**
- AWS Lambda (Python)  
- AWS API Gateway  

### **External API**
- **CalorieNinjas API** for nutrition data  

---

## 👩‍💻 Author & Contribution Summary  

### **Author:**  
**Elizabeth Ho**

### **What I Built:**  
- Designed and implemented the **Next.js frontend**
- Added **autocomplete search** for efficient food lookup  
- Created the **AWS Lambda backend** in Python  
- Integrated **API Gateway** for routing requests  
- Displayed nutrition results in a clean UI  
- Handled **CORS** and API communication  
- Built the app end-to-end as a **solo project** for a class assignment  
