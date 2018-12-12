from django.shortcuts import render
from code_main.models import Cipher


def list_creator() -> list:
    letters = []
    for i in 'abcdefghijklmnopqrstuvwxyz':
        letters.append(i)

    LETTERS = []
    for j in letters:
        LETTERS.append(j.upper())

    nums = []
    for k in range(0, 10):
        nums.append(k)

    signs = []
    for l in ",./;:[]{}-_<>' ":
        signs.append(l)

    return (letters + LETTERS + nums + signs) * 2


def dict_creator(direction='right', translation=3) -> dict:
    cipher_list = list_creator()
    cipher_dict = {}
    if direction == 'right':
        for o in range(len(cipher_list) - translation):
            cipher_dict[cipher_list[o]] = cipher_list[o + translation]
    else:
        for o in range(len(cipher_list) + translation):
            cipher_dict[cipher_list[o]] = cipher_list[o - translation]
    return cipher_dict


def coder(message: str) -> str:
    coder_list = []
    cipher_dict = dict_creator(direction='right', translation=3)
    for char in message:
        coder_list.append(cipher_dict[char])
    return ''.join(coder_list)

print(coder('Tomek Beben'))

def cesar_cipher(request):
    to = ''
    direction = 'right'
    translation = 3
    message = ''
    result = ''

    if request.GET.get('to'):
        to = request.GET.get('to')
        if request.GET.get('direction'):
            direction = request.GET.get('direction')
            if request.GET.get('translation'):
                tr = request.GET.get('translation')
                translation = int(tr)
                if request.GET.get('message'):
                    message = request.GET.get('message')
                    result = coder(message)

    obj = Cipher.objects.create(to=to,message=message, direction=direction, translation=translation,
                                result=result)
    obj.save()

    return render(
        request,
        'index.html',
        {
            'to': to,
            'message': message,
            'direction': direction,
            'tramslation': translation,
            'result': result

        }
    )
