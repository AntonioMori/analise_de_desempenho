-- criacao das tabelas do banco de dados
CREATE TABLE Autor (
    ID_Autor INTEGER PRIMARY KEY,
    Nome TEXT NOT NULL,
    Data_Nascimento DATE
);

CREATE TABLE Categoria (
    ID_Categoria INTEGER PRIMARY KEY,
    Nome TEXT NOT NULL
);

CREATE TABLE Livro (
    ID_Livro INTEGER PRIMARY KEY,
    Titulo TEXT NOT NULL,
    ID_Autor INTEGER,
    Ano_Publicacao INTEGER,
    FOREIGN KEY (ID_Autor) REFERENCES Autor(ID_Autor)
);

CREATE TABLE Livro_Categoria (
    ID_Livro INTEGER,
    ID_Categoria INTEGER,
    PRIMARY KEY (ID_Livro, ID_Categoria),
    FOREIGN KEY (ID_Livro) REFERENCES Livro(ID_Livro),
    FOREIGN KEY (ID_Categoria) REFERENCES Categoria(ID_Categoria)
);

CREATE TABLE Usuario (
    ID_Usuario INTEGER PRIMARY KEY,
    Nome TEXT NOT NULL,
    Email TEXT NOT NULL
);

CREATE TABLE Emprestimo (
    ID_Emprestimo INTEGER PRIMARY KEY,
    ID_Livro INTEGER,
    ID_Usuario INTEGER,
    Data_Emprestimo DATE NOT NULL,
    Data_Devolucao DATE,
    FOREIGN KEY (ID_Livro) REFERENCES Livro(ID_Livro),
    FOREIGN KEY (ID_Usuario) REFERENCES Usuario(ID_Usuario)
);
