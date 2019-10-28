def infinit_sum_parameter(*args):
    suma = 0

    for number in args:
        suma += number

    return suma


print('Suma infinita:')
print(infinit_sum_parameter(1,2,3))


def infinit_kev_value_arguments(**kwargs):
    print(kwargs)


print('Key value infinito')
infinit_kev_value_arguments(perro="Pepe",gato="Michi",loro="pepito")


def combine_words(word,**kwargs):
    print(kwargs.get('prefix'))

    if 'prefix' in kwargs:
        return kwargs["prefix"]+word
    elif 'suffix' in kwargs:
        return word+kwargs["suffix"]
    return word


print(combine_words("child",prefixsd="dsssd"))