one_dimension_test:
	python3 one_dimension/test_one_dimension.py

general_case_test:
	python3 general_case/test_general_case.py

hooke_law_experience:
	python3 applications/physics/hooke_law_experience.py

viscosity_experience:
	python3 applications/physics/viscosity_experience.py


all: one_dimension_test general_case_test hooke_law_experience

clean:
	rm -rf one_dimension/__pycache__/ one_dimension/graph/graph_for_*.png
	rm -rf general_case/__pycache__/ general_case/graph/graph_for_*.png	
	rm -rf applications/physics/__pycache__/ applications/physics/graphs/graph_for_*.png

.PHONY: one_dimension_test general_case_test
