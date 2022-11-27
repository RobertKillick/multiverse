VENV_PATH=venv

.PHONY: setup
setup: venv install-requirements

.PHONY: venv
venv:
	python -m venv ${VENV_PATH}

.PHONEY: install-requirements
install-requirements:
	source ${VENV_PATH}/bin/activate && pip install -r requirements.txt

.PHONY: clean
clean:
	rm -rf ${VENV_PATH}
