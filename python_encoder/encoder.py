import flatbuffers
 
# Generated by `flatc`.
import Schema.Client
import Schema.Group
import Schema.Person
import Schema.Type


class Encoder:
    def __init__(self, client_name="client"):
        self.name = client_name

    def serialize_string(self, builder, string):
        return builder.CreateString(string)     
        
    def serialize_person(self, name, age, weight, gender):
        
        builder = flatbuffers.Builder(0)

        #  Create a person
        name = self.serialize_string(builder, name)
        gender = self.serialize_string(builder,gender)

        Schema.Person.PersonStart(builder)
        
        Schema.Person.PersonAddName(builder, name)
        Schema.Person.PersonAddAge(builder, age)
        Schema.Person.PersonAddWeight(builder, weight)
        Schema.Person.PersonAddGender(builder, gender)

        person = Schema.Person.PersonEnd(builder)        

        buf = self.serialize_client(builder, person, Schema.Type.Type().Person)

        return buf

    def serialize_group(self, groupName, age, weight, listOfNames):
            
        builder = flatbuffers.Builder(0)

        #  Create a group
        groupName = self.serialize_string(builder, groupName)

        offsetOfNames = []
        for name in listOfNames:
            temp = self.serialize_string(builder, name)
            offsetOfNames.append(temp)

        Schema.Group.GroupStartListVector(builder, len(offsetOfNames))
        # Note: Since we prepend the data, prepend the names in reverse order.
        for offset in reversed(offsetOfNames):
                builder.PrependUOffsetTRelative(offset)

        listOfNames = builder.EndVector()

        Schema.Group.GroupStart(builder)
        
        Schema.Group.GroupAddName(builder, groupName)
        Schema.Group.GroupAddAge(builder, age)
        Schema.Group.GroupAddWeight(builder, weight)
        Schema.Group.GroupAddList(builder, listOfNames)

        group = Schema.Group.GroupEnd(builder)

        # Serialize the FlatBuffer data.
        buf = self.serialize_client(builder, group, Schema.Type.Type().Group)

        return buf
        
    def serialize_client(self, builder, obj, obj_type):    

        client_name = self.serialize_string(builder, self.name)
        
        Schema.Client.ClientStart(builder)
        
        Schema.Client.ClientAddName(builder, client_name)
        Schema.Client.ClientAddClientDataType(builder, obj_type)
        Schema.Client.ClientAddClientData(builder, obj)

        client = Schema.Client.ClientEnd(builder)

        builder.Finish(client)  

        buf = builder.Output()

        return buf

        

    def dump_data_into_file(self, buf, file):

        with open(file, "wb") as f:            
            f.write(buf)


