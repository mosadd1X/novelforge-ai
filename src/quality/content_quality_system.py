#!/usr/bin/env python3
"""
Content Quality Metrics & Tracking System

This system measures and tracks the quality of generated content, including:
- Fictional author voice consistency
- Genre appropriateness
- User satisfaction ratings
- Content improvement over time
"""

import json
import sqlite3
import hashlib
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from enum import Enum

from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console(markup=True)

class QualityMetric(Enum):
    """Quality metrics for content evaluation."""
    AUTHOR_VOICE_CONSISTENCY = "author_voice_consistency"
    GENRE_APPROPRIATENESS = "genre_appropriateness"
    NARRATIVE_COHERENCE = "narrative_coherence"
    CHARACTER_DEVELOPMENT = "character_development"
    WRITING_STYLE_QUALITY = "writing_style_quality"
    THEMATIC_DEPTH = "thematic_depth"
    OVERALL_SATISFACTION = "overall_satisfaction"

@dataclass
class QualityAssessment:
    """Data class for quality assessment results."""
    content_id: str
    content_type: str  # "book", "chapter", "series"
    fictional_author: str
    genre: str
    metrics: Dict[QualityMetric, float]  # 0.0 to 1.0 scale
    user_rating: Optional[float] = None  # 1-5 scale
    user_feedback: Optional[str] = None
    timestamp: datetime = None
    enhancement_used: bool = False

    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now()

@dataclass
class ContentMetadata:
    """Metadata for generated content."""
    content_id: str
    title: str
    fictional_author: str
    genre: str
    themes: List[str]
    writing_style: str
    target_length: str
    word_count: int
    generation_time: float
    enhancement_used: bool
    timestamp: datetime

