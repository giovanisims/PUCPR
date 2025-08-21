package com.example.javaapp;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class MyActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_my);

        Button btnIniciar = findViewById(R.id.btnIniciar);
        Button btnConsultar = findViewById(R.id.btnConsultar);

        EditText edtPrimeiro = findViewById(R.id.edtPrimeiro);
        EditText edtSegundo = findViewById(R.id.edtSegundo);

        btnIniciar.setOnClickListener(v -> {
            double primeiro = Double.parseDouble(edtPrimeiro.getText().toString());
            double segundo = Double.parseDouble(edtSegundo.getText().toString());

            Intent intent = new Intent(this, MyService.class);
            intent.putExtra("primeiro", primeiro);
            intent.putExtra("segundo", segundo);

            startService(intent);

            Toast.makeText(this, "Clicou", Toast.LENGTH_LONG).show();

        });
        btnConsultar.setOnClickListener(v -> {
            Intent intent = new Intent(this, SecondActivity.class);
            startActivity(intent);
        });
    }
}
