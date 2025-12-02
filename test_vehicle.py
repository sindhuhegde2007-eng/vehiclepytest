from vehicle import vehicle_registration

def test_vehicle_registration():
    expected_output = (
        "Vehicle number:KA31N2881\n"
        "vehicle owner name:sara\n"
        "vehicle type:car\n"
        "year of manufacture:2015"
    )

    assert vehicle_registration("KA31N2881", "sara", "car", 2015) == expected_output

