from django.utils.safestring import mark_safe

paircrop_dict = {
    'Maize' : mark_safe("""
<ul>
<li>Legumes<li>
<li>Cowpea<li>
<li>Soyabean</li>
</ul>                        
    
    """
        ),
    'Coconut' : mark_safe("""
<ul>
<li>Banana<li>
<li>Okra<li>
</ul> 
    
    """
        ),
    'Sorghum' : mark_safe("""
Legumes
    
    """
        ),
    'Cotton' : mark_safe("""
Soyabean
    
    """
        ),
    'Beans' : mark_safe("""
<ul>
<li>Corn<li>
<li>Sorghum<li>
</ul>  

    
    """
        ),
    'Peas' : mark_safe("""
<ul>
<li>Corn<li>
<li>Sorghum<li>
</ul>  

    
    """
        ),
    'Sunflowers' : mark_safe("""
<ul>
<li>Beans<li>
<li>Cucumber<li>
</ul>  

    
    """
        ),
    'Herbs' : mark_safe("""
Vegetables
    
    """
        ),
    'Tomato' : mark_safe("""
<ul>
<li>beans<li>
<li>Marigold<li>
<li>Basil</li>
</ul>  

    
    """
        ),
    'Corn' : mark_safe("""
<ul>
<li>Beans<li>
<li>Squash<li>
</ul>  

    
    """
        ),
    'Wheat' : mark_safe("""
<ul>
<li>Mustard</li>
<li>Legumes</li>
</ul>
    
    """
        ),
    'Carrot' : mark_safe("""
Onions
    
    """
        ),
    'Potato' : mark_safe("""
Horseradish
    
    """
        ),



}