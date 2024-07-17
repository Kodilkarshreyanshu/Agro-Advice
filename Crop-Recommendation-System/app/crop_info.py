from django.utils.safestring import mark_safe

crop_dict = {
    'Tomato': {
        'description': mark_safe("""
            <ul>
                <li>Soil: Well drain, sandy loam, PH-6-7.5</li>
                <li>Climate: Warm & Humid, Temperature 21-27 °C</li>
                <li>Varieties: Pusa Ruby, Sioux, Dhanshree, Rajshree, Pusa Gaurav, Arka Vikas, Arka Saurabh, Pusa Sheetal.</li>
                Propn method: Seed<br>
                Seed Rate:                 400-500 g/ha,<br>
                Spacing: 60 x 45 cm,<br>
                Planting season: Kharif & Rabi.<br>
                FIELD7:
                Fertilizer dose: FYM-25 t/ha, 100:50:50 Kg NPK/ha
                FIELD9:
                Maturity Indices: Mature Green stage, Pink Stage, Ripe Stage, Fully Ripe Stage.<br>
                Harvesting: Harvesting done manually by plucking at different stage of maturity.<br>
                FIELD12:
                Yield: 25-30 t/ha, F1- 50-60 t/ha <br>
                FIELD15:<br>
                Pests: Fruit borer, White fly, Thrips, leaf minor.<br>
                FIELD17:<br>
                Diseases: Early blight, late blight, leaf curl virus (WF), Spotted wilt virus (Thrips)
            </ul>
        """),
        'crop_image_url': 'https://images-na.ssl-images-amazon.com/images/I/71DYmqoq-VL._SL1024_.jpg'
    },

'Potato' :{
    'description': mark_safe("""Soil: Well drain, sandy loam, red lateritic, PH-6-6.5<br>
Climate: Warm & Humid, Temp.18-22°C <br>
Varieties: Pusa Purple Long, Pusa Kranti, Pusa Anmol, Manjri Gota, Krishna, Pragati, Arka Navneet, Phule Harit.<br>
Propn method: Seed<br>
Seed Rate:
 600-800 g/ha<br>
Spacing : 60 x 60 cm,
60 x 45 cm,
45 x 45 cm <br>
Planting Season: Kharif, Rabi,<br>

FIELD7:<br>
Fertilizer dose: FYM-25 t/ha, 100:50:50 KgNPK/ha<br>
FIELD9:<br>
Maturity Indices: Desirable size, colour & tender stage<br>
Harvesting: Harvesting done by cutting with a small pruning shear or sharp knife<br>
FIELD12:<br>
Yield: 20-30t/ha, F1- 40-50t/ha<br>
FIELD15:<br>
Pests: Brinjal fruit and shoot borer, stem borer,aphids<br>
FIELD17:<br>
Diseases: Phomopsis blight, damping off, wilt, little leaf (Jassids)""",
        ),
        'crop_image_url': 'https://www.sunnyslopeorganicfarm.com/wp-content/uploads/2017/01/Potato-harvest.png?gid=5'
},  

           'Brinjal' :{ 
           'description': mark_safe(""" 
Soil: Well drain, sandy loam, red lateritic, PH-6-6.5<br>
Climate: Warm & Humid, Temp.18-22°C <br>
Varieties: Pusa Purple Long, Pusa Kranti, Pusa Anmol, Manjri Gota, Krishna, Pragati, Arka Navneet, Phule Harit.<br>
Propn method: Seed<br>
Seed Rate:
 600-800 g/ha<br>
Spacing : 60 x 60 cm,
60 x 45 cm,
45 x 45 cm <br>
Planting Season: Kharif, Rabi,<br>

FIELD7:<br>
Fertilizer dose: FYM-25 t/ha, 100:50:50 KgNPK/ha<br>
FIELD9:<br>
Maturity Indices: Desirable size, colour & tender stage<br>
Harvesting: Harvesting done by cutting with a small pruning shear or sharp knife<br>
FIELD12:<br>
Yield: 20-30t/ha, F1- 40-50t/ha<br>
FIELD15:<br>
Pests: Brinjal fruit and shoot borer, stem borer,aphids<br>
FIELD17:<br>
Diseases: Phomopsis blight, damping off, wilt, little leaf (Jassids)
      
  """ ), 
  'crop_image_url': 'https://img.onmanorama.com/content/dam/mm/en/food/features/images/2021/4/7/chillies.jpg'
  },
   'Chilli ': {
   'description': mark_safe("""
      
Soil: Fertile, sandy loam,PH-6-8<br>
Climate: Warm & Humid, Temp. 18-22°C<br>
Varieties: Pusa Jwala, Agnirekha, Pusa Sadabahar, Pant C- 1, Arka Mohini, Arka Gaurav, Arka Lohit.<br>
Propn method: Seed<br>
Seed Rate: 1-1.5 Kg/ha,<br>
Spacing: 60 x 45 cm,
45 x 45 cm <br>
Planting season: Kharif, Rabi, Summer.<br>
FIELD7:<br>
Fertilizer dose: FYM-25 t/ha, 100:50:50 KgNPK/ha<br>
FIELD9:<br>
Maturity Indices: Harvested at two stages Green in colour & dry chilli when red in colour.<br>
Harvesting: Fruit are picked either green or fully red ripen.<br>
FIELD12:<br>
Yield: 5-7 t/ha<br>

FIELD15:<br>
Pests: Thrips<br>
FIELD17:<br>
Diseases: Anthracnose, leaf curl(WF & Thrips), mosaic(Aphids)
      
   """),
   'crop_image_url': 'https://img.onmanorama.com/content/dam/mm/en/food/features/images/2021/4/7/chillies.jpg'
},


 'Okra' : {
     'description' : mark_safe(""" 
    Soil: Sandy loam to clay, well drain, PH-6- 6.8<br>
Climate: Warm & Humid, Temp.20-30°C,continues rain are harmful.<br>
Varieties: Pusa Sawani, Parbhani Kranti, Arka Anamica, Punjab Padmini, phule Kirti, Phule Uttakarsha.<br>
Propn method: Seed<br>
Seed Rate,: 12-15 Kg/ha.<br>
Spacing: 45x 30 cm, 
Planting season: Kharif & Summer.<br>
FIELD7:<br>
Fertilizer dose: FYM-25 t/ha, 100:50:50 KgNPK/ha<br>
FIELD9:<br>
Maturity Indices: Green tender, Size 6-8cm, 6-7 days after opening of flower<br>
Harvesting: Harvesting done by picking of tender fruit.<br>
FIELD12:<br>
Yield: 12-15t/ha<br>
Pests: Shoot and borer, jassids, White fly (WF)<br>
FIELD17:<br>
Diseases: Yellow vein mosaic virus (WF),Enation leaf curl virus(WF).<br>
  """ ),
  'crop_image_url': 'https://i0.wp.com/www.healthfitnessrevolution.com/wp-content/uploads/2016/10/iStock-520883902.jpg?fit=2120%2C1415&ssl=1'
 }, 

   'Onion' : {
       'description' : mark_safe(""" 
Soil: Sandy loam with good organic matter, PH- 6-7.5.<br>
Climate: Cool season grows well under mild climate, temp.20-25°C.<br>
Varieties: N-53, Baswant 780, Phule Safed, Pusa Red, Phule Utkarsha, Arka Kalyan, Phule Suvarna.<br>
Propn method: Seed<br>
Seed Rate: 10-12 Kg/ha for rabi, 12-15 Kg/ha for Kharif.<br>
Spacing: 15 x 10 cm, 12.5 x 7.5 cm, 
Planting season: Kharif, Rabi, Summer.<br>
FIELD7:<br>
Fertilizer dose: FYM-25 t/ha, 150:50:50 Kg NPK/ha<br>
FIELD9:<br>
Maturity Indices: 3-4 month after transplanting, Neck Fall 60-70%,<br>
Harvesting: Harvesting is done by pulling out plants when tops are drooping but still green.<br>
FIELD12:<br>
Yield: 20-25 t/ha,<br>

Pests: Thrips, onion fly, leaf eating caterpillar, head borer, cutworm.<br>
FIELD17:<br>
Diseases: Purple blotch, onion smut, downey mildew<br>
  """ ),
  'crop_image_url': 'https://th.bing.com/th/id/OIP.gghloS31O7iGemZDeHvhHAHaFG?rs=1&pid=ImgDetMain'
   }, 

   'Cabbage' :{
       'description': mark_safe(""" 
Soil: Well drain, sandy to heavy clay loam, PH 6-8.<br>
Climate: Cool season crop, temp.13-16°C,<br>
Varieties: Golden Acre, Pride of India, Pusa Drum Head, Copenhagen Market, Pusa Mukta, Pusa Ageti, Pusa Sambandh.<br>
Propn method: Seed<br>
Seed Rate : 400-500 g/ha,<br>
Spacing: 45 x 15 cm,
60 x 45 cm<br>
Planting season: Kharif, Rabi<br>
FIELD7:<br>
Fertilizer dose: FYM-25 t/ha, 150:50:50 KgNPK/ha<br>
FIELD9:<br>
Maturity Indices: Colour changes to light green at maturity, compact head.<br>
Harvesting: The heads are cut with sickle attached with some wrapper leaves.<br>
FIELD12:<br>
Yield: 20-30t/ha<br>

Pests: Diamond back moth, cabbage butterfly, mustard saw fly.<br>
FIELD17:<br>
Diseases: Damping off, club rot, black rot<br>
  """ ),
  'crop_image_url': 'https://images.squarespace-cdn.com/content/v1/65ac11e0696c1d6058d94af4/900f5ed3-9824-4bf9-8577-af9f0a065f15/Measure+to+Improve+-+Produce+Sustainability+Consulting.jpg'
   }, 

     'Cauliflower' :{
        'description':  mark_safe(""" 
Soil: Sandy loam, Well drain, PH 6.5-7.5<br>
Climate: Cool season crop, temp.<br>
o<br>
17-20 °C<br>
Varieties: Pusa Ketki, Pusa Himjyoti, Pusa Snowball K-1, Pusa Meghna, Hisar- 1, Pusa Deepali, Pant Shubhra. Arka kanti<br>
Propn method: Seed<br>
Seed Rate : 400-500 g/ha,<br>
Spacing: 45 x 15 cm,
60 x 45 cm<br>
Planting season: Kharif, Rabi<br>
FIELD7:<br>
Fertilizer dose: FYM-15 t/ha, 100:50:50 KgNPK/ha<br>
FIELD9:<br>
Maturity Indices: Curd attained desirable size, head are compact.<br>
Harvesting: Curd cut with sharp knife with 2-3 large leaves to protect the curd.<br>
FIELD12:<br>
Yield: 15-20t/ha<br>

Pests: Diamond back moth, cabbage butterfly, mustardsaw fly.<br>
FIELD17:<br>
Diseases: Damping off, club rot, black rot<br>
  """ ),
  'crop_image_url': 'https://www.thespruce.com/thmb/AGqD-ZcXtOTxvlagSuFtRQ8SJ4w=/4696x3130/filters:fill(auto,1)/how-to-grow-cauliflower-1403494-hero-76cf5f524a564adabb1ac6adfa311482.jpg'
   }, 

  'Cucumber' :{
      'description': mark_safe(""" 
  Soil: Sandy loam to clay soil. PH 5.5 -6.8<br>
  Climate: Warm season crop, Temp. 18- 24°C<br>
  Varieties: Phule Shubhangi, Pusa Sanyog, Himangi, Poona Khira, Sheetal, Pusa Uday, Swarna Ageti.<br>
  Propn method: Seed<br>
  Seed Rate: 2.5-3.5 Kg/ha<br>
                               Spacing: 1 x 0.5 m <br>
  Planting season: Kharif & Summer.<br>
  FIELD7: FYM-15 t/ha, 100:50:50 Kg NPK/ha<br>
  Fertilizer dose:<br>
  FIELD9: Tender/ immature stage, 60-70 days after sowing<br>
  Maturity Indices:<br>
  Harvesting:<br>
  FIELD12: Regular harvesting of fruit is necessary, to avoid inhabitation of further fruit set on plant<br>
  Yield:<br>
 
  FIELD15: 25-35t/ha<br>
  Pests:<br>
  FIELD17: Fruit Fly,<br>
  Red Pumpkin beetle,<br>
  Diseases: Cucumber mosaic virus,<br>
 
  """ ),
  'crop_image_url': 'https://th.bing.com/th/id/OIP.wrylQ8mAb9BSRHNrAWKfhQHaEK?rs=1&pid=ImgDetMain'
   }, 

  'Watermelon' : {
      'description' :mark_safe(""" 
  Soil: Loam & Sandy loam best, rich in organic matter, PH 6-6.5<br>
  Climate: Warm season crop, Temp. 24- 27°C, high temp & low humidity suitable for  watermelon.<br>
  Varieties: Sugar Baby, Arka Manik, Arka Jyoti, Pusa Bedana (seedless variety), Durgapura Meetha, Durgapura Keshar, Durgapura Lal.<br>
  Propn method: Seed<br>
  Seed Rate: 3.5-5 kg/ha<br>
  Spacing: 2 x 0.5 m <br>
  Planting season: Summer<br>
  FIELD7: 25 t FYM/ha  100:50:50 KgNPK/ha<br>
  Fertilizer dose:<br>
  FIELD9: 95-120 days after seed sowing, change of ground spot color green to yellow & dull-thud sound on  thumping the fruit.<br>
  Maturity Indices:<br>
  Harvesting:<br>
  FIELD12: Harvested at full ripening stage,<br>
  Yield:<br>
  FIELD14:
  FIELD15: 25-35t/ha<br>
  Pests:<br>
  FIELD17: Epilachna Beetle, Aphids,<br>
  Diseases: Green Mottle Mosaic.<br>
  
  """ ),
  'crop_image_url': 'https://hoorahtohealth.com/wp-content/uploads/2021/08/Watermelon-1024x1024.jpg'
   }, 

  'Muskmelon' :{
      'description': mark_safe(""" 
  Soil: Loam & Sandy loam best, rich in organic matter, PH 6-7.5<br>
  Climate: High temp. & low humidity for fruit ripening, temp. 20-25°C.<br>
  Varieties: Arka Jeet, Arka Rajhans, Pusa Madhuras, Pusa Sharbati, Pusa Rasraj, Panjab Raseela, Hara Madhu, Durgapura Madhu, Hisar Saras.<br>
  Propn method: Seed<br>
  Seed Rate: 5-6 kg/ha,<br>
  Spacing: 1.5 x 0.5m,
  90 x 60 cm<br>
  Planting season: Summer<br>
  FIELD7: 15 t FYM/ha,  100:50:50 Kg NPK/ha<br>
  Fertilizer dose:<br>
  FIELD9: Mature fruit separate (slip) easily from stem is called full slip  stage, half slip stage half stem separate from stem easily.<br>
  Maturity Indices:<br>
  Harvesting:<br>
  FIELD12: Half slip for long-distance market, Full slip stage for local market & 90-125 day after seedsowing,<br>
  Yield:<br>
  
  FIELD15: 10-15 t/ha<br>
  Pests:<br>
  FIELD17: Mites.<br>
  Diseases: Bud Necrosis,<br>
 
  """ ),
  'crop_image_url': 'https://www.womenfitness.net/wp/wp-content/uploads/2019/10/3b1b7b74f35daeca8a380fc09456d70e1.jpeg'
   }, 

  'Bottle_gourd' :{
      'description': mark_safe(""" 
  Soil: Well-drained sandy loam with rich organic matter, PH 6-7<br>
  Climate: Warm and humid climate and slightly cool, temp. 24-27°C.<br>
  Varieties: Samrat, Pusa Sandesh, Pusa Meghdoot, Arka Bahar, Pusa Navneet, Pusa Manjari, Panjab Komal.<br>
  Propn method: Seed<br>
  Seed Rate: 3-4 kg/ha,<br>
  Spacing: 2.5 x 1 m, 3 x 1 m,<br>
  Planting season: Kharif & Rabi<br>
  FIELD7: 15 t FYM/ha, 100:50:50 Kg NPK/ha<br>
  Fertilizer dose:<br>
  FIELD9: Tender/immature stage, 60-70 days after seed sowing<br>
  Maturity Indices:<br>
  Harvesting:<br>
  FIELD12: The fruit harvested at attain marketable stage, harvesting should be carefully so fruit do not get  Bruised.<br>
  Yield:<br>
  
  FIELD15: 25-30 t/ha<br>
  Pests:<br>
  FIELD17:<br>
  Diseases: Downy<br>
  
  """ ),
  'crop_image_url': 'https://th.bing.com/th/id/OIP.Uk-VHhTmOuUbENR8R2aoAAHaE6?rs=1&pid=ImgDetMain'
   }, 

  'Ridge_gourd' :{
      'description': mark_safe(""" 
  Soil: Sandy loam with rich in organic matter PH 6-7<br>
  Climate: Warm season crop, warm and humid climate, Temp. 24-27°C<br>
  Varieties: Pusa Nasdar, Co-1, Co-2, Satputia, Panjab Sada Bahar, PKM-1, Arka Sujath, Konkan Harita<br>
  Propn method: Seed<br>
  Seed Rate: 3.5-5 kg/ha<br>
  Spacing: 2 x 1 m<br>
  Planting season: Kharif & Summer<br>
  FIELD7: 15 t FYM/ha, 100:50:50 Kg NPK/ha<br>
  Fertilizer dose:<br>
  FIELD9: Tender/ immature stage, 60-90 days after seed sowing<br>
  Maturity Indices:<br>
  Harvesting:<br>
  FIELD12: The fruit harvested at attain marketable stage after 5-7 days after anthesis<br>
  
  
  FIELD15: 12-15 t/ha<br>
  Pests:<br>
  FIELD17:<br>
  Diseases:
  """ ),
  'crop_image_url': 'https://i.etsystatic.com/18026585/r/il/8152c0/2594417462/il_fullxfull.2594417462_7is9.jpg'
   }, 

  'Sponge_gourd ' : {
      'description': mark_safe(""" 
  Soil: Sandy loam with rich in organic matter  PH 6-7<br>
  Climate: Warm season crop, warm and humid climate, Temp. 24-27°C<br>
  Varieties: Pusa Chikni, Pusa Supriya, Pusa Sneha, Arka Sumeet, Pusa Nutan<br>
  Propn method: Seed<br>
  Seed Rate: 2.5-3.5 kg/ha<br>
  Spacing: 2 x 1 m<br>
  Planting season: Kharif & Summer<br>
  FIELD7: 15 t FYM/ha,   100:50:50 Kg NPK/ha<br>
  Fertilizer dose:<br>
  FIELD9: Tender/ immature stage, 60-90 days after seed sowing<br>
  Maturity Indices:<br>
  Harvesting:<br>
  FIELD12: The fruit harvested at attain marketable stage after 5-7 days after anthesis<br>
  
  FIELD15: 8-12  t/ha<br>
  
  Diseases:
  """ ),
  'crop_image_url': 'https://www.honestseedco.com/wp-content/uploads/2020/06/luffa-scaled.jpg'
   }, 

  'Bitter_gourd' :{
      'description': mark_safe(""" 
  Soil: Sandy loam with rich in organic matter PH 6-7<br>
  Climate: Warm season crop, Temp. 25- 30°C<br>
  Varieties: Hirkani, Phule Green Gold, Pusa Do Mausami, Pusa Vishesh, Arka Harit, Konkan Tara<br>
  Propn method: Seed<br>
  Seed Rate: 4-6 kg/ha<br>
  Spacing: 2 x 1 m, 
    Planting season: Kharif & Summer<br>
  FIELD7: 15 t FYM/ha 100:50:50 Kg NPK/ha<br>
  Fertilizer dose:<br>
  FIELD9: Tender/ immature stage, 50-60 days after seed sowing<br>
  Maturity Indices:<br>
  Harvesting:<br>
  FIELD12: Harvested at fruit attain marketable stage for 2-3 weeks after anthesis<br>
  
  FIELD15: 10-15  t/ha<br>
  Pests:<br>
  FIELD17:<br>
  Diseases:
  """ ), 
  'crop_image_url': 'https://th.bing.com/th/id/OIP.w86w0WsfaRSIodn9a7BqyAHaHa?w=500&h=500&rs=1&pid=ImgDetMain'
   },

  'Mango' :{
      'description': mark_safe(""" 
  Soil: Alluvial soil, Slightly acidic having PH-5.5-7 with good drainage is ideal.<br>
  Climate: Tropical climate having temp. 24-27°C is ideal, high temp. during fruit development give good quality fruit.<br>
  Varieties: Monoembryonic: Alphanso, Kesar, Langra, Vanraj, totapuri, Polyemryonic: Olour, Bappakai, Goa,<br>
  Hybrid: Mallika, Amrapali, Ratna, Sindhu<br>
  Propn method: Stone grafting, Soft wood grafting<br>
  Seed Rate : 10 x 10 m 
  Spacing : 8 x 8 m, 2.5 x 2.5 m (HDP)<br>
  Planting season : June-July, Aug- September<br>
  FIELD7: 100 kg FYM/plant/ year 1000:500:1000g NPK/plant/ year<br>
  Fertilizer dose:<br>
  FIELD9: Tapka stage, specific gravity-1.01-1.02, TSS-12-15%, Colour
  dark green to light green, shoulder out grow the stalk end<br>
  
  Harvesting:<br>
  FIELD12: Harvesting should be done fruit attain full size, harvesting should be done with help of nutal zela or mango harvester.<br>
  Yield:1.5t <br>
  
  FIELD15: 2000-3000<br>
  
  Pests:<br>
  FIELD17: Fruit Fly, Stem Borer, Stone Weevil, Aphid.<br>
  Diseases: Powdery Mildew, Anthracnose.<br>
  """ ), 
  'crop_image_url': 'https://cdn.shopify.com/s/files/1/1754/3821/products/Carrier-Mango-Kernel-Butter-1X1_1024x1024.png?v=1662658872'
   },


  'Banana' :{
      'description': mark_safe(""" 
  Soil: Deep, alluvial, well drained, loamy with good organic matter<br>
  PH 6-8<br>
  Climate: Warm and humid, rainy climate, temp. 20-30°C, rain fall 120 cm.<br>
  Varieties: Grand-9, Basarai, Srimanti, Harisal, Lal Velchi, Safed Velchi, Mahalaxmi, Poovan, Nendran.<br>
  Propn method: Rhizome (500-750g  wt.), suckers, Tissue culture.<br>
  Seed Rate: 2 x 2 m<br>
  Spacing: 1.8 x 1.8 m,
  1.5 x 1.5 m <br>
  Planting season: June-July -Sept-oct.<br>
  FIELD7: 50 kg FYM/plant/ year 200:40:200 g NPK/plant/ year<br>
  Fertilizer dose:<br>
  FIELD9: 11-14 month after planting, fruit mature after 120-140 day after flowering, metallic sound at finger taping, drying of upper leaves.<br>
  Maturity Indices:<br>
  Harvesting:<br>
  FIELD12: The trunk is lopped with sickle, the bunch will not fall to ground to avoid injury and about 30 cm of stalk must be left to make handling easy.<br>
  
  FIELD15: 40 t/ha<br>
  Pests:<br>
  FIELD17: Weevil, Aphid.<br>
  Diseases: Sigatoka, Bunchy Top, Panama Wilt.
  """ ), 
  'crop_image_url': 'https://as1.ftcdn.net/v2/jpg/01/05/77/44/1000_F_105774492_NQm3wqBCsBY53A6HDHqX0wHvWKMRVOvi.jpg'
   },


  'Grape' : {
      'description': mark_safe(""" 
  Soil: well drained, light, medium, alluvial soil, with good organic matter  PH 6.5-8<br>
  Climate: Semi arid and sub-tropical, summer hot and dry & mild winter, bright sunny days, temp. 10-40.<br>
  Varieties: Thompson Seed Less, Sonaka, Tas-E Ganesh, Sharad Seed Lees (Black colour), Manik Chaman, Manjari Naveen, Perlette, Arkavati.<br>
  Propn method: Hard Wood Cutting (Root stock- Bangalore Dogridge, One-10-R.<br>
  Seed Rate:3 x 1.5 m<br>
  Spacing: 2.5 x 1.5 m<br> 
   Planting season: Jan-Feb.<br>
  FIELD7: 50 kg FYM/plant/ year 900:500:700 g NPK/plant/ year<br>
  Fertilizer dose:<br>
  FIELD9: Fruit mature 120-140 day after fruit pruning, TSS-16-20 % (Brix)<br>
  Maturity Indices:<br>
  Harvesting:<br>
  FIELD12: Fully ripe fruit are harvested, the bunch removed from vine by sharp secateurs.<br>
  
  FIELD15: 25-40 t/ha<br>
  Pests:<br>
  FIELD17: Udya Beetle, Mealy Bug, Stem Girdler, Thrips<br>
  Diseases: Powdery mildew, Downy Mildew, Anthracnose.
  """ ),
  'crop_image_url': 'https://th.bing.com/th/id/OIP.r4gzGgFQwO6Pzo1mFJ2AyQHaE8?rs=1&pid=ImgDetMain'
   }, 
  
  'Pomegranate' :{
      'description': mark_safe(""" 
  Soil: Loamy and alluvial soil, medium or light soil is ideal, PH 6-7.5<br>
  Climate: Cool winter and hot & dry summer where rainfall is low, temp. 10-40°C<br>
  Varieties: Phule Bhagwa, Phule Arakta, Ganesh, Mridula<br>
  Propn method: Air Layering<br>
  Spacing   5 x 5 m <br>
                               Planting season: June - July<br>
  FIELD7: 50 kg FYM/plant/ year 625:250:250 g NPK/plant/  year<br>
  Fertilizer dose:<br>
  FIELD9: Fruit ready 150-170 day after flowering, TSS 16-17%, dark red color and surface become soft<br>
  Maturity Indices:<br>
  Harvesting:<br>
  FIELD12: The fruit are harvested at proper stage of maturity<br>
  
  FIELD15: 25-30 t/ha<br>
  
  FIELD17: Fruit Borer, Anar Caterpillar<br>
  Diseases: Bacterial blight<br>
  """ ), 
  'crop_image_url': 'https://www.thespruce.com/thmb/Dx4WmB6YLkYYadhZQ90SeAeahiE=/2126x1412/filters:fill(auto,1)/155351657-56a98c8c3df78cf772a82cd7.jpg'
   },

  'Sapota' :{
      'description': mark_safe(""" 
  Soil: Deep alluvial good organic matter,  PH 6-7.5<br>
  Climate: Tropical climate rain fall125-250 cm, temp. range 20-34°C<br>
  Varieties: Kalipatti, Pillipatti, Cricket Ball, Dhola Diwani, Culcutta Round<br>
  Propn method: Aproch Grafting, Inarch Grafting<br>
  Spacing : 10x10 m,   8x8 m <br>
                               Planting season: June - July<br>
  FIELD7: 100 kg FYM/plant/ year 1000:500:500 g  NPK/plant/  year<br>
  Fertilizer dose:<br>
  FIELD9: Fruit mature 240-270 days after flowering, fruit develop dull orange or potato color, milky latex  content reduce<br>
  
  
  FIELD12: Fully mature fruit are harvested with the help of sapota harvester<br>
 
  FIELD15: 3000  fruit/ plant/ year<br>
  
  FIELD17: Fruit Fly, Leaf Eating Caterpillar, Scale<br>
  Insect<br>
  Diseases: Leaf Spot and Fruit Rot<br>
  """ ),
  'crop_image_url': 'https://4.bp.blogspot.com/-rBydd-HtKiQ/VXSDCOttCWI/AAAAAAAABYc/YkqduyGIXYo/s1600/Sapodilla.jpg'
   }, 


  'Guava' :{
      'description': mark_safe(""" 
  Soil: Sandy loam with good organic matter  PH 6-7.5<br>
  Climate: Basically tropical climate grow wide range of climate<br>
  Varieties: L-49 (Sardar), Allahabad Safeda, Lalit, Banaras<br>
  Propn method: Air Layering, ground layering<br>
  Seed Rate, Spacing :  7x7 m 5x5 m<br>
  Planting season: June - July<br>
  FIELD7: 50 kg FYM/plant/ year 625:250:250 g  NPK/plant/  year<br>
  Fertilizer dose:<br>
  FIELD9: Fruit mature 140-160 days after flowering, color change from pale green fruit become soft<br>
  
  FIELD12: Hand pulling, picking is done 2-3 times in a weeks, fruit collect in basket<br>
  
  FIELD15: 1500Fruit/ plant/ year<br>
  Pests:<br>
  FIELD17: Fruit fly, White fly<br>
  Diseases: Anthracnose, Guava Canker
  """ ),
  'crop_image_url': 'https://medmunch.com/wp-content/uploads/2020/08/Guava-4.jpg'
   }, 


  'Mandarin' :{
      'description': mark_safe(""" 
  Soil: Sandy loam with good organic matter PH 6-7.5<br>
  Climate: Tropical climate, temp.  25-35°C<br>
  Varieties: Nagpur Mandarin, coorg Mandarin, Khashi, Kamla<br>
  Propn method: T-  Budding<br>
  Seed Rate, Spacing :  7x7 m 5x5 m <br>
                               Planting season: June-July<br>
  FIELD7:<br>
  Fertilizer dose: 50 kg FYM/plant/ year 1000: 500:500 g  NPK/plant/ year<br>
  FIELD9:<br>
  Maturity Indices: Mature 210-240 day after flowering,<br>
  Harvesting: Fruit picker collect the fruit manually<br>
 
  FIELD14: 800-  1200  fruit/ plant/ year<br>
  FIELD15:<br>
  Pests: Fruit fly leaf minor, leaf eating caterpillar<br>
  FIELD17:<br>
  Diseases: Gummosis, Citrus Canker, Dieback<br>
  """ ), 
  'crop_image_url': 'https://images6.alphacoders.com/663/663909.jpg'
   },


  'Sweet orange' :{
      'description': mark_safe(""" 
  Soil: Sandy loam with good organic matter  PH 6-7.5<br>
  Climate: Sub-tropical, dry climates, low rainfall, temp. 20-30°C<br>
  Varieties: Mosambi, Katol Gold, Pine Apple, Washington Novel, Satgudi, Jaffa<br>
  Propn method: T-  Budding<br>
  Seed Rate, Spacing : 6x6 m 5x5 m <br>
                               Planting season:: June-July<br>
  FIELD7:<br>
  Fertilizer dose: 50 kg FYM/plant/ year  1000: 500:500 g  NPK/plant/  year<br>
  FIELD9:<br>
  Maturity Indices: Mature 210-240 day after flowering,<br>
  Harvesting: Fruit picker collect the fruit manually<br>
  
  FIELD14: 600-  800  fruit/ plant/  year<br>
  FIELD15:<br>
  Pests: Fruit sucking moth, leaf minor<br>
  FIELD17:<br>
  Diseases: Gummosis, Citrus Canker, Dieback<br>
  """ ), 
  'crop_image_url': 'https://th.bing.com/th/id/OIP.PZem76T-IYVO2vPPlDpz3wHaE7?w=260&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7'
   },


  'Acid Lime' :{
      'description': mark_safe(""" 
  Soil: Sandy loam with good organic matter  PH 6-7.5<br>
  Climate: Sub-tropical, dry climates, low rainfall, temp. 20-30°C<br>
  Varieties: Sai Sarbati, Vikram Pramalini, Chakradhar (seedless) Baramasi, PDKV Bahar<br>
  Propn method: T- Budding<br>
  Seed Rate, Spacing: 5x5 m <br>
                               Planting season: June-July<br>
  FIELD7:<br>
  Fertilizer dose: 50 kg FYM/plant/ year  600: 300:300 g  NPK/plant/  year<br>
  FIELD9:<br>
  Maturity Indices: Mature 120-150 day after flowering,<br>
  Harvesting: Fruit picker collect the fruit manually<br>
  
  FIELD14: 3000  fruit/ plant/ year<br>
  FIELD15:<br>
  Pests: Fruit fly leaf minor, leaf eating caterpillar<br>
  FIELD17:<br>
  Diseases: Gummosis, Citrus Canker, Dieback
  """ ),
  'crop_image_url': 'https://www.farmatma.in/wp-content/uploads/2020/06/acid-lime-cultivation-600x450.jpg'
   }, 


   


  'Rose' :{
      'description': mark_safe(""" 
  Soil: Well drained, medium loam soil having PH 6-7.5 is ideal<br>
  Climate: Cool climate, Loves sunshine & free ventilation, Night Temp.  16°C, produce more flower.<br>
  Varieties: Hybrid Tea: Super Star, Raktagandha, Arjun, Rajkumari, Bhim, Floribundas: Mohini, Sindhoor, Suchitra.<br>
  Propn method: Shield budding & Cutting.<br>
  Seed Rate, Spacing: 60 x 75 cm,  60 x 45 cm. <br>
                               Planting season: Oct to Dec & May to June.<br>
  FIELD7:<br>
  Fertilizer dose: 8-10 kg / plant 250:500:375 kg/ha<br>
  FIELD9:<br>
  Maturity Indices: Cut flower: Tight bud stage<br>
  Loose Flower:  Fully open.<br>
  Harvesting: Harvesting should be done early morning or late evening<br>
 
  FIELD14: 30-40 flower/ plant/y r.<br>
  FIELD15:<br>
  Pests: Red Scale, Mites, Thrips, Mealy Bug.<br>
  FIELD17:<br>
  Diseases: Dieback, Powdery mildew, Black Spot, Rust.<br>
  """ ), 
  'crop_image_url': 'https://th.bing.com/th/id/OIP.AgfS2U_JqQ8e65IXiydNqQHaD4?w=337&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7'
   },

  'Chrysanthemum' :{
      'description': mark_safe(""" 
  Soil: Well drained, sandy loam with good organic matter  PH 6.5-7<br>
  Climate: Short Day Plant, Temp.  20-27°C<br>
  Varieties: Sonar Bangla, Sweet Heart, Kirti, Indira, Chandrama, Day Dream, Mahatma Gandhi, Chandrakant.<br>
  Propn method: Seeds, Root suckers or Terminal cuttings.<br>
  Seed Rate, Spacing : 45 x 30 cm,  30 x 30 cm. <br>
                               Planting season: Jan-Feb., Jun-July.<br>
  FIELD7:<br>
  Fertilizer dose: 20-30 t FYM/ha  200:200:200  kg/ha<br>
  FIELD9:<br>
  Maturity Indices: Standard: 40-  50% flower open,  Dwarf Var.: 80-85% flower open.<br>
  Harvesting: 3-4 months after TP,  fully open flower are harvested.<br>
  
  FIELD14: 10-12  t/ha<br>
  FIELD15:<br>
  Pests: Aphids<br>
  FIELD17:<br>
  Diseases: Wilt, Stem & Foot rot<br>
  """ ), 
  'crop_image_url': 'https://th.bing.com/th/id/OIP.p4BUediWPBLDhe_7xBOanQHaE8?rs=1&pid=ImgDetMain'
   },

  'Aster' : {
      'description': mark_safe(""" 
   <ul>
            Soil: Well-drained loamy soil<br>
            Climate: Cool, Temperature 15-25 °C<br>
            Varieties: Matsumoto, Viking, Tower, Apricot, Lilliput<br>
            Propagation method: Seeds<br>
            Seed Rate, Spacing & Planting season:
            
                1.5-2.0 kg/ha,
                30 x 30 cm,
                Spring or Autumn
            
            Fertilizer dose: 50:100:100 Kg NPK/ha<br>
            Maturity Indices: Harvesting when the flowers are in bud stage<br>
            Harvesting: Harvesting is done when 50% of the flowers are in the bud stage<br>
            Yield: 40-50 t/ha<br>
            Pests: Aphids, Thrips, Spider mites<br>
            Diseases: Powdery mildew, Leaf spot, Stem rot<br>
        
  """ ), 
  'crop_image_url': 'https://th.bing.com/th/id/OIP.Z3mzyKfaP7K3Kfumlq4wNQHaE7?rs=1&pid=ImgDetMain'
   },

  'Marigold' :{
      'description': mark_safe(""" 
  <>
            Soil: Well-drained loamy soil<br>
            Climate: Warm, Temperature 20-30 °C<br>
            Varieties: African Marigold (Tagetes erecta), French Marigold (Tagetes patula)<br>
            Propagation method: Seeds<br>
            Seed Rate, Spacing & Planting season:
            
            1.0-1.5 kg/ha,
            30 x 30 cm,
            Year-round<br>
        
            Fertilizer dose: 50:100:100 Kg NPK/ha<br>
            Maturity Indices: Harvesting when the flower is fully open<br>
            Harvesting: Flowers are harvested when fully open in the morning<br>
            Yield: 25-30 t/ha<br>
            Pests: Aphids, Thrips, Spider mites<br>
            Diseases: Powdery mildew, Botrytis blight, Root rot<br>
        
  """ ), 
  'crop_image_url': 'https://th.bing.com/th/id/OIP.UMPoZ0v-k2AIK2b9MvnAHQHaG9?w=221&h=190&c=7&r=0&o=5&dpr=1.3&pid=1.7'
   },

  'Gladiolus' :{
      'description': mark_safe(""" 
  <ul>
            Soil: Well-drained sandy loam<br>
            Climate: Warm, Temperature 18-24 °C<br>
            Varieties: Traderhorn, Friendship, Spice Market, Peppermint<br>
            Propagation method: Corms<br>
            Seed Rate, Spacing & Planting season:
            
            2,000-3,000 kg/ha,
            20 x 20 cm,
            Spring<br>
            
            Fertilizer dose: 50:100:100 Kg NPK/ha<br>
            Maturity Indices: Harvesting when the first two or three florets on the lower spike begin to open<br>
            Harvesting: Harvesting is done when florets are 2/3 open, early in the morning<br>
            Yield: 40-50 q/ha<br>
            Pests: Thrips, Mites, Aphids, Caterpillars<br>
            Diseases: Fusarium wilt, Rust, Botrytis, Soft rot<br>
        
  """ ), 
  'crop_image_url': 'https://cdn.shopify.com/s/files/1/1419/7120/products/Star_Jasmine-1.SHUT.jpg?v=1559235370'
   },

  'Blanket flower' :{
      'description': mark_safe(""" 
  
            Soil: Well-drained sandy loam<br>
            Climate: Warm, Temperature 18-24 °C<br>
            Varieties: Goblin, Mesa Yellow, Mesa Red, Fanfare, Oranges and Lemons<br>
            Propagation method: Seeds<br>
            Seed Rate, Spacing & Planting season:
            
            500 g/ha,
            30 x 30 cm,
            Spring<br>
            
            Fertilizer dose: 20:40:20 g/plant<br>
            Maturity Indices: Blooming of flowers<br>
            Harvesting: Flowers are picked when fully open in the morning<br>
            Yield: 1,500-2,000 kg/ha<br>
            Pests: Aphids, Thrips, Spider mites<br>
            Diseases: Powdery mildew, Botrytis blight<br>
        
  """ ), 
  'crop_image_url': 'https://cdn.shopify.com/s/files/1/1419/7120/products/Star_Jasmine-1.SHUT.jpg?v=1559235370'
   },

  'Jasmine' :{
      'description': mark_safe(""" 
  
            Soil: Well-drained sandy loam<br>
            Climate: Warm and humid, Temperature 20-30 °C<br>
            Varieties: Grand Duke of Tuscany, Arabian jasmine, Maid of Orleans, Belle of India<br>
            Propagation method: Cutting<br>
            Seed Rate, Spacing & Planting season:
            
            Through cuttings,
            30 x 30 cm,
            Year-round<br>
            
            Fertilizer dose: 20:40:20 g/plant<br>
            Maturity Indices: Blooming of flowers<br>
            Harvesting: Flowers are picked early in the morning before they fully open<br>
            Yield: 20-30 kg/ha<br>
            Pests: Aphids, Red spider mites, Whiteflies, Thrips<br>
            Diseases: Powdery mildew, Downy mildew, Leaf spot<br>
        
  """ ),
  'crop_image_url': 'https://cdn.shopify.com/s/files/1/1419/7120/products/Star_Jasmine-1.SHUT.jpg?v=1559235370'
   }, 


  'Mogra' :{
      'description': mark_safe(""" 
  Soil: with good<br>
  Climate: climate, warm<br>
  Varieties: Mohora, Double<br>
  Propn method: cutting,<br>
  Seed Rate, Spacing & Planting season: Jun - July.<br>
  FIELD7:<br>
  Fertilizer dose: FYM/Plant/yr.<br>
  FIELD9:<br>
  
  Harvesting: opened flower<br>
  FIELD12:<br>
  Yield: t/ha<br>
  FIELD14:<br>
  FIELD15:<br>
  Pests: Red Mites,<br>
  FIELD17:<br>
  Diseases: Spot, Leaf<br>
  """ ),
  'crop_image_url': 'https://th.bing.com/th/id/OIP.LHJ2j_5xqZOCGggTCRC_CQHaEK?w=280&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7'
   }, 

  'Jai' :{
      'description': mark_safe(""" 
  Soil: Sandy loam<br>
  Climate: Mild tropical<br>
  Varieties:  Co-1 Pitchi,<br>
  Propn method: Semi hard<br>
  Seed Rate, Spacing & Planting season: 1.5 x 1.5 m,<br>
  FIELD7:<br>
  Fertilizer dose: 10 kg<br>
  FIELD9:<br>
  Maturity Indices: Flowering start<br>
  Harvesting: fully develop/<br>
  FIELD12:<br>
  Yield: 10-Aug<br>
  FIELD14:<br>
  FIELD15:<br>
  Pests: Bud Warm,<br>
  FIELD17:<br>
  Diseases: Wilt, Leaf<br>
  """ ), 
  'crop_image_url': 'https://www.plantsguru.com/image/cache/foliage-plants/jasminum-humile-revolutum-750x750.jpg'
   },

  'Jui' : {
      'description': mark_safe(""" 
  Soil: Sandy loam<br>
  Climate: Mild tropical<br>
  Varieties: Co-1 Mullai, Co-2 Mullai.<br>
  Propn method: Semi hard<br>
  Seed Rate, Spacing & Planting season: 1.8 x 1.8 m,<br>
  FIELD7:<br>
  Fertilizer dose: 10 kg<br>
  FIELD9:<br>
  Maturity Indices: Flowering start<br>
  Harvesting: fully develop/<br>
  FIELD12:<br>
  Yield: 8<br>
  FIELD14:<br>
  FIELD15:<br>
  Pests: Bud Warm,<br>
  FIELD17:<br>
  Diseases: Wilt, Leaf<br>
  """ ), 
  'crop_image_url': 'https://i.pinimg.com/736x/cf/c3/f4/cfc3f4ae034b55b90b288d96fddd1b40--bonsai-jasmine.jpg'
   }, 

}