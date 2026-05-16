#create DATABASE loja;
use loja;

CREATE TABLE componentes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    quantidade INT,
    preco_unitario DECIMAL(10, 2)
);


