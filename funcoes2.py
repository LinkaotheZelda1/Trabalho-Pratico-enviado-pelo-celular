# FUNÇÃO, LogIn Usuário

def loginUsuario(perfil):
    if perfil.lower() == 'admin':
        print('Bem-vindo, Administrador')
    else:
        print('Bem vindo, Usuário')

#todos que estão escritos admin, independente se maiúsculo ou mínusculo, devem entrar na função IF.
loginUsuario('Admin')
loginUsuario("admin")
loginUsuario("User")
loginUsuario("usuário")
loginUsuario("ADMIN")
loginUsuario("cliente")

#como o restante está diferente de admin, vai cair na função else.
# Surgiu uma dúvida também, tem como chamar uma função pelo input?

loginUsuario(input('Digite o perfil: '))

#nessa última, o python me ajudou interpretando o código.