# Sistema-de-Estoque-e-Vendas
Projeto 1 da matéria de Estrutura de dados Objetivo Construir um sistema de linha de comando para controlar produtos, vendas e relatorios. O projeto deve aplicar conteudos das secoes 2 a 5 (Python basico, Big-O, vetores nao ordenados e vetores ordenados).

# Projeto 1 - Sistema de Estoque e Vendas (Secao 2 a 5)

## Objetivo
Construir um sistema de linha de comando para controlar produtos, vendas e relatorios. O projeto deve aplicar conteudos das secoes 2 a 5 (Python basico, Big-O, vetores nao ordenados e vetores ordenados).

## Escopo do sistema
- Cadastro de produtos com codigo, nome, categoria, preco e quantidade.
- Registro de vendas e atualizacao de estoque.
- Relatorios por categoria, menor/maior preco e produtos com baixo estoque.

## Requisitos funcionais (obrigatorios)
1. Cadastrar produto (codigo unico).
2. Editar produto (nome, preco, quantidade, categoria).
3. Remover produto pelo codigo.
4. Buscar produto por codigo (busca binaria em vetor ordenado por codigo).
5. Buscar produtos por nome (busca linear em vetor nao ordenado).
6. Registrar venda (reduz estoque, valida quantidade).
7. Listar produtos ordenados por codigo (vetor ordenado).
8. Listar produtos por categoria (filtro).
9. Relatorio de estoque baixo (quantidade < limite configuravel).
10. Salvar e carregar dados em arquivo (CSV ou JSON).

## Requisitos nao funcionais (obrigatorios)
- Interface por terminal com menu claro.
- Dados persistidos em arquivo.
- Codigo organizado em modulos e funcoes.
- Tratamento de erros de entrada (numero, texto, vazio).
- Complexidade explicada: justificar uso de busca linear e binaria.

## Requisitos nao funcionais (nao obrigatorios, mas recomendados)
- Logs simples de operacoes (data/hora).
- Mensagens amigaveis ao usuario.
- Paginacao simples na listagem.

## Regras de negocio
- Nao permitir codigo duplicado.
- Nao permitir venda com estoque insuficiente.
- Preco deve ser positivo.
- Quantidade nao pode ser negativa.

## Estrutura sugerida (arquivos)
- main.py (menu e fluxo)
- produto.py (classe/estrutura e validacoes)
- estoque.py (operacoes de cadastro e busca)
- arquivos.py (salvar/carregar)

## Requisitos de dados
- Vetor nao ordenado para cadastro inicial e buscas por nome.
- Vetor ordenado por codigo para busca binaria.
- Operacoes devem manter o vetor ordenado ao inserir/remover.

## Versionamento e boas praticas (obrigatorio)
- Usar Git com commits pequenos e mensagens claras.
- Criar repositorio no GitHub e enviar o codigo.
- Escrever README com como executar e exemplos.
- Seguir PEP 8 (nomes, identacao, organizacao).
- Usar funcoes pequenas e responsaveis.
- Evitar codigo duplicado.

## Entregaveis
- Codigo fonte completo.
- Arquivo de dados de exemplo.
- README com instrucoes.
- Relatorio curto explicando escolhas de busca e ordenacao.

## Criterios de avaliacao
- Funciona sem erros.
- Atende todos os requisitos obrigatorios.
- Usa busca binaria em vetor ordenado corretamente.
- Persistencia de dados funcionando.
- Codigo limpo e organizado.