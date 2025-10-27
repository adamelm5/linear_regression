one_dimension_test:
	python3 one_dimension/test_one_dimension.py

general_case_test:
	python3 general_case/test_general_case.py

all: one_dimension general_case

clean:
	rm -rf one_dimension/__pycache__/
	rm -rf general_case/__pycache__/
	rm -rf graph_tools/__pycache__/

test: one_dimension general_case