from models.user import User
from sqlalchemy import func

class UserRepository:

    @staticmethod
    def get_by_handle(db, handle: str):

        return (
            db.query(User)
            .filter(
                func.lower(User.handle)
                ==
                handle.lower()
            )
            .first()
        )
    @staticmethod
    def create(db, profile):

        user = User(
            handle=profile["handle"],
            current_rating=profile.get("rating"),
            max_rating=profile.get("maxRating"),
            current_rank=profile.get("rank"),
            max_rank=profile.get("maxRank")
        )

        db.add(user)

        db.commit()

        db.refresh(user)

        return user
    @staticmethod
    def get_all_handles(db):
        
        return [
            user.handle
            for user in db.query(User).all()
        ]