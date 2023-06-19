prepare:
	@mkdir assets
	@mkdir assets/audios
	@mkdir assets/fonts
	@mkdir assets/output_videos
	@mkdir assets/texts
	@mkdir assets/videos
	@pip3 install -r requirements.txt

run: 
	python3 run.py