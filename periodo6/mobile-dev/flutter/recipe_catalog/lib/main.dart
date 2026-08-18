import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:recipe_catalog/favorites_provider.dart';
import 'package:recipe_catalog/favorites_screen.dart';
import 'package:recipe_catalog/recipe_detail_screen.dart';
import 'package:recipe_catalog/recipe_model.dart';

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(title: 'Recipe Catalog', home: ListRecipesScreen());
  }
}

class ListRecipesScreen extends StatelessWidget {
  const ListRecipesScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Minhas receitas'),
        actions: [
          IconButton(
            icon: const Icon(Icons.favorite),
            onPressed: () {
              Navigator.push(
                context,
                MaterialPageRoute(
                  builder: (context) {
                    return ListFavoriteRecipesScreen(
                      recipes: recipes,
                    );
                  },
                ),
              );
            },
          ),
        ],
      ),

      body: ListView.builder(
        itemCount: recipes.length,

        itemBuilder: (ctx, index) {
          final recipe = recipes[index];

          return Card(
            margin: const EdgeInsets.all(10),

            child: ListTile(
              leading: CircleAvatar(
                // backgroundImage: NetworkImage(receita.imageUrl), // Descomente se tiver URLs
                child: Text(recipe.id.toUpperCase()),
              ),
              title: Text(recipe.title),
              subtitle: const Text('Clique para ver detalhes'),
              onTap: () => {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) => RecipeDetailScreen(recipe: recipe),
                  ),
                ),
              },
              trailing: Consumer<FavoritesProvider>(
                builder: (ctx, favoritesProvider, child) {
                  final isFav = favoritesProvider.isFavorite(recipe.id);

                  return IconButton(
                    onPressed: () =>
                        favoritesProvider.toggleFavorite(recipe.id),
                    icon: Icon(
                      isFav ? Icons.favorite : Icons.favorite_border,
                      color: Colors.red,
                    ),
                  );
                },
              ),
            ),
          );
        },
      ),
    );
  }
}

void main() {
  runApp(
    ChangeNotifierProvider(
      create: (context) => FavoritesProvider(),
      child: const MyApp(),
    ),
  );
}

final List<Recipe> recipes = [
  Recipe(
    id: 'r1',
    title: 'Bolo de Chocolate',
    ingredients: 'Farinha, ovos, chocolate...',
    preparationMethod: 'Misture tudo e asse.',
    imageURL: 'URL_DA_IMAGEM_BOLO',
  ),

  Recipe(
    id: 'r2',
    title: 'Macarrão à Carbonara',
    ingredients: 'Massa, ovos, bacon...',
    preparationMethod: 'Cozinhe a massa e misture.',
    imageURL: 'URL_DA_IMAGEM_MACARRAO',
  ),
];
