# CFInsight

## AI-Powered Codeforces Analytics & Competitive Programming Intelligence Platform

CFInsight is a backend-driven analytics platform that transforms publicly available Codeforces data into comprehensive performance reports, behavioral insights, AI-generated evaluations, search trends, and competitive programming analytics.

The platform combines FastAPI, PostgreSQL, caching, Trie-based autocomplete, monitoring systems, and Large Language Models to provide a deeper understanding of a programmer's competitive programming journey.

---

# Table of Contents

* Overview
* Problem Statement
* Key Features
* System Architecture
* Analytics Workflow
* Performance Optimizations
* Technology Stack
* API Endpoints
* Project Structure
* Database Design
* Engineering Decisions
* Monitoring & Observability
* Codeforces APIs Used
* Future Enhancements
* Disclaimer

---

# Overview

Codeforces provides valuable competitive programming data including ratings, contests, submissions, and rankings. However, it does not provide deeper analytical insights regarding performance trends, growth patterns, problem-solving behavior, submission quality, or competitive programming strengths and weaknesses.

CFInsight bridges this gap by automatically:

* Fetching public Codeforces data
* Generating detailed analytics reports
* Evaluating contest performance
* Analyzing problem-solving behavior
* Detecting unusual competitive programming patterns
* Producing AI-generated profile evaluations
* Tracking trending Codeforces profiles
* Providing fast autocomplete suggestions
* Optimizing response times through caching

The platform follows a layered architecture to ensure scalability, maintainability, and separation of concerns.

---

# Problem Statement

Competitive programmers often have access to large amounts of raw data but lack meaningful insights regarding:

* Long-term rating growth
* Contest consistency
* Problem-solving strengths
* Difficulty progression
* Topic expertise
* Submission quality
* Competitive programming behavior
* Overall profile evaluation

CFInsight converts raw Codeforces data into actionable intelligence.

---

# Key Features

## 1. Profile Analytics

Provides a summary of the user's competitive programming profile.

### Information Displayed

* Handle
* Current Rating
* Maximum Rating
* Current Rank
* Maximum Rank

---

## 2. Contest Analytics

Analyzes the user's entire contest history.

### Metrics

* Total Contests Participated
* Current Rating
* Maximum Rating
* Average Rating
* Rating Growth
* Average Rating Change
* Largest Rating Increase
* Largest Rating Decrease
* Best Rank
* Worst Rank
* Average Rank

### Insights Generated

* Rating progression trends
* Contest consistency evaluation
* Growth trajectory analysis

---

## 3. Problem Solving Analytics

Analyzes accepted submissions and solved problems.

### Metrics

* Total Problems Solved
* Hardest Problem Solved
* Average Problem Difficulty

### Difficulty Distribution

* 800 – 1200
* 1200 – 1600
* 1600 – 2000
* 2000 – 2400
* 2400+

### Topic Distribution

Based on Codeforces problem tags:

* Dynamic Programming
* Graph Theory
* Greedy Algorithms
* Binary Search
* Mathematics
* Strings
* Data Structures
* Implementation
* And many more

---

## 4. Activity Analytics

Analyzes submission behavior and platform activity.

### Metrics

* Total Submissions
* Accepted Submissions
* Wrong Answers
* Runtime Errors
* Memory Limit Exceeded
* Time Limit Exceeded
* Skipped Submissions
* Submission Success Rate

### Verdict Analysis

Provides a complete breakdown of submission outcomes and success patterns.

---

## 5. Suspicion Analysis Engine

CFInsight includes a rule-based behavioral analytics engine.

The purpose is not to detect cheating but to identify statistically unusual competitive programming patterns.

### Factors Considered

* Difficulty progression
* Contest performance consistency
* Rating growth behavior
* Submission patterns
* Skipped submissions

### Suspicion Levels

| Score Range | Level     |
| ----------- | --------- |
| 0 – 30      | Low       |
| 31 – 60     | Moderate  |
| 61 – 80     | High      |
| 81 – 100    | Very High |

### Example Output

```json
{
  "score": 57,
  "level": "Moderate"
}
```

---

## 6. AI-Powered Insights

CFInsight uses LangChain and Groq-hosted Llama models to generate intelligent profile evaluations.

### Inputs Used

* Contest Performance
* Rating Trends
* Problem Solving Metrics
* Activity Analytics
* Behavioral Analysis
* Suspicion Score

### Generated Sections

* Strengths
* Weaknesses
* Growth Analysis
* Performance Summary
* Behavioral Evaluation
* Overall Assessment

### Example

```text
Strengths:
Strong rating growth and excellent graph problem solving.

Weaknesses:
Lower acceptance rate on higher-rated problems.

Growth Analysis:
Consistent improvement over recent contests.

Overall Evaluation:
Strong competitive programmer with solid analytical skills.
```

