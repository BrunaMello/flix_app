from reviews.repository import ReviewRepository


class ReviewService:

	def __init__(self):
		self.reviews_repository = ReviewRepository()

	def get_reviews(self):
		return self.reviews_repository.get_reviews()

	def create_reviews(self, movie, stars, comment):
		review = dict(
			movie=movie,
			stars=stars,
			comment=comment,
		)
		return self.reviews_repository.create_review(review)
