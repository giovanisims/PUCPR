import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:recipe_catalog/favorites_provider.dart';
import 'package:recipe_catalog/recipe_detail_screen.dart';
import 'package:recipe_catalog/recipe_model.dart';

class ListFavoriteRecipesScreen extends StatelessWidget {
  final List<Recipe> recipes;

  const ListFavoriteRecipesScreen({super.key, required this.recipes});

  @override
  Widget build(BuildContext context) {
    final favoritesProvider = context.watch<FavoritesProvider>();

    final favoriteRecipes = recipes
        .where(
          (recipe) => favoritesProvider.favoriteRecipesIds.contains(recipe.id),
        )
        .toList();

    return Scaffold(
      appBar: AppBar(title: const Text('Minhas receitas favoritas')),
      body: favoriteRecipes.isEmpty
          ? const Center(child: Text('Você ainda não tem receitas favoritas.'))
          : ListView.builder(
              itemCount: favoriteRecipes.length,
              itemBuilder: (ctx, index) {
                final recipe = favoriteRecipes[index];

                return Card(
                  margin: const EdgeInsets.all(10),
                  child: ListTile(
                    leading: CircleAvatar(
                      child: Text(recipe.id.toUpperCase()),
                    ),
                    title: Text(recipe.title),
                    subtitle: const Text('Clique para ver detalhes'),
                    onTap: () {
                      Navigator.push(
                        context,
                        MaterialPageRoute(
                          builder: (context) {
                            return RecipeDetailScreen(recipe: recipe);
                          },
                        ),
                      );
                    },
                    trailing: IconButton(
                      onPressed: () {
                        favoritesProvider.toggleFavorite(recipe.id);
                      },
                      icon: const Icon(Icons.favorite, color: Colors.red),
                    ),
                  ),
                );
              },
            ),
    );
  }
}