class ContentQualitySystem:
    """Main system for tracking and analyzing content quality."""

    def __init__(self, db_path: str = "data/content_quality.db"):
        """Initialize the content quality system."""
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(exist_ok=True)
        self._init_database()

    def _init_database(self):
        """Initialize the SQLite database for quality tracking."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            # Content metadata table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS content_metadata (
                    content_id TEXT PRIMARY KEY,
                    title TEXT NOT NULL,
                    fictional_author TEXT NOT NULL,
                    genre TEXT NOT NULL,
                    themes TEXT,  -- JSON array
                    writing_style TEXT,
                    target_length TEXT,
                    word_count INTEGER,
                    generation_time REAL,
                    enhancement_used BOOLEAN,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)

            # Quality assessments table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS quality_assessments (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    content_id TEXT NOT NULL,
                    content_type TEXT NOT NULL,
                    fictional_author TEXT NOT NULL,
                    genre TEXT NOT NULL,
                    metric_name TEXT NOT NULL,
                    metric_value REAL NOT NULL,
                    user_rating REAL,
                    user_feedback TEXT,
                    enhancement_used BOOLEAN,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (content_id) REFERENCES content_metadata (content_id)
                )
            """)

            # User feedback table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS user_feedback (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    content_id TEXT NOT NULL,
                    rating INTEGER CHECK (rating >= 1 AND rating <= 5),
                    feedback_text TEXT,
                    feedback_categories TEXT,  -- JSON array
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (content_id) REFERENCES content_metadata (content_id)
                )
            """)

            # Quality trends table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS quality_trends (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    fictional_author TEXT NOT NULL,
                    genre TEXT NOT NULL,
                    metric_name TEXT NOT NULL,
                    avg_score REAL NOT NULL,
                    sample_count INTEGER NOT NULL,
                    trend_direction TEXT,  -- "improving", "stable", "declining"
                    calculation_date DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """)

            conn.commit()

    def register_content(self, metadata: ContentMetadata) -> str:
        """Register new content for quality tracking."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT OR REPLACE INTO content_metadata
                    (content_id, title, fictional_author, genre, themes, writing_style,
                     target_length, word_count, generation_time, enhancement_used, timestamp)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    metadata.content_id,
                    metadata.title,
                    metadata.fictional_author,
                    metadata.genre,
                    json.dumps(metadata.themes),
                    metadata.writing_style,
                    metadata.target_length,
                    metadata.word_count,
                    metadata.generation_time,
                    metadata.enhancement_used,
                    metadata.timestamp
                ))
                conn.commit()

            console.print(f"[green]✓[/green] Registered content: {metadata.title}")
            return metadata.content_id

        except Exception as e:
            console.print(f"[red]Failed to register content: {e}[/red]")
            return ""

    def assess_content_quality(self, content_id: str, content: str,
                             fictional_author: str, genre: str) -> QualityAssessment:
        """Assess the quality of generated content using various metrics."""
        try:
            # Generate content hash for ID if not provided
            if not content_id:
                content_id = hashlib.md5(content.encode()).hexdigest()[:16]

            # Calculate quality metrics
            metrics = {}

            # Author voice consistency (basic heuristic)
            metrics[QualityMetric.AUTHOR_VOICE_CONSISTENCY] = self._assess_author_voice_consistency(
                content, fictional_author
            )

            # Genre appropriateness
            metrics[QualityMetric.GENRE_APPROPRIATENESS] = self._assess_genre_appropriateness(
                content, genre
            )

            # Narrative coherence
            metrics[QualityMetric.NARRATIVE_COHERENCE] = self._assess_narrative_coherence(content)

            # Character development
            metrics[QualityMetric.CHARACTER_DEVELOPMENT] = self._assess_character_development(content)

            # Writing style quality
            metrics[QualityMetric.WRITING_STYLE_QUALITY] = self._assess_writing_style_quality(content)

            # Thematic depth
            metrics[QualityMetric.THEMATIC_DEPTH] = self._assess_thematic_depth(content)

            # Create assessment
            assessment = QualityAssessment(
                content_id=content_id,
                content_type="book",  # Default to book
                fictional_author=fictional_author,
                genre=genre,
                metrics=metrics
            )

            # Store assessment in database
            self._store_quality_assessment(assessment)

            return assessment

        except Exception as e:
            console.print(f"[red]Quality assessment failed: {e}[/red]")
            # Return default assessment
            return QualityAssessment(
                content_id=content_id or "unknown",
                content_type="book",
                fictional_author=fictional_author,
                genre=genre,
                metrics={metric: 0.5 for metric in QualityMetric}
            )

    def _assess_author_voice_consistency(self, content: str, fictional_author: str) -> float:
        """Assess how well the content matches the fictional author's voice."""
        # Basic heuristic assessment
        # In a full implementation, this would use NLP analysis

        # Check content length (longer content generally allows for better voice development)
        length_score = min(len(content) / 10000, 1.0)  # Normalize to 10k words

        # Check for narrative complexity (sentence variety)
        sentences = content.split('.')
        avg_sentence_length = sum(len(s.split()) for s in sentences) / len(sentences) if sentences else 0
        complexity_score = min(avg_sentence_length / 20, 1.0)  # Normalize to 20 words

        # Combine scores
        return (length_score * 0.4 + complexity_score * 0.6)

    def _assess_genre_appropriateness(self, content: str, genre: str) -> float:
        """Assess how well the content fits the specified genre."""
        # Basic keyword-based assessment
        genre_keywords = {
            "Literary Fiction": ["character", "emotion", "relationship", "society", "human"],
            "Mystery": ["detective", "clue", "suspect", "investigation", "murder"],
            "Science Fiction": ["technology", "future", "space", "alien", "scientific"],
            "Fantasy": ["magic", "dragon", "quest", "kingdom", "wizard"],
            "Romance": ["love", "heart", "relationship", "passion", "romance"],
            "Horror": ["fear", "dark", "terror", "nightmare", "haunted"],
            "Historical Fiction": ["history", "period", "era", "historical", "past"]
        }

        keywords = genre_keywords.get(genre, [])
        if not keywords:
            return 0.7  # Default score for unknown genres

        content_lower = content.lower()
        keyword_count = sum(1 for keyword in keywords if keyword in content_lower)

        return min(keyword_count / len(keywords), 1.0)

    def _assess_narrative_coherence(self, content: str) -> float:
        """Assess the narrative coherence of the content."""
        # Basic coherence assessment
        paragraphs = content.split('\n\n')

        if len(paragraphs) < 2:
            return 0.5

        # Check for consistent tense usage (simplified)
        past_tense_indicators = ['was', 'were', 'had', 'did', 'said']
        present_tense_indicators = ['is', 'are', 'has', 'does', 'says']

        past_count = sum(content.lower().count(word) for word in past_tense_indicators)
        present_count = sum(content.lower().count(word) for word in present_tense_indicators)

        # Prefer consistent tense usage
        total_tense = past_count + present_count
        if total_tense == 0:
            return 0.5

        consistency = max(past_count, present_count) / total_tense
        return consistency

    def _assess_character_development(self, content: str) -> float:
        """Assess character development in the content."""
        # Basic character development assessment
        # Look for dialogue and character actions

        dialogue_count = content.count('"')
        action_indicators = ['walked', 'ran', 'looked', 'thought', 'felt', 'said']
        action_count = sum(content.lower().count(word) for word in action_indicators)

        # Normalize scores
        dialogue_score = min(dialogue_count / 20, 1.0)  # Normalize to 20 dialogue instances
        action_score = min(action_count / 50, 1.0)  # Normalize to 50 action instances

        return (dialogue_score * 0.5 + action_score * 0.5)

    def _assess_writing_style_quality(self, content: str) -> float:
        """Assess the overall writing style quality."""
        # Basic style quality assessment
        words = content.split()

        if len(words) < 100:
            return 0.3  # Too short for proper assessment

        # Check vocabulary diversity
        unique_words = len(set(word.lower().strip('.,!?";') for word in words))
        vocabulary_diversity = unique_words / len(words)

        # Check sentence variety
        sentences = content.split('.')
        sentence_lengths = [len(s.split()) for s in sentences if s.strip()]

        if not sentence_lengths:
            return 0.3

        avg_length = sum(sentence_lengths) / len(sentence_lengths)
        length_variety = len(set(sentence_lengths)) / len(sentence_lengths)

        # Combine metrics
        vocab_score = min(vocabulary_diversity * 2, 1.0)  # Boost vocabulary importance
        variety_score = length_variety
        length_score = min(avg_length / 15, 1.0)  # Normalize to 15 words per sentence

        return (vocab_score * 0.4 + variety_score * 0.3 + length_score * 0.3)

    def _assess_thematic_depth(self, content: str) -> float:
        """Assess the thematic depth of the content."""
        # Basic thematic depth assessment
        # Look for abstract concepts and emotional depth

        thematic_words = [
            'meaning', 'purpose', 'identity', 'truth', 'justice', 'love', 'loss',
            'hope', 'despair', 'freedom', 'responsibility', 'growth', 'change',
            'memory', 'time', 'mortality', 'society', 'family', 'friendship'
        ]

        content_lower = content.lower()
        thematic_count = sum(1 for word in thematic_words if word in content_lower)

        # Normalize to content length
        words_count = len(content.split())
        if words_count == 0:
            return 0.0

        thematic_density = thematic_count / (words_count / 1000)  # Per 1000 words
        return min(thematic_density / 5, 1.0)  # Normalize to 5 thematic words per 1000

    def _store_quality_assessment(self, assessment: QualityAssessment):
        """Store quality assessment in the database."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()

                # Store each metric as a separate row
                for metric, value in assessment.metrics.items():
                    cursor.execute("""
                        INSERT INTO quality_assessments
                        (content_id, content_type, fictional_author, genre, metric_name,
                         metric_value, user_rating, user_feedback, enhancement_used, timestamp)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (
                        assessment.content_id,
                        assessment.content_type,
                        assessment.fictional_author,
                        assessment.genre,
                        metric.value,
                        value,
                        assessment.user_rating,
                        assessment.user_feedback,
                        assessment.enhancement_used,
                        assessment.timestamp
                    ))

                conn.commit()

        except Exception as e:
            console.print(f"[red]Failed to store quality assessment: {e}[/red]")

    def add_user_feedback(self, content_id: str, rating: int, feedback_text: str = "",
                         feedback_categories: List[str] = None) -> bool:
        """Add user feedback for content."""
        try:
            if not (1 <= rating <= 5):
                console.print("[red]Rating must be between 1 and 5[/red]")
                return False

            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO user_feedback
                    (content_id, rating, feedback_text, feedback_categories)
                    VALUES (?, ?, ?, ?)
                """, (
                    content_id,
                    rating,
                    feedback_text,
                    json.dumps(feedback_categories or [])
                ))
                conn.commit()

            console.print(f"[green]✓[/green] User feedback recorded (Rating: {rating}/5)")
            return True

        except Exception as e:
            console.print(f"[red]Failed to add user feedback: {e}[/red]")
            return False

    def get_quality_report(self, fictional_author: str = None, genre: str = None,
                          days: int = 30) -> Dict[str, Any]:
        """Generate a comprehensive quality report."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()

                # Build query conditions
                conditions = ["timestamp >= datetime('now', '-{} days')".format(days)]
                params = []

                if fictional_author:
                    conditions.append("fictional_author = ?")
                    params.append(fictional_author)

                if genre:
                    conditions.append("genre = ?")
                    params.append(genre)

                where_clause = " AND ".join(conditions)

                # Get average scores by metric
                cursor.execute(f"""
                    SELECT metric_name, AVG(metric_value) as avg_score, COUNT(*) as count
                    FROM quality_assessments
                    WHERE {where_clause}
                    GROUP BY metric_name
                """, params)

                metric_scores = {row[0]: {"avg_score": row[1], "count": row[2]}
                               for row in cursor.fetchall()}

                # Get user feedback summary
                cursor.execute(f"""
                    SELECT AVG(rating) as avg_rating, COUNT(*) as feedback_count
                    FROM user_feedback uf
                    JOIN content_metadata cm ON uf.content_id = cm.content_id
                    WHERE cm.timestamp >= datetime('now', '-{days} days')
                    {' AND cm.fictional_author = ?' if fictional_author else ''}
                    {' AND cm.genre = ?' if genre else ''}
                """, params)

                feedback_row = cursor.fetchone()
                user_feedback_summary = {
                    "avg_rating": feedback_row[0] if feedback_row[0] else 0,
                    "feedback_count": feedback_row[1]
                }

                # Get content generation stats
                cursor.execute(f"""
                    SELECT COUNT(*) as total_content,
                           AVG(word_count) as avg_word_count,
                           AVG(generation_time) as avg_generation_time,
                           SUM(CASE WHEN enhancement_used THEN 1 ELSE 0 END) as enhanced_count
                    FROM content_metadata
                    WHERE timestamp >= datetime('now', '-{days} days')
                    {' AND fictional_author = ?' if fictional_author else ''}
                    {' AND genre = ?' if genre else ''}
                """, params)

                stats_row = cursor.fetchone()
                generation_stats = {
                    "total_content": stats_row[0],
                    "avg_word_count": stats_row[1] if stats_row[1] else 0,
                    "avg_generation_time": stats_row[2] if stats_row[2] else 0,
                    "enhanced_count": stats_row[3],
                    "enhancement_rate": (stats_row[3] / stats_row[0] * 100) if stats_row[0] > 0 else 0
                }

                return {
                    "period_days": days,
                    "fictional_author": fictional_author,
                    "genre": genre,
                    "metric_scores": metric_scores,
                    "user_feedback": user_feedback_summary,
                    "generation_stats": generation_stats,
                    "timestamp": datetime.now().isoformat()
                }

        except Exception as e:
            console.print(f"[red]Failed to generate quality report: {e}[/red]")
            return {}

    def get_author_performance_comparison(self) -> Dict[str, Any]:
        """Compare performance across different fictional authors."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()

                # Get average scores by fictional author
                cursor.execute("""
                    SELECT fictional_author, metric_name, AVG(metric_value) as avg_score
                    FROM quality_assessments
                    WHERE timestamp >= datetime('now', '-30 days')
                    GROUP BY fictional_author, metric_name
                """)

                author_metrics = {}
                for row in cursor.fetchall():
                    author, metric, score = row
                    if author not in author_metrics:
                        author_metrics[author] = {}
                    author_metrics[author][metric] = score

                # Get user ratings by author
                cursor.execute("""
                    SELECT cm.fictional_author, AVG(uf.rating) as avg_rating, COUNT(*) as count
                    FROM user_feedback uf
                    JOIN content_metadata cm ON uf.content_id = cm.content_id
                    WHERE cm.timestamp >= datetime('now', '-30 days')
                    GROUP BY cm.fictional_author
                """)

                author_ratings = {row[0]: {"avg_rating": row[1], "count": row[2]}
                                for row in cursor.fetchall()}

                return {
                    "author_metrics": author_metrics,
                    "author_ratings": author_ratings,
                    "timestamp": datetime.now().isoformat()
                }

        except Exception as e:
            console.print(f"[red]Failed to generate author comparison: {e}[/red]")
            return {}

    def display_quality_dashboard(self, fictional_author: str = None, genre: str = None):
        """Display a comprehensive quality dashboard."""
        console.print(Panel.fit(
            "[bold cyan]📊 Content Quality Dashboard[/bold cyan]\n"
            f"Fictional Author: {fictional_author or 'All'}\n"
            f"Genre: {genre or 'All'}\n"
            "Last 30 days",
            border_style="cyan"
        ))

        # Get quality report
        report = self.get_quality_report(fictional_author, genre, 30)

        if not report:
            console.print("[red]No data available for the specified criteria[/red]")
            return

        # Display metrics table
        if report.get("metric_scores"):
            table = Table(title="Quality Metrics")
            table.add_column("Metric", style="cyan")
            table.add_column("Average Score", style="green")
            table.add_column("Sample Count", style="yellow")
            table.add_column("Grade", style="white")

            for metric_name, data in report["metric_scores"].items():
                score = data["avg_score"]
                count = data["count"]

                # Convert to letter grade
                if score >= 0.9:
                    grade = "A+"
                elif score >= 0.8:
                    grade = "A"
                elif score >= 0.7:
                    grade = "B"
                elif score >= 0.6:
                    grade = "C"
                else:
                    grade = "D"

                table.add_row(
                    metric_name.replace("_", " ").title(),
                    f"{score:.3f}",
                    str(count),
                    grade
                )

            console.print(table)

        # Display user feedback summary
        feedback = report.get("user_feedback", {})
        if feedback.get("feedback_count", 0) > 0:
            console.print(f"\n[bold cyan]User Feedback Summary:[/bold cyan]")
            console.print(f"  Average Rating: {feedback['avg_rating']:.1f}/5.0")
            console.print(f"  Total Feedback: {feedback['feedback_count']}")

        # Display generation statistics
        stats = report.get("generation_stats", {})
        if stats.get("total_content", 0) > 0:
            console.print(f"\n[bold cyan]Generation Statistics:[/bold cyan]")
            console.print(f"  Total Content Generated: {stats['total_content']}")
            console.print(f"  Average Word Count: {stats['avg_word_count']:.0f}")
            console.print(f"  Average Generation Time: {stats['avg_generation_time']:.2f}s")
            console.print(f"  Enhancement Usage: {stats['enhancement_rate']:.1f}%")

    def get_improvement_recommendations(self, fictional_author: str = None) -> List[str]:
        """Generate recommendations for improving content quality."""
        recommendations = []

        try:
            report = self.get_quality_report(fictional_author, days=30)
            metrics = report.get("metric_scores", {})

            # Analyze each metric and provide recommendations
            for metric_name, data in metrics.items():
                score = data["avg_score"]

                if score < 0.6:  # Poor performance
                    if metric_name == "author_voice_consistency":
                        recommendations.append(
                            "Consider using AI enhancement to improve author voice consistency"
                        )
                    elif metric_name == "genre_appropriateness":
                        recommendations.append(
                            "Review genre-specific themes and writing techniques"
                        )
                    elif metric_name == "narrative_coherence":
                        recommendations.append(
                            "Focus on improving story structure and flow"
                        )
                    elif metric_name == "character_development":
                        recommendations.append(
                            "Enhance character depth and dialogue quality"
                        )
                    elif metric_name == "writing_style_quality":
                        recommendations.append(
                            "Improve vocabulary diversity and sentence variety"
                        )
                    elif metric_name == "thematic_depth":
                        recommendations.append(
                            "Incorporate more meaningful themes and concepts"
                        )

            # Check user feedback
            feedback = report.get("user_feedback", {})
            if feedback.get("avg_rating", 0) < 3.5:
                recommendations.append(
                    "User satisfaction is below average - consider gathering more specific feedback"
                )

            # Check enhancement usage
            stats = report.get("generation_stats", {})
            if stats.get("enhancement_rate", 0) < 50:
                recommendations.append(
                    "Consider using AI enhancement more frequently for better quality"
                )

            if not recommendations:
                recommendations.append("Quality metrics are performing well - maintain current approach")

            return recommendations

        except Exception as e:
            console.print(f"[red]Failed to generate recommendations: {e}[/red]")
            return ["Unable to generate recommendations due to data issues"]

# Global quality system instance
quality_system = ContentQualitySystem()
