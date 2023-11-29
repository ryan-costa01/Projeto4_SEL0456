<a name="readme-top"></a>


# Projeto 4 SEL0456
4° projeto da matéria SEL0456 - Técnicas em Desenvolvimento de Software Livre.

Este é um sistema de uma API responsável por retornar o valor do fatorial de um número 'n1' e o valor do termo 'n2' da sequência de Fibonacci. A estrutura de dados recebida pela API é um arquivo JSON, seguindo o método 'POST'. 

## :rocket: Rodando o projeto

1. Clone o repositório
   ```sh
   git clone git@github.com:ryan-costa01/Projeto4_SEL0456.git
   ```
2. Inicialize o programa em um Virtual Eviroment
   ```cmd
   export FLASK_APP=Project4.py
   flask run
   ```
3. Faça o envio do objeto JSON(utilizando outra janela do terminal)
   ```cmd
   curl -X POST http://127.0.0.1:5000/myapi -H 'Content-Type: application/json' -d '{"fact":n1,"fib":n2}'
   ```
   
## :wrench: Explicação do programa
### Envio do Objeto JSON
Ao inicializar o programa, o usuário deverá inserir um número inteiro entre 1 e 4, onde cada número representa uma função do programa.
```
1. Inicia o Servidor Local
```
Ao utilizar os comando do passo '2', seu server fica inicializado. É possível acessá-lo pelo link `http://127.0.0.1:5000/`
```
2. Enviar o objeto JSON
```
Com o passo '3', você realiza o envio do seu objeto JSON. Modifique os valores `n1` e `n2` por números inteiros que você quiser. O resultado será exibido no próprio terminal.


### Funcionalidades Adicionais

Certifique-se de que o arquivo `FunctionsAPI.py` esteja na mesma pasta que o código quando você o executar.

Este é um sistema simples de utilização de API que pode ser usado como base para projetos mais avançados.

## :memo: License

Distributed under the GNU General Public License v3.0. See `LICENSE.txt` for more information.

## :handshake: Colaboradores
<table>
  <tr>
    <td align="center">
      <a href="https://github.com/ryan-costa01">
        <img src="https://avatars.githubusercontent.com/u/63657064?s=400&u=cae3d15c188ed977d1713fb373a5a42a145ae3ba&v=4" width="100px;" alt="Foto de Ryan Costa no GitHub"/><br>
        <sub>
          <b>Ryan Costa</b>
        </sub>
      </a>
    </td>
