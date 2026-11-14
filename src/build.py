"""Assemble index.html: template + embedded Montserrat + logo paths + starting menu."""
import base64, json, os
H = os.path.dirname(os.path.abspath(__file__))
rd = lambda f, m='r': open(os.path.join(H, f), m).read()
faces = ''.join(
    "@font-face{font-family:'Montserrat';font-weight:%d;font-style:normal;font-display:block;"
    "src:url(data:font/woff2;base64,%s) format('woff2')}\n" % (w, base64.b64encode(rd('M-%s.woff2' % n, 'rb')).decode())
    for n, w in [('Regular', 400), ('Bold', 700), ('ExtraBold', 800)])
faces += ''.join(
    "@font-face{font-family:'Sofia Sans Extra Condensed';font-weight:%d;font-style:normal;font-display:block;"
    "src:url(data:font/woff2;base64,%s) format('woff2')}\n" % (w, base64.b64encode(rd('S-%s.woff2' % n, 'rb')).decode())
    for n, w in [('Regular', 400), ('Bold', 700)])
seed = json.dumps(json.loads(rd('seed.json')), ensure_ascii=False).replace('</', '<\\/')
html = rd('template.html').replace('/*FONTS*/', faces).replace('__SEED__', seed).replace('__WM__', rd('wm.txt')).replace('__LOGO__', rd('logo.svg'))
OUT = os.path.join(H, '..', 'index.html')
open(OUT, 'w').write(html)
print(len(html), 'bytes')
