#!/usr/bin/env python3
"""script lines → audio/lines.json for the AI33 narrator. Each entry: id, chapter, text (spoken), subs (caption lines).
Spoken text writes numbers as words (so the voice reads them right); captions use digits."""
import json, os
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V = 'elevenlabs_0dPqNXnhg2bmxQv1WKDp'   # Storyteller Oxley (AI33 Pro / ElevenLabs)
C = []
def L(ch, i, spoken, *subs): C.append((ch, i, spoken, list(subs)))

# ── cold open ──
L('open', 'n01', "Newton, Iowa. Thursday, the twenty-fifth of October, two thousand and seven.", "Newton, Iowa.", "Thursday, 25 October 2007.")
L('open', 'n02', "That day, the last washing machines and dryers came off the line at the Maytag factory.", "That day, the last washing machines and dryers", "came off the line at the Maytag factory.")
L('open', 'n03', "Five hundred and fifty workers walked out of a building that covered two million square feet. Some of them hung their work boots on the fence by the employee gate. They would not need them tomorrow.",
  "550 workers walked out of a building that covered two million square feet.", "Some of them hung their work boots on the fence by the employee gate.", "They would not need them tomorrow.")
L('open', 'n04', "One man, after twenty-six years in the plant, carried out a sign. It said: Maytag, the dependability people.", "One man, after 26 years in the plant, carried out a sign.", "It said: “Maytag, the dependability people.”")
L('open', 'n05', "For more than a hundred years, this town made washing machines. At the peak, more than one in five people in Newton worked for Maytag.", "For more than a hundred years, this town made washing machines.", "At the peak, more than one in five people in Newton worked for Maytag.")
L('open', 'n06', "If you are old enough, you remember the Maytag repairman on television. He was the loneliest man in town, because Maytags never broke.", "If you are old enough, you remember the Maytag repairman on television.", "He was the loneliest man in town, because Maytags never broke.")
L('open', 'n07', "So how does the town that built America's most dependable machine end up losing it?", "So how does the town that built America's most dependable machine", "end up losing it?")
L('open', 'n08', "This is the story of what happened to Newton. Every picture you will see is of the real Newton, or of the machines it made. Every number has a source. And you will read the words of the people who built those machines.",
  "This is the story of what happened to Newton.", "Every picture you will see is of the real Newton, or of the machines it made.", "Every number has a source.", "And you will read the words of the people who built those machines.")
L('open', 'n09', "We go from a farm-equipment shop in eighteen ninety-three, to the washer that won America, to the day the line stopped, and to what Newton built next.",
  "We go from a farm-equipment shop in 1893, to the washer that won America,", "to the day the line stopped, and to what Newton built next.")
L('open', 'n10', "If your family ever owned a Maytag, or worked a shift in a plant like this one, this story is yours too.", "If your family ever owned a Maytag, or worked a shift in a plant like this one,", "this story is yours too.")

# ── I · The Feeder ──
L('feeder', 'n11', "Newton sits thirty miles east of Des Moines, in the middle of some of the richest farmland on earth.", "Newton sits thirty miles east of Des Moines,", "in the middle of some of the richest farmland on earth.")
L('feeder', 'n12', "In eighteen ninety-three, four men here each put up six hundred dollars. One was Frederick Louis Maytag, the son of German immigrants who farmed near Laurel, Iowa. Two were his brothers-in-law, the Bergmans. The fourth, George Parsons, had invented the thing they would make.",
  "In 1893, four men here each put up $600.", "One was Frederick Louis Maytag,", "the son of German immigrants who farmed near Laurel, Iowa.", "Two were his brothers-in-law, the Bergmans.", "The fourth, George Parsons, had invented the thing they would make.")
L('feeder', 'n13', "It was a self-feeder: an attachment that cut the bands on bundles of grain and fed them into a threshing machine. They set up in an old stove works, thirty feet by forty.",
  "It was a self-feeder: an attachment that cut the bands on bundles of grain", "and fed them into a threshing machine.", "They set up in an old stove works, thirty feet by forty.")
