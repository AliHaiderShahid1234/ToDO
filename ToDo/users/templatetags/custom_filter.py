from django import template

# Create a new instance of the template library
register = template.Library()

# Example custom filter: Capitalize first letter of a string
@register.filter(name='capitalize_first')
def capitalize_first(value):
    """Capitalize the first letter of a string."""
    if isinstance(value, str):
        return value.capitalize()
    return value  # Return the original value if not a string
