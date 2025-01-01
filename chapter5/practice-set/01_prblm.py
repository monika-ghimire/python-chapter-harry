# write program to create a dictionary of hindi words with value as
#  their engligh translion. provide user with an option to look it up

d_lang ={
    'nameste' :'hello',
    'sanchai_xau': 'how are you'
}

a = input(f'put and word \n{d_lang.keys()}')

print(f'{d_lang[a]} , this is menaing of {a} ')