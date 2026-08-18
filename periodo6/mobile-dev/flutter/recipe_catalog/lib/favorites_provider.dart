import 'package:flutter/material.dart';

class FavoritesProvider extends ChangeNotifier {
  final List<String> _favoriteRecipesIds = [];

  List<String> get favoriteRecipesIds => _favoriteRecipesIds;

  bool isFavorite(String id) {
    return favoriteRecipesIds.contains(id);
  }

  void toggleFavorite(String id) {

    if (isFavorite(id)) {
      favoriteRecipesIds.remove(id);
    } else {
      favoriteRecipesIds.add(id);
    }

    notifyListeners();
  }
}