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
```

## Fields

**Required:**
- `title` - Recipe name
- `ingredients` - Array of ingredient strings
- `instructions` - Array of instruction strings

**Optional (can be `null` or left out):**
- `description` - Intro text
- `servings` - Number of servings
- `prepTime` - Prep time
- `cookTime` - Cook time  
- `totalTime` - Total time (if you don't list prep/cook separately)
- `source` - Where the recipe is from
- `image` - Path to image file (e.g., "images/apple-pie.jpg")
- `notes` - Additional notes/tips

## Tips

1. **Multiple recipes:** Separate them with commas in the JSON array
2. **Plain text conversion:** Send me your recipes in any format and I'll convert them
3. **Images:** Put images in an "images" folder next to recipes.html, then reference them like: `"image": "images/yourphoto.jpg"`
4. **Times:** Write them however you want - "30 min", "1 hour", "2 hours 15 minutes"

## Example Plain Text Format

If you want to send me recipes to convert, this format works great:

```
# Recipe Title

Description paragraph here.

Servings: 6
Prep: 15 minutes
Cook: 30 minutes

## Ingredients
- ingredient 1
- ingredient 2

## Instructions
1. Step one
2. Step two

## Notes
Any notes here
```

But honestly, any consistent format will work - I can parse most things!
