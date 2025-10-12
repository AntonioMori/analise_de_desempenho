-- Header/Título
SELECT 'hero' AS component,
       'Atividade 04 - Análise de Desempenho' AS title,
       'Sistema de Gerenciamento de Biblioteca' AS description,
       'primary' AS color;

-- Menu de navegação
SELECT 'list' AS component,
       'Operações Disponíveis' AS title;

SELECT 'Criar Tabelas' AS title,
       'criacao.sql' AS link,
       'Criar estrutura do banco de dados' AS description;

SELECT 'Inserir Dados' AS title,
       'insercao.sql' AS link,
       'Adicionar registros nas tabelas' AS description;

SELECT 'Consultas' AS title,
       'buscas.sql' AS link,
       'Executar queries otimizadas no banco' AS description;

-- Seção de informações
SELECT 'alert' AS component,
       'Como Usar' AS title,
       'Execute os arquivos na ordem: 1) Criar Tabelas, 2) Inserir Dados, 3) Consultas' AS description,
       'info' AS color;

-- Estatísticas do banco (se já existirem dados)
SELECT 'card' AS component,
       'Estatísticas do Sistema' AS title;

SELECT
    'Tabelas' AS title,
    COUNT(*) AS value,
    'Total de tabelas criadas' AS description
FROM sqlite_master
WHERE type='table' AND name NOT LIKE 'sqlite_%';

