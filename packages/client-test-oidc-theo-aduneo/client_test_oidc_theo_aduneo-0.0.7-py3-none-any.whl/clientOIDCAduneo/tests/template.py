import sys 
sys.path.append('..')

from Template import Template

items = [{"nom": "Clavier", "prix": "20€"}, {"nom": "Souris", "prix": "10€"}]
print(Template.apply_template("""
Bonjour {{ nom }}. {% for i in range(1,5) %} Hello {{ i*m }} {% endfor %}{% for item in items %} Nom {{ item['nom'] }} Prix {{ item['prix'] }} {% endfor %}
{% if nom == 'Jean' %} Mais c'est Jean ! {% elif nom == 'Pierre' %} Mais c'est Pierre ! {% else %} Ce n'est ni Jean ni Pierre {% endif %}
""", 
  nom='Pierre', m=6, items=items))
