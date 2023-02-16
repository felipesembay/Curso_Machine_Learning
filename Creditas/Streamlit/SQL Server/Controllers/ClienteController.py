import services.database1 as db;

def Incluir(cliente):
    count = db.cursor.execute("""
    INSERT INTO Cliente (clinome, clisexo, cliphone_code, clicpf_restrition, clirenda, climodel_year, cliautovalue, cliautodebt, 
    cliloan_amount, cliidade, clidiff_created, cliprevisao) 
    VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""",
    cliente.nome, cliente.sexo, cliente.phone_code, cliente.cpf_restrition, cliente.renda, cliente.model_year, cliente.autovalue, cliente.auto_debt, cliente.loan_amount, cliente.idade, cliente.diff_created, cliente.previsao).rowcount
    db.cnxn.commit()
    
    
    
    

