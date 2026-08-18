import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:recipe_catalog/favorites_provider.dart';
import 'recipe_model.dart';

class RecipeDetailScreen extends StatelessWidget {
  final Recipe recipe;
  
  const RecipeDetailScreen({super.key, required this.recipe});

  @override
  Widget build(BuildContext context) {
    final favoritesProvider = context.watch<FavoritesProvider>();
    final isFav = favoritesProvider.isFavorite(recipe.id);

    return Scaffold(
      appBar: AppBar(
        title: Text(recipe.title),

        actions: [
          IconButton(onPressed: () {
            context.read<FavoritesProvider>().toggleFavorite(recipe.id);
          }, icon: Icon(isFav ? Icons.favorite : Icons.favorite_border))
        ],
      ),
    body: SingleChildScrollView(
      padding: const EdgeInsets.all(16),

      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          // Image.network(receita.imageUrl), // Descomente se tiver URLs
          const SizedBox(height: 10,),
          Text('Ingredientes', style: Theme.of(context).textTheme.titleLarge,),
          Text(recipe.ingredients),
          const SizedBox(height: 20,),
          Text('Modo de preparo', style: Theme.of(context).textTheme.titleLarge,),
          Text(recipe.preparationMethod),
        ],
      ),
    ),
    );
  }
}