# INNER JOIN vs LEFT JOIN

## INNER JOIN (Intersecção - só o que combina)

**Quando usar:** Quando você quer APENAS os registros que **TÊM correspondência** nas duas tabelas.

**Sintaxe:**
```sql
SELECT coluna1, coluna2
FROM TabelaA
INNER JOIN TabelaB ON TabelaA.id = TabelaB.id;
```

**Exemplo visual:**
```
Usuario              Emprestimo
---------            -----------
1 | João       ←──   ID_Usuario: 1  ✅ Combina
2 | Maria      ←──   ID_Usuario: 2  ✅ Combina
3 | Pedro            (sem empréstimo)
4 | Ana              (sem empréstimo)
```

**INNER JOIN retorna:**
```
João   (tem empréstimo)
Maria  (tem empréstimo)
```

---

## LEFT JOIN (Tudo da esquerda + o que combina da direita)

**Quando usar:** Quando você quer TODOS os registros da **primeira tabela** (esquerda), mesmo que não tenham correspondência na segunda.

**Sintaxe:**
```sql
SELECT coluna1, coluna2
FROM TabelaA
LEFT JOIN TabelaB ON TabelaA.id = TabelaB.id;
```

**LEFT JOIN retorna:**
```
João   | ID_Emprestimo: 1
Maria  | ID_Emprestimo: 2
Pedro  | NULL  ← Não tem empréstimo
Ana    | NULL  ← Não tem empréstimo
```

---

## Exemplos práticos:

### 1️⃣ Usuários que **TÊM** empréstimos (INNER JOIN)
```sql
SELECT Usuario.Nome
FROM Usuario
INNER JOIN Emprestimo ON Usuario.ID_Usuario = Emprestimo.ID_Usuario;
```
**Retorna:** João, Maria

---

### 2️⃣ Usuários que **NÃO TÊM** empréstimos (LEFT JOIN + IS NULL)
```sql
SELECT Usuario.Nome
FROM Usuario
LEFT JOIN Emprestimo ON Usuario.ID_Usuario = Emprestimo.ID_Usuario
WHERE Emprestimo.ID_Usuario IS NULL;
```
**Retorna:** Pedro, Ana

**Por que funciona:**
- LEFT JOIN traz TODOS os usuários
- Onde não tem empréstimo, `Emprestimo.ID_Usuario` fica NULL
- WHERE IS NULL filtra só os que têm NULL (sem empréstimo)

---

### 3️⃣ TODOS os usuários (com ou sem empréstimo)
```sql
SELECT Usuario.Nome, Emprestimo.ID_Emprestimo
FROM Usuario
LEFT JOIN Emprestimo ON Usuario.ID_Usuario = Emprestimo.ID_Usuario;
```
**Retorna:**
```
João  | 1
Maria | 2
Pedro | NULL
Ana   | NULL
```

---

## Resumo visual:

```
INNER JOIN          LEFT JOIN
    ╔═══╗               ╔═══╗
    ║ A ║               ║ A ║
    ╠═══╣               ╠═══╣══╗
    ║ B ║               ║ B ║  ║
    ╚═══╝               ╚═══╩══╝
   Só o que            Tudo de A
   combina             + o que combina de B
```

---

## Regra de ouro:

| Você quer... | Use... |
|--------------|--------|
| **Apenas** registros que combinam | **INNER JOIN** |
| **Todos** da primeira tabela, mesmo sem correspondência | **LEFT JOIN** |
| Encontrar registros **sem** correspondência | **LEFT JOIN + WHERE IS NULL** |

---

## Exemplo completo: Usuários sem empréstimos

```sql
-- Pegar todos os usuários que NÃO têm empréstimos
SELECT Usuario.Nome, Usuario.Email
FROM Usuario
LEFT JOIN Emprestimo ON Usuario.ID_Usuario = Emprestimo.ID_Usuario
WHERE Emprestimo.ID_Usuario IS NULL;
```

**Explicação passo a passo:**
1. `FROM Usuario` → Começa pela tabela Usuario (TODOS os usuários)
2. `LEFT JOIN Emprestimo` → Junta com Emprestimo (se existir)
3. `ON Usuario.ID_Usuario = Emprestimo.ID_Usuario` → Condição de junção
4. `WHERE Emprestimo.ID_Usuario IS NULL` → Filtra só os que têm NULL (sem empréstimo)

---

## Outros tipos de JOIN (menos usados):

### RIGHT JOIN
Igual ao LEFT JOIN, mas inverte: pega TODOS da tabela da direita.

```sql
SELECT *
FROM TabelaA
RIGHT JOIN TabelaB ON TabelaA.id = TabelaB.id;
```
(Na prática, é melhor usar LEFT JOIN e inverter a ordem das tabelas)

### FULL OUTER JOIN
Pega TUDO das duas tabelas, com ou sem correspondência.
(Não é suportado nativamente no SQLite)

---

**Dica:** Na maioria dos casos, você vai usar INNER JOIN (90% das vezes) ou LEFT JOIN (10% das vezes). Os outros são raros!
