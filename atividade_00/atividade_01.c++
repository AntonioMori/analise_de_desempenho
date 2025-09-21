#include <iostream> // Para entrada e saída (cin, cout)
#include <vector>   // Para usar arrays dinâmicos
#include <string>   // Para trabalhar com strings
#include <fstream> // Para manipulação de arquivos

using namespace std; // Para não precisar escrever std:: sempre

// cout server para imprimir na tela
// cin server para ler o que o usuário digita

int main()
{

    //REQUISITO 1
    int n;
    cout << "Digite um número inteiro N > 0: ";

    if (!(cin >> n)) // se a entrada falhar em converter o input para o tipo int que é definido na definição da variável n então ele
    // entra no scope do if e portanto vai dar uma mensagem de falha senão ele passa para a próxima etapa
    {
        cout << "Erro: Digite apenas números!" << endl;
        return 1;
    }
    if (n <= 0) // se n for menor ou igual a 0 então entra no scope do if e dá a mensagem de erro senão ele passa para a próxima etapa
    {
        cout << "Erro: N deve ser maior que 0!" << endl;
        return 1;
    }
 
    //REQUISITO 2
    int contadorPrimos = 0;
    vector<int> primosEncontrados(n);

    for (int i = 2; i <= n; ++i) {
        //para cada numero de 2 até n verifica se é primo, o número 1 por definição não é primo

        bool isPrime = true;

        for (int j = 2; j * j <= i; ++j) { // verifica se i é divisível por algum número de 2 até a raiz quadrada de i
            //SE i for divisível por j então i não é primo
            if (i % j == 0) {
                isPrime = false;
                break;
            }
        }
        if (isPrime) {
            // acessa a posição atual no array e define o valor como o i atual (no caso já confirmamos que é primo)

            primosEncontrados[contadorPrimos] = i; // armazena o número primo encontrado no array
            ++contadorPrimos;
        }
    }

    //REQUISITO 3
    cout << "Quantidade de números primos entre 1 e " << n << ": " << contadorPrimos << endl;

    ofstream arquivo("primos.txt");
    if (!arquivo) {
        cout << "Erro ao abrir o arquivo para escrita!" << endl;
        return 1;
    }

    arquivo << "Números primos encontrados: ";
    for (int k = 0; k < contadorPrimos; ++k) {
        arquivo << primosEncontrados[k] << " ";
    }
    arquivo << endl;
    arquivo << "valor de n: " << n << endl;
    arquivo.close();

    cout << "Números primos salvos em primos.txt" << endl;


    // Seu código vai aqui
    return 0; // Indica que o programa terminou com sucesso
}