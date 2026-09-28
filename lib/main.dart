import 'package:flutter/material.dart';

import 'screens/home_screen.dart';

void main() {
  runApp(const MovieWatchlistApp());
}

class MovieWatchlistApp extends StatelessWidget {
  const MovieWatchlistApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Movie Watchlist',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        useMaterial3: true,
        colorScheme: ColorScheme.fromSeed(
          seedColor: const Color(0xFF1F2A78),
          brightness: Brightness.light,
        ),
        scaffoldBackgroundColor: const Color(0xFFF5F7FF),
      ),
      home: const HomeScreen(),
    );
  }
}
