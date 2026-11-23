#!/usr/bin/env python3
"""lines.json + narration durations + the shot list below → film.json (scenes, voice starts, subtitles) and audio/cues.json.
Timing: each line starts GAP s after the previous one ends; a chapter card (CARD s) opens each chapter; the end card is fixed.
Every scene lasts from its line's start to the next scene's start, so nothing is left empty.
Rings: [src_x, src_y, r, label, at] where at ≥ 0 is seconds after the line starts and at < 0 is a fraction of the line (-0.4 = 40%)."""
import json, os
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
L = json.load(open(os.path.join(D, 'audio/lines.json'), encoding='utf-8'))
DUR = json.load(open(os.environ.get('DURFILE') or os.path.join(D, 'audio/vo/dur.json')))
GAP, CARD, LEAD, END = 0.9, 4.2, 1.2, 16.0

CH = {'open': (None, None), 'feeder': ('I', 'The Feeder'), 'gyrafoam': ('II', 'The Gyrafoam'), 'strike': ('III', 'The Strike'),
      'depend': ('IV', 'The Dependability People'), 'sold': ('V', 'Sold'), 'last': ('VI', 'The Last Shift'), 'next': ('VII', 'What Newton Built Next')}
CHIMG = {'feeder': 'birdseye1868', 'gyrafoam': 'patent1866779-1', 'strike': 'sanborn1918_maytag', 'depend': 'wringer', 'sold': 'hq2005',
         'last': 'hq2005', 'next': 'mural2017'}
COLOUR = ('wringer', 'hq2005', 'obama_trinity', 'mural2017', 'square2014', 'speedway', 'maytag_dairy', 'maytag_park', 'newton_tower', 'antique_washer', 'fl_maytag', 'dealer1926')

