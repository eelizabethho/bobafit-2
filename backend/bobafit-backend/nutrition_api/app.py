import json
import os
import requests

# configuration constants
API_TIMEOUT = 10
DEFAULT_SERVING_SIZE = 100

def build_response(status_code, body, headers=None):
    """
    helper function to build consistent api responses with cors headers
    makes it easier to return responses without repeating the header setup
    """
    default_headers = {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Methods': 'GET,POST,OPTIONS'
    }
    if headers:
        default_headers.update(headers)
    
    return {
        'statusCode': status_code,
        'headers': default_headers,
        'body': json.dumps(body) if isinstance(body, dict) else body
    }

def extract_food_query(event):
    """
    extract the food name from the api gateway event
    handles both get requests (query string) and post requests (body)
    """
    # check query string first since that's what we're using
    query_params = event.get('queryStringParameters') or {}
    if isinstance(query_params, dict) and query_params.get('food'):
        return query_params['food']
    
    # fallback to body for post requests (not really using this but good to have)
    if event.get('body'):
        try:
            body = json.loads(event['body']) if isinstance(event.get('body'), str) else event.get('body')
            if body and isinstance(body, dict):
                return body.get('food')
        except (json.JSONDecodeError, TypeError):
            pass
    
    return None

def parse_nutrition_item(item):
    """
    extract nutrition data from a single item in the api response
    converts sodium from mg to grams to keep units consistent
    """
    return {
        'calories': item.get('calories', 0),
        'protein': item.get('protein_g', 0),
        'carbs': item.get('carbohydrates_total_g', 0),
        'fat': item.get('fat_total_g', 0),
        'fiber': item.get('fiber_g', 0),
        'sugar': item.get('sugar_g', 0),
        'sodium': item.get('sodium_mg', 0) / 1000.0,  # convert mg to grams
        'saturated_fat': item.get('fat_saturated_g', 0),
        'cholesterol': item.get('cholesterol_mg', 0),
        'potassium': item.get('potassium_mg', 0)
    }

def aggregate_nutrition(items):
    """
    when the user searches for multiple foods (like "apple and banana"),
    we need to add up all the nutrition values
    """
    totals = {
        'calories': 0,
        'protein': 0,
        'carbs': 0,
        'fat': 0,
        'fiber': 0,
        'sugar': 0,
        'sodium': 0,
        'saturated_fat': 0,
        'cholesterol': 0,
        'potassium': 0
    }
    
    for item in items:
        nutrition = parse_nutrition_item(item)
        for key in totals:
            totals[key] += nutrition.get(key, 0)
    
    return totals

def lambda_handler(event, context):
    """
    main lambda handler that gets nutrition info from calorieninjas api
    """
    
    # handle cors preflight requests from the browser
    if event.get('httpMethod') == 'OPTIONS':
        return build_response(200, {})
    
    api_key = os.environ.get('CALORIENINJAS_API_KEY', '')
    
    try:
        food_query = extract_food_query(event)
        
        if not food_query:
            return build_response(400, {'error': 'Food parameter is required'})
        
        # if no api key is set, return mock data for testing
        # this makes it easier to test locally without needing the api key
        if not api_key:
            return build_response(200, {
                'food': food_query,
                'nutrition': {
                    'calories': 250,
                    'protein': 10,
                    'carbs': 30,
                    'fat': 8,
                    'fiber': 5
                },
                'message': 'Using mock data. Set CALORIENINJAS_API_KEY environment variable for real data.'
            })
        
        # make the api call to calorieninjas
        api_url = 'https://api.calorieninjas.com/v1/nutrition'
        params = {'query': food_query}
        api_headers = {'X-Api-Key': api_key}
        
        response = requests.get(api_url, headers=api_headers, params=params, timeout=API_TIMEOUT)
        
        if response.status_code != 200:
            error_text = response.text[:200] if hasattr(response, 'text') else 'Unknown error'
            return build_response(response.status_code, {
                'error': f'API request failed: {error_text}'
            })
        
        data = response.json()
        items = data.get('items', [])
        
        if not items or len(items) == 0:
            return build_response(404, {
                'error': f'No nutrition data found for "{food_query}"'
            })
        
        # handle single food item
        if len(items) == 1:
            item = items[0]
            nutrition = parse_nutrition_item(item)
            
            return build_response(200, {
                'food': item.get('name', food_query),
                'serving_size': item.get('serving_size_g', DEFAULT_SERVING_SIZE),
                'nutrition': nutrition
            })
        else:
            # multiple items in the query - aggregate the nutrition values
            nutrition = aggregate_nutrition(items)
            item_names = [item.get('name', '') for item in items if item.get('name')]
            
            return build_response(200, {
                'food': ', '.join(item_names) if item_names else food_query,
                'items_count': len(items),
                'nutrition': nutrition
            })
            
    except requests.exceptions.RequestException as e:
        # network errors or request timeouts
        return build_response(500, {
            'error': f'Request error: {str(e)}'
        })
    except Exception as e:
        # catch any other unexpected errors
        return build_response(500, {
            'error': f'Internal error: {str(e)}'
        })
