import 'package:flutter/material.dart';

void main() {
  runApp(const CalculatorApp());
}

class CalculatorApp extends StatefulWidget {
  const CalculatorApp({super.key});

  @override
  State<StatefulWidget> createState() => _CalculatorState();
}

class _CalculatorState extends State<CalculatorApp> {
  double? _result;

  final TextEditingController _leftNumController = TextEditingController();
  final TextEditingController _rightNumController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: const Text(
            'CALCULATOR',
            style: TextStyle(fontWeight: FontWeight.bold),
          ),
          backgroundColor: Colors.lightBlue,
          centerTitle: true,
        ),
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Row(
                children: [
                  _numberField(_leftNumController),
                  const SizedBox(width: 12),
                  _numberField(_rightNumController),
                ],
              ),
              const SizedBox(height: 16),
              Text('Resultado: $_result'),
              const SizedBox(height: 16),
              Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  ElevatedButton(
                    onPressed: () => _setResult(
                      _add(
                        _getNum(_leftNumController),
                        _getNum(_rightNumController),
                      ),
                    ),
                    child: const Text('+'),
                  ),
                  const SizedBox(width: 8),
                  ElevatedButton(
                    onPressed: () => _setResult(
                      _subtract(
                        _getNum(_leftNumController),
                        _getNum(_rightNumController),
                      ),
                    ),
                    child: const Text('-'),
                  ),
                  const SizedBox(width: 8),
                  ElevatedButton(
                    onPressed: () => _setResult(
                      _multiply(
                        _getNum(_leftNumController),
                        _getNum(_rightNumController),
                      ),
                    ),
                    child: const Text('x'),
                  ),
                  const SizedBox(width: 8),
                  ElevatedButton(
                    onPressed: () => _setResult(
                      _divide(
                        _getNum(_leftNumController),
                        _getNum(_rightNumController),
                      ),
                    ),
                    child: const Text('/'),
                  ),
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }

  double _add(double left, double right) => left + right;

  double _subtract(double left, double right) => left - right;

  double _multiply(double left, double right) => left * right;

  double _divide(double dividend, double divisor) {
    if (divisor == 0) {
      return 1;
    }

    return dividend / divisor;
  }

  Widget _numberField(TextEditingController controller) {
    return TextField(
      controller: controller,
      keyboardType: TextInputType.number,
      decoration: const InputDecoration(
        border: OutlineInputBorder(),
        labelText: 'Digite um número',
      ),
    );
  }

  double _getNum(TextEditingController controller) {
    return double.tryParse(controller.text) ?? 0;
  }

  void _setResult(double result) {
    setState(() {
      _result = result;
    });
  }
}
