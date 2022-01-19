# Extract Transform Load

### Sobre o Projeto
O projeto tem como sua finalidade principal extrair dados do site [https://www.escritas.org/pt](https://www.escritas.org/pt/poemas) de forma automatizada, tratar esses dados e inseri-los como documentos no banco de dados não relacional *MongoDB*. A posteriori o repositório [Beautiful Pyems](https://github.com/RodrigoSiliunas/beautiful-pyems) consumirá os documentos armazenados e retornará esses dados de diferentes maneiras em formato de API *Flask*.

### Tecnologias Utilizadas
O projeto utiliza várias tecnologias por de baixo dos panos, eu listarei **apenas** as principais, incluindo bibliotecas.

> 1. *Python*
> 2. *Pandas*
> 3. *Selenium*
> 4. *BeautifulSoup*
> 5. *MongoDB*


### Rodando o Projeto
O código principal fica em `src/main.py`. Antes de executar o código você deve se certificar que tem o *Python* em sua **versão minima** 3.10.1 instalada em sua máquina. Você também deverá ter o MongoDB instalado em sua máquina.

Se estiver cumprindo os requisitos basta abrir o *terminal/powershell* na pasta raiz do projeto e ativar a venv com o comando:

    enviroment/Scripts/activate

As bibliotecas seram carregadas e você pode simplesmente executar o comando:

    python src/main.py

A mágica toda vai acontecer, você só precisa aguardar enquanto as informações são extraidas do site e carregadas em seu MongoDB. 😎
<br/>

### Fluxo do Sistema
![Fluxo do sistema em imagem](/out/fluxo.png)

### Observações Importantes ⚠️

O módulo ***LinkFinder*** possui apenas um parâmetro **obrigatório**. Ele é o inteiro que representa quanto tempo você deseja aguardar até que a página seja carregada completamente. Single Page Aplications tem o seu HTML renderizado pouco tempo após o cliente fazer a requisição, por isso ele é necessário para que tudo funcione corretamente. Se a sua conexão com a internet e o seu computador forem de alta performance você pode reduzir o tempo, caso contrário você pode aumentar o tempo para que tudo ocorra sem problemas.

### Considerações Finais
Esse foi um projeto muito divertido de ser feito, do inicio ao fim eu estive completamente focado e o entretenimento e satisfação pessoal foi tanta que acabou se passando o tempo sem que eu sequer notasse.

Conceitos importantes do Selenium e do BeautifulSoup foram aprendidos e um novo leque de possibilidades se abriu na minha mente. Eu espero que esse repositório possa ajudar alguma pessoa da mesma maneira que repositórios alheios me ajudaram/inspiraram.

De qualquer tempoespaço em que você leitor estiver, desejo profundo sucesso e boa sorte na vida. Obrigado por ler até aqui e se eu puder ajudar em alguma coisa me procure nas minhas [redes sociais](https://www.instagram.com/rosiliunas/). ✨🎉  😉✌  ✨🎉
