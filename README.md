# BobaFit 🧋

Nutrition tracking app that shows nutrition facts for foods using the CalorieNinjas API.

## Project Overview

Search for any food and get nutrition information like calories, protein, carbs, fat, fiber, and more. The app has autocomplete suggestions so you can quickly find foods.

Built with Next.js frontend and AWS Lambda backend.

## Video Demo

[Add your video link here]

## Installation

### What You Need

- Node.js 18+
- Python 3.12
- AWS SAM CLI
- Docker
- CalorieNinjas API key (free at https://www.calorieninjas.com/)

### Setup

1. **Backend:**
   ```bash
   cd backend/bobafit-backend
   ```
   
   Edit `env.json` and add your API key:
   ```json
   {
     "NutritionFunction": {
       "CALORIENINJAS_API_KEY": "your-key-here"
     }
   }
   ```
   
   Build and run:
   ```bash
   sam build
   sam local start-api --port 3001 --env-vars env.json
   ```

2. **Frontend:**
   ```bash
   npm install
   npm run dev
   ```

3. Open http://localhost:3000

## How to Run

1. Start backend in one terminal (port 3001)
2. Start frontend in another terminal (port 3000)
3. Open browser and search for foods

**Example:** Search "apple" to see nutrition facts like 53 calories, 0.3g protein, 14.1g carbs, etc.

## Technologies Used

- Next.js / React / TypeScript
- AWS Lambda (Python)
- AWS API Gateway
- CalorieNinjas API
- Tailwind CSS

## Author

[Your Name]

**What I Built:**
- Frontend with autocomplete search
- Backend Lambda function
- API Gateway integration
- Nutrition data display
- CORS handling

Solo project for class assignment.