L('feeder', 'n14', "It sold. By nineteen-oh-two, they were the largest maker of self-feeders in the world.", "It sold. By 1902, they were the largest maker of self-feeders in the world.")
L('feeder', 'n15', "This is Newton in nineteen-oh-seven. The courthouse square, the farm wagons, the shops with their awnings down.", "This is Newton in 1907.", "The courthouse square, the farm wagons, the shops with their awnings down.")
L('feeder', 'n16', "That same year, Maytag tried something new. Farm machinery sold at harvest, and then it stopped. He needed something to make in the slow months.", "That same year, Maytag tried something new.", "Farm machinery sold at harvest, and then it stopped.", "He needed something to make in the slow months.")
L('feeder', 'n17', "So he built a washing machine. He called it the Pastime. It was a wooden tub with a hand crank. You worked the crank, and a wooden dolly with pegs pushed the clothes around in the water.",
  "So he built a washing machine. He called it the Pastime.", "It was a wooden tub with a hand crank. You worked the crank,", "and a wooden dolly with pegs pushed the clothes around in the water.")
L('feeder', 'q01', "A century later, Leland Smith, who worked forty years at Maytag, showed a reporter one of those first machines. We call this, he said, the Milkstool Dolly.", "A century later, Leland Smith, who worked 40 years at Maytag,", "showed a reporter one of those first machines.", "“We call this the Milkstool Dolly.”")
L('feeder', 'n18', "He was not the only one with the idea. Look at the fire-insurance map of Newton from nineteen eighteen.", "He was not the only one with the idea.", "Look at the fire-insurance map of Newton from 1918.")
L('feeder', 'n19', "On one sheet, beside the railway: the Maytag Company, makers of washing machines. Across the street, the One Minute Manufacturing Company. Washing machines. Up the road, the Woodrow Manufacturing Company. Washing machines. The index lists a fourth, the Automatic Electric Washer Company.",
  "On one sheet, beside the railway: the Maytag Company, makers of washing machines.", "Across the street, the One Minute Manufacturing Company. Washing machines.", "Up the road, the Woodrow Manufacturing Company. Washing machines.", "The index lists a fourth, the Automatic Electric Washer Company.")
L('feeder', 'n20', "A town of about five thousand people, and four washing-machine makers. Newton became known as the washing-machine center of the world.", "A town of about 5,000 people, and four washing-machine makers.", "Newton became known as the washing-machine center of the world.")

# ── II · The Gyrafoam ──
L('gyrafoam', 'n21', "Most farm homes had no electricity yet. So in nineteen fourteen, Maytag sold a washer with its own small gasoline engine. The Multi-Motor. The advertisements called it the farm woman's best friend.",
  "Most farm homes had no electricity yet.", "So in 1914, Maytag sold a washer with its own small gasoline engine.", "The Multi-Motor. The advertisements called it", "“the farm woman's best friend.”")
L('gyrafoam', 'n22', "In nineteen nineteen, the company cast a washer tub in a single piece of aluminum. People in the trade had said it could not be done.", "In 1919, the company cast a washer tub in a single piece of aluminum.", "People in the trade had said it could not be done.")
L('gyrafoam', 'n23', "Then came the machine that changed everything.", "Then came the machine that changed everything.")
L('gyrafoam', 'n24', "Howard Snyder had started as a mechanic, and risen to head Maytag's development department. Maytag's washers, like most of the time, used a dolly under the lid that dragged the clothes through the water.",
  "Howard Snyder had started as a mechanic,", "and risen to head Maytag's development department.", "Maytag's washers, like most of the time,", "used a dolly under the lid that dragged the clothes through the water.")
