const path = require('path');
const MaquinaDeLerArquivos = require('./MaquinaDeLerArquivos.js');

function main() {
    
    const maquinaTopada = new MaquinaDeLerArquivos();
    maquinaTopada.debugMode = false;

    // Usar o separador de arquivo apropriado para o sistema operacional
    const scriptDir = __dirname;
    const arquivo = path.join(scriptDir, "arq-novo.txt");
    console.log(`Lendo arquivo: ${arquivo}`);
    maquinaTopada.lerArquivo(arquivo);
}

if (require.main === module) {
    main();
}