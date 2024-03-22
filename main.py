import pytest
from testing_layer.api_tests.add_area_test import AreaTests
from infra_layer.infra_ui.wrapper import browserWrapper
from testing_layer.ui_tests.check_area_test import areaTests

@pytest.fixture
def infra_layer():
    return browserWrapper()

def test_run_grid_serial(infra_layer):
    print(infra_layer.cab_list)
    for cabs in infra_layer.cab_list:
        # Instantiate the areaTests class
        search_test_instance = areaTests()
        # Pass any necessary parameters to the test method
        search_test_instance.verify_successful_area_add(cabs)
        # You may add additional test methods from areaTests if needed

if __name__ == "__main__":
    pytest.main([__file__])
