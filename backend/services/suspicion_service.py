class SuspicionService:

    @staticmethod
    def get_skipped_score(
        skipped_submissions,
        total_submissions
    ):

        if total_submissions == 0:
            return 0

        ratio = (
            skipped_submissions
            /
            total_submissions
        ) * 100

        if ratio < 1:
            return 0

        elif ratio < 3:
            return 25

        elif ratio < 5:
            return 50

        elif ratio < 10:
            return 75

        return 100

    @staticmethod
    def get_difficulty_score(
        current_rating,
        average_recent_contest_difficulty
    ):

        gap = (
            average_recent_contest_difficulty
            -
            current_rating
        )

        if gap <= 200:
            return 0

        elif gap <= 400:
            return 25

        elif gap <= 600:
            return 50

        elif gap <= 800:
            return 75

        return 100

    @staticmethod
    def get_level(score):

        if score <= 25:
            return "Low"

        elif score <= 50:
            return "Moderate"

        elif score <= 75:
            return "High"

        return "Very High"

    @staticmethod
    def calculate(
        current_rating,
        average_recent_contest_difficulty,
        skipped_submissions,
        total_submissions
    ):
        current_rating = current_rating or 0
        average_recent_contest_difficulty = average_recent_contest_difficulty or 0
        skipped_submissions = skipped_submissions or 0
        total_submissions = total_submissions or 0
        skipped_ratio = (
            round(
                skipped_submissions
                * 100
                / total_submissions,
                2
            )
            if total_submissions
            else 0
        )

        difficulty_gap = (
            average_recent_contest_difficulty
            -
            current_rating
        )

        skipped_score = (
            SuspicionService.get_skipped_score(
                skipped_submissions,
                total_submissions
            )
        )

        difficulty_score = (
            SuspicionService.get_difficulty_score(
                current_rating,
                average_recent_contest_difficulty
            )
        )

        final_score = round(
            (
                0.4 * skipped_score
            )
            +
            (
                0.6 * difficulty_score
            )
        )

        return {
            "score": final_score,

            "level": SuspicionService.get_level(
                final_score
            ),

            "metrics": {

                "current_rating":
                    current_rating,

                "average_recent_contest_difficulty":
                    average_recent_contest_difficulty,

                "difficulty_gap":
                    difficulty_gap,

                "skipped_submissions":
                    skipped_submissions,

                "total_submissions":
                    total_submissions,

                "skipped_ratio":
                    skipped_ratio,

                "skipped_score":
                    skipped_score,

                "difficulty_score":
                    difficulty_score
            }
        }