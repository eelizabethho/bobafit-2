// helper functions for formatting nutrition data
// created these because i was duplicating the same rounding logic in multiple places

export function roundToDecimal(value: number, decimals: number = 1): number {
  const multiplier = Math.pow(10, decimals);
  return Math.round(value * multiplier) / multiplier;
}

// not really using this function but keeping it in case i need it later
export function formatNutritionValue(value: number, unit: string = 'g'): string {
  if (value === 0) return '0' + unit;
  return roundToDecimal(value, 1) + unit;
}

// convert sodium from grams to milligrams for display
// the api returns sodium in mg but we convert to grams, then convert back for display
export function sodiumToMg(grams: number): number {
  return Math.round(grams * 1000);
}

// check if a nutrition value should be displayed
// only show values that exist and are greater than 0
export function shouldShowValue(value: number | undefined): boolean {
  if (value === undefined) return false;
  return value > 0;
}
