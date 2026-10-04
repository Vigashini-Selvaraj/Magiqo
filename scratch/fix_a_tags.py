with open('c:/Users/vigas/Desktop/magiqo/entertainers.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix missing </a> tag
content = content.replace('">View Details\n', '">View Details</a>\n')

with open('c:/Users/vigas/Desktop/magiqo/entertainers.html', 'w', encoding='utf-8') as f:
    f.write(content)
