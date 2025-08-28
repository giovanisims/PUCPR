package com.example.javaapp;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.util.Log;
import android.widget.Button;

public class MyReceiver extends BroadcastReceiver {

    private final Button btnConsultar;
    public MyReceiver(Button btnConsultar) {
        this.btnConsultar = btnConsultar;
    }

    @Override
    public void onReceive(Context context, Intent intent) {
        Log.d("App Com", "Received intent" + intent.getAction());

        btnConsultar.setEnabled(true);
    }
}