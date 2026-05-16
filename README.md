# Sistema de Controle de Estoque (CRUD) - Python & MySQL

Este é um sistema de linha de comando (CLI) desenvolvido em Python para o gerenciamento e controle de estoque de componentes eletrônicos. O projeto realiza a integração completa com um banco de dados relacional MySQL Workbench, aplicando conceitos fundamentais de Engenharia de Software e Banco de Dados.

## 🚀 Funcionalidades

*   **Cadastrar novo componente:** Insere o nome, a quantidade em estoque e o preço unitário com persistência em banco de dados.
*   **Consultar componentes:** Lista os componentes cadastrados de forma limpa e organizada no terminal.
*   **Excluir componente:** Remove um registro específico utilizando o ID como chave primária, com validação de impacto.
*   **Tratamento de Exceções:** Proteção contra entradas inválidas do usuário (letras em campos numéricos) e tratamento de falhas de conexão com o SGBD.

## 🛠️ Tecnologias Utilizadas

*   **Python 3.x**
*   **MySQL Server / MySQL Workbench**
*   **Biblioteca `mysql-connector-python`**

## 📐 Boas Práticas Aplicadas (Conceitos de Ciência da Computação)

1.  **Prevenção contra SQL Injection:** Utilização de placeholders (`%s`) no método `execute()` para garantir a segurança e higienização dos dados inseridos pelo usuário.
2.  **Gerenciamento de Transações (ACID):** Uso explícito do `conn.commit()` logo após operações de escrita (`INSERT` e `DELETE`) para assegurar a persistência correta e evitar locks desnecessários nas tabelas.
3.  **Performance em Consultas:** Evitado o uso de `SELECT *` na listagem de dados, especificando as colunas estritamente necessárias para otimizar o consumo de memória e tráfego de rede.
4.  **Robustez de Fluxo:** Implementação de estruturas `try/except` para capturar `ValueError`, garantindo que falhas de digitação do usuário não quebrem a execução do programa (resiliência).

