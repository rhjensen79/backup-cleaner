build:
	docker build -t backup-cleaner:latest .

run:
	docker run -v ./dummy_folder:/data backup-cleaner:latest

test: 
	make build
	python3 dummy_files.py
	make run
