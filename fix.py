import json, glob 
for f in glob.glob('*.ipynb'): 
    nb = json.load(open(f, encoding='utf-8')) 
    nb['metadata']['kernelspec'] = nb['metadata'].get('kernelspec', {}) 
    json.dump(nb, open(f, 'w', encoding='utf-8'), indent=1) 
    print('Touched:', f) 
