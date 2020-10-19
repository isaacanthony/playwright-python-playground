build:
	@docker build -t playwright-python-playground .

run:
	@docker run \
		--name playwright-python-playground \
		--rm \
		-it \
		-v $(PWD)/img:/img \
		-v $(PWD)/src:/src \
		playwright-python-playground
