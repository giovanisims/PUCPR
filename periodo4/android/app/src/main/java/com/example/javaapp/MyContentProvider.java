package com.example.javaapp;

import android.content.ContentProvider;
import android.content.ContentValues;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.net.Uri;

public class MyContentProvider extends ContentProvider {

    // Autoridade do provider, deve estar registrada no AndroidManifest.xml
    private static final String AUTHORITY = "com.example.javaapp";

    // Nome da tabela a ser acessada
    private static final String TABLE = "resultados";

    // URI de acesso público à tabela, usada por outras partes da aplicação
    public static final Uri CONTENT_URI = Uri.parse("content://" + AUTHORITY + "/" + TABLE);

    // Referência ao banco de dados SQLite
    private SQLiteDatabase db;

    /**
     * Método chamado quando o ContentProvider é iniciado pela primeira vez.
     * Abre conexão com o banco de dados para leitura (modo readonly).
     * @return true se o banco foi inicializado com sucesso.
     */
    @Override
    public boolean onCreate() {
        DBHelper helper = new DBHelper(getContext());
        db = helper.getReadableDatabase(); // Abre banco somente leitura
        return true;
    }

    /**
     * Método principal de consulta de dados do ContentProvider.
     * Utiliza o método query do SQLiteDatabase para retornar os registros solicitados.
     *
     * @param uri URI solicitada (deve bater com CONTENT_URI)
     * @param projection Colunas desejadas (null = todas)
     * @param selection Cláusula WHERE
     * @param selectionArgs Argumentos para o WHERE
     * @param sortOrder Ordenação (ex: "_id DESC")
     * @return Cursor com os dados encontrados
     */
    @Override
    public Cursor query(Uri uri, String[] projection, String selection, String[] selectionArgs, String sortOrder) {
        return db.query(TABLE, projection, selection, selectionArgs, null, null, sortOrder);
    }

    // Métodos abaixo não são implementados, pois o provider é somente leitura.
    @Override
    public String getType(Uri uri) {
        return null; // Não implementado porque não há tipos MIME específicos definidos
    }

    @Override
    public Uri insert(Uri uri, ContentValues values) {
        return null; // Operação de inserção não suportada
    }

    @Override
    public int delete(Uri uri, String selection, String[] selectionArgs) {
        return 0; // Operação de exclusão não suportada
    }

    @Override
    public int update(Uri uri, ContentValues values, String selection, String[] selectionArgs) {
        return 0; // Operação de atualização não suportada
    }
}
