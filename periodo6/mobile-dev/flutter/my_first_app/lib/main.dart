import 'package:flutter/material.dart';

// A função main() é o ponto de entrada de todo app Flutter.

void main() {
  // runApp() "infla" o widget principal e o exibe na tela.

  runApp(const ProfileApp());
}

// Nosso widget principal. Ele é Stateless porque, por enquanto, não guarda nenhum estado.

class ProfileApp extends StatefulWidget {
  const ProfileApp({super.key});

  @override
  State<ProfileApp> createState() => _ProfileAppState();
}

class _ProfileAppState extends State<ProfileApp> {
  String _displayedName = 'Nome do Usuário';

  // 1. Crie o controller.

  final TextEditingController _nameController = TextEditingController();

  void _updateName() {
    // setState() diz ao Flutter: "O estado mudou, por favor, reconstrua a UI!"

    setState(() {
      // Lê o texto do controller e atualiza a variável de estado.

      _displayedName = _nameController.text;
    });
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: const Text('Cartão de Perfil Interativo'),

          backgroundColor: Colors.blueGrey,
        ),

        body: Container(
          padding: const EdgeInsets.all(16.0),

          alignment: Alignment.center,

          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,

            children: [
              Text(_displayedName),

              const Text('Desenvolvedor(a) Flutter em treinamento'),

              // Adicione um espaçamento
              const SizedBox(height: 30),

              // O widget para entrada de texto.
              TextField(
                controller:
                    _nameController, // Conecta o controller ao TextField.

                decoration: const InputDecoration(
                  border: OutlineInputBorder(),

                  labelText: 'Digite seu nome',
                ),
              ),
              const SizedBox(height: 20),

              ElevatedButton(
                onPressed: _updateName,
                child: const Text('Atualizar o nome'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
