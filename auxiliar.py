#listas
nomes = ["Jose","Laercio","Emera","JoaoPaulo"]

#pegar a informaçao de uma lista
primeiro = nomes[0]
print(primeiro)

#adicionar informaçao
nomes.append("Maria")
print(nomes)

#dicionarios
pessoa = {"nome": "Jose", "idade": 12, "peso": 50, "cidade": "Varzea Grande"}


peso = pessoa["peso"]
print(peso)

##como vamos usar
lista_mensagens = []

mensagem1 = {"role": "user", "content": "fala galera"}
mensagem2 = {"role": "assistant", "content": "resposta da IA"}

lista_mensagens.append(mensagem1)
lista_mensagens.append(mensagem2)

print(lista_mensagens)

lista_mensagens = {
    {"role": "user", "content": "fala galera"},
    {"role": "assistant", "content": "resposta da IA"}
}