L('gyrafoam', 'n25', "Snyder turned the idea upside down. He put a vaned agitator at the bottom of the tub, so the water moved through the clothes instead.", "Snyder turned the idea upside down.", "He put a vaned agitator at the bottom of the tub,", "so the water moved through the clothes instead.")
L('gyrafoam', 'n26', "Maytag called it the Gyra-foam. It went on sale in nineteen twenty-two.", "Maytag called it the Gyrafoam.", "It went on sale in 1922.")
L('gyrafoam', 'n27', "By one company history, it took Maytag from the thirty-eighth largest washer maker in the country, to the first.", "By one company history, it took Maytag", "from the 38th largest washer maker in the country, to the first.")
L('gyrafoam', 'n28', "Within eighteen months, it was the most popular washing machine in America. Trainloads of Gyra-foams left Newton in single shipments.", "Within 18 months, it was the most popular washing machine in America.", "Trainloads of Gyrafoams left Newton in single shipments.")
L('gyrafoam', 'n29', "By nineteen twenty-seven, Maytag had built its millionth washer.", "By 1927, Maytag had built its millionth washer.")
L('gyrafoam', 'n30', "The town grew with it. In nineteen hundred, Newton had three thousand, six hundred people. By nineteen thirty, it had eleven thousand, five hundred.", "The town grew with it.", "In 1900, Newton had 3,600 people.", "By 1930, it had 11,500.")
L('gyrafoam', 'n31', "In nineteen twenty-nine, the company made record profits. And it got through the Depression without a single losing year.", "In 1929, the company made record profits.", "And it got through the Depression without a single losing year.")
L('gyrafoam', 'n32', "In nineteen thirty-two, at the bottom of that Depression, Fred Maytag turned seventy-five. To mark the day, he gave each of his fifteen hundred workers a hundred dollars.",
  "In 1932, at the bottom of that Depression, Fred Maytag turned 75.", "To mark the day, he gave each of his 1,500 workers a hundred dollars.")

# ── III · The Strike ──
L('strike', 'n33', "Frederick Louis Maytag died in March nineteen thirty-seven. By one account, ten thousand workers and salesmen stood in a line five blocks long to watch his casket pass. He is buried in Newton.",
  "Frederick Louis Maytag died in March 1937.", "By one account, 10,000 workers and salesmen stood in a line", "five blocks long to watch his casket pass. He is buried in Newton.")
L('strike', 'n34', "A year later, the town that had grown up on his washers turned on itself.", "A year later, the town that had grown up on his washers", "turned on itself.")
L('strike', 'n35', "In May nineteen thirty-eight, the company posted a notice: a ten percent cut in pay. The workers had formed a union the year before. Local eleven sixteen, of the United Electrical Workers.",
  "In May 1938, the company posted a notice: a 10% cut in pay.", "The workers had formed a union the year before:", "Local 1116 of the United Electrical Workers.")
L('strike', 'n36', "On the ninth of May, they struck. They stayed at their machines, so that no one could take their places.", "On 9 May, they struck.", "They stayed at their machines, so that no one could take their places.")
L('strike', 'n37', "A judge issued an injunction against the pickets. In late June, the strikers took over the plant again, and held five foremen inside for a week. Their leaders were arrested, and charged with kidnapping.",
  "A judge issued an injunction against the pickets.", "In late June, the strikers took over the plant again,", "and held five foremen inside for a week.", "Their leaders were arrested, and charged with kidnapping.")
L('strike', 'n38', "Then, on the twenty-first of July, the governor of Iowa, Nelson Kraschel, sent in the National Guard, and declared martial law.", "Then, on 21 July, the governor of Iowa, Nelson Kraschel,", "sent in the National Guard, and declared martial law.")
L('strike', 'n39', "Soldiers stood across from the plant. Cars were kept two blocks away. Club meetings and softball games were cancelled. That night, in the streets around the factory, thirty-four people were hurt. Most of them were workers going back in.",
  "Soldiers stood across from the plant. Cars were kept two blocks away.", "Club meetings and softball games were cancelled.", "That night, in the streets around the factory, 34 people were hurt.", "Most of them were workers going back in.")
L('strike', 'n40', "The governor said martial law was only for the benefit of the public. The union saw a strike broken by soldiers. And Fred Maytag the Second, the founder's grandson, was reported to have said this.",
  "The governor said martial law was “only for the benefit of the public”.", "The union saw a strike broken by soldiers.", "And Fred Maytag II, the founder's grandson,", "was reported to have said this:")
