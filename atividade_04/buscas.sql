-- BUSCAS OTIMIZADAS - Sistema de Biblioteca

-- Título da página
SELECT 'hero' AS component,
       'Consultas Otimizadas' AS title,
       'Queries melhoradas com JOINs explícitos e índices' AS description;

-- Seção de Índices para Otimização
SELECT 'alert' AS component,
       'Índices Criados para Otimização' AS title,
       'Os seguintes índices melhoram o desempenho das queries' AS description,
       'info' AS color;

-- Criar índices para otimizar as buscas
CREATE INDEX IF NOT EXISTS idx_livro_autor ON Livro(ID_Autor);
CREATE INDEX IF NOT EXISTS idx_emprestimo_livro ON Emprestimo(ID_Livro);
CREATE INDEX IF NOT EXISTS idx_emprestimo_usuario ON Emprestimo(ID_Usuario);
CREATE INDEX IF NOT EXISTS idx_livro_categoria_livro ON Livro_Categoria(ID_Livro);
CREATE INDEX IF NOT EXISTS idx_livro_categoria_cat ON Livro_Categoria(ID_Categoria);

-- ========================================
-- BUSCA 1: Livros com seus autores (OTIMIZADA)
-- ========================================
SELECT 'table' AS component,
       'Livros e Autores' AS title,
       'Query otimizada usando INNER JOIN' AS description;

SELECT
    L.Titulo AS 'Título do Livro',
    A.Nome AS 'Autor',
    L.Ano_Publicacao AS 'Ano'
FROM Livro L
INNER JOIN Autor A ON L.ID_Autor = A.ID_Autor
ORDER BY L.Ano_Publicacao DESC;

-- ========================================
-- BUSCA 2: Empréstimos ativos com detalhes (OTIMIZADA)
-- ========================================
SELECT 'table' AS component,
       'Empréstimos Ativos' AS title,
       'Livros emprestados que ainda não foram devolvidos' AS description;

SELECT
    U.Nome AS 'Usuário',
    L.Titulo AS 'Livro',
    A.Nome AS 'Autor',
    E.Data_Emprestimo AS 'Data do Empréstimo'
FROM Emprestimo E
INNER JOIN Usuario U ON E.ID_Usuario = U.ID_Usuario
INNER JOIN Livro L ON E.ID_Livro = L.ID_Livro
INNER JOIN Autor A ON L.ID_Autor = A.ID_Autor
WHERE E.Data_Devolucao IS NULL
ORDER BY E.Data_Emprestimo DESC;

-- ========================================
-- BUSCA 3: Livros por categoria (OTIMIZADA)
-- ========================================
SELECT 'table' AS component,
       'Livros por Categoria' AS title,
       'Relação completa de livros e suas categorias' AS description;

SELECT
    C.Nome AS 'Categoria',
    L.Titulo AS 'Livro',
    A.Nome AS 'Autor',
    L.Ano_Publicacao AS 'Ano'
FROM Livro_Categoria LC
INNER JOIN Livro L ON LC.ID_Livro = L.ID_Livro
INNER JOIN Categoria C ON LC.ID_Categoria = C.ID_Categoria
INNER JOIN Autor A ON L.ID_Autor = A.ID_Autor
ORDER BY C.Nome, L.Titulo;

-- ========================================
-- BUSCA 4 (NOVA): Livros mais emprestados
-- ========================================
SELECT 'table' AS component,
       'Top 10 Livros Mais Emprestados' AS title,
       'Ranking dos livros mais populares' AS description;

SELECT
    L.Titulo AS 'Livro',
    A.Nome AS 'Autor',
    COUNT(E.ID_Emprestimo) AS 'Total de Empréstimos'
FROM Livro L
INNER JOIN Autor A ON L.ID_Autor = A.ID_Autor
LEFT JOIN Emprestimo E ON L.ID_Livro = E.ID_Livro
GROUP BY L.ID_Livro, L.Titulo, A.Nome
ORDER BY COUNT(E.ID_Emprestimo) DESC
LIMIT 10;

-- ========================================
-- BUSCA 5 (NOVA): Autores mais prolíficos
-- ========================================
SELECT 'table' AS component,
       'Autores com Mais Livros' AS title,
       'Ranking de autores por quantidade de obras' AS description;

SELECT
    A.Nome AS 'Autor',
    A.Data_Nascimento AS 'Data de Nascimento',
    COUNT(L.ID_Livro) AS 'Quantidade de Livros'
FROM Autor A
LEFT JOIN Livro L ON A.ID_Autor = L.ID_Autor
GROUP BY A.ID_Autor, A.Nome, A.Data_Nascimento
HAVING COUNT(L.ID_Livro) > 0
ORDER BY COUNT(L.ID_Livro) DESC;

-- ========================================
-- BUSCA 6 (NOVA): Usuários mais ativos
-- ========================================
SELECT 'table' AS component,
       'Usuários Mais Ativos' AS title,
       'Ranking de usuários por número de empréstimos' AS description;

SELECT
    U.Nome AS 'Usuário',
    U.Email AS 'Email',
    COUNT(E.ID_Emprestimo) AS 'Total de Empréstimos',
    SUM(CASE WHEN E.Data_Devolucao IS NULL THEN 1 ELSE 0 END) AS 'Empréstimos Ativos'
FROM Usuario U
LEFT JOIN Emprestimo E ON U.ID_Usuario = E.ID_Usuario
GROUP BY U.ID_Usuario, U.Nome, U.Email
ORDER BY COUNT(E.ID_Emprestimo) DESC;

-- ========================================
-- BUSCA 7 (NOVA): Livros por década de publicação
-- ========================================
SELECT 'table' AS component,
       'Livros por Década' AS title,
       'Distribuição temporal das obras' AS description;

SELECT
    (L.Ano_Publicacao / 10) * 10 AS 'Década',
    COUNT(*) AS 'Quantidade de Livros',
    GROUP_CONCAT(L.Titulo, ', ') AS 'Livros'
FROM Livro L
GROUP BY (L.Ano_Publicacao / 10) * 10
ORDER BY (L.Ano_Publicacao / 10) * 10;

-- ========================================
-- BUSCA 8 (NOVA): Categorias mais populares
-- ========================================
SELECT 'table' AS component,
       'Categorias Mais Populares' AS title,
       'Ranking de categorias por quantidade de livros' AS description;

SELECT
    C.Nome AS 'Categoria',
    COUNT(LC.ID_Livro) AS 'Quantidade de Livros'
FROM Categoria C
LEFT JOIN Livro_Categoria LC ON C.ID_Categoria = LC.ID_Categoria
GROUP BY C.ID_Categoria, C.Nome
ORDER BY COUNT(LC.ID_Livro) DESC;

-- Botão para voltar
SELECT 'button' AS component;
SELECT 'Voltar ao Início' AS title, 'index.sql' AS link;
