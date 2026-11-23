#!/bin/sh
# Archive material for "What Happened to Newton, Iowa?" — public domain or CC BY only (licences logged in SOURCES.jsonl).
cd "$(dirname "$0")/.." || exit 1
PY=${PY:-python -I}
F="$PY tools/footage.py fetch"
big() {   # name, commons file title, credit, licence, width
  ls raw/$1.* >/dev/null 2>&1 && return 0
  enc=$($PY -c "import sys,urllib.parse;print(urllib.parse.quote(sys.argv[1].replace(' ','_')))" "$2")
  $F "https://commons.wikimedia.org/wiki/Special:FilePath/$enc?width=${5:-2600}" --name "$1" \
    --page "https://commons.wikimedia.org/wiki/File:$enc" --license "$4" --credit "$3"
}
flk() {   # name, flickr page url, credit, licence
  ls raw/$1.* >/dev/null 2>&1 && return 0
  img=$(curl -s -L -A "lemo-film-research/1.0" "$2" | grep -oE 'property="og:image" content="[^"]+"' | head -1 | sed 's/.*content="//;s/"$//')
  [ -n "$img" ] || { echo "no image for $1"; return 1; }
  $F "$img" --name "$1" --page "$2" --license "$4" --credit "$3"
}
SB="Sanborn Map Company (Library of Congress)"
SBF="Sanborn Fire Insurance Map from Newton, Jasper County, Iowa. LOC sanborn02773"
big sanborn1918_index "$SBF 007-1.jpg" "$SB, Nov 1918" "Public domain" 3400
big sanborn1918_maytag "$SBF 007-3.jpg" "$SB, Nov 1918" "Public domain" 3400
big sanborn1883 "$SBF 001.jpg" "$SB, Nov 1883" "Public domain" 3000
big sanborn1906_index "$SBF 005-1.jpg" "$SB, Feb 1906" "Public domain" 3000
big pano1907 "Newton, IA LCCN2007660887.tif" "F.J. Bandholtz, 1907 (Library of Congress)" "Public domain" 3257
big birdseye1868 "Bird's eye view of Newton, Jasper Co., Iowa 1868. LOC 73693405.jpg" "A. Ruger, 1868 (Library of Congress)" "Public domain" 3600
big fl_maytag_1935 "Frederick Maytag, 1935.jpg" "Los Angeles Times, 12 March 1935 (UCLA Library, CC BY 4.0)" "CC BY 4.0" 2400
big dealer1926 "Maytag dealer.jpg" "Maytag dealer, Butler County, c. 1926" "Public domain" 600
big antique_washer "Antique Maytag Washing Machine.jpg" "AdamjVogt, Wikimedia Commons" "Public domain" 785
big wringer "Old Maytag wringer washing machine clothes washer.jpg" "Watts, Flickr (CC BY 2.0)" "CC BY 2.0" 2068
big hq2005 "Maytaghqnight.jpg" "Adm58, English Wikipedia, 2005" "Public domain" 640
big newton_tower "Newton Tower - panoramio.jpg" "Corey Coyle, 2007 (CC BY 3.0)" "CC BY 3.0" 1484
big maytag_dairy "Maytag.jpg" "Christiane Tas, 2010" "Public domain" 2600
big maytag_park "Rabbit Maytag Park Newton Iowa 8-2011.jpg" "Xtianetas, 2011 (CC BY 3.0)" "CC BY 3.0" 1568
big obama_trinity1 "Barack Obama at Trinity Structural Towers Manufacturing Plant 4-22-09.JPG" "Pete Souza, White House, 22 April 2009" "Public domain" 525
big obama_trinity2 "Barack Obama at Trinity Structural Towers Manufacturing Plant 4-22-09 2.JPG" "Pete Souza, White House, 22 April 2009" "Public domain" 624
big speedway2007 "IowaSpeedwayJune2007.jpg" "Matt Owen, 2007 (CC BY 2.0)" "CC BY 2.0" 3008
big speedway2017 "20170708 10 Iowa Speedway (43817176824).jpg" "David Wilson, 2017 (CC BY 2.0)" "CC BY 2.0" 2816
big ww1_maytag "Maytag in World War 1 (9409650193).jpg" "Maytag advertisement, c. 1918; scan dok1 (CC BY 2.0)" "CC BY 2.0" 1800
DW="David Wilson, 2014 (CC BY 2.0)"
flk square2014_a "https://www.flickr.com/photos/32693718@N07/18945602798" "$DW" "CC BY 2.0"
flk square2014_b "https://www.flickr.com/photos/32693718@N07/18970042910" "$DW" "CC BY 2.0"
flk square2014_court "https://www.flickr.com/photos/32693718@N07/19131594396" "$DW" "CC BY 2.0"
flk square2014_c "https://www.flickr.com/photos/32693718@N07/19131593676" "$DW" "CC BY 2.0"
flk mural2017 "https://www.flickr.com/photos/32693718@N07/49087017453" "David Wilson, 2017 (CC BY 2.0)" "CC BY 2.0"
DK="Maytag advertisement; scan dok1 (CC BY 2.0)"
flk ad1916 "https://www.flickr.com/photos/51096110@N00/3209788016" "$DK" "CC BY 2.0"
flk ad1916_dream "https://www.flickr.com/photos/51096110@N00/12352289753" "$DK" "CC BY 2.0"
flk ad1921_mm "https://www.flickr.com/photos/51096110@N00/9577066645" "$DK" "CC BY 2.0"
flk ad_mm_power "https://www.flickr.com/photos/51096110@N00/15497702385" "$DK" "CC BY 2.0"
flk ad_mm_outdoors "https://www.flickr.com/photos/51096110@N00/15046136844" "$DK" "CC BY 2.0"
flk ad_mm_tree "https://www.flickr.com/photos/51096110@N00/19278755386" "$DK" "CC BY 2.0"
flk ad_evolution "https://www.flickr.com/photos/51096110@N00/23772845104" "$DK" "CC BY 2.0"
