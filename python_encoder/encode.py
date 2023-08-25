import encoder
import sys

    
def encode():
    """
    Note : this function is only for testing encoder
    """
    path = sys.argv[1]

    name = "Ram"
    age = 21
    weight = 76.5
    gender = "Male"

    obj = encoder.Encoder()
    buf = obj.serialize_person(name, age, weight, gender)

    path_person = path + "person_bytes.bin"
    obj.dump_data_into_file(buf, path_person)

    groupName = "FightClub"
    age = 24.5
    weight = 66
    listOfNames = ["Ram", "Shayam", "Raghuveer"]

    buf = obj.serialize_group(groupName, age, weight, listOfNames)

    path_group = path + "group_bytes.bin"
    obj.dump_data_into_file(buf, path_group)


if __name__ == "__main__":
    encode()    
    