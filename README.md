# BobaFit 🧋

A nutrition tracking application I developed for a class project. Users can search for foods and receive detailed nutrition information using the CalorieNinjas API.

## Project Overview and Purpose

This application allows users to input a food item (such as "apple" or "chicken breast") and displays comprehensive nutrition facts including calories, protein, carbohydrates, fat, fiber, sugar, sodium, and other nutrients. I implemented an autocomplete feature with a dropdown that shows food suggestions as users type, making it easier to search for foods that are available in the database.

The purpose of this project was to learn about serverless architecture using AWS Lambda and API Gateway, while building a practical application that could help people track their nutrition. The backend uses AWS Lambda functions to call the CalorieNinjas API, and the frontend is built with Next.js to provide a responsive user interface.

## Video Demonstration

[Add video link here when available]

## Installation and Setup Instructions

### Prerequisites

- Node.js 18 or higher
- Python 3.12
- AWS SAM CLI (for local testing and deployment)
- Docker (required for local Lambda testing)
- CalorieNinjas API key (available for free at https://www.calorieninjas.com/)

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend/bobafit-backend
   ```

2. Edit the `env.json` file and add your CalorieNinjas API key:
   ```json
   {
     "NutritionFunction": {
       "CALORIENINJAS_API_KEY": "your-api-key-here"
     }
   }
   ```

3. Build the Lambda function:
   ```bash
   sam build
   ```

4. For local testing, start the SAM local API:
   ```bash
   sam local start-api --port 3001 --env-vars env.json
   ```
   
   Keep this terminal window open as the backend server needs to remain running.

5. For deployment to AWS:
   ```bash
   sam deploy --guided
   ```
   Follow the prompts and provide your API key when asked.

### Frontend Setup

1. Install project dependencies:
   ```bash
   npm install
   ```

2. If you deployed the backend to AWS, create a `.env.local` file in the root directory:
   ```
   NEXT_PUBLIC_API_ENDPOINT=https://your-api-url.execute-api.region.amazonaws.com/Prod
   ```
   
   If running locally, the application will automatically use the local API route which proxies requests to the SAM local server on port 3001.

3. Start the development server:
   ```bash
   npm run dev
   ```

## How to Run the Program and Reproduce Results

### Running Locally

1. **Start the backend** (Terminal 1):
   ```bash
   cd backend/bobafit-backend
   sam build
   sam local start-api --port 3001 --env-vars env.json
   ```
   You should see output indicating the API is running on port 3001.

2. **Start the frontend** (Terminal 2):
   ```bash
   npm run dev
   ```
   The application will be available at http://localhost:3000

3. **Test the application**:
   - Open http://localhost:3000 in your browser
   - Type a food item in the search bar (e.g., "apple", "chicken breast", "boba")
   - You should see autocomplete suggestions appear as you type
   - Click on a suggestion or press Enter to search
   - Nutrition facts will be displayed including calories, protein, carbs, fat, fiber, and other nutrients
   - The serving size in grams will also be shown

### Expected Results

When you search for "apple", you should see:
- Food name: "apple"
- Serving size: 100g (or the actual serving size from the API)
- Calories: approximately 53 kcal
- Protein: approximately 0.3g
- Carbs: approximately 14.1g
- Fat: approximately 0.2g
- Fiber: approximately 2.4g
- Sugar: approximately 10.3g

The exact values may vary slightly based on the CalorieNinjas API data.

### Troubleshooting

- If you see "Using mock data" message, make sure the SAM local API is running on port 3001
- If autocomplete doesn't work, check the browser console for errors
- If API calls fail, verify your CalorieNinjas API key is correct in `env.json`

## Technologies and Libraries Used

### Frontend
- **Next.js 16.0.7** - React framework for building the web application
- **React 19.2.0** - UI library
- **TypeScript** - Type safety and better development experience
- **Tailwind CSS** - Styling and responsive design

### Backend
- **Python 3.12** - Programming language for Lambda functions
- **AWS Lambda** - Serverless compute for running the nutrition API
- **AWS API Gateway** - REST API endpoint
- **AWS SAM (Serverless Application Model)** - Infrastructure as code for deployment
- **requests** - Python library for HTTP requests to CalorieNinjas API
- **certifi** - SSL certificate handling
- **urllib3** - HTTP client library

### External APIs
- **CalorieNinjas API** - Provides nutrition data for food items

### Development Tools
- **Docker** - Required for local Lambda testing with SAM
- **AWS SAM CLI** - Command-line tool for building and deploying serverless applications
- **npm** - Package manager for Node.js dependencies

## Author and Contribution Summary

**Author:** [Your Name]

**Contribution Summary:**
- Designed and implemented the full-stack application architecture
- Developed the frontend using Next.js with autocomplete search functionality
- Created AWS Lambda function to integrate with CalorieNinjas API
- Configured API Gateway for REST API endpoints
- Implemented CORS handling for cross-origin requests
- Built helper utilities for nutrition data formatting
- Tested and debugged API integration issues
- Cleaned up codebase and removed unused sample files
- Wrote documentation and setup instructions

This was a solo project developed for a class assignment to demonstrate understanding of serverless architecture, API integration, and full-stack web development.

## Development Experience

### Challenges Encountered

During development, I encountered several challenges that required problem-solving:

- Initially attempted to use the FatSecret API, but encountered issues with their search functionality. Switched to CalorieNinjas API which proved more reliable.
- CORS configuration required significant troubleshooting to ensure proper communication between frontend and backend.
- Implementing the dropdown autocomplete feature was more complex than anticipated and required multiple iterations.
- Code refactoring was necessary to eliminate duplicate logic and improve maintainability.

### Key Learnings

This project provided valuable experience with:

- AWS Lambda functions and serverless architecture
- API integration and error handling
- TypeScript for type safety and improved code quality
- React hooks and state management
- CORS configuration and cross-origin requests

## Future Enhancements

Potential improvements for future iterations:

- User favorites list for frequently searched foods
- Search history functionality
- Meal planning features
- Enhanced error messaging and user feedback
- Expanded food suggestions database
- User authentication and personalized profiles

## Technical Notes

- The food suggestions list can be customized in `app/components/SearchBar.tsx`
- Backend API timeout is configured to 10 seconds
- CORS is currently configured to allow all origins; this should be restricted in production environments
- The application handles both single food items and multiple food queries (aggregating nutrition values)

## Acknowledgments

- CalorieNinjas API for providing nutrition data
- Next.js documentation for framework guidance
- AWS SAM documentation for serverless deployment assistance
