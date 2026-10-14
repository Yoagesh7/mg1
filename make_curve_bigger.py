import re
import shutil

def update_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()

    # 1. Update CSS
    # Increase stage container min-height from 580px to 680px to accommodate larger dome
    text = text.replace('min-height: 580px;', 'min-height: 680px;')

    # Increase cards min-height from 500px to 540px so content remains perfectly proportioned
    text = text.replace('min-height: 500px;', 'min-height: 540px;')

    # Increase desktop black-curl-overlay height from 180px to 260px
    # Let's locate the exact rule
    old_overlay_css = """.black-curl-overlay {
      position: absolute;
      bottom: 0;
      left: 0;
      width: 100%;
      height: 180px;
      pointer-events: none;
      z-index: 20;
      overflow: visible;
    }"""

    new_overlay_css = """.black-curl-overlay {
      position: absolute;
      bottom: 0;
      left: 0;
      width: 100%;
      height: 260px;
      pointer-events: none;
      z-index: 20;
      overflow: visible;
    }"""
    text = text.replace(old_overlay_css, new_overlay_css)

    # In tablet: change height from 130px to 190px
    text = text.replace('height: 130px;', 'height: 190px;')

    # In mobile: change height from 85px to 130px
    text = text.replace('height: 85px;', 'height: 130px;')

    # 2. Update the SVG DOM
    # Old SVG:
    # <svg class="w-full h-full block" viewBox="0 0 1920 180" preserveAspectRatio="none" fill="none">
    #   <!-- Reduced Black Circle Dome Arch: Leaves card titles & descriptions visible, fills cleanly down -->
    #   <path d="M -40 140 Q 960 10 1960 140 L 1960 400 L -40 400 Z" fill="#000000" stroke="#000000" stroke-width="4"/>
    # </svg>
    old_svg = """<svg class="w-full h-full block" viewBox="0 0 1920 180" preserveAspectRatio="none" fill="none">
          <!-- Reduced Black Circle Dome Arch: Leaves card titles & descriptions visible, fills cleanly down -->
          <path d="M -40 140 Q 960 10 1960 140 L 1960 400 L -40 400 Z" fill="#000000" stroke="#000000" stroke-width="4"/>
        </svg>"""

    new_svg = """<svg class="w-full h-full block" viewBox="0 0 1920 260" preserveAspectRatio="none" fill="none">
          <!-- Expansive Majestic Black Circle Dome Arch: Bigger arch sweep, seamlessly merged with base -->
          <path d="M -60 220 Q 960 10 1980 220 L 1980 500 L -60 500 Z" fill="#000000" stroke="#000000" stroke-width="6"/>
        </svg>"""
    text = text.replace(old_svg, new_svg)

    # 3. Base floor height: make it robust (h-20 sm:h-24)
    text = text.replace('<div class="w-full bg-black h-16 sm:h-20 relative z-20 -mt-1 shadow-2xl"></div>',
                        '<div class="w-full bg-black h-20 sm:h-24 relative z-20 -mt-1 shadow-2xl"></div>')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f'Updated {filename}')

update_file('html.html')
shutil.copyfile('html.html', 'index.html')
print('Synchronized to index.html')
