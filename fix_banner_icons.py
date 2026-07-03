import urllib.parse
import re

def fix():
    with open('estilos.css', 'r', encoding='utf-8') as f:
        css = f.read()

    # Extract the 3 SVGs
    m1 = re.search(r'\.banner-mod-icon\.icono-sub-1\s*\{\s*-webkit-mask-image:\s*url\("data:image/svg\+xml,(.+?)"\);', css)
    m2 = re.search(r'\.banner-mod-icon\.icono-sub-2\s*\{\s*-webkit-mask-image:\s*url\("data:image/svg\+xml,(.+?)"\);', css)
    m3 = re.search(r'\.banner-mod-icon\.icono-sub-3\s*\{\s*-webkit-mask-image:\s*url\("data:image/svg\+xml,(.+?)"\);', css)

    if not (m1 and m2 and m3):
        print("Could not find SVGs!")
        return

    svg1 = urllib.parse.unquote(m1.group(1)).replace("'", '"')
    svg2 = urllib.parse.unquote(m2.group(1)).replace("'", '"')
    svg3 = urllib.parse.unquote(m3.group(1)).replace("'", '"')

    # Add fill="currentColor" to the SVG root tags
    svg1 = svg1.replace('<svg ', '<svg fill="currentColor" ')
    svg2 = svg2.replace('<svg ', '<svg fill="currentColor" ')
    svg3 = svg3.replace('<svg ', '<svg fill="currentColor" ')

    # Fix HTML script
    with open('html_adicional.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # inject SVGs into JS
    js_svgs = f"""
            var svg1 = `{svg1}`;
            var svg2 = `{svg2}`;
            var svg3 = `{svg3}`;
            """

    html = re.sub(r'var icon3 = \[.*?\];', r'\g<0>' + js_svgs, html)

    html = html.replace("iconEl.classList.add('icono-sub-1');", "iconEl.innerHTML = svg1;")
    html = html.replace("iconEl.classList.add('icono-sub-2');", "iconEl.innerHTML = svg2;")
    html = html.replace("iconEl.classList.add('icono-sub-3');", "iconEl.innerHTML = svg3;")
    
    # ensure default icon for elements without number
    html = html.replace("if (match) {", f"iconEl.innerHTML = svg1;\n                    if (match) {{")

    with open('html_adicional.html', 'w', encoding='utf-8') as f:
        f.write(html)

    # Now fix CSS
    # For .banner-mod-icon inside .banner-grande
    css = re.sub(r'\.banner-mod-icon\s*\{[^}]+mask-image:[^\}]+\}', r'''.banner-mod-icon {
            width: 24px;
            height: 24px;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
            color: var(--mmz-p4) !important;
            margin-right: 8px;
        }''', css, count=1)
        
    # For .banner-mod-icon inside .banner-cintillo
    css = re.sub(r'\.banner-mod-icon\s*\{[^}]+mask-image:[^\}]+\}', r'''.banner-mod-icon {
            width: 24px;
            height: 24px;
            color: var(--mmz-p3) !important;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
        }''', css, count=1)

    # Remove the custom classes .icono-sub-* completely
    css = re.sub(r'/\*\s*conos SVG Personalizados.*?(?=\s*\.banner-mod-name)', '', css, flags=re.DOTALL)
    css = re.sub(r'/\*\s*conos SVG Personalizados.*?(?=\s*\})', '', css, flags=re.DOTALL)
    css = re.sub(r'\.banner-mod-icon\.icono-sub-\d+\s*\{[^}]+\}', '', css)

    with open('estilos.css', 'w', encoding='utf-8') as f:
        f.write(css)

    print("Success!")

if __name__ == '__main__':
    fix()
