from django.utils.safestring import mark_safe

fertilizer_dic = {
    'NHigh': mark_safe("""
        <ol>
            <li><b>Manure:</b> Adding manure is one of the simplest ways to amend your soil with nitrogen. Be careful as there are various types of manures with varying degrees of nitrogen.</li>
            <li><b>Coffee Grinds:</b> Use coffee grinds, which are rich in nitrogen. They also improve drainage in the soil as they break down.</li>
            <li><b>Plant Nitrogen Fixing Plants:</b> Plant vegetables like peas, beans, and soybeans from the Fabaceae family to increase nitrogen in your soil.</li>
            <li><b>Plant 'Green Manure' Crops:</b> Consider planting crops like cabbage, corn, and broccoli.</li>
            <li><b>Use Mulch:</b> Apply wet grass or other materials like sawdust and scrap soft woods as mulch while growing crops.</li>
        </ol>
    """),

    'Nlow': mark_safe("""
        <ol>
            <li><b>Add Sawdust or Fine Woodchips:</b> The carbon in sawdust/woodchips helps the soil to absorb more nitrogen.</li>
            
            <li><b>Water:</b> Soaking your soil with water helps leach nitrogen deeper into the soil.</li>
            <li><b>Sugar:</b> Limited studies suggest that adding sugar can potentially reduce nitrogen in the soil. Sugar is high in carbon, which attracts and soaks up nitrogen.</li>
            <li><b>Add Composted Manure:</b> Composted manure is an excellent source of nitrogen.</li>
            <li><b>Plant Nitrogen Fixing Plants:</b> Consider peas or beans.</li>
            <li><b>Use NPK Fertilizers with High N Value.</b></li>
            
        </ol>
    """),

    'PHigh': mark_safe("""
        <ol>
            <li><b>Avoid Adding Manure:</b> Manure contains high levels of phosphorous. Limiting its addition helps reduce phosphorus in the soil.</li>
            <li><b>Use Only Phosphorus-Free Fertilizer:</b> Limit phosphorous by choosing a fertilizer with numbers like 10-0-10, where zero represents no phosphorous.</li>
            <li><b>Water Your Soil:</b> Soaking your soil helps drive phosphorous out.</li>
            <li><b>Plant Nitrogen Fixing Vegetables:</b> Beans and peas increase nitrogen without increasing phosphorous.</li>
            <li><b>Use Crop Rotations:</b> Rotate crops to decrease high phosphorous levels.</li>
        </ol>
    """),

    'Plow': mark_safe("""
        <ol>
            <li><b>Bone Meal:</b> A fast-acting source rich in phosphorous made from ground animal bones.</li>
            <li><b>Rock Phosphate:</b> A slower-acting source that needs soil conversion.</li>
            <li><b>Phosphorus Fertilizers:</b> Apply a fertilizer with high phosphorous content (e.g., 10-20-10).</li>
            <li><b>Organic Compost:</b> Quality organic compost increases phosphorous content.</li>
            <li><b>Manure:</b> Manure is an excellent source of phosphorous.</li>
            <li><b>Clay Soil:</b> Introduce clay particles to fix phosphorus deficiencies.</li>
            <li><b>Ensure Proper Soil pH:</b> Maintain a pH of 6.0 to 7.0 for optimal phosphorus uptake.</li>
            <li>If pH is low, add lime or potassium carbonate. If pH is high, add organic matter.</li>
        </ol>
    """),

    'KHigh': mark_safe("""
        <ol>
            <li><b>Loosen the Soil:</b> Deeply dig and water to dissolve water-soluble potassium. Allow the soil to dry and repeat.</li>
            <li><b>Sift Through the Soil:</b> Remove rocks to reduce slow-release potassium from minerals.</li>
            <li><b>Stop Applying Potassium-Rich Fertilizer:</b> Use only fertilizer with '0' in the final number field.</li>
            <li><b>Mix Crushed Eggshells, Crushed Seashells, Wood Ash, or Soft Rock Phosphate:</b> Add calcium and up to 10% organic compost.</li>
            <li><b>Use NPK Fertilizers with Low K Levels and Organic Fertilizers:</b> They have low NPK values.</li>
            <li><b>Grow a Cover Crop of Legumes:</b> Legumes fix nitrogen without increasing phosphorus or potassium.</li>
        </ol>
    """),

    'Klow': mark_safe("""
        <ol>
            <li>Mix in muricate of potash or sulphate of potash.</li>
            <li>Try kelp meal or seaweed.</li>
            <li>Try Sul-Po-Mag.</li>
            <li>Bury banana peels an inch below the soil's surface.</li>
            <li>Use Potash fertilizers since they contain high values of potassium.</li>
        </ol>
    """)
}
