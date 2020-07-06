from app.register import register
from flask import render_template, request

owners = {}
counter = 1


@register.route('/', methods=['GET', 'POST'])
def register_start():
    return render_template('register/register_start.html')


@register.route('/menu', methods=['GET', 'POST'])
def register_menu():
    if request.method == 'POST':
        global counter, owners, pets
        owners[counter] = {
            'name': request.form['name'],
            'age': request.form['age'],
            'city': request.form['city'],
            'pets': []
        }

        counter += 1

    return render_template('register/register_menu.html', owners=owners)


@register.route('/pet_reg', methods=['GET', 'POST'])
def register_pet():
    if request.method == 'POST':
        global owners
        for k, v in owners[int(request.form['index'])].items():
            if k == 'pets':
                v.append({
                    'name': request.form['pet_name'],
                    'age': request.form['pet_age'],
                    'type': request.form['type']
                })

    return render_template('register/register_pet.html', owners=owners)


@register.route('/single_owner')
def single_owner():

    return render_template('register/single_owner.html')
