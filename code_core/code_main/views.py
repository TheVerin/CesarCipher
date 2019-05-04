from django.shortcuts import render
from code_main.models import Cipher


def list_creator() -> list:
    letters = []
    for i in 'abcdefghijklmnopqrstuvwxyz':
        letters.append(i)

    LETTERS = []
    for j in letters:
        LETTERS.append(j.upper())

    signs_nums = []
    for l in ",./;:[]{}-_<>' 0123456789":
        signs_nums.append(l)

    return (letters + LETTERS + signs_nums) * 2


def dict_creator(direction='right', displacement=3) -> dict:
    cipher_list = list_creator()
    cipher_dict = {}
    if direction == 'right':
        for o in range(len(cipher_list) - displacement):
            cipher_dict[cipher_list[o]] = cipher_list[o + displacement]
    else:
        for o in range(len(cipher_list) + displacement):
            cipher_dict[cipher_list[o]] = cipher_list[o - displacement]
    return cipher_dict


def coder(message: str) -> str:
    coder_list = []
    cipher_dict = dict_creator(direction='right', displacement=3)
    for char in message:
        coder_list.append(cipher_dict[char])
    return ''.join(coder_list)


def cesar_cipher(request):
    to = ''
    direction = ''
    displacement = 3
    message = ''
    result = ''

    if request.GET.get('to'):
        to = request.GET.get('to')
        if request.GET.get('direction'):
            direction = request.GET.get('direction')
            if request.GET.get('displacement'):
                tr = request.GET.get('displacement')
                displacement = int(tr)
                if request.GET.get('message'):
                    message = request.GET.get('message')
                    result = coder(message)

    obj = Cipher.objects.create(to=to, message=message, direction=direction, displacement=displacement,
                                result=result)
    obj.save()

    return render(
        request, 
        'index.html',
        {
            'to': to,
            'message': message,
            'direction': direction,
            'displacement': displacement,
            'result': result

        }
    )