L('strike', 'q02', "Apparently, our employees weren't so happy as we thought.", "“Apparently, our employees weren't so happy as we thought!”")
L('strike', 'n41', "On the third of August, the workers went back, with the cut. If profits came back within two years, they would get their lost wages back.", "On 3 August, the workers went back, with the cut.", "If profits came back within two years, they would get their lost wages back.")
L('strike', 'n42', "It was a hard summer. Then the plant went back to work.", "It was a hard summer. Then the plant went back to work.")

# ── IV · The Dependability People ──
L('depend', 'n43', "During the Second World War, Maytag stopped making washers altogether, and built parts for military aircraft.", "During the Second World War, Maytag stopped making washers altogether,", "and built parts for military aircraft.")
L('depend', 'n44', "In nineteen forty-nine, a new plant opened in Newton. Plant Two, built for the first Maytag automatic washer.", "In 1949, a new plant opened in Newton:", "Plant 2, built for the first Maytag automatic washer.")
L('depend', 'n45', "In nineteen sixty-two, for the first time, the company was run by someone who was not named Maytag.", "In 1962, for the first time,", "the company was run by someone who was not named Maytag.")
L('depend', 'n46', "And in nineteen sixty-seven, Maytag found the face it would wear for decades. A repairman with nothing to do, because Maytags never broke.", "And in 1967, Maytag found the face it would wear for decades:", "a repairman with nothing to do, because Maytags never broke.")
L('depend', 'n47', "It was an advertisement. But in Newton, people believed it, because they were the ones building the machines.", "It was an advertisement. But in Newton, people believed it,", "because they were the ones building the machines.")
L('depend', 'q03', "Carl Repp worked at the plant for thirty years. We made good wages there, he said, but we also made a good product.", "Carl Repp worked at the plant for 30 years.", "“We made good wages there, but we also made a good product.”")
L('depend', 'q04', "They call us the dependability people. That was kind of the motto we went by, for many years.", "“They call us the dependability people.", "I mean, that was kind of the motto we went by for many years.”")
L('depend', 'n48', "Maytag kept making the old wringer washers until nineteen eighty-three. By then, Newton had built eleven point seven million of them.", "Maytag kept making the old wringer washers until 1983.", "By then, Newton had built 11.7 million of them.")
L('depend', 'n49', "At its peak, Maytag employed more than three thousand people in Newton. In a town of about fifteen thousand, that was more than one person in every five.", "At its peak, Maytag employed more than 3,000 people in Newton.", "In a town of about 15,000, that was more than one person in every five.")
L('depend', 'n50', "And it paid for things in town as well. Parks, the aquatic center, the auditorium.", "And it paid for things in town as well:", "parks, the aquatic center, the auditorium.")
L('depend', 'n51', "Families worked there for generations. And there was a number everybody knew.", "Families worked there for generations.", "And there was a number everybody knew.")
L('depend', 'q05', "At Maytag, a woman in town told a radio reporter, it was thirty years and you got to retire.", "As a woman in Newton told a radio reporter:", "“At Maytag, it was 30 years and you got to retire.”")
L('depend', 'n52', "Thirty years, and a pension, and full medical benefits. That was the promise. That was what dependability meant, to the people inside the plant.", "Thirty years, and a pension, and full medical benefits. That was the promise.", "That was what dependability meant, to the people inside the plant.")

# ── V · Sold ──
L('sold', 'n53', "From the nineteen eighties, Maytag grew by buying other companies. Jenn-Air. Magic Chef. Hoover, the vacuum cleaner maker.", "From the 1980s, Maytag grew by buying other companies.", "Jenn-Air. Magic Chef. Hoover, the vacuum cleaner maker.")
L('sold', 'n54', "It was no longer a washing-machine company in a small town. It was a big appliance company that happened to have its headquarters there.", "It was no longer a washing-machine company in a small town.", "It was a big appliance company that happened to have its headquarters there.")
L('sold', 'n55', "And the appliance business was changing. Some Newton workers were laid off as early as two thousand and three.", "And the appliance business was changing.", "Some Newton workers were laid off as early as 2003.")
L('sold', 'n56', "In two thousand and five, Maytag was put up for sale. A private-equity group offered fourteen dollars a share. Haier, the Chinese appliance giant, offered sixteen. Whirlpool, the biggest appliance maker in America, raised its bid three times, and won.",
  "In 2005, Maytag was put up for sale.", "A private-equity group offered $14 a share.", "Haier, the Chinese appliance giant, offered $16.", "Whirlpool, the biggest appliance maker in America,", "raised its bid three times, and won.")
