from pygal.maps.world import World

worldmap_chart = World()
country_codes = {
    'AUSTRALIA': 'au',
    'EURO AREA': ['at', 'be', 'cy', 'ee', 'fi', 'fr', 'de', 'gr', 'ie', 'it', 'lv', 'lt', \
                 'lu', 'mt', 'nl', 'pt', 'sk', 'si', 'es'],
    'NEW ZEALAND':'nz',
    'UNITED KINGDOM': 'uk',
    'BRAZIL': 'br',
    'CANADA': 'ca',
    'CHINA': 'cn',
    'HONG KONG': 'hk',
    'INDIA': 'in',
    'KOREA': ['kp', 'kr'],
    'MEXICO': 'mx',
    'SOUTH AFRICA': 'za',
    'SINGAPORE': 'sg',
    'DENMARK': 'dk',
    'JAPAN': 'jp',
    'MALAYSIA': 'my',
    'NORWAY': 'no',
    'SWEDEN': 'se',
    'SRI LANKA': 'lk',
    'SWITZERLAND': 'ch',
    'TAIWAN': 'tw'
}
worldmap_chart.title = 'Exchange Rate Change Percentage w.r.t to US Dollar'
worldmap_chart.add('AUSTRALIA', {'au' : 4})
worldmap_chart.render()
#display(SVG(worldmap_chart.render(disable_xml_declaration=True)))from pygal.maps.world import World

worldmap_chart = World()
country_codes = {
    'AUSTRALIA': 'au',
    'EURO AREA': ['at', 'be', 'cy', 'ee', 'fi', 'fr', 'de', 'gr', 'ie', 'it', 'lv', 'lt', \
                 'lu', 'mt', 'nl', 'pt', 'sk', 'si', 'es'],
    'NEW ZEALAND':'nz',
    'UNITED KINGDOM': 'uk',
    'BRAZIL': 'br',
    'CANADA': 'ca',
    'CHINA': 'cn',
    'HONG KONG': 'hk',
    'INDIA': 'in',
    'KOREA': ['kp', 'kr'],
    'MEXICO': 'mx',
    'SOUTH AFRICA': 'za',
    'SINGAPORE': 'sg',
    'DENMARK': 'dk',
    'JAPAN': 'jp',
    'MALAYSIA': 'my',
    'NORWAY': 'no',
    'SWEDEN': 'se',
    'SRI LANKA': 'lk',
    'SWITZERLAND': 'ch',
    'TAIWAN': 'tw'
}
worldmap_chart.title = 'Exchange Rate Change Percentage w.r.t to US Dollar'
worldmap_chart.add('AUSTRALIA', {'au' : 4})
worldmap_chart.render_to_file("word.svg")
