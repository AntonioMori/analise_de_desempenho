### **Modelo (Tabelas e suas colunas) :**

* **Livro**  
  * ID\_Livro (PK)  
  * Título  
  * Autor  
  * Ano\_Publicacao  
* **Autor**  
  * ID\_Autor (PK)  
  * Nome  
  * Data\_Nascimento  
* **Categoria**  
  * ID\_Categoria (PK)  
  * Nome  
* **Emprestimo**  
  * ID\_Emprestimo (PK)  
  * ID\_Livro (FK)  
  * ID\_Usuario (FK)  
  * Data\_Emprestimo  
  * Data\_Devolucao  
* **Usuario**  
  * ID\_Usuario (PK)  
  * Nome  
  * Email

\* PK \= primary key (chave primária)

\* FK \=  foreign key (chave estrangeira) 

### **Relações:**

* Um **Livro** pode ter um **Autor**.  
* Um **Livro** pode pertencer a uma ou mais **Categoria**s.  
* Um **Emprestimo** envolve um **Livro** e um **Usuario**.  
* Um **Usuario** pode fazer vários **Emprestimo**s.

