from tkinter import *
from tkinter import messagebox
from tkinter import ttk

agenda = []
index = 0
# Functions
def adicionarContato() -> None:
    nome = txt_nome.get()
    telefone = txt_telefone.get()
    categoria = cb_categorias.get()
    contato = {
        "nome": nome,
        "telefone": telefone,
        "categoria": categoria
    }
    agenda.append(contato)
    messagebox.showinfo("Adicionado!", "Contato adicionado com sucesso!")
    limparCampos()
    atualizarTabela()

def editarContato() -> None:
    opcao = messagebox.askyesno("Tem Certeza", "Deseja Alterar os dados do contato")
    if opcao:
        agenda[index] = {
            "nome": txt_nome.get(),
            "telefone": txt_telefone.get(),
            "categoria": cb_categorias.get()
        }
        messagebox.showinfo("Sucesso!", "Dados atualizados com sucesso!")
    limparCampos()
    atualizarTabela()
def excluirContato() -> None:
    opcao = messagebox.askyesno("Tem certeza?", "Deseja deletar a conta?")
    if opcao:
        contato = agenda[index]
        agenda.remove(contato)
        messagebox.showinfo("Apagado!","Contato Removido com sucesso")
        limparCampos()
        atualizarTabela()
def limparCampos() -> None:
    txt_nome.delete(0, END)
    txt_telefone.delete(0, END)
    cb_categorias.delete(0, END)

def atualizarTabela() -> None:
    # Limpa a tabela
    for linha in tabela.get_children():
        tabela.delete(linha)
    # atualizar a tabela
    for contato in agenda:
        tabela.insert("",END,values =(contato['nome'],
                                  contato['telefone'],
                                  contato['categoria']))

def tabelaClique(event):
    # Pegando o código da linha selecionada
    linha_clicada = tabela.selection()[0]
    # Atualizando o index
    index = tabela.index(linha_clicada)
    contato = agenda[index]
    limparCampos()
    txt_nome.insert(0, contato['nome'])
    txt_telefone.insert(0, contato['telefone'])
    cb_categorias.set(contato['categoria'])


# widget
janela = Tk()
janela.title("Agenda telefonica")

label_nome = Label(janela, text="Nome:", fg="navy",
                   font="Tahoma 14 bold")
label_nome.grid(row=0, column=0)

txt_nome = Entry(janela, font="Tahoma 14", width=27)
txt_nome.grid(row=0, column=1)

label_telefone = Label(janela, text="Telefone:", fg="navy",
                       font="Tahoma 14 bold")
label_telefone.grid(row=1, column=0)

txt_telefone = Entry(janela, font="Tahoma 14", width=27)
txt_telefone.grid(row=1, column=1)

label_categoria = Label(janela, text="Categoria:", fg="navy",
                        font="Tahoma 14 bold")
label_categoria.grid(row=2, column=0)
categorias = ["Amigos", "Família", "Trabalho"]
cb_categorias = ttk.Combobox(janela, values=categorias,
                             width=25, font="Tahoma 14")
cb_categorias.grid(row=2, column=1)

btn_adicionar = Button(janela, text="Adicionar", fg="navy",
                       bg="white", font="Tahoma 12 bold", width=8,
                       command=adicionarContato)
btn_adicionar.grid(row=3, column=0)

btn_editar = Button(janela, text="Editar", fg="navy",
                    bg="white", font="Tahoma 12 bold", width=8,
                    command=editarContato)
btn_editar.grid(row=3, column=1)

btn_excluir = Button(janela, text="Excluir", fg="navy",
                     bg="white", font="Tahoma 12 bold", width=8,
                     command=excluirContato)
btn_excluir.grid(row=3, column=2)

# tabela => treeview
tabela = ttk.Treeview(janela, columns=("Nome", "Telefone", "Categoria"),
                      show="headings")
# Nomeando as colunas/cabeçalho
tabela.heading("Nome", text="Nome")
tabela.heading("Telefone", text="Telefone")
tabela.heading("Categoria", text="Categoria")
# Criando ação para quando clicar-mos na tabela
tabela.bind("<ButtonRelease-1>",tabelaClique)
tabela.grid(row=4, columnspan=3)

janela.mainloop()