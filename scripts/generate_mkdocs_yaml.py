import os
import yaml

def get_title(file_path):
    """Extracts the first # Heading from a markdown file."""
    if not os.path.exists(file_path):
        return os.path.basename(file_path).replace('.md', '').title()
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('# '):
                return line.replace('# ', '').strip()
    return os.path.basename(file_path).replace('.md', '').title()

def build_nav_section(directory):
    nav = []
    if not os.path.exists(directory):
        return nav
    # Include index.md first if it exists
    index_path = os.path.join(directory, 'index.md')
    if os.path.exists(index_path):
        nav.append({'Index': index_path.replace('docs/', '')})
    
    files = sorted([f for f in os.listdir(directory) if f.endswith('.md') and f != 'index.md'])
    for f in files:
        file_path = os.path.join(directory, f)
        title = get_title(file_path)
        nav.append({title: file_path.replace('docs/', '')})
    return nav

config = {
    'site_name': 'SBS DhammaVinaya Learning Tools',
    'site_url': 'https://sasanarakkha.github.io/study-tools/',
    'docs_dir': 'docs',
    'site_dir': 'site',
    'theme': {
        'name': 'material',
        'language': 'en',
        'custom_dir': 'identity',
        'font': {'text': False, 'code': False},
        'palette': [
            {'media': '(prefers-color-scheme: light)', 'scheme': 'default', 'primary': 'custom', 'accent': 'custom', 'toggle': {'icon': 'material/brightness-7', 'name': 'Switch to dark mode'}},
            {'media': '(prefers-color-scheme: dark)', 'scheme': 'slate', 'primary': 'custom', 'accent': 'custom', 'toggle': {'icon': 'material/brightness-4', 'name': 'Switch to light mode'}}
        ],
        'features': [
            'navigation.tabs',
            'navigation.tabs.sticky',
            'navigation.top',
            'navigation.indexes',
            'content.code.copy',
            'hide.generator'
        ]
    },
    'markdown_extensions': ['attr_list', {'toc': {'permalink': True}}, 'tables', 'md_in_html', 'nl2br'],
    'plugins': ['search'],
    'extra_css': ['identity/sbs.css'],
    'nav': [
        {'Pre-Pāli Study': 'pre-pali-study.md'},
        {'Dictionaries': build_nav_section('docs/dict')},
        {'Pātimokkha': 'patimokkha.md'},
        {'Bhikkhu Pātimokkha': build_nav_section('docs/bhikkhu_patimokkha')},
        {'Anki Decks': build_nav_section('docs/anki-decks')},
        {'Pāli Class': build_nav_section('docs/pali-class')},
        {'SBS-PER Analysis': 'sbs-per-analysis.md'},
        {'Notebook LM': 'notebook_lm.md'}
    ]
}

print("Generating mkdocs.yaml...")
with open('mkdocs.yaml', 'w', encoding='utf-8') as f:
    yaml.dump(config, f, sort_keys=False, allow_unicode=True)
print("Done.")
