package com.example.javaapp;

import android.app.Service;
import android.content.ContentValues;
import android.content.Intent;
import android.database.sqlite.SQLiteDatabase;
import android.os.IBinder;
import android.util.Log;

public class MyService extends Service {

    /**
     * Método chamado quando o serviço é iniciado.
     * Os parâmetros "primeiro" e "segundo" são recebidos via intent e usados para o cálculo.
     * Após a conclusão, é enviado um broadcast e o serviço é finalizado.
     * @param intent  intent que inicia o serviço, contendo os dados para o cálculo
     * @param flags   flags de controle (não usados neste exemplo)
     * @param startId identificador da instância do serviço
     * @return        START_NOT_STICKY indica que o serviço não será recriado automaticamente
     */
    @Override
    public int onStartCommand(Intent intent, int flags, int startId) {

        // Recupera os parâmetros da intent
        double primeiro = intent.getDoubleExtra("primeiro", 0.0);
        double segundo = intent.getDoubleExtra("segundo", 0.0);

        // Executa o processamento em uma nova thread para não travar a UI
        new Thread(() -> {
            try {
                // Simula um delay de 2 segundos
                Thread.sleep(2000);

                // Simula um cálculo de multiplicação (soma repetida)
                double resultado = 0;
                for (int i = 0; i < segundo; i++) {
                    resultado += primeiro;
                }

                // Grava o resultado no banco de dados SQLite
                gravarResultadoNoBanco((int) resultado);

                // Envia um broadcast indicando que o cálculo foi finalizado
                Intent broadcastIntent = new Intent("CALCULO_FINALIZADO");
                sendBroadcast(broadcastIntent);

                // Registra no log
                Log.d("AppVazio", "Resultado: " + resultado);

                // Finaliza o serviço explicitamente
                stopSelf();

            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
        }).start();

        // Indica que o serviço não deve ser recriado automaticamente se for finalizado pelo sistema
        return START_NOT_STICKY;
    }

    /**
     * Método obrigatório para serviços, usado apenas em serviços ligados (bind).
     * Como não usamos bind neste exemplo, retorna null.
     */
    @Override
    public IBinder onBind(Intent intent) {
        return null;
    }

    /**
     * Grava o resultado do cálculo na tabela "resultados" do banco de dados local.
     * @param resultado valor numérico a ser salvo
     */
    private void gravarResultadoNoBanco(int resultado) {
        DBHelper helper = new DBHelper(this);
        SQLiteDatabase db = helper.getWritableDatabase();
        ContentValues values = new ContentValues();
        values.put("resultado", resultado);
        db.insert("resultados", null, values);
        db.close();
    }
}
