# Questão 4 - Banco de Dados

## Modelo Lógico Proposto

### Tabela Cliente:
- `cliente_id` (PK) - Identificador único do cliente.
- `nome` - Nome ou razão social do cliente.
- `estado_id` (FK) - Referência ao estado onde o cliente reside.

### Tabela Telefone:
- `telefone_id` (PK) - Identificador único do telefone.
- `numero` - Número de telefone.
- `cliente_id` (FK) - Referência ao cliente dono do telefone.
- `tipo_telefone_id` (FK) - Referência ao tipo de telefone.

### Tabela TipoTelefone:
- `tipo_telefone_id` (PK) - Identificador único do tipo de telefone.
- `descricao` - Descrição do tipo (Ex: Celular, Comercial, Residencial).

### Tabela Estado:
- `estado_id` (PK) - Identificador único do estado.
- `sigla` - Sigla do estado (Ex: SP, RJ).
- `nome` - Nome do estado.

## Relacionamentos:
- Um **Cliente** pode ter vários **Telefones** (1:N).
- **Telefone** se refere a um **Cliente** e a um **TipoTelefone** (N:1).
- Um **Cliente** está associado a um único **Estado** (N:1).

## Consulta SQL:

A seguinte query busca os clientes que estão no estado de São Paulo (código "SP"), retornando o código do cliente, sua razão social e os números de telefone.

```sql
SELECT 
    c.cliente_id, 
    c.nome, 
    t.numero AS telefone
FROM 
    Cliente c
JOIN 
    Telefone t ON c.cliente_id = t.cliente_id
JOIN 
    Estado e ON c.estado_id = e.estado_id
WHERE 
    e.sigla = 'SP';