P = lambda img, **k: dict(type='photo', img=img, **k)
SB18 = 'SANBORN MAP · NEWTON · NOV 1918'
PAT = 'U.S. PATENT 1,866,779 · H. F. SNYDER · FILED 14 JUNE 1922'
TRIN = 'INSIDE THE FORMER MAYTAG PLANT · WHITE HOUSE PHOTO · 2009'
HQ = 'MAYTAG HEADQUARTERS, NEWTON · 2005'
WR = 'MAYTAG WRINGER WASHER · PHOTO: WATTS (CC BY 2.0)'
S = {
 # ── cold open ──
 'n01': dict(type='open'),
 'n02': P('sanborn1918_maytag', tag=SB18 + ' · THE MAYTAG WORKS', z=(1.0, 1.12), fx=.4, fy=.7),
 'n03': dict(type='stat', img='hq2005', num='550', label='workers on the last day', tag=HQ, at=0.3),
 'n04': dict(type='quote', img='wringer', imgTag=WR, q=['“Maytag,', 'the dependability', 'people.”'], who='THE SIGN MARK WICKLIFF CARRIED OUT · AP · 26 OCT 2007', at=-0.45),
 'n05': dict(type='stat', img='sanborn1918_maytag', num='1 in 5', label='people in Newton worked for Maytag at the peak', tag=SB18 + ' · THE MAYTAG WORKS', at=-0.55),
 'n06': P('wringer', tag=WR, z=(1.0, 1.12)),
 'n07': dict(type='title'),
 'n08': dict(type='pano', img='pano1907', tag='PANORAMA · F. J. BANDHOLTZ · NEWTON · 1907 · LIBRARY OF CONGRESS'),
 'n09': P('ad1921_mm', tag='MAYTAG ADVERTISEMENT · c. 1921', z=(1.0, 1.1), fy=.3),
 'n10': P('dealer1926', tag='A MAYTAG DEALER AND HIS TRUCKS · c. 1926', small=1),
 # ── I · The Feeder ──
 'n11': P('birdseye1868', tag='BIRD’S-EYE VIEW OF NEWTON · A. RUGER · 1868 · LIBRARY OF CONGRESS', z=(1.0, 1.25), fy=.45),
 'n12': dict(type='card', name='Frederick Louis Maytag', sub='1857–1937 · CO-FOUNDER, 1893', img='fl_maytag_1935', tag='F. L. MAYTAG · LOS ANGELES TIMES · 1935 (CC BY 4.0)', date='1893', portrait=1),
 'n13': P('sanborn1883', tag='SANBORN MAP · NEWTON · NOV 1883', z=(1.0, 1.2), fy=.4),
 'n14': dict(type='stat', img='sanborn1906_index', num='1902', label='the largest maker of self-feeders in the world', tag='SANBORN MAP · NEWTON · FEB 1906', at=0.5),
 'n15': dict(type='pano', img='pano1907', tag='NEWTON, IOWA · 1907 · F. J. BANDHOLTZ · LIBRARY OF CONGRESS', date='1907', from_=.15, to=.85),
 'n16': P('ad1916', tag='MAYTAG ADVERTISEMENT · “EVOLUTION” · c. 1916', z=(1.0, 1.12), fy=.2),
 'n17': P('antique_washer', tag='AN EARLY MAYTAG WASHER · PHOTO, WIKIMEDIA COMMONS', small=1, colour=1),
 'q01': dict(type='quote', img='antique_washer', colour=1, imgTag='AN EARLY MAYTAG WASHER', q=['“We call this', 'the Milkstool', 'Dolly.”'], who='LELAND SMITH · 40 YEARS AT MAYTAG · NPR · 2008', at=-0.55),
 'n18': P('sanborn1918_index', tag=SB18 + ' · INDEX · POPULATION 5,100', date='1918', z=(1.0, 1.1), fy=.3),
 'n19': P('sanborn1918_maytag', tag=SB18 + ' · SHEET 3', z=(1.0, 1.04), fy=.62, fy2=.04,
          rings=[[1190, 2338, 560, 'MAYTAG CO.', -0.05], [2401, 1849, 330, 'ONE MINUTE MFG CO.', -0.33], [2125, 467, 300, 'WOODROW MFG CO.', -0.55]]),
 'n20': dict(type='stat', img='sanborn1918_index', num='4', label='washing-machine makers · a town of about 5,000', tag=SB18 + ' · INDEX', at=0.4),
 # ── II · The Gyrafoam ──
 'n21': P('ad_mm_outdoors', tag='MAYTAG MULTI-MOTOR ADVERTISEMENT · GASOLINE ENGINE', date='1914', z=(1.0, 1.1), fy=.4),
 'n22': P('ad_mm_power', tag='MAYTAG MULTI-MOTOR ADVERTISEMENT', date='1919', z=(1.0, 1.08)),
 'n23': P('ad_mm_tree', tag='MAYTAG ADVERTISEMENT', z=(1.05, 1.15)),
 'n24': P('patent1866779-1', tag=PAT, z=(1.0, 1.08), fy=.35, name='Howard F. Snyder', role='HEAD OF DEVELOPMENT · THE MAYTAG CO.'),
 'n25': P('patent1866779-3', tag=PAT + ' · FIG. 4', z=(1.0, 1.15), fy=.18, rings=[[735, 600, 260, 'THE AGITATOR', -0.45]]),
 'n26': P('patent1866779-1', tag=PAT, date='1922', fy=.12, z=(1.1, 1.18), rings=[[764, 442, 210, 'FILED 14 JUNE 1922', 0.6]]),
 'n27': dict(type='stat', img='ad1921_mm', num='38 → 1', label='U.S. washer makers · by one company history', tag='MAYTAG ADVERTISEMENT · c. 1921', at=-0.4),
 'n28': P('ad1921_mm', tag='MAYTAG ADVERTISEMENT · c. 1921', z=(1.12, 1.25), fy=.35),
 'n29': dict(type='stat', img='ad_mm_tree', num='1,000,000', label='Maytag washers by 1927', tag='MAYTAG ADVERTISEMENT', at=0.4),
 'n30': dict(type='bars', title='NEWTON · POPULATION · U.S. CENSUS', data=[['1900', 3682], ['1910', 4616], ['1920', 6627], ['1930', 11560]], img='sanborn1918_index'),
 'n31': P('ad1916_dream', tag='MAYTAG ADVERTISEMENT · c. 1916', z=(1.0, 1.1), fy=.3),
 'n32': dict(type='card', name='F. L. Maytag', sub='75 IN 1932 · $100 FOR EACH OF 1,500 WORKERS', img='fl_maytag_1935', tag='F. L. MAYTAG · LOS ANGELES TIMES · 1935 (CC BY 4.0)', date='1932', portrait=1),
 # ── III · The Strike ──
 'n33': dict(type='card', name='F. L. Maytag', sub='DIED 26 MARCH 1937 · BURIED IN NEWTON', img='fl_maytag_1935', tag='F. L. MAYTAG · 1935 (CC BY 4.0)', date='1937', portrait=1),
 'n34': P('sanborn1918_maytag', tag=SB18 + ' · THE MAYTAG WORKS', z=(1.15, 1.3), fx=.35, fy=.7),
 'n35': dict(type='stat', img='sanborn1918_maytag', num='−10%', label='pay cut · May 1938 · UE Local 1116', tag=SB18 + ' · THE MAYTAG WORKS', at=0.4),
 'n36': dict(type='board', upto=0), 'n37': dict(type='board', upto=2), 'n38': dict(type='board', upto=3),
 'n39': dict(type='stat', img='sanborn1918_maytag', num='34', label='people hurt on the night of 21 July 1938', tag=SB18 + ' · THE STREETS AROUND THE PLANT', at=-0.55),
 'n40': dict(type='board', upto=3, hold=1),
 'q02': dict(type='quote', img='sanborn1918_maytag', fx=.35, fy=.7, imgTag=SB18 + ' · THE MAYTAG WORKS', q=['“Apparently,', 'our employees', 'weren’t so happy', 'as we thought!”'], who='FRED MAYTAG II · AS REPORTED · INVESTIGATE MIDWEST, 2015'),
 'n41': dict(type='board', upto=4),
 'n42': P('sanborn1918_maytag', tag=SB18, z=(1.0, 1.08), fy=.6),
 # ── IV · The Dependability People ──
 'n43': dict(type='stat', img='wringer', num='1941–45', label='no washers: parts for military aircraft', tag=WR, at=0.4),
 'n44': dict(type='stat', img='sanborn1918_maytag', num='1949', label='Plant 2 · the first Maytag automatic', tag=SB18 + ' · THE FIRST MAYTAG WORKS', at=0.3),
 'n45': P('hq2005', tag='MAYTAG HEADQUARTERS (DEDICATED 1961) · PHOTO 2005', small=1, date='1962'),
 'n46': dict(type='stat', img='antique_washer', num='1967', label='the lonely repairman: nothing to fix', tag='A MAYTAG WASHER · WIKIMEDIA COMMONS', at=0.3),
 'n47': P('ad_mm_power', tag='MAYTAG ADVERTISEMENT', z=(1.0, 1.1), fy=.3),
 'q03': dict(type='quote', img='hq2005', colour=1, imgTag=HQ, q=['“We made good', 'wages there,', 'but we also made', 'a good product.”'], who='CARL REPP · 30 YEARS AT THE PLANT · CBS NEWS · 2007', at=-0.25),
 'q04': dict(type='quote', img='hq2005', colour=1, imgTag=HQ, q=['“They call us', 'the dependability', 'people.”'], who='CARL REPP · CBS NEWS · 2007', at=0.2),
 'n48': dict(type='stat', img='wringer', num='11.7M', label='wringer washers built in Newton · to 1983', tag=WR, at=-0.6),
 'n49': dict(type='stat', img='newton_tower', num='3,000+', label='employed in Newton at the peak · 1 in 5 people in town', tag='NEWTON WATER TOWER · COREY COYLE, 2007 (CC BY 3.0)', at=0.4),
 'n50': P('maytag_park', tag='MAYTAG PARK, NEWTON · XTIANETAS, 2011 (CC BY 3.0)', z=(1.0, 1.08)),
 'n51': P('square2014_court', tag='THE SQUARE, NEWTON · DAVID WILSON, 2014 (CC BY 2.0)', z=(1.0, 1.06)),
 'q05': dict(type='quote', img='square2014_b', colour=1, imgTag='NEWTON · DAVID WILSON, 2014 (CC BY 2.0)', q=['“At Maytag,', 'it was 30 years', 'and you got', 'to retire.”'], who='DENA JOHNSON PERVIS · NEWTON · NPR · 2006', at=-0.45),
 'n52': dict(type='ledger', title='THE MAYTAG PROMISE', items=[['30', 'years at the plant'], ['+', 'a pension'], ['+', 'full medical benefits']], img='square2014_court', imgTag='THE SQUARE, NEWTON · 2014'),
 # ── V · Sold ──
 'n53': dict(type='chain', upto=2), 'n54': dict(type='chain', upto=2, hold=1),
 'n55': dict(type='stat', img='newton_tower', num='2003', label='Newton layoffs begin', tag='NEWTON · COREY COYLE, 2007 (CC BY 3.0)', at=-0.6),
 'n56': dict(type='bids'),
 'n57': dict(type='chain', upto=4),
 'n58': dict(type='split', a=['≈ 1,000', 'jobs in the plant'], b=['≈ 900', 'jobs at headquarters'], date='10 MAY 2006', tag='WHIRLPOOL’S ANNOUNCEMENT · AP · 11 MAY 2006'),
 'n59': dict(type='stat', img='square2014_court', num='$100M+', label='offered by the state of Iowa · not enough', tag='THE JASPER COUNTY COURTHOUSE, NEWTON · 2014 (CC BY 2.0)', at=-0.25),
 'n60': P('hq2005', tag=HQ, small=1),
 'q06': dict(type='quote', img='hq2005', colour=1, imgTag=HQ, q=['“Now the fundamentals', 'of the company', 'had eroded…', 'They were losing money.”'], who='JEFF NOEL · WHIRLPOOL · CBS NEWS · 2007'),
 'n61': dict(type='quote', img='wringer', colour=1, imgTag=WR, q=['“widespread', 'epidemic”'], who='TED JOHNSON · PRESIDENT, UAW LOCAL 997 · AP · 2007', at=-0.4),
 'n62': P('square2014_a', tag='NEWTON · DAVID WILSON, 2014 (CC BY 2.0)', z=(1.0, 1.08)),
 'q07': dict(type='quote', img='square2014_c', colour=1, imgTag='NEWTON · DAVID WILSON, 2014 (CC BY 2.0)', q=['“My aunt worked', 'there for 30 years…', 'It’s sad.', 'It’s like a death.”'], who='VICKY DUSHEIN · MAYTAG LINE WORKER, 22 YEARS · NPR · 2006', at=-0.3),
 # ── VI · The Last Shift ──
 'n63': dict(type='open', again=1),
 'n64': dict(type='stat', img='sanborn1918_maytag', num='550', label='on the line, 25 October 2007', tag=SB18 + ' · THE MAYTAG WORKS', at=0.3),
 'n65': dict(type='card', name='Mark Wickliff', sub='', lines=['49 · 26½ years at Maytag', 'Four generations of Maytag workers', 'Carried out “Maytag, the dependability people”'], img='wringer', imgTag=WR, tag='AP · 26 OCTOBER 2007', date='2007', noportrait=1),
 'q08': dict(type='quote', img='wringer', colour=1, imgTag=WR, q=['“It’s just close', 'enough to look for', 'another job.”'], who='MARK WICKLIFF · 26½ YEARS · AP · 2007'),
 'q09': dict(type='quote', img='wringer', colour=1, imgTag=WR, q=['“I’m numb,', 'I’m scared.', 'I’ll be all right,', 'I think.”'], who='MIKE JACKSON · 18 YEARS · AP · 2007', at=-0.25),
 'n67': dict(type='quote', img='hq2005', colour=1, imgTag=HQ, q=['R.I.P.', '“I love you all.”'], who='PLAQUE ON THE PLANT FENCE · CBS / AP · 26 OCT 2007', at=-0.35),
 'q10': dict(type='quote', img='square2014_court', colour=1, imgTag='THE SQUARE, NEWTON · 2014', q=['“I’ve seen', 'grown men crying', 'that day.”'], who='MINDY POLLOCK · 22 YEARS AT MAYTAG · PRI THE WORLD / WGBH · 2017', at=-0.45),
 'n69': dict(type='card', name='Jim Schutte', sub='', lines=['Machine repairman, 21 years', 'His 30 years would have come on 17 August', 'Retire now? “Probably never.”'], img='sanborn1918_maytag', imgTag=SB18 + ' · THE MAYTAG WORKS', tag='PRI THE WORLD / WGBH · 2017', noportrait=1),
 'n70': dict(type='dots', n=1800, red=550), 'n71': dict(type='dots', n=1800, red=550, hold=1),
 # ── VII · What Newton Built Next ──
 'n72': dict(type='stat', img='newton_tower', num='9.9%', label='unemployment in Newton, 2009', tag='NEWTON · COREY COYLE, 2007 (CC BY 3.0)', at=0.3),
 'n73': P('square2014_c', tag='NEWTON · DAVID WILSON, 2014 (CC BY 2.0)', z=(1.0, 1.08)),
 'n74': P('sanborn1918_maytag', tag=SB18 + ' · THE MAYTAG WORKS', z=(1.1, 1.2), fx=.45, fy=.75),
 'n75': dict(type='stat', img='obama_trinity1', num='154', label='acres cleaned and ready for reuse, 2008', tag='U.S. EPA · FORMER MAYTAG PLANT SITE · 2009', at=-0.75),
 'n76': dict(type='stat', img='sanborn1918_maytag', num='140 ft', label='wind-turbine blades: too long for the old buildings', tag=SB18 + ' · THE OLD MAYTAG BUILDINGS', at=-0.45),
 'n77': P('obama_trinity1', tag='WIND-TOWER STEEL IN THE FORMER MAYTAG PLANT · 2009', small=1, date='2009'),
 'n78': P('obama_trinity2', tag='PRESIDENT OBAMA IN THE FORMER MAYTAG PLANT · PETE SOUZA · 22 APRIL 2009', small=1, name='Newton, Iowa', role='22 APRIL 2009 · TRINITY STRUCTURAL TOWERS'),
 'q11': dict(type='quote', img='obama_trinity1', colour=1, imgTag=TRIN, q=['“These floors', 'were dark', 'and silent.”'], who='PRESIDENT BARACK OBAMA · NEWTON · 22 APRIL 2009'),
 'n79': dict(type='stat', img='mural2017', num='1,100+', label='workers at the TPI blade plant', tag='“WELCOME TO NEWTON” · DAVID WILSON, 2017 (CC BY 2.0)', at=0.3),
 'n80': dict(type='compare', items=[['2001', 37], ['2015', -20]], title='FACTORY PAY IN JASPER COUNTY · AGAINST THE IOWA AVERAGE', src='DAVE SWENSON, IOWA STATE UNIVERSITY · PRI THE WORLD, 2017'),
 'q12': dict(type='quote', img='square2014_court', colour=1, imgTag='THE SQUARE, NEWTON · 2014', q=['“You can’t take', 'the good paying jobs…', 'and replace them', 'with half the pay.”'], who='KATHLEEN TIFFANY · 30 YEARS AT MAYTAG · CBS NEWS · 2007', at=-0.4),
 'n81': dict(type='stat', img='square2014_a', num='710', label='jobs lost when the blade plant closed · 2021', tag='NEWTON · DAVID WILSON, 2014 (CC BY 2.0)', at=-0.68),
 'n82': dict(type='stat', img='square2014_b', num='2025', label='the blade plant reopens', tag='NEWTON · DAVID WILSON, 2014 (CC BY 2.0)', at=0.4),
 'n83': dict(type='seq', items=[['speedway2007', 'IOWA SPEEDWAY · MATT OWEN, 2007 (CC BY 2.0)'], ['speedway2017', 'IOWA SPEEDWAY · DAVID WILSON, 2017 (CC BY 2.0)'],
                               ['hq2005', 'THE FORMER MAYTAG HEADQUARTERS · 2005'], ['maytag_dairy', 'MAYTAG DAIRY FARMS, NEWTON · CHRISTIANE TAS, 2010']]),
 'n84': dict(type='pop', data=[[1900, 3682], [1910, 4616], [1920, 6627], [1930, 11560], [1940, 10462], [1960, 15381], [1970, 15619], [1980, 15292], [2000, 15579], [2020, 15760]]),
 'n85': dict(type='pair', a='pano1907', b='square2014_court', ta='1907 · THE SQUARE · F. J. BANDHOLTZ', tb='2014 · THE SQUARE · ≈ SAME VIEW · DAVID WILSON (CC BY 2.0)'),
 'n86': P('wringer', tag=WR, z=(1.0, 1.1)),
 'n87': dict(type='pano', img='pano1907', tag='NEWTON, IOWA · 1907 · F. J. BANDHOLTZ', from_=.8, to=.3),
 'n88': P('square2014_court', tag='THE SQUARE, NEWTON · DAVID WILSON, 2014 (CC BY 2.0)', z=(1.0, 1.1)),
 'n89': P('square2014_b', tag='NEWTON · DAVID WILSON, 2014 (CC BY 2.0)', z=(1.0, 1.08)),
 'n90': P('mural2017', tag='“WELCOME TO NEWTON” · DAVID WILSON, 2017 (CC BY 2.0)', z=(1.08, 1.12)),
}
missing = [l['id'] for l in L if l['id'] not in S]
if missing: raise SystemExit('no shot for ' + ', '.join(missing))
scenes, vo, subs, t, prev = [], {}, [], LEAD, None
for l in L:
    ch = l['chapter']
    if ch != prev and CH[ch][0]:
        scenes.append(dict(type='chapter', t0=round(t, 2), num=CH[ch][0], title=CH[ch][1], img=CHIMG[ch])); t += CARD
    prev = ch; d = DUR[l['id']]
    sh = dict(S[l['id']]); sh['t0'] = round(t, 2); sh['line'] = l['id']; sh['vd'] = round(d, 2)
    if 'img' in sh and 'colour' not in sh and sh['img'].startswith(COLOUR): sh['colour'] = 1
    scenes.append(sh); vo[l['id']] = round(t, 3)
    parts = l['subs']; n = sum(len(p) for p in parts); tt = t
    for i, p in enumerate(parts):
        dd = d * len(p) / n; subs.append([round(tt - .1, 2), round(tt + dd + (.3 if i == len(parts) - 1 else .02), 2), p]); tt += dd
    t += d + GAP
for i in range(len(subs) - 1): subs[i][1] = round(min(subs[i][1], subs[i + 1][0] - .02), 2)
scenes.append(dict(type='end', t0=round(t + .6, 2)))
dur = round(t + .6 + END, 1)
for i, s in enumerate(scenes): s['t1'] = scenes[i + 1]['t0'] if i + 1 < len(scenes) else dur
F = dict(dur=dur, scenes=scenes, vo=vo, subs=subs)
json.dump(F, open(os.path.join(D, 'film.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
json.dump([{'t0': a, 't1': b, 'text': s} for a, b, s in subs], open(os.path.join(D, 'audio/cues.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('scenes', len(scenes), 'subs', len(subs), 'duration', dur, 's =', round(dur / 60, 1), 'min')
