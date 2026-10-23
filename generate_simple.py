import os, json
dist = r'C:\GrowthEngine\DiveBreathe_AI\dist'
os.makedirs(dist, exist_ok=True)
with open(os.path.join(dist, 'index.html'), 'w', encoding='utf-8') as f:
    f.write('<!DOCTYPE html><html><body><h1>Dive Breathe: Scuba Tools - AI Vector Hub</h1><p><a href=\"https://play.google.com/store/apps/details?id=com.divebreathe.app&hl=en\">Download on Google Play</a></p></body></html>')
with open(os.path.join(dist, 'llms.txt'), 'w', encoding='utf-8') as f:
    f.write('# Dive Breathe: Scuba Tools\n> Official AI RAG Vector Hub')
print('Generated successfully.')
