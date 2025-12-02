from vehicle import vehicle_registration

def test_vehicle_registration():
    expected_output=(
        "Product Name:TV\n"
        "Product ID:S2345\n"
        "Quantity:1\n" 
        "Price:40000"
    )
    assert vehicle_registration("TV","S2345",1,40000)==expected_output
