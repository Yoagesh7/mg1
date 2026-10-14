import sys
import shutil

def update_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()

    # 1. Update Stage Container min-height for grand proportions
    text = text.replace('min-height: 680px;', 'min-height: 820px;')
    text = text.replace('min-height: 540px;', 'min-height: 600px;')

    # 2. Update .black-curl-overlay height to 380px on desktop
    old_overlay_css = """.black-curl-overlay {
      position: absolute;
      bottom: 0;
      left: 0;
      width: 100%;
      height: 260px;
      pointer-events: none;
      z-index: 20;
      overflow: visible;
    }"""

    new_overlay_css = """.black-curl-overlay {
      position: absolute;
      bottom: 0;
      left: 0;
      width: 100%;
      height: 380px;
      pointer-events: none;
      z-index: 20;
      overflow: visible;
    }"""
    text = text.replace(old_overlay_css, new_overlay_css)

    # In tablet: change from 190px to 270px
    text = text.replace('height: 190px;', 'height: 270px;')

    # In mobile: change from 130px to 180px
    text = text.replace('height: 130px;', 'height: 180px;')

    # 3. Update the SVG DOM to match 380px height and a dramatic, grand arch curve
    old_svg = """<svg class="w-full h-full block" viewBox="0 0 1920 260" preserveAspectRatio="none" fill="none">
          <!-- Expansive Majestic Black Circle Dome Arch: Bigger arch sweep, seamlessly merged with base -->
          <path d="M -60 220 Q 960 10 1980 220 L 1980 500 L -60 500 Z" fill="#000000" stroke="#000000" stroke-width="6"/>
        </svg>"""

    new_svg = """<svg class="w-full h-full block" viewBox="0 0 1920 380" preserveAspectRatio="none" fill="none">
          <!-- Grand Expansive Black Half-Circle Arch Dome: Massive curvature sweep with zero gaps -->
          <path d="M -80 340 Q 960 10 2000 340 L 2000 650 L -80 650 Z" fill="#000000" stroke="#000000" stroke-width="8"/>
        </svg>"""
    text = text.replace(old_svg, new_svg)

    # 4. Enlarge solid black base floor
    text = text.replace('<div class="w-full bg-black h-20 sm:h-24 relative z-20 -mt-1 shadow-2xl"></div>',
                        '<div class="w-full bg-black h-24 sm:h-32 relative z-20 -mt-1 shadow-2xl"></div>')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f'Updated {filename}')

update_file('html.html')
shutil.copyfile('html.html', 'index.html')
print('Synchronized to index.html')
