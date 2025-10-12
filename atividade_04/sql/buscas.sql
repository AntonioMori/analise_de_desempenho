-- ==============================================================================
-- BUSCA 1: Listar todos os livros com seus autores
-- ==============================================================================

-- ANTES (NÃO OTIMIZADO):
-- Problema: Usa sintaxe antiga (FROM Autor, Livro WHERE)
-- O banco cria um produto cartesiano (todos autores × todos livros)
-- e depois filtra, desperdiçando processamento
/*
SELECT Autor.Nome, Livro.Titulo
FROM Autor, Livro
WHERE Autor.ID_Autor = Livro.ID_Autor;
*/

-- DEPOIS (OTIMIZADO):
-- Solução: Usa INNER JOIN moderno
-- O banco já sabe que deve juntar apenas registros que combinam
-- Requer índice em Livro.ID_Autor para máxima performance
SELECT Autor.Nome, Livro.Titulo
FROM Autor
INNER JOIN Livro ON Autor.ID_Autor = Livro.ID_Autor;


-- ==============================================================================
-- BUSCA 2: Listar todos os empréstimos e os usuários correspondentes
-- ==============================================================================

-- ANTES (NÃO OTIMIZADO):
-- Problema: Sintaxe antiga + sem índice em Emprestimo.ID_Usuario
-- Para cada empréstimo, varre TODA a tabela Usuario
/*
SELECT Emprestimo.ID_Emprestimo, Usuario.Nome
FROM Emprestimo, Usuario
WHERE Emprestimo.ID_Usuario = Usuario.ID_Usuario;
*/

-- DEPOIS (OTIMIZADO):
-- Solução: INNER JOIN + índice em Emprestimo.ID_Usuario
-- O banco usa o índice para encontrar diretamente o usuário de cada empréstimo
SELECT Emprestimo.ID_Emprestimo, Usuario.Nome
FROM Emprestimo
INNER JOIN Usuario ON Emprestimo.ID_Usuario = Usuario.ID_Usuario;


-- ==============================================================================
-- BUSCA 3: Listar todos os livros e suas categorias
-- ==============================================================================

-- ANTES (NÃO OTIMIZADO):
-- Problema: 3 tabelas com sintaxe antiga
-- Cria produto cartesiano de 3 tabelas antes de filtrar
-- Exemplo: 1000 livros × 500 categorias × 2000 relações = muito processamento
/*
SELECT Livro.Titulo, Categoria.Nome
FROM Livro, Livro_Categoria, Categoria
WHERE Livro.ID_Livro = Livro_Categoria.ID_Livro
AND Livro_Categoria.ID_Categoria = Categoria.ID_Categoria;
*/

-- DEPOIS (OTIMIZADO):
-- Solução: Múltiplos INNER JOINs em cadeia
-- Requer índices em Livro_Categoria.ID_Livro e Livro_Categoria.ID_Categoria
-- O banco une as tabelas de forma eficiente, uma de cada vez
SELECT Livro.Titulo, Categoria.Nome
FROM Livro
INNER JOIN Livro_Categoria ON Livro.ID_Livro = Livro_Categoria.ID_Livro
INNER JOIN Categoria ON Livro_Categoria.ID_Categoria = Categoria.ID_Categoria;


-- ==============================================================================
-- BUSCA 4: Listar todos os livros emprestados
-- ==============================================================================

-- ANTES (NÃO OTIMIZADO):
-- Problema: 3 tabelas com sintaxe antiga
-- Sem índices em Emprestimo.ID_Livro e Emprestimo.ID_Usuario
-- O banco faz varredura completa em múltiplas tabelas
/*
SELECT Livro.Titulo, Usuario.Nome
FROM Livro, Emprestimo, Usuario
WHERE Livro.ID_Livro = Emprestimo.ID_Livro
AND Emprestimo.ID_Usuario = Usuario.ID_Usuario;
*/

-- DEPOIS (OTIMIZADO):
-- Solução: Múltiplos INNER JOINs
-- Com índices em Emprestimo.ID_Livro e Emprestimo.ID_Usuario
-- O banco usa índices para juntar as tabelas rapidamente
SELECT Livro.Titulo, Usuario.Nome
FROM Livro
INNER JOIN Emprestimo ON Livro.ID_Livro = Emprestimo.ID_Livro
INNER JOIN Usuario ON Emprestimo.ID_Usuario = Usuario.ID_Usuario;


-- ==============================================================================
-- NOTA: Esta busca é DUPLICADA (igual à Busca 1) - pode ser removida
-- ==============================================================================

-- Listar todos os autores e seus livros publicados (DUPLICADO):
-- Esta query é idêntica à Busca 1, não precisa estar aqui
/*
SELECT Autor.Nome, Livro.Titulo
FROM Autor, Livro
WHERE Autor.ID_Autor = Livro.ID_Autor;
*/


-- ==============================================================================
-- IMPORTANTE: Para que as queries otimizadas funcionem bem, você precisa
-- criar os índices ANTES de executar as buscas.
--
-- Execute os comandos abaixo UMA VEZ (eles ficam salvos no banco):
--
-- CREATE INDEX idx_livro_autor ON Livro(ID_Autor);
-- CREATE INDEX idx_emprestimo_usuario ON Emprestimo(ID_Usuario);
-- CREATE INDEX idx_emprestimo_livro ON Emprestimo(ID_Livro);
-- CREATE INDEX idx_livro_categoria_livro ON Livro_Categoria(ID_Livro);
-- CREATE INDEX idx_livro_categoria_categoria ON Livro_Categoria(ID_Categoria);
-- ==============================================================================
