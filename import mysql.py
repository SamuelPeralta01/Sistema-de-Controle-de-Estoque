import mysql.connector

def menu():
    print("1 - Cadastrar novo componente")
    print("2 - Consultar componentes")
    print("3 - Excluir componente")
    print("4 - Sair")

# 1. Configurar a conexão com o seu Workbench
config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'senha',
    'database': 'database'
}

try:
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()


    while True:
        menu()
        try:
            opcao = int(input("Escolha a opção que deseja realizar: "))
        except ValueError:
            print("Opção inválida, selecione uma das opções ")
    
        match opcao:
        
            case 1:
                print("--- Cadastro de Novo Componente ---")
                nome_comp = input("Nome do componente: ")
                qtd_comp = int(input("Quantidade em estoque: "))
                preco_comp = float(input("Preço unitário: "))

                
                comando_sql = "INSERT INTO componentes (nome, quantidade, preco_unitario) VALUES (%s, %s, %s)"
                valores = (nome_comp, qtd_comp, preco_comp)
                
                cursor.execute(comando_sql,valores)
                conn.commit()
            case 2: 
                print("--- Consulta de Componentes ---")
                cursor.execute("SELECT * FROM componentes")
                linhas = cursor.fetchall()
                for linha in linhas:
                
                    print(f"ID: {linha[0]} - Nome: {linha[1]} - quantidade: {linha[2]}")
                    

            case 3:
                
                id = int(input("Digite o id do componente que quer deletar:"))
                comando_sql = "DELETE FROM componentes WHERE id = %s"
                
                cursor.execute(comando_sql,[id])
                conn.commit() 
                if cursor.rowcount == 0:
                    print("Nenhum componente encontrado com esse ID.")
                else:
                    
                    print(f"\nSucesso! {cursor.rowcount} registro(s) deletado(s).")
    
            case 4: 
                print("Saindo do programa...")
                break
    

except mysql.connector.Error as erro:
    print(f"Erro ao inserir no MySQL: {erro}")

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        
        
        
        