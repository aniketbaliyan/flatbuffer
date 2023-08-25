import encoder

import Schema.Client
import Schema.Group
import Schema.Person
import Schema.Type

def test_person():
    name = "Ram"
    age = 21
    weight = 76.5
    gender = "Male"

    obj = encoder.Encoder()

    buf = obj.serialize_person(name, age, weight, gender)

    client = Schema.Client.Client.GetRootAs(buf, 0)

    assert client.Name() == b"client"
    assert client.ClientDataType() == Schema.Type.Type().Person

    person = Schema.Person.Person()
    person.Init(client.ClientData().Bytes, client.ClientData().Pos)

    assert person.Name() == b"Ram"
    assert person.Age() == 21
    assert person.Weight() == 76.5
    assert person.Gender() == b"Male"

def test_group():

    groupName = "FightClub"
    age = 24.5
    weight = 66
    listOfNames = ["Ram", "Shayam", "Raghuveer"]

    obj = encoder.Encoder()
    buf = obj.serialize_group(groupName, age, weight, listOfNames)

    client = Schema.Client.Client.GetRootAs(buf, 0)

    assert client.Name() == b"client"
    assert client.ClientDataType() == Schema.Type.Type().Group

    group = Schema.Group.Group()
    group.Init(client.ClientData().Bytes, client.ClientData().Pos)

    assert group.Name() == b"FightClub"
    assert group.Age() == 24.5
    assert group.Weight() == 66
    assert group.List(0) == b"Ram"
    assert group.List(1) == b"Shayam"
    assert group.List(2) == b"Raghuveer"
