# PERGUNTAS:
* Como preencher o id_conta automaticamente?

# Operações para cada um dos modelos e suas consequências

## BancoModel
* Apenas os desenvolvedores devem poder modificar essa tabela!
* Automatizar a população da tabela baseada em um índice de bancos? Talvez...
* Não implementaremos CRUD para este modelo!

## CategoriaModel
* Apenas os desenvolvedores devem poder modificar essa tabela!
* Não implementaremos CRUD para este modelo (por enquanto, talvez no futuro cada usuário poderá criar suas próprias categorias)!

## ContaBancariaModel
* CRUD simples com Owners

## TransacaoRecorrenteModel
* CRUD simples com Owners
* A cada mês, seta pago_no_mes = False (o frontend usará esse campo para gerar botões (ou não) que permitirá ao usuário consumar esse gasto)
* Cada usuário poderá fazer seu próprio CRUD de transações recorrentes e verificar suas próprias transações financeiras
* Endpoint para consumar TransacaoRecorrente
* Retrieve não pagos no mês

## ControleModel
* CRUD simples com Owners
* Retrieve "normal" verifica apenas Controles do mês atual
* A cada novo mês, cria novos ControleModels do último mês e que sejam recorrentes para cada usuário! Como isso seria feito? (Airflow? DAG mensal?)
* Retrieve "historico" retorna os Controles a cada mês de um usuário! (fazer _controller_ com Range!)

## Transacao
* Create: modifica a ContaBancaria associada de tal forma que ContaBancaria.quantia += Transacao.quantia e o controle tbm
* Delete: modifica a Conta associada de tal forma que ContaBancaria.quantia -= Transacao.quantia e o controle tbm
* Update: faz as seguintes operações: 
    1. Conta.quantia += Transacao.quantiaNova - Transacao.quantiaVelha
    1. VelhoControle.gasto -= Transacao.quantiaVelha
    1. Seleciona NovoControle baseado em Transacao.mesNovo e Transacao.id_controle
    1. NovoControle.gasto += Transacao.quantiaNova
* Retrieve "normal": somente no mês atual
* Retrieve "historico": todos os meses