# BobaFit 🧋

Nutrition tracking app that shows nutrition facts for foods using the CalorieNinjas API.

## Project Overview

Search for any food and get nutrition information like calories, protein, carbs, fat, fiber, and more. The app has autocomplete suggestions so you can quickly find foods.

Built with Next.js frontend and AWS Lambda backend.

## Video Demo

https://youtu.be/WRKjoRxcGOI  

## How to Run

### Quick Start (All You Need!)

1. **Install Node.js 18+** if you don't have it: [nodejs.org](https://nodejs.org/)

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Run the app:**
   ```bash
   npm run dev
   ```

4. **Open your browser:**
   Go to http://localhost:3000 and start searching for foods!

The app will work with mock nutrition data. Just type a food name (like "apple" or "chicken breast") and see the nutrition facts!

**Example:** Search "apple" to see nutrition facts like 53 calories, 0.3g protein, 14.1g carbs, etc.

---

## Optional: Testing with Real API Data

If you want to test the Lambda backend locally with real CalorieNinjas API data, you'll need:

- **Python 3.12**
- **AWS SAM CLI** - [Install guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html)
- **Docker** - [Download](https://www.docker.com/)
- **CalorieNinjas API key** - Get a free one at [calorieninjas.com](https://www.calorieninjas.com/)

### Setup Backend

1. **Configure API key:**
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

2. **Build the backend:**
   ```bash
   sam build
   ```

3. **Start the backend** (in one terminal):
   ```bash
   sam local start-api --port 3001 --env-vars env.json
   ```

4. **Start the frontend** (in another terminal):
   ```bash
   npm run dev
   ```

Now the app will use real API data instead of mock data!

## Technologies Used

- Next.js / React / TypeScript
- AWS Lambda (Python)
- AWS API Gateway
- CalorieNinjas API
- Tailwind CSS

## Author

Elizabeth Ho 

**What I Built:**
- Frontend with autocomplete search
- Backend Lambda function
- API Gateway integration
- Nutrition data display
- CORS handling

Solo project for class assignment.
