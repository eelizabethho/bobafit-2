// api endpoint configuration
// might move this to environment variables later but this works for now

const getApiEndpoint = (): string => {
  // check localStorage first in case i want to test with a different endpoint
  if (typeof window !== 'undefined') {
    const stored = localStorage.getItem('api_endpoint');
    if (stored) {
      return stored;
    }
  }
  
  // fallback to env variable or default to local proxy route
  return process.env.NEXT_PUBLIC_API_ENDPOINT || '';
};

export const API_CONFIG = {
  endpoint: getApiEndpoint(),
  timeout: 10000,
  retryAttempts: 2,
};

// build the full url for nutrition api calls
// handles cases where the base url might already have query parameters
export function buildNutritionUrl(food: string): string {
  const base = API_CONFIG.endpoint || '/api/nutrition';
  const separator = base.includes('?') ? '&' : '?';
  return `${base}${separator}food=${encodeURIComponent(food)}`;
}
