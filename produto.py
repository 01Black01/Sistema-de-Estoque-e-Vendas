class Produto:
    """Classe que representa um produto no sistema de estoque"""
    
    def __init__(self, codigo, nome, categoria, preco, quantidade, descricao=""):
        """
        Inicializa um novo produto
        
        Args:
            codigo: Identificador único do produto
            nome: Nome do produto
            categoria: Categoria do produto
            preco: Preço unitário do produto
            quantidade: Quantidade em estoque
            descricao: Descrição do produto (opcional)
        """
        self.codigo = codigo
        self.nome = nome
        self.categoria = categoria
        self.preco = float(preco)
        self.quantidade = int(quantidade)
        self.descricao = descricao
    
    def __str__(self):
        """Representação em string do produto"""
        return f"Produto(código={self.codigo}, nome='{self.nome}', categoria='{self.categoria}', preço=R${self.preco:.2f}, estoque={self.quantidade})"
    
    def __repr__(self):
        """Representação para debug"""
        return self.__str__()
    
    def adicionar_estoque(self, quantidade):
        """Adiciona quantidade ao estoque"""
        if quantidade < 0:
            raise ValueError("A quantidade não pode ser negativa")
        self.quantidade += quantidade
        return self.quantidade
    
    def remover_estoque(self, quantidade):
        """Remove quantidade do estoque"""
        if quantidade < 0:
            raise ValueError("A quantidade não pode ser negativa")
        if quantidade > self.quantidade:
            raise ValueError(f"Estoque insuficiente. Disponível: {self.quantidade}")
        self.quantidade -= quantidade
        return self.quantidade
    
    def atualizar_preco(self, novo_preco):
        """Atualiza o preço do produto"""
        if novo_preco < 0:
            raise ValueError("O preço não pode ser negativo")
        self.preco = float(novo_preco)
    
    def calcular_valor_total(self):
        """Calcula o valor total em estoque"""
        return self.preco * self.quantidade
    
    def em_falta(self):
        """Verifica se o produto está em falta"""
        return self.quantidade == 0
    
    def estoque_baixo(self, minimo=10):
        """Verifica se o estoque está abaixo do mínimo"""
        return self.quantidade < minimo