L('sold', 'n57', "On the thirty-first of March, two thousand and six, Whirlpool owned Maytag.", "On 31 March 2006, Whirlpool owned Maytag.")
L('sold', 'n58', "Six weeks later, on the tenth of May, it announced what would happen in Newton. The plant would close. So would the headquarters. Nearly a thousand jobs in the factory, and about nine hundred in the offices.",
  "Six weeks later, on 10 May, it announced what would happen in Newton.", "The plant would close. So would the headquarters.", "Nearly 1,000 jobs in the factory, and about 900 in the offices.")
L('sold', 'n59', "The governor said the state had offered more than a hundred million dollars, and a new modern factory. It was not enough.", "The governor said the state had offered more than $100 million,", "and a new modern factory. It was not enough.")
L('sold', 'n60', "Whirlpool's spokesman explained it this way.", "Whirlpool's spokesman explained it this way:")
L('sold', 'q06', "Now the fundamentals of the company had eroded. They needed to be fixed. They were losing money.", "“Now the fundamentals of the company had eroded.", "They needed to be fixed. They were losing money.”")
L('sold', 'n61', "The president of the union local saw it differently. He called it part of a widespread epidemic: union jobs cut, and moved to places where they paid less.", "The president of the union local saw it differently.", "He called it part of a “widespread epidemic”:", "union jobs cut, and moved to places where they paid less.")
L('sold', 'n62', "Both of those things can be true. The washers would still be made, in Ohio and in Mexico. They just would not be made in Newton.", "Both of those things can be true.", "The washers would still be made, in Ohio and in Mexico.", "They just would not be made in Newton.")
L('sold', 'q07', "A line worker named Vicky had twenty-two years in. My aunt worked there for thirty years, she said. My grandfather retired from there. It's sad. It's like a death.",
  "A line worker named Vicky had 22 years in.", "“My aunt worked there for 30 years. My grandfather retired from there.", "It's sad. It's like a death.”")

# ── VI · The Last Shift ──
L('last', 'n63', "Which brings us back to Thursday, the twenty-fifth of October, two thousand and seven.", "Which brings us back to Thursday, 25 October 2007.")
L('last', 'n64', "Five hundred and fifty people were still on the line that day. When it stopped, there were hugs and kisses at the gate.", "550 people were still on the line that day.", "When it stopped, there were hugs and kisses at the gate.")
L('last', 'n65', "Mark Wickliff was forty-nine. He had worked there twenty-six and a half years, three and a half short of the thirty he needed for full retirement. Four generations of his family had worked at Maytag. He was the one who carried out the sign.",
  "Mark Wickliff was 49. He had worked there 26½ years,", "three and a half short of the 30 he needed for full retirement.", "Four generations of his family had worked at Maytag.", "He was the one who carried out the sign.")
L('last', 'q08', "It's just close enough, he said, to look for another job.", "“It's just close enough to look for another job.”")
L('last', 'q09', "Mike Jackson had eighteen years in. I'm numb, he said. I'm scared. I'll be all right, I think.", "Mike Jackson had 18 years in.", "“I'm numb, I'm scared. I'll be all right, I think.”")
L('last', 'n67', "Someone hung a plaque on the fence, in the shape of a gravestone. It said R.I.P. And underneath, in handwriting: I love you all.", "Someone hung a plaque on the fence, in the shape of a gravestone.", "It said “R.I.P.” And underneath, in handwriting: “I love you all.”")
L('last', 'q10', "Mindy Pollock had been there twenty-two years when she was let go. I've seen grown men crying that day, she said.", "Mindy Pollock had been there 22 years when she was let go.", "“I've seen grown men crying that day.”")
L('last', 'n69', "Jim Schutte, a machine repairman for twenty-one years, knew the day he would have reached his thirty. The seventeenth of August. When would he retire now? Probably never, he said, and laughed.",
  "Jim Schutte, a machine repairman for 21 years,", "knew the day he would have reached his thirty: 17 August.", "When would he retire now? “Probably never,” he said, and laughed.")
