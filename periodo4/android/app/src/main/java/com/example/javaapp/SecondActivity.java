package com.example.javaapp;

import android.database.Cursor;
import android.os.Bundle;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class SecondActivity extends AppCompatActivity {

    /**
     * Método chamado ao criar a activity. Configura a interface gráfica e
     * realiza a consulta ao ContentProvider para exibir o último resultado salvo.
     * @param savedInstanceState estado salvo anteriormente, se houver (não usado aqui)
     */
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_second);

        // Referência para o TextView onde será exibido o resultado
        TextView txtResultado = findViewById(R.id.txtResultado);

        // Consulta ao ContentProvider, solicitando a última linha da tabela "resultados"
        Cursor cursor = getContentResolver().query(
                MyContentProvider.CONTENT_URI,               // URI do ContentProvider
                new String[]{"resultado"},             // Colunas desejadas
                null, null,                            // Sem cláusulas WHERE ou parâmetros
                "_id DESC LIMIT 1");                   // Ordena por ID decrescente, pegando o último resultado

        // Se encontrou algum resultado
        if (cursor != null && cursor.moveToFirst()) {
            int resultado = cursor.getInt(0); // Recupera o valor da primeira (e única) coluna
            txtResultado.setText("Resultado: " + resultado); // Exibe no TextView
            cursor.close(); // Fecha o cursor para liberar recursos
        }
    }
}