---

## 7. Search Leaderboard

Tracks the most searched Codeforces handles on the platform.

### Information Displayed

* Handle
* Search Count
* Ranking Position

### Purpose

* Identify trending competitive programmers
* Measure platform engagement
* Provide popularity insights

---

## 8. Trie-Based Handle Suggestions

Successfully searched handles are stored inside an in-memory Trie.

### Benefits

* Fast prefix search
* Case-insensitive lookup
* No database query per keystroke
* Efficient autocomplete experience

### Example

```text
Prefix: yas

Suggestions:
- YashSingh
- YashSharma
- YashKumar
```

---

## 9. Report Caching

Generated reports are cached in PostgreSQL.

### Benefits

* Reduces external API requests
* Improves response times
* Avoids unnecessary AI generation
* Enhances user experience

### Cache Statistics

The platform tracks:

* Cache Hits
* Cache Misses
* Cache Hit Rate

---

## 10. Performance Metrics

Custom middleware tracks runtime metrics.

### Metrics Tracked

* Total Report Requests
* Average Response Time
* Maximum Response Time

These metrics help evaluate platform performance and caching effectiveness.

---

# System Architecture

```text
                      Client
                         |
                         v
                  FastAPI Backend
                         |
     ------------------------------------------------
     |                    |                         |
     v                    v                         v
PostgreSQL           Trie Engine             Metrics Engine
     |
     v
Report Cache
     |
     v
Codeforces API
     |
     v
Analytics Engine
     |
     v
Suspicion Engine
     |
     v
AI Insight Engine
     |
     v
Final Report
```

---

# Analytics Workflow

```text
User Searches Handle
          |
          v
Check Cached Report
          |
    ----------------
    |              |
 Cache Hit    Cache Miss
    |              |
    |         Fetch Codeforces Data
    |              |
    |         Generate Analytics
    |              |
    |      Calculate Suspicion Score
    |              |
    |       Generate AI Insights
    |              |
    |         Store Report
    |              |
    ----------------
          |
          v
      Return Report
```

---

# Performance Optimizations

## PostgreSQL Report Caching

Generated reports are cached and reused whenever possible.

Benefits:

* Lower latency
* Reduced API calls
* Reduced AI generation overhead

---

## Trie-Based Autocomplete

Autocomplete suggestions are generated using a Trie data structure.

Benefits:

* Efficient prefix search
* Predictable lookup performance
* Minimal database dependency

---

## Search Analytics

Maintains:

* Search frequencies
* Trending handles
* Leaderboard rankings

---

## Middleware-Based Monitoring

Automatically tracks:

* Request volume
* Average latency
* Peak latency

---

# Technology Stack

## Backend

* Python 3.12
* FastAPI
* SQLAlchemy

## Database

* PostgreSQL

## AI Layer

* LangChain
* Groq API
* Llama Models

## Deployment

* Railway

## External Data Source

* Codeforces Public API

---

# API Endpoints

| Endpoint             | Description                        |
| -------------------- | ---------------------------------- |
| GET /report/{handle} | Generate complete analytics report |
| GET /leaderboard     | View most searched profiles        |
| GET /suggest?prefix= | Trie-based handle suggestions      |
| GET /cache-stats     | Cache hit/miss statistics          |
| GET /metrics         | API performance metrics            |
| GET /health          | Service health check               |

---

# Project Structure

```text
backend/

├── api/
│   ├── report.py
│   ├── leaderboard.py
│   ├── suggest.py
│   ├── cache_stats.py
│   ├── metrics.py
│   └── health.py
│
├── services/
│   ├── codeforces_service.py
│   ├── analytics_service.py
│   ├── suspicion_service.py
│   ├── ai_service.py
│   ├── cache_service.py
│   ├── cache_stats_service.py
│   └── metrics_service.py
│
├── repositories/
│   ├── user_repository.py
│   ├── report_repository.py
│   ├── search_stats_repository.py
│   └── cache_stats_repository.py
│
├── models/
│   ├── user.py
│   ├── report.py
│   ├── search_stats.py
│   └── cache_stats.py
│
├── schemas/
│   ├── report.py
│   ├── leaderboard.py
│   ├── cache_stats.py
│   └── metrics.py
│
├── utils/
│   └── trie.py
│
├── core/
│   ├── database.py
│   ├── config.py
│   ├── trie_store.py
│   └── metrics_store.py
│
├── middleware/
│   └── timing.py
│
├── prompts/
│   └── report_prompt.py
│
└── main.py
```
# Performance Optimizations

CFInsight incorporates multiple optimization strategies to improve responsiveness, reduce external API dependency, and minimize unnecessary computation.

