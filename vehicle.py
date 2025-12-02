import pytest
def vehicle_registration(number,owner_name,vehicle_type,manifacture):
    result=(
        f"Vehicle number:{number}\n"
        f"vehicle owner name:{owner_name}\n"
        f"vehicle type:{vehicle_type}\n"
        f"year of manufacture:{manifacture}"
    )
    return result
if __name__=="__main__":
    number="KA31N2881"
   owner_name="sara"
    vehicle_type="car"
    manifacture=2015
    print(vehicle_registration(number,owner_name,vehicle_type,manifacture))