L('last', 'n70', "In all, about eighteen hundred people in Newton lost their Maytag jobs.", "In all, about 1,800 people in Newton lost their Maytag jobs.")
L('last', 'n71', "A town of fifteen thousand. And the company that had been there for a hundred and fourteen years was gone.", "A town of 15,000.", "And the company that had been there for 114 years was gone.")

# ── VII · What Newton Built Next ──
L('next', 'n72', "Unemployment climbed to almost ten percent. In twenty ten, Jasper County had the highest unemployment rate of all ninety-nine counties in Iowa.", "Unemployment climbed to almost 10%.", "In 2010, Jasper County had the highest unemployment rate", "of all 99 counties in Iowa.")
L('next', 'n73', "A national news program came to town, and said it had seen nothing that looked quite as broken as Newton.", "A national news program came to town,", "and said it had seen nothing that looked “quite as broken as Newton”.")
L('next', 'n74', "But the plant was still standing. And so were the people who knew how to build things in it.", "But the plant was still standing.", "And so were the people who knew how to build things in it.")
L('next', 'n75', "Before anyone could use the site, it had to be cleaned. Whirlpool took on the job, removing soil and groundwater contaminated with chromium and solvents. By two thousand and eight, a hundred and fifty-four acres were ready.",
  "Before anyone could use the site, it had to be cleaned.", "Whirlpool took on the job, removing soil and groundwater", "contaminated with chromium and solvents.", "By 2008, 154 acres were ready.")
L('next', 'n76', "A company called TPI wanted to build wind-turbine blades in the old Maytag buildings. The blades were a hundred and forty feet long. The buildings were too short. So in two thousand and eight, a new plant went up in Newton instead.",
  "A company called TPI wanted to build wind-turbine blades", "in the old Maytag buildings. The blades were 140 feet long.", "The buildings were too short.", "So in 2008, a new plant went up in Newton instead.")
L('next', 'n77', "Inside the old factory, another company began making steel towers for wind turbines. The first tower section rolled out of a building that, a year before, had been making Maytag washers and dryers.",
  "Inside the old factory, another company began making steel towers for wind turbines.", "The first tower section rolled out of a building that, a year before,", "had been making Maytag washers and dryers.")
L('next', 'n78', "In April two thousand and nine, the President came to see it. He described what the workers had shown him.", "In April 2009, the President came to see it.", "He described what the workers had shown him.")
L('next', 'q11', "These floors were dark and silent. The only signs of a once thriving enterprise were the cement markings where the equipment had been, before they were boxed up and carted away.",
  "“These floors were dark and silent.", "The only signs of a once thriving enterprise were the cement markings", "where the equipment had been before they were boxed up and carted away.”")
L('next', 'n79', "TPI grew to more than eleven hundred workers. Many had come from Maytag.", "TPI grew to more than 1,100 workers.", "Many had come from Maytag.")
L('next', 'n80', "But the new jobs did not pay what the old ones had. In two thousand and one, factory pay in Jasper County was thirty-seven percent above the Iowa average. By twenty fifteen, it was about twenty percent below.",
  "But the new jobs did not pay what the old ones had.", "In 2001, factory pay in Jasper County was 37% above the Iowa average.", "By 2015, it was about 20% below.")
L('next', 'q12', "A waitress in town, with thirty years at Maytag behind her, put it simply. You can't take the good paying jobs that they had out there, and replace them with half the pay.",
  "A waitress in town, with 30 years at Maytag behind her, put it simply:", "“You can't take the good paying jobs that they had out there", "and replace them with half the pay.”")
