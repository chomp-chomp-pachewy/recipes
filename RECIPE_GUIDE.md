# Recipe Site - Quick Guide

## Files
- `recipes.html` - The main page (open this in your browser)
- `recipes.json` - Your recipe data (edit this to add recipes)

## Adding a Recipe

Just add a new entry to the `recipes.json` file. Here's the template:

```json
{
  "title": "Recipe Name",
  "description": "Optional description or story about the recipe",
  "servings": "6",
  "prepTime": "15 minutes",
  "cookTime": "30 minutes",
  "totalTime": "45 minutes",
  "source": "Optional - where it came from",
  "image": null,
  "category": "chomp chomp",
  "ingredients": [
    "1 cup flour",
    "2 eggs",
    "etc"
  ],
  "instructions": [
    "First step here",
    "Second step here",
    "etc"
  ],
  "notes": "Optional notes section"
}