## PostgreSQL Report Caching

Generated reports are stored in PostgreSQL and reused whenever possible.

### Benefits

* Eliminates repeated Codeforces API requests
* Avoids regenerating AI insights
* Reduces response latency
* Improves scalability under repeated access
* Reduces overall processing overhead

### Cache Analytics

The platform continuously tracks cache effectiveness.

Metrics tracked:

* Cache Hits
* Cache Misses
* Cache Hit Rate

Cache Hit Rate is calculated as:

```text
Hit Rate = Hits / (Hits + Misses) × 100
```

This provides visibility into cache efficiency and helps evaluate overall system performance.

---

## Trie-Based Search Optimization

Successfully searched Codeforces handles are stored in an in-memory Trie.

### Benefits

* Fast prefix-based autocomplete
* No database query for every keystroke
* Reduced database load
* Better user experience
* Efficient search suggestions

### Time Complexity

```text
Insertion : N

Lookup    : P + K
```

Where:

* P = Prefix Length
* K = Number of Suggestions Returned

This makes Trie an ideal choice for autocomplete functionality.

---

## Middleware-Based Performance Monitoring

A custom FastAPI middleware measures request latency for report-generation endpoints.

Metrics tracked:

* Total Report Requests
* Average Response Time
* Maximum Response Time

This allows monitoring of platform performance and helps evaluate the effectiveness of caching strategies.

---

## Search Analytics

The platform tracks search activity to identify trending Codeforces profiles.

Benefits:

* Leaderboard generation
* User engagement analysis
* Popular profile tracking
* Search trend monitoring

```
```

---

# Database Design

## users

Stores Codeforces user information and cached profile metadata.

### Fields

* id
* handle
* current_rating
* max_rating
* current_rank
* max_rank
* created_at
* last_updated

---

## reports

Stores generated analytics reports.

### Fields

* id
* user_id
* report_json
* generated_at

---

## search_stats

Stores handle search frequencies used for leaderboard generation.

### Fields

* id
* handle
* search_count
* month
* year
* last_searched_at

---

## cache_stats

Stores cache monitoring information.

### Fields

* id
* hits
* misses

---

# Engineering Decisions

## Layered Architecture

The backend follows:

```text
API Layer
    ↓
Service Layer
    ↓
Repository Layer
    ↓
Database Layer
```

Benefits:

* Separation of concerns
* Easier maintenance
* Improved scalability
* Better testability

---

## Repository Pattern

Database operations are isolated within repository classes.

Benefits:

* Cleaner business logic
* Reduced duplication
* Better maintainability

---

## Caching Strategy

Caching was introduced to minimize expensive report generation operations.

Benefits:

* Faster responses
* Reduced external dependencies
* Lower processing overhead

---

## Trie-Based Search

Trie was chosen because autocomplete is fundamentally a prefix-search problem.

Benefits:

* Efficient lookups
* Scalable suggestions
* Predictable performance

---

# Monitoring & Observability

CFInsight includes built-in monitoring capabilities.

### Cache Monitoring

Tracks:

* Cache Hits
* Cache Misses
* Cache Hit Rate

### Performance Monitoring

Tracks:

* Request Count
* Average Response Time
* Maximum Response Time

This allows evaluation of platform efficiency and caching effectiveness.

---

# Codeforces APIs Used

### user.info

Provides:

* Profile information
* Ratings
* Ranks

### user.rating

Provides:

* Contest history
* Rating changes
* Contest performance

### user.status

Provides:

* Submission history
* Problem difficulty data
* Verdict statistics
* Problem tags

---

# Future Enhancements

* Historical Report Comparison
* User-to-User Comparison
* Visual Analytics Dashboard
* Personalized Training Recommendations
* ML-Based Suspicion Scoring
* Advanced Trend Analysis
* Distributed Caching Support

---

# Disclaimer

CFInsight uses publicly available Codeforces data.

Suspicion scores and AI-generated evaluations are analytical estimates intended for educational and informational purposes only. They should not be interpreted as evidence of cheating, plagiarism, AI usage, or misconduct.


# Live Deployment

## API Base URL

https://pocketskye-cfinsight.hf.space

## Interactive API Documentation

https://pocketskye-cfinsight.hf.space/docs

## Available Endpoints

### Health Check

GET /health

### Generate Analytics Report

GET /report/{handle}

Example:

GET /report/tourist

### Search Leaderboard

GET /leaderboard

### Handle Suggestions

GET /suggest?prefix=tou

### Cache Statistics

GET /cache-stats

### Performance Metrics

GET /metrics

---

The backend is deployed on Hugging Face Spaces using Docker and connected to Neon PostgreSQL for persistent storage.
