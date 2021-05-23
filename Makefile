develop-up:
	uvicorn main:app --reload

requirements:
	pipenv lock -r > requirements.txt




