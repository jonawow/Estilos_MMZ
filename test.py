import re

def fix_css():
    with open('estilos.css', 'r', encoding='utf-8') as f:
        c = f.read()
    
    def replacer(m):
        return m.group(0).replace(' ', '%20')
        
    c = re.sub(r'data:image/svg\+xml,[^\"]+', replacer, c)
    
    with open('estilos.css', 'w', encoding='utf-8') as f:
        f.write(c)
        
if __name__ == '__main__':
    fix_css()