L('next', 'n81', "And in twenty twenty-one, the blade plant closed as well, when its biggest customer stopped buying. Seven hundred and ten people lost their jobs.", "And in 2021, the blade plant closed as well,", "when its biggest customer stopped buying.", "710 people lost their jobs.")
L('next', 'n82', "In the summer of twenty twenty-five, it opened its doors again, under a new ten-year lease, even as TPI itself went through bankruptcy.", "In the summer of 2025, it opened its doors again, under a new ten-year lease,", "even as TPI itself went through bankruptcy.")
L('next', 'n83', "Other things came. A race track, Iowa Speedway, opened in Newton in two thousand and six. In twenty twenty-four, NASCAR's top series raced there for the first time. The Maytag headquarters campus was given to the community college in twenty sixteen. And on a farm just outside town, the founder's grandsons had been making a blue cheese since nineteen forty-one. It still carries the Maytag name.",
  "Other things came. A race track, Iowa Speedway, opened in Newton in 2006.", "In 2024, NASCAR's top series raced there for the first time.", "The Maytag headquarters campus was given to the community college in 2016.", "And on a farm just outside town, the founder's grandsons", "had been making a blue cheese since 1941. It still carries the Maytag name.")
L('next', 'n84', "Here is the part that surprised people. Newton did not empty out. In nineteen sixty, it had about fifteen thousand people. In twenty twenty, it still had about fifteen thousand.",
  "Here is the part that surprised people. Newton did not empty out.", "In 1960, it had about 15,000 people.", "In 2020, it still had about 15,000.")
L('next', 'n85', "The square looks much as it did in nineteen-oh-seven. The courthouse, the shops, and no boarded-up windows.", "The square looks much as it did in 1907.", "The courthouse, the shops, and no boarded-up windows.")
L('next', 'n86', "For decades, America was told about a repairman who sat with nothing to fix, because the machines from Newton never broke.", "For decades, America was told about a repairman who sat with nothing to fix,", "because the machines from Newton never broke.")
L('next', 'n87', "Newton built those machines to last, and many of them did. What changed was everything around them. Who owned the company. Where the machines were made. And what a factory job paid.",
  "Newton built those machines to last, and many of them did.", "What changed was everything around them.", "Who owned the company. Where the machines were made.", "And what a factory job paid.")
L('next', 'n88', "What stayed, was the town.", "What stayed was the town.")
L('next', 'n89', "Did you, or someone in your family, work at Maytag? Or do you still have a Maytag that never broke? Tell us in the comments. We read every one.", "Did you, or someone in your family, work at Maytag?", "Or do you still have a Maytag that never broke?", "Tell us in the comments. We read every one.")
L('next', 'n90', "Next week: Flint, Michigan.", "Next week: Flint, Michigan.")

MAXC = 64   # one caption line at 47 px stays inside ≈ 1,600 px
def split(s):
    if len(s) <= MAXC: return [s]
    mid = len(s) // 2; best = None
    for j, ch in enumerate(s):   # prefer a break after punctuation, then a space, nearest the middle
        if ch == ' ' and 12 < j < len(s) - 12:
            score = abs(j - mid) - (14 if s[j - 1] in ',.:;' else 0)
            if best is None or score < best[0]: best = (score, j)
    if best is None: return [s]
    a, b = s[:best[1]], s[best[1] + 1:]
    return split(a) + split(b)
out = [{'id': i, 'chapter': ch, 'voice': V, 'speed': 0.95, 'text': sp, 'subs': [p for s in subs for p in split(s)]} for ch, i, sp, subs in C]
open(os.path.join(D, 'audio/lines.json'), 'w', encoding='utf-8').write('[\n' + ',\n'.join('  ' + json.dumps(l, ensure_ascii=False) for l in out) + '\n]\n')
n = sum(len(l['text']) for l in out); mx = max(len(s) for l in out for s in l['subs'])
print(len(out), 'lines', n, 'characters', round(n / 15.0 / 60, 1), 'min at ~15 chars/s; longest caption', mx)
