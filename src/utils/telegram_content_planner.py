"""
Telegram Content Planning and Queue Management for NovelForge AI

Handles intelligent content planning, genre strategy, and publication queue
management for optimal audience growth and engagement.
"""

import json
import random
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime, timedelta
from pathlib import Path

class TelegramContentPlanner:
    """
    Intelligent content planning system for Telegram publishing.
    
    Manages genre rotation, posting schedules, and queue prioritization
    to maximize audience engagement and growth.
    """
    
    def __init__(self):
        """Initialize the content planner."""
        self.genre_performance = self.load_genre_performance()
        self.content_calendar = self.load_content_calendar()
        self.posting_schedule = self.get_posting_schedule()
        self.genre_strategy = self.load_genre_strategy()
    
    def load_genre_performance(self) -> Dict[str, Dict[str, Any]]:
        """Load genre performance data."""
        # Default performance data for new channels
        return {
            'Romance': {'engagement_score': 8.5, 'growth_rate': 0.12, 'priority': 'high'},
            'Mystery': {'engagement_score': 7.8, 'growth_rate': 0.10, 'priority': 'high'},
            'Science Fiction': {'engagement_score': 7.5, 'growth_rate': 0.09, 'priority': 'high'},
            'Fantasy': {'engagement_score': 8.0, 'growth_rate': 0.11, 'priority': 'high'},
            'Thriller': {'engagement_score': 7.2, 'growth_rate': 0.08, 'priority': 'medium'},
            'Contemporary Fiction': {'engagement_score': 6.8, 'growth_rate': 0.07, 'priority': 'medium'},
            'Historical Fiction': {'engagement_score': 6.5, 'growth_rate': 0.06, 'priority': 'medium'},
            'Horror': {'engagement_score': 6.0, 'growth_rate': 0.05, 'priority': 'low'},
            'Literary Fiction': {'engagement_score': 5.5, 'growth_rate': 0.04, 'priority': 'low'}
        }
    
    def load_content_calendar(self) -> Dict[str, Any]:
        """Load content calendar configuration."""
        return {
            'weekly_themes': {
                1: {'theme': 'Popular Picks', 'focus': ['Romance', 'Mystery', 'Sci-Fi']},
                2: {'theme': 'Adventure Week', 'focus': ['Fantasy', 'Thriller', 'Adventure']},
                3: {'theme': 'Contemporary Mix', 'focus': ['Contemporary Fiction', 'Drama', 'Romance']},
                4: {'theme': 'Genre Fusion', 'focus': ['Mixed', 'Experimental', 'Popular']}
            },
            'monthly_campaigns': {
                1: 'New Year Fresh Starts',
                2: 'Love Stories Month',
                3: 'Adventure Awaits',
                4: 'Mystery & Suspense',
                5: 'Sci-Fi May',
                6: 'Summer Romance',
                7: 'Fantasy July',
                8: 'Thriller August',
                9: 'Back to School',
                10: 'Horror October',
                11: 'Gratitude Stories',
                12: 'Holiday Magic'
            }
        }
    
    def get_posting_schedule(self) -> Dict[str, Any]:
        """Get optimal posting schedule."""
        return {
            'frequency': 3,  # posts per week
            'days': ['Monday', 'Wednesday', 'Friday'],
            'times': ['10:00', '14:00', '18:00'],  # UTC times
            'timezone': 'UTC',
            'max_daily_posts': 1,
            'overflow_strategy': 'queue'  # queue, skip, or priority
        }
    
    def load_genre_strategy(self) -> Dict[str, Any]:
        """Load genre strategy configuration."""
        return {
            'strategy_type': 'balanced_growth',  # focused, balanced_growth, or diverse
            'primary_genres': ['Romance', 'Mystery', 'Science Fiction', 'Fantasy'],
            'secondary_genres': ['Thriller', 'Contemporary Fiction', 'Historical Fiction'],
            'experimental_genres': ['Horror', 'Literary Fiction', 'Poetry Collection'],
            'rotation_pattern': 'performance_weighted',  # random, sequential, or performance_weighted
            'new_genre_introduction_rate': 0.1  # 10% chance to try new genres
        }
    
    def prioritize_publication_queue(self, books: List[Dict[str, Any]], 
                                   max_books: int = 10) -> List[Dict[str, Any]]:
        """
        Prioritize books in publication queue based on strategy.
        
        Args:
            books: List of books to prioritize
            max_books: Maximum books to return
            
        Returns:
            Prioritized list of books
        """
        if not books:
            return []
        
        # Score each book
        scored_books = []
        for book in books:
            score = self.calculate_book_priority_score(book)
            scored_books.append((score, book))
        
        # Sort by score (highest first)
        scored_books.sort(key=lambda x: x[0], reverse=True)
        
        # Apply genre diversity filter
        prioritized = self.apply_genre_diversity_filter(
            [book for score, book in scored_books], 
            max_books
        )
        
        return prioritized
    
    def calculate_book_priority_score(self, book: Dict[str, Any]) -> float:
        """
        Calculate priority score for a book.
        
        Args:
            book: Book information
            
        Returns:
            Priority score (higher = more priority)
        """
        score = 0.0
        genre = book.get('genre', 'Unknown')
        
        # Genre performance weight (40%)
        genre_perf = self.genre_performance.get(genre, {})
        engagement_score = genre_perf.get('engagement_score', 5.0)
        score += (engagement_score / 10.0) * 0.4
        
        # Creation date weight (20% - newer books get slight priority)
        created_date = book.get('created_date', '')
        if created_date:
            try:
                created = datetime.fromisoformat(created_date.replace('Z', '+00:00'))
                days_old = (datetime.now() - created).days
                freshness_score = max(0, 1 - (days_old / 30))  # Decay over 30 days
                score += freshness_score * 0.2
            except:
                pass
        
        # Series bonus (15% - series books get priority)
        series_info = book.get('series_info')
        if series_info:
            try:
                series_data = json.loads(series_info) if isinstance(series_info, str) else series_info
                if series_data and series_data.get('is_series'):
                    score += 0.15
            except:
                pass
        
        # Quality indicators (15%)
        word_count = book.get('word_count', 0)
        if word_count > 10000:  # Substantial books get bonus
            score += 0.1
        
        if book.get('cover_base64'):  # Books with covers get bonus
            score += 0.05
        
        # Calendar alignment (10%)
        calendar_bonus = self.get_calendar_alignment_bonus(book)
        score += calendar_bonus * 0.1
        
        return score
    
    def get_calendar_alignment_bonus(self, book: Dict[str, Any]) -> float:
        """Get bonus score for calendar alignment."""
        genre = book.get('genre', 'Unknown')
        current_month = datetime.now().month
        current_week = datetime.now().isocalendar()[1] % 4 + 1
        
        # Monthly campaign alignment
        monthly_campaign = self.content_calendar['monthly_campaigns'].get(current_month, '')
        if self.genre_matches_campaign(genre, monthly_campaign):
            return 0.5
        
        # Weekly theme alignment
        weekly_theme = self.content_calendar['weekly_themes'].get(current_week, {})
        focus_genres = weekly_theme.get('focus', [])
        if genre in focus_genres or 'Mixed' in focus_genres:
            return 0.3
        
        return 0.0
    
    def genre_matches_campaign(self, genre: str, campaign: str) -> bool:
        """Check if genre matches monthly campaign."""
        campaign_lower = campaign.lower()
        genre_lower = genre.lower()
        
        matches = {
            'love stories': ['romance', 'contemporary romance', 'paranormal romance'],
            'adventure': ['adventure', 'fantasy', 'thriller'],
            'mystery': ['mystery', 'thriller', 'mystery thriller'],
            'sci-fi': ['science fiction', 'speculative fiction'],
            'summer romance': ['romance', 'contemporary fiction'],
            'fantasy': ['fantasy', 'epic fantasy', 'urban fantasy'],
            'thriller': ['thriller', 'mystery thriller', 'suspense'],
            'horror': ['horror', 'thriller']
        }
        
        for campaign_key, genre_list in matches.items():
            if campaign_key in campaign_lower and genre_lower in genre_list:
                return True
        
        return False
    
    def apply_genre_diversity_filter(self, books: List[Dict[str, Any]], 
                                   max_books: int) -> List[Dict[str, Any]]:
        """
        Apply genre diversity filter to avoid too many books of same genre.
        
        Args:
            books: Prioritized list of books
            max_books: Maximum books to return
            
        Returns:
            Filtered list with genre diversity
        """
        if len(books) <= max_books:
            return books
        
        selected = []
        genre_counts = {}
        max_per_genre = max(1, max_books // 3)  # Max 1/3 of posts per genre
        
        for book in books:
            if len(selected) >= max_books:
                break
            
            genre = book.get('genre', 'Unknown')
            current_count = genre_counts.get(genre, 0)
            
            # Allow if under genre limit or if we need to fill remaining slots
            if current_count < max_per_genre or len(selected) < max_books - 2:
                selected.append(book)
                genre_counts[genre] = current_count + 1
        
        return selected
    
    def get_optimal_genre_mix(self, num_books: int) -> List[str]:
        """
        Get optimal genre mix for a given number of books.
        
        Args:
            num_books: Number of books to publish
            
        Returns:
            List of recommended genres
        """
        strategy = self.genre_strategy['strategy_type']
        
        if strategy == 'focused':
            # Focus on top 2-3 genres
            top_genres = ['Romance', 'Mystery', 'Science Fiction']
            return (top_genres * ((num_books // len(top_genres)) + 1))[:num_books]
        
        elif strategy == 'balanced_growth':
            # 60% primary, 30% secondary, 10% experimental
            primary = self.genre_strategy['primary_genres']
            secondary = self.genre_strategy['secondary_genres']
            experimental = self.genre_strategy['experimental_genres']
            
            mix = []
            primary_count = int(num_books * 0.6)
            secondary_count = int(num_books * 0.3)
            experimental_count = num_books - primary_count - secondary_count
            
            mix.extend(random.choices(primary, k=primary_count))
            mix.extend(random.choices(secondary, k=secondary_count))
            mix.extend(random.choices(experimental, k=experimental_count))
            
            return mix
        
        else:  # diverse
            # Equal distribution across all genres
            all_genres = list(self.genre_performance.keys())
            return random.choices(all_genres, k=num_books)
    
    def handle_publication_overflow(self, overflow_books: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Handle overflow when more books are ready than can be published.
        
        Args:
            overflow_books: Books that couldn't be published this cycle
            
        Returns:
            Overflow handling strategy and actions
        """
        strategy = self.posting_schedule['overflow_strategy']
        
        if strategy == 'queue':
            # Queue for next publication cycle
            return {
                'action': 'queue',
                'queued_books': len(overflow_books),
                'next_publication': self.get_next_publication_date(),
                'message': f"Queued {len(overflow_books)} books for next publication cycle"
            }
        
        elif strategy == 'priority':
            # Increase publication frequency temporarily
            return {
                'action': 'increase_frequency',
                'additional_posts': min(len(overflow_books), 2),
                'message': f"Scheduling {min(len(overflow_books), 2)} additional posts this week"
            }
        
        else:  # skip
            # Skip lower priority books
            return {
                'action': 'skip',
                'skipped_books': len(overflow_books),
                'message': f"Skipped {len(overflow_books)} lower priority books"
            }
    
    def get_next_publication_date(self) -> str:
        """Get the next scheduled publication date."""
        today = datetime.now()
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        schedule_days = self.posting_schedule['days']
        
        for i in range(1, 8):  # Check next 7 days
            check_date = today + timedelta(days=i)
            day_name = days[check_date.weekday()]
            if day_name in schedule_days:
                return check_date.strftime('%Y-%m-%d')
        
        return (today + timedelta(days=7)).strftime('%Y-%m-%d')
    
    def generate_content_recommendations(self) -> Dict[str, Any]:
        """Generate content recommendations for the next week."""
        current_week = datetime.now().isocalendar()[1] % 4 + 1
        current_month = datetime.now().month
        
        weekly_theme = self.content_calendar['weekly_themes'].get(current_week, {})
        monthly_campaign = self.content_calendar['monthly_campaigns'].get(current_month, '')
        
        return {
            'weekly_theme': weekly_theme.get('theme', 'General Mix'),
            'focus_genres': weekly_theme.get('focus', ['Romance', 'Mystery', 'Sci-Fi']),
            'monthly_campaign': monthly_campaign,
            'recommended_mix': self.get_optimal_genre_mix(3),
            'special_opportunities': self.get_special_opportunities()
        }
    
    def get_special_opportunities(self) -> List[str]:
        """Get special content opportunities."""
        opportunities = []
        today = datetime.now()
        
        # Holiday tie-ins
        if today.month == 2 and today.day <= 14:
            opportunities.append("Valentine's Day romance focus")
        elif today.month == 10:
            opportunities.append("Halloween horror/thriller focus")
        elif today.month == 12:
            opportunities.append("Holiday-themed stories")
        
        # Seasonal opportunities
        if today.month in [6, 7, 8]:
            opportunities.append("Summer reading - lighter genres")
        elif today.month in [9, 10, 11]:
            opportunities.append("Back-to-school - educational themes")
        
        return opportunities

def get_content_planner() -> TelegramContentPlanner:
    """Factory function to get content planner instance."""
    return TelegramContentPlanner()
