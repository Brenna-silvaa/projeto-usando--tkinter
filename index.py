from tkinter import *

janela = Tk()
janela.title("Receita")
janela.geometry("750x600")
janela.configure(background="#F5DEB3")

img = PhotoImage(file="imagem/BrigadeiroSmall.png")

txt1 = Label(
    janela, 
    text="Receita de Brigadeiro",
    justify="center", 
    foreground="#8B4513", 
    background="#F5DEB3",  
    font="Arial 18 bold",
    pady=10
)
txt1.pack()

imagem = Label(
    janela,
    image=img,
    width=200,
    height=200,
    background="#F5DEB3"
).pack()

text2 = Label (
    janela,
    text="Ingredientes",
    justify="center",
    font="Arial 16 bold",
    foreground="#8B4513", 
    background="#F5DEB3",
).pack()

text3 = Label (
    janela,
    text="2 caixas de leite condensado\n 4 colheres de sopa de chocolate em pó \n 1 colher de sopa de margarina sem sal\n Chocolate granulado",
    justify="center",
    font="Arial 12 bold",
    foreground="#D2691E", 
    background="#F5DEB3",
    pady=2
).pack()

text4 = Label (
    janela,
    text="Modo de preparo",
    justify="center",
    font="Arial 16 bold",
    foreground="#8B4513", 
    background="#F5DEB3",
    pady= 20
).pack()

text5 = Label (
    janela,
    text="Em uma panela funda, acrescente o leite condensado, a margarina e o chocolate em pó.\n Cozinhe em fogo médio e mexa até que o brigadeiro comece a desgrudar da panela.\n Deixe esfriar e faça pequenas bolas com a mão passando a massa no chocolate granulado.",
    justify="center",
    font="Arial 12 bold",
    foreground="#D2691E", 
    background="#F5DEB3",
).pack()

janela.mainloop()