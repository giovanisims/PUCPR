package com.example.javaapp;

import android.app.Service;
import android.content.Intent;
import android.os.IBinder;
import android.util.Log;

public class MyService extends Service {

    @Override
    public int onStartCommand(Intent intent, int flags, int startId){

            Log.d("AppCom", "Started the Service");

            double primeiro = intent.getDoubleExtra("primeiro", 0.0);
            double segundo = intent.getDoubleExtra("segundo", 0.0);

            Log.d("AppCom", "First Value: " + primeiro);
            Log.d("AppCom", "Second Value: " + segundo);

            double result = 0;
            for (int i = 0; i < segundo; i++) {
                result += primeiro;
            }

            Log.d("AppCom", "Result: " + result);

            Intent BroadCastIntent = new Intent("CALCULATION_FINISHED");
            sendBroadcast(BroadCastIntent);

            Log.d("AppCom", "Stopped the Service");
            stopSelf();

            return START_NOT_STICKY;
    }

    @Override
    public IBinder onBind(Intent intent) {
        // TODO: Return the communication channel to the service.
        throw new UnsupportedOperationException("Not yet implemented");
    }

}