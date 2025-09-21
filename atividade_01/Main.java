public class Main {
    public static void main(String[] args) {
        MaquinaDeLerArquivos maquinaTopada = new MaquinaDeLerArquivos();
        maquinaTopada.debugMode = true;
        maquinaTopada.lerArquivo("atividade_01" + java.io.File.separator + "giga.txt");
        // maquinaTopada.lerArquivo("atividade_01\\exemplo.txt");
        //classe para path feature


    }
}