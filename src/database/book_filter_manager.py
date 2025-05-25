"""
Book filtering and display management for the database system.
Provides intelligent filtering to prevent UI overload with hundreds of books.
"""

import random
from typing import Dict, Any, List, Optional, Set
from collections import defaultdict
from rich.console import Console

from src.database.database_manager import get_database_manager
from src.utils.genre_defaults import get_all_genres

console = Console()


class BookFilterManager:
    """
    Manages intelligent filtering and display of books from the database.
    Prevents UI overload by showing relevant subsets of books.
    """

    def __init__(self):
        """Initialize the book filter manager."""
        self.db_manager = get_database_manager()
        self.default_display_limit = 10
        self.max_books_per_genre = 3

    def get_filtered_books_for_display(self,
                                     current_genre: Optional[str] = None,
                                     max_books: int = None,
                                     include_series: bool = True) -> List[Dict[str, Any]]:
        """
        Get a filtered list of books optimized for UI display.

        Args:
            current_genre: Current genre context for related book selection
            max_books: Maximum number of books to return
            include_series: Whether to include series books

        Returns:
            List of filtered book dictionaries
        """
        if max_books is None:
            max_books = self.default_display_limit

        # Get all completed books
        all_books = self.db_manager.get_books(status="completed")

        if not all_books:
            return []

        # If we have fewer books than the limit, return all
        if len(all_books) <= max_books:
            return all_books

        # Apply intelligent filtering
        filtered_books = self._apply_intelligent_filtering(
            all_books, current_genre, max_books, include_series
        )

        return filtered_books

    def get_books_by_genre_smart(self,
                                target_genre: str,
                                max_books: int = None,
                                include_related: bool = True) -> List[Dict[str, Any]]:
        """
        Get books from a specific genre with smart related genre inclusion.

        Args:
            target_genre: The primary genre to filter by
            max_books: Maximum number of books to return
            include_related: Whether to include books from related genres

        Returns:
            List of filtered book dictionaries
        """
        if max_books is None:
            max_books = self.default_display_limit

        # Get books from target genre
        target_books = self.db_manager.get_books(genre=target_genre, status="completed")

        # If we have enough books from the target genre, return a subset
        if len(target_books) >= max_books:
            return self._select_diverse_subset(target_books, max_books)

        # If we need more books and should include related genres
        if include_related and len(target_books) < max_books:
            related_genres = self._get_related_genres(target_genre)
            remaining_slots = max_books - len(target_books)

            # Get books from related genres
            related_books = []
            for genre in related_genres:
                if remaining_slots <= 0:
                    break

                genre_books = self.db_manager.get_books(genre=genre, status="completed")
                # Take a few books from each related genre
                books_to_take = min(2, remaining_slots, len(genre_books))
                related_books.extend(genre_books[:books_to_take])
                remaining_slots -= books_to_take

            # Combine target and related books
            all_books = target_books + related_books
            return all_books[:max_books]

        return target_books

    def get_recent_books(self, max_books: int = None) -> List[Dict[str, Any]]:
        """
        Get recently created or updated books.

        Args:
            max_books: Maximum number of books to return

        Returns:
            List of recent book dictionaries
        """
        if max_books is None:
            max_books = self.default_display_limit

        return self.db_manager.get_books(status="completed", limit=max_books)

    def get_books_for_genre_recommendations(self,
                                          exclude_book_id: str,
                                          target_genre: str,
                                          max_books: int = 5) -> List[Dict[str, Any]]:
        """
        Get books to show in the "If You Enjoyed This [Genre]" back matter section.

        Args:
            exclude_book_id: Book ID to exclude from recommendations
            target_genre: Genre to focus recommendations on
            max_books: Maximum number of books to recommend

        Returns:
            List of recommended book dictionaries
        """
        # Get books from the same genre
        same_genre_books = [
            book for book in self.db_manager.get_books(genre=target_genre, status="completed")
            if book["book_id"] != exclude_book_id
        ]

        # Get books from related genres
        related_genres = self._get_related_genres(target_genre)
        related_books = []
        for genre in related_genres[:2]:  # Limit to 2 related genres
            genre_books = [
                book for book in self.db_manager.get_books(genre=genre, status="completed")
                if book["book_id"] != exclude_book_id
            ]
            related_books.extend(genre_books[:2])  # Max 2 books per related genre

        # Combine and limit
        all_recommendations = same_genre_books[:3] + related_books[:2]
        return all_recommendations[:max_books]

    def get_series_books_for_display(self, series_title: str) -> List[Dict[str, Any]]:
        """
        Get all books in a specific series for display.

        Args:
            series_title: Title of the series

        Returns:
            List of series book dictionaries sorted by book number
        """
        all_books = self.db_manager.get_books(status="completed")

        series_books = []
        for book in all_books:
            series_info = book.get("series_info", {})
            if (series_info.get("is_part_of_series") and
                series_info.get("series_title") == series_title):
                series_books.append(book)

        # Sort by book number
        series_books.sort(key=lambda x: x.get("series_info", {}).get("book_number", 0))

        return series_books

    def get_genre_distribution(self) -> Dict[str, int]:
        """
        Get the distribution of books across genres.

        Returns:
            Dictionary mapping genres to book counts
        """
        all_books = self.db_manager.get_books(status="completed")

        genre_counts = defaultdict(int)
        for book in all_books:
            genre = book.get("genre", "Unknown")
            genre_counts[genre] += 1

        return dict(genre_counts)

    def _apply_intelligent_filtering(self,
                                   all_books: List[Dict[str, Any]],
                                   current_genre: Optional[str],
                                   max_books: int,
                                   include_series: bool) -> List[Dict[str, Any]]:
        """
        Apply intelligent filtering to select the most relevant books.

        Args:
            all_books: List of all available books
            current_genre: Current genre context
            max_books: Maximum number of books to return
            include_series: Whether to include series books

        Returns:
            List of intelligently filtered books
        """
        # Group books by genre
        books_by_genre = defaultdict(list)
        for book in all_books:
            genre = book.get("genre", "Unknown")
            books_by_genre[genre].append(book)

        selected_books = []

        # If we have a current genre context, prioritize it
        if current_genre and current_genre in books_by_genre:
            genre_books = books_by_genre[current_genre]
            # Take up to max_books_per_genre from the current genre
            selected_count = min(self.max_books_per_genre, len(genre_books), max_books)
            selected_books.extend(self._select_diverse_subset(genre_books, selected_count))

            # Remove selected books from the pool
            remaining_books = [b for b in all_books if b not in selected_books]
            books_by_genre = defaultdict(list)
            for book in remaining_books:
                genre = book.get("genre", "Unknown")
                books_by_genre[genre].append(book)

        # Fill remaining slots with diverse selection from other genres
        remaining_slots = max_books - len(selected_books)
        if remaining_slots > 0:
            # Get related genres if we have a current genre
            if current_genre:
                related_genres = self._get_related_genres(current_genre)
                # Prioritize related genres
                genre_priority = related_genres + [g for g in books_by_genre.keys() if g not in related_genres]
            else:
                # No current genre context, use all genres
                genre_priority = list(books_by_genre.keys())

            # Distribute remaining slots across genres
            books_per_genre = max(1, remaining_slots // len(genre_priority)) if genre_priority else 0

            for genre in genre_priority:
                if remaining_slots <= 0:
                    break

                genre_books = books_by_genre[genre]
                if not genre_books:
                    continue

                # Take a few books from this genre
                take_count = min(books_per_genre, remaining_slots, len(genre_books))
                selected_books.extend(self._select_diverse_subset(genre_books, take_count))
                remaining_slots -= take_count

        return selected_books[:max_books]

    def _select_diverse_subset(self, books: List[Dict[str, Any]], count: int) -> List[Dict[str, Any]]:
        """
        Select a diverse subset of books from a list.

        Args:
            books: List of books to select from
            count: Number of books to select

        Returns:
            List of selected books
        """
        if len(books) <= count:
            return books

        # Prioritize recent books and series variety
        books_with_score = []
        for book in books:
            score = 0

            # Boost score for recent books
            if book.get("updated_date"):
                # Simple recency boost (could be more sophisticated)
                score += 1

            # Boost score for series books (for variety)
            series_info = book.get("series_info", {})
            if series_info.get("is_part_of_series"):
                score += 0.5

            books_with_score.append((book, score))

        # Sort by score (descending) and take top books
        books_with_score.sort(key=lambda x: x[1], reverse=True)

        # Add some randomness to avoid always showing the same books
        top_candidates = books_with_score[:count * 2] if len(books_with_score) > count * 2 else books_with_score
        selected = random.sample(top_candidates, min(count, len(top_candidates)))

        return [book for book, score in selected]

    def _get_related_genres(self, genre: str) -> List[str]:
        """
        Get genres related to the given genre.

        Args:
            genre: The genre to find related genres for

        Returns:
            List of related genre names
        """
        # Define genre relationships
        genre_relationships = {
            "Fantasy": ["Science Fiction", "Adventure", "Mythology"],
            "Science Fiction": ["Fantasy", "Thriller", "Dystopian"],
            "Mystery": ["Thriller", "Crime", "Suspense"],
            "Thriller": ["Mystery", "Suspense", "Crime"],
            "Romance": ["Contemporary", "Historical", "Fantasy"],
            "Historical": ["Biography", "Literary Fiction", "Romance"],
            "Horror": ["Thriller", "Supernatural", "Gothic"],
            "Adventure": ["Fantasy", "Science Fiction", "Action"],
            "Literary Fiction": ["Contemporary", "Historical", "Drama"]
        }

        return genre_relationships.get(genre, [])

    def get_display_summary(self) -> Dict[str, Any]:
        """
        Get a summary of the current display state for UI information.

        Returns:
            Dictionary containing display summary information
        """
        all_books = self.db_manager.get_books(status="completed")
        genre_dist = self.get_genre_distribution()

        return {
            "total_books": len(all_books),
            "total_genres": len(genre_dist),
            "display_limit": self.default_display_limit,
            "books_per_genre_limit": self.max_books_per_genre,
            "genre_distribution": genre_dist,
            "most_common_genre": max(genre_dist.items(), key=lambda x: x[1])[0] if genre_dist else None
        }


# Global book filter manager instance
_book_filter_manager = None

def get_book_filter_manager() -> BookFilterManager:
    """Get the global book filter manager instance."""
    global _book_filter_manager
    if _book_filter_manager is None:
        _book_filter_manager = BookFilterManager()
    return _book_filter_manager
